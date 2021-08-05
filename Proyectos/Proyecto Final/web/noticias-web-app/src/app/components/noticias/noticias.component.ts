import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Respuesta } from 'src/app/interfaces/respuesta';
import { NoticiasServiceService } from 'src/app/services/noticias-service.service';

@Component({
  selector: 'app-noticias',
  templateUrl: './noticias.component.html',
  styleUrls: ['./noticias.component.scss'],
  providers: [NoticiasServiceService]
})
export class NoticiasComponent implements OnInit {

  constructor(private http: HttpClient, private noticiasService: NoticiasServiceService) { }

  enlace: string = '';

  opcionSeleccionada = '';

  noticia: boolean;

  respuesta = '';

  ngOnInit() {}

  private clasificarNoticia(){
      this.noticiasService.getResponsePregunta(this.enlace).subscribe((response: Respuesta) => {
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
