%define        _gimppluginsdir %(gimptool-2.0 --gimpplugindir)/plug-ins/

Name:          gimp-plugin-scaler-biakima
Version:       1.0.0
Release:       alt1
Summary:       A GIMP plugin that scales an image using Akima spline instead of cubic interpolation method
License:       MIT
Group:         Graphics
Url:           https://github.com/ImageProcessing-ElectronicPublications/gimp-plugin-scaler-biakima
Vcs:           git@github.com:ImageProcessing-ElectronicPublications/gimp-plugin-scaler-biakima.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires: libgimp-devel
BuildRequires: glib2-devel
BuildRequires: intltool

%description
A GIMP plugin that scales an image using Akima spline instead of cubic
interpolation method.

This plugin is based on GIMP plugin Ogniewski Scaler.


%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
%find_lang gimp20-plugin-template

%files         -f gimp20-plugin-template.lang
%_gimppluginsdir/*
%_datadir/scaler-biakima


%changelog
* Wed Jan 04 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- initial build for Sisyphus
