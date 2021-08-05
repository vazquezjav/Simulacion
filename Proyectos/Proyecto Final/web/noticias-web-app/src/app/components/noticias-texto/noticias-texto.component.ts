import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Respuesta } from 'src/app/interfaces/respuesta';
import { NoticiasServiceService } from 'src/app/services/noticias-service.service';

@Component({
  selector: 'app-noticia',
  templateUrl: './noticias-texto.component.html',
  styleUrls: ['./noticias-texto.component.scss'],
})
export class NoticiasTextoComponent implements OnInit {

  constructor(private http: HttpClient, private noticiasService: NoticiasServiceService) { }

  textoNoticia: string

  noticia: boolean;

  respuesta = '';

  ngOnInit() {}

  private obtenerTexto(evento: CustomEvent){
    this.textoNoticia= evento.detail.value
    console.log(evento.detail.value)
  }

  private clasificarNoticia(){
    if(this.textoNoticia !=''){
      this.noticiasService.getResponseTexto(this.textoNoticia).subscribe((response: Respuesta) => {
        if (response.id == 0){
          this.noticia = false
        }else{
          this.noticia = true
        }
        this.respuesta = response.respuesta
        console.log(response)
      });
    }
}

}
