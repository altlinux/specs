%define        _gimppluginsdir %(gimptool-2.0 --gimpplugindir)/plug-ins/

Name:          gimp-plugin-ogniewski-scaler
Version:       20220826
Release:       alt1
Summary:       Image scaling plugin for the GIMP
License:       GPL-3.0-only
Group:         Graphics
Url:           https://github.com/pannacotta98/ogniewski-scaler
Vcs:           git@github.com:pannacotta98/ogniewski-scaler.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires: gcc-c++
BuildRequires: libgimp-devel
BuildRequires: intltool
BuildRequires: glib2-devel

%description
Image scaling plugin for the GIMP

%prep
%setup
touch NEWS README AUTHORS

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
%find_lang gimp20-plugin-template

%files         -f gimp20-plugin-template.lang
%_gimppluginsdir/*
%_datadir/ogniewski-scaler


%changelog
* Tue Jan 03 2023 Pavel Skrylev <majioa@altlinux.org> 20220826-alt1
- initial build for Sisyphus
