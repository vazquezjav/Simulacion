import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse, HttpParams } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class NoticiasServiceService {

  constructor(private http:HttpClient) { }

  public getResponsePregunta(enlace:any){
    console.log('Entra service noticias')
    let header = new HttpHeaders().set('Content-Type', 'application/json; charset=utf-8');
    return this.http.get("/app/api?link="+enlace,{headers:header})
  }

  public getResponseTexto(texto:any){
    
    let header = new HttpHeaders().set('Content-Type', 'application/json; charset=utf-8');
    return this.http.get("/app/texto?texto="+texto,{headers:header})
  }
  
}
