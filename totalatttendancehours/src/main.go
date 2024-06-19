package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"
)

func addCORS(w http.ResponseWriter, r *http.Request) {
	// Set CORS headers
	w.Header().Set("Access-Control-Allow-Origin", "*")
	w.Header().Set("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
	w.Header().Set("Access-Control-Allow-Headers", "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With")

	if r.Method == "OPTIONS" {
		w.WriteHeader(http.StatusOK)
		return
	}
}

func handler(w http.ResponseWriter, r *http.Request) {
	addCORS(w, r)

	validation := func(name string, min, max int) (int, error) {
		getString := r.URL.Query().Get(name)
		if getString == "" {
			return 0, fmt.Errorf("missing value for %s", name)
		}
		paramValue, err := strconv.Atoi(getString)
		if err != nil {
			return 0, fmt.Errorf("invalid value for %s. Must be an integer", name)
		}
		if paramValue < min || paramValue > max {
			return 0, fmt.Errorf("invalid value for %s. Must be between %d and %d", name, min, max)
		}
		return paramValue, nil
	}

	att1, err := validation("att1", 1, 33)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	att2, err := validation("att2", 1, 22)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	att3, err := validation("att3", 1, 44)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	att4, err := validation("att4", 1, 55)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	result := TotalAttendance(att1, att2, att3, att4)
	res := struct {
		Result int `json:"total_attendance"`
	}{
		Result: result,
	}
	w.Header().Set("Content-Type", "application/json")
	err = json.NewEncoder(w).Encode(res)
	if err != nil {
		http.Error(w, "Json Encoder Error", http.StatusBadRequest)
		return
	}
}

func main() {
	http.HandleFunc("/", handler)
	err := http.ListenAndServe(":8090", nil)
	if err != nil {
		return
	}
}
