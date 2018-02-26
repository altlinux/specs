%define photos_dir %_datadir/wallpapers
%define rname napkins-lunetta

Name: wallpapers-%rname
Version: 1.0
Release: alt1

Summary: various photo wallpapers.
License: Free Art License
Group: Graphics
Url: http://lunetta.ru
Packager: Anna Shadeeva <lunetta at altlinux.ru>

Buildarch: noarch
Source: wallpapers-%rname-%version.tar.bz2

%description
Collection of author's work
Packaged as 1600x1200 and 1920x1200 JPEGs


%prep
%setup -q

%build

%install

mkdir -p %buildroot/%photos_dir/%rname/{1920x1200,1600x1200}
install -m 0644 1920x1200/*.jpg %buildroot%photos_dir/%rname/1920x1200
install -m 0644 1600x1200/*.jpg %buildroot%photos_dir/%rname/1600x1200

%files
%photos_dir/*

%changelog

* Sun Dec 21 2008 Anna Shadeeva <lunetta@altlinux.ru> 1.0-alt1
- Initial build
