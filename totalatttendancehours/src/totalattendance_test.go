package main

import (
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
)

func TestHandler(t *testing.T) {
	req, err := http.NewRequest("GET", "/?att1=1&att2=2&att3=3&att4=4", nil)
	if err != nil {
		t.Fatal(err)
	}
	rr := httptest.NewRecorder()
	handler(rr, req)
	if status := rr.Code; status != http.StatusOK {
		t.Errorf("handler returned wrong status code: result was %v expected %v", status, http.StatusOK)
	}
	expected := `{"total_attendance":10}`
	actual := strings.TrimSpace(rr.Body.String())
	if actual != expected {
		t.Errorf("handler returned unexpected body: result was %v expected %v", actual, expected)
	}
}

func TestTotal(t *testing.T) {
	score := TotalAttendance(5, 5, 5, 5)
	if score != 20 {
		t.Error("Expected 20, got ", score)
	}
}
