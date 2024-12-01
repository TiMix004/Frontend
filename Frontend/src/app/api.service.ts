import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://127.0.0.1:8000/items_create/';

  constructor(private http: HttpClient) { }

  createItem(data: any): Observable<any> {
    const headers = new HttpHeaders({ 'X-CSRFToken': 'your-csrf-token' }).set(
      'Content-Type',
      'application/json'
    );

    return this.http.post<any>(this.apiUrl, JSON.stringify(data), {
      headers: headers,
    })
  }
}
