import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  url: any;
  constructor(private httpClient: HttpClient) { }

  addUser(param: any){
    this.url = "http://54.91.238.161:8000/addUser/"
    return this.httpClient.post(this.url, param);
  }

  checkUser(param: any){
    this.url = "http://54.91.238.161:8000/checkLogin/"
    return this.httpClient.post(this.url, param)
  }
}
