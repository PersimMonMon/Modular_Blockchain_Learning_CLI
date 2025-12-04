package main

// add imports
import (
	"crypto/sha1"
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"net/http"
)

// Create struct instances: map JSON and add struct tag to represent JSON fields
type hashRequest struct {
	Input string `json:"input"`
	Hash  string `json:"hash"`
}

type hashResponse struct {
	Hash string `json:"hash"`
}

// compute the hash
func computeHash(input string, algorithm string) string {
	switch algorithm {
	case "sha1":
		hash := sha1.Sum([]byte(input)) // convert to byte slice and later convert to hex string
		return hex.EncodeToString(hash[:])
	default:
		hash := sha256.Sum256([]byte(input))
		return hex.EncodeToString(hash[:])
	}
}

// receive JSON POST request
func hashHandler(w http.ResponseWriter, r *http.Request) {

	// check if right request
	if r.Method != http.MethodPost {
		http.Error(w, "This microservice only takes in POST requests", http.StatusMethodNotAllowed)
		return
	}

	// create new struct instances
	req := hashRequest{}

	// read JSON request, convert to Go, return error if any
	err := json.NewDecoder(r.Body).Decode(&req)
	if err != nil || req.Input == "" {
		http.Error(w, "Invalid request", http.StatusBadRequest)
		return
	}

	// set default to use sha256
	if req.Hash == "" {
		req.Hash = "sha256"
	}

	// compute hash
	result := computeHash(req.Input, req.Hash)

	// set response to JSON and write back a response
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(hashResponse{Hash: result})

}

// create server
func main() {
	fmt.Println("Server running on port 3000.")
	http.HandleFunc("/hash", hashHandler)
	http.ListenAndServe(":3000", nil)
}
