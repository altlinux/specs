%define photos_dir %_datadir/wallpapers
%define rname rm-nature

Name: wallpapers-rm-nature
Version: 20201006
Release: alt1

Summary: Photos for screen backgrounds
License: Distributable
Group: Graphics

Source: %name-%version.tar

BuildArch: noarch

Summary(ru_RU.UTF-8): Фотографии для рабочего стола

BuildRequires(pre): ImageMagick-tools

%description
Photographed by the wife of Roman Myskin.

Packed as original photos and as adapted photos for widescreen monitors.

%description -l ru_RU.UTF-8
Сфотографировано супругой Романа Мыскина.

Упакованы как оригинальные фотографии, так и адаптированные для широкоформатных мониторов.

%prep
%setup

%build

%install
mkdir -p %buildroot/%photos_dir/%rname/{default,1024x768,3024x1701}
# 768×1024
convert -rotate -90 image0.jpeg %buildroot%photos_dir/%rname/1024x768/image0.jpeg
# 3024×4032
convert -crop 1701x3024+1008+0 image1.jpeg %buildroot%photos_dir/%rname/3024x1701/image1.jpeg
install -m 0644 *.jpeg %buildroot%photos_dir/%rname/default

%files
%photos_dir/%rname/

%changelog
* Tue Oct 06 2020 Leontiy Volodin <lvol@altlinux.org> 20201006-alt1
- Initial built for ALT Linux.
