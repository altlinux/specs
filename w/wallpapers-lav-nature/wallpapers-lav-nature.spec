%define oname lav-nature
%define photos_dir %_datadir/wallpapers/%oname

Name: wallpapers-%oname
Version: 20040726
Release: alt2

Summary: Photos for screen backgrounds
Summary(ru_RU.KOI8-R): Фото для фонов
Summary(uk_UA.KOI8-U): Фото для тла

License: Distributable
Group: Graphics
#Url: 

Packager: Vitaly Lipatov <lav@altlinux.ru>

Buildarch: noarch
Source: wallpapers-%oname-%version.tar.bz2

%description
Collection of botanic photos

%prep
%setup -q

%build

%install

mkdir -p %buildroot%photos_dir/
install -m 0644 *.jpg %buildroot%photos_dir/

%files
%photos_dir/
%doc READ.ME

%changelog
* Fri Mar 31 2006 Vitaly Lipatov <lav@altlinux.ru> 20040726-alt2
- cleanup spec, fix non latin char in filename

* Mon Jul 26 2004 Vitaly Lipatov <lav@altlinux.ru> 20040726-alt1
- first build for Sisyphus
