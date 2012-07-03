Name: clipart-sodipodi
Version: 2.1
Release: alt1

Summary: Clipart with SVG files for sodipodi
License: Public domain
Group: Graphics

Url: http://sodipodi.sourceforge.net/
Source: sodipodi-clipart-%version.tar.bz2

Summary(ru_RU.KOI8-R): Коллекция векторных изображений SVG для sodipodi

Buildarch: noarch

%description
Collection of svg images

%description -l ru_RU.KOI8-R
Коллекция векторных изображений в svg

%define clip_dir %_datadir/design/cliparts/sodipodi

%prep
%setup -n Sodipodi-clipart-%version

%build

%install

%__install -d %buildroot%clip_dir
cp -pr * %buildroot%clip_dir

%files
%dir %clip_dir
%clip_dir/*
%doc README

%changelog
* Sun Jan 04 2004 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt1
- first build for Sisyphus
