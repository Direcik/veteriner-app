# veteriner-app

<li> <a href=https://pypi.org/project/Django/3.2.9> django 3.2.9 </a></li>
<br>

```cmd
> pip install Django==3.2.9
```
<li> <a href=https://pypi.org/project/django-crispy-forms/1.13.0>django-crispy-forms 1.13.0</a></li>

<br>

```cmd
> pip install django-crispy-forms==1.13.0
```

<br>
<br>

# Amacı Nedir?
<p> Kişilerin sisteme kayıt olup sahibi olduğu hayvanları ekleyebildiği ve güncelleyebildiği bir uygulamadır. </p>

<br>

# Sınıflandırmalar

<ul>
    <li> Standart kullanıcılar sisteme kayıt olabiliyor, hayvan ekleyebiliyor, eklemiş olduğu hayvanları tablo biçiminde görebiliyor ve hayvanları güncelleyebiliyor. </li>
    <li> Yönetici olan kullanıcılar farklı kişilere hayvan ekleyebiliyor, veritabanında yer alan tüm hayvanları tablo biçiminde görebiliyor, güncelleme ve silme işlemlerini gerçekleştirebiliyor. </li>
    <li> Ayrıca hayvan adı kullanılarak filtreleme işlemleri yapılabiliyor. </li>
</ul>

# Nasıl Kullanılır?
#### İndirmek için;
```cmd
git clone https://github.com/Direcik/veteriner-app.git
```

#### Uygulama içerisinde cmd ekranı açılır ve veritabanında yer alacak tablolar oluşturulur.
```cmd
> python manage.py makemigrations
```
```cmd
> python manage.py migrate
```
#### Yönetici kullanıcıyı oluşturmak için;
```cmd
> python manage.py createsuperuser
```
#### Uygulamayı çalıştırmak için;
```cmd
> python manage.py runserver
```

#### işlemleri yapılır ve http://127.0.0.1:8000/ adresine gidilir.

<br>

# Kullanılan Çeşitli Teknikler
<li> Site önyüz temasında bootstrap teması kullanılmıştır. </li>

<li> Kayıt olma ve hayvan ekleme bölümlerinde yer alan formların daha güzel bir şekilde görünmesi için django-crispy-forms'ta yer alan bootstrap4 teması kullanılmıştır. </li>

<li> Yapılacak olan tüm işlemler Kontrol Paneli üzerinden gerçekleştirilebilir. </li>

<br>

# Form Yapıları ve Yetkilendirme

Kullanıcının yetki sınıfına göre ekranda görünecek form yapılarının yapısı ayarlanmıştır.

```python
if request.user.is_superuser:
    pass
else:
    pass
```

3 farklı form çeşidi kullanılmıştır.
<br>
<li> Kullanıcı kayıt bölümünde django içerisinde yer alan forms.Form yapısı ile form oluşturma işlemi yapılmıştır.

```python
class RegisterForm(forms.Form):
    ...

    def clean(self):
        ...

        values = {
        }
        return values

```
</li>
<br>
<li> Hayvan kayıt bölümünde forms.ModelForm yapısı ile form oluşturma işlemi yapılmıştır.

```python
class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['type_of_animal', 'genus', 'name_of_animal', 'age_of_animal', 'explanation']

```
</li>
<li> Arama bölümünde ise HTML form yapısı kullanılmıştır. Action metodu aynı sayfaya dönüleceği için tercih edilmemiştir.

``` html
    <form>
      {% csrf_token %}
      <input type="text" name="keyword" class="input-sm" maxlength="64" placeholder="Hayvan Adı">
      <button type="submit" class="btn btn-primary">Ara</button>
    </form>
```
</li>