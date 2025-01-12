from django.core.management.base import BaseCommand
from users.models.typology import Typology
from users.models.users import User 
from django.contrib.auth.hashers import make_password
from users.models.api_url import ApiUrl
from users.models.typology_api_url import TypologyApiUrl

class Command(BaseCommand):
    help = "Seed db with initial permissions"
    
    def handle(self, *args, **options):
        
        #typologies seeders
        Typology.objects.get_or_create(
            typology_name = "Admin"
        )
        
        Typology.objects.get_or_create(
            typology_name = "Restaurant Admin"
        )
        
        Typology.objects.get_or_create(
            typology_name = "Dealer"
        )
        
        Typology.objects.get_or_create(
            typology_name = "Customer"
        )
        
        # api url seeders
        
        # users
        ApiUrl.objects.get_or_create(
            name="Crear Usuario",
            url="/api/users/",
            method="POST"
        )
        
        ApiUrl.objects.get_or_create(
            name="Obtener listado de usuarios",
            url="/api/users/list",
            method="GET"
        )
        
        ApiUrl.objects.get_or_create(
            name="Eliminar usuario por id",
            url="/api/users/delete/{pk}",
            method="DELETE"
        )
        
        ApiUrl.objects.get_or_create(
            name="Obtener usuario por id",
            url="/api/users/find/{pk}",
            method="GET"
        )
        
        ApiUrl.objects.get_or_create(
            name="Actualizar usuario",
            url="/api/users/update/{pk}",
            method="PUT"
        )
        
        ApiUrl.objects.get_or_create(
            name="Actualizar contraseña de usuario",
            url="/api/users/reset_password/",
            method="PATCH"
        )
        
        #typologies
        ApiUrl.objects.get_or_create(
            name="Crear tipologia",
            url="/api/typologies/",
            method="POST"
        )
        
        ApiUrl.objects.get_or_create(
            name="Obtener listado de tipologias",
            url="/api/typologies/list",
            method="GET"
        )
        
        ApiUrl.objects.get_or_create(
            name="Obtener tipologia por id",
            url="/api/typologies/find/{pk}",
            method="GET"
        )
        
        ApiUrl.objects.get_or_create(
            name="Actualizar tipologia",
            url="/api/typologies/update/{pk}",
            method="PUT"
        )
        
        # ApiUrl.objects.get_or_create(
        #     name="Eliminar tipologia",
        #     name="/api/typologies/delete/{pk}",
        #     method="DELETE"
        # )
        
        #apiurls
        ApiUrl.objects.get_or_create(
            name="Crear api url",
            url="/api/apiurl/",
            method="POST"
        )
        
        ApiUrl.objects.get_or_create(
            name="Obtener listado de urls",
            url="/api/apiurl/list",
            method="GET"
        )
        
        ApiUrl.objects.get_or_create(
            name="Obtener url por id",
            url="/api/apiurl/find/{pk}",
            method="GET"
        )
        
        ApiUrl.objects.get_or_create(
            name="Actualizar url",
            url="/api/apiurl/update/{pk}",
            method="PUT"
        )
        
        ApiUrl.objects.get_or_create(
            name="Eliminar url",
            url="/api/apiurl/delete/{pk}",
            method="DELETE"
        )
        
        # typology_api_urls
        ApiUrl.objects.get_or_create(
            name="Asignar permisos a una tipologia",
            url="/api/typology/apiurl/",
            method="POST"
        )
        
        ApiUrl.objects.get_or_create(
            name="Ver listado de permisos",
            url="/api/typology/apiurl/list",
            method="GET"
        )
        
        ApiUrl.objects.get_or_create(
            name="Ver permiso por id",
            url="/api/typology/apiurl/find/{pk}",
            method="GET"
        )
        
        ApiUrl.objects.get_or_create(
            name="Eliminar permiso de una tipologia",
            url="/api/typology/apiurl/delete/{pk}",
            method="DELETE"
        )
        
        #restaurants
        ApiUrl.objects.get_or_create(
            name="Crear restaurante",
            url="/api/restaurants/",
            method="POST"
        )
        
        ApiUrl.objects.get_or_create(
            name="Obtener listado de restaurantes",
            url="/api/restaurants/list",
            method="POST"
        )
        
        ApiUrl.objects.get_or_create(
            name="Obtener restaurante",
            url="/api/restaurants/find/{pk}",
            method="GET"
        )
        
        #23
        ApiUrl.objects.get_or_create(
            name="Actualizar restaurante",
            url="/api/restaurants/update/{pk}",
            method="PUT"
        )
        
        # asign permissions
        for i in range(1, 23):
            TypologyApiUrl.objects.get_or_create(
                typology_id = 1,
                api_url_id = i
            )
        
        TypologyApiUrl.objects.get_or_create(
            typology_id = 2,
            api_url_id = 23
        )
        
        TypologyApiUrl.objects.get_or_create(
            typology_id = 2,
            api_url_id = 1
        )
        # TypologyApiUrl.objects.get_or_create(
        #     typology_id = 2,
        #     api_url_id = 3
        # )
        
        TypologyApiUrl.objects.get_or_create(
            typology_id = 2,
            api_url_id = 4
        )
        
        TypologyApiUrl.objects.get_or_create(
            typology_id = 2,
            api_url_id = 5
        )
        
        TypologyApiUrl.objects.get_or_create(
            typology_id = 2,
            api_url_id = 6
        )
        
        TypologyApiUrl.objects.get_or_create(
            typology_id = 2,
            api_url_id = 22
        )
        
        TypologyApiUrl.objects.get_or_create(
            typology_id = 3,
            api_url_id = 1
        )
        
        TypologyApiUrl.objects.get_or_create(
            typology_id = 3,
            api_url_id = 6
        )
        
        TypologyApiUrl.objects.get_or_create(
            typology_id = 3,
            api_url_id = 5
        )
        
        TypologyApiUrl.objects.get_or_create(
            typology_id = 3,
            api_url_id = 21
        )
        
        TypologyApiUrl.objects.get_or_create(
            typology_id = 3,
            api_url_id = 20
        )
        
        TypologyApiUrl.objects.get_or_create(
            typology_id = 4,
            api_url_id = 1
        )
        
        TypologyApiUrl.objects.get_or_create(
            typology_id = 4,
            api_url_id = 3
        )
        
        TypologyApiUrl.objects.get_or_create(
            typology_id = 4,
            api_url_id = 4
        )
                
        TypologyApiUrl.objects.get_or_create(
            typology_id = 4,
            api_url_id = 5
        )
                
        TypologyApiUrl.objects.get_or_create(
            typology_id = 4,
            api_url_id = 6
        )
        
        TypologyApiUrl.objects.get_or_create(
            typology_id = 4,
            api_url_id = 21
        )
        
        TypologyApiUrl.objects.get_or_create(
            typology_id = 4,
            api_url_id = 20
        )
        
        User.objects.get_or_create(
            first_name =  "Test",
            last_name = "Admin",
            email = "admintest@gmail.com",
            password = make_password("Quick2024*"),
            phone = "344444444",
            address = "Transversal 93 # 51 - 98 Und. 24 -25",
            typology_id = 1,
        )
        
        self.stdout.write(self.style.SUCCESS("Successfully seeded dbs"))
        
    