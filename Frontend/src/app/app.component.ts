import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CommonModule, NgFor } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,AppComponent,NgFor,CommonModule, FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'Frontend';

  items: any[] = [];

  newUser = { firstname: '', lastname: '', username: '', email: '', password: '', date_of_birth: '' };

  constructor(private apiService: ApiService) {}

  addUser() {

    this.apiService.addUser(this.newUser).subscribe({ 
      next: (response: any) => {
        console.log('Start to insert..');
        console.log(response);
      }
    });
  }

}
