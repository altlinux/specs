%define gimpplugindir %(gimptool-2.0 --gimpplugindir)/plug-ins

Name:          gimp-plugin-laser
Version:       20240107
Release:       alt1
Summary:       Gimp plugin to generate g-code for laser engraving
Summary(ru_RU.UTF8): Плагин создает управляющую программу для лазерной гравировки
License:       GPLv3
Group:         Graphics
# Gimp plugin dir is arch dependant :(
##BuildArch:     noarch
Packager: Alexei Mezin <alexvm@altlinux.org>

Source:        %name-%version.tar
Url: https://github.com/buildbotics/gimp-laser-plugin


BuildRequires: libgimp-devel rpm-build-python
Requires: gimp

%description
A plugin for Gimp which turns images into G-Code for laser engravers.

%description -l ru_RU.UTF8
Расширения для Gimp, преобразующее картинку в программу для ЧПУ лазерного гравёра.

%prep
%setup

%build

%install
install -D -t %buildroot/%gimpplugindir -m0755 BUILDBOTICS-laser-plugin.py

%files
%gimpplugindir/*.py


%changelog
* Sun Jan 07 2024 Alexei Mezin <alexvm@altlinux.org> 20240107-alt1
- Initial build

