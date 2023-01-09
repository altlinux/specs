%define        gimppluginsdir %(gimptool-2.0 --gimpplugindir)/plug-ins/

Name:          gimp-plugin-bimp
Version:       2.6
Release:       alt1
Summary:       BIMP - Batch Image Manipulation Plugin for GIMP
License:       %gpl2plus
Group:         Graphics
Url:           https://alessandrofrancesconi.it/projects/bimp/
Vcs:           https://github.com/alessandrofrancesconi/gimp-plugin-bimp.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
Patch:         install.patch
BuildRequires(pre): rpm-build-licenses
BuildRequires: libgimp-devel
BuildRequires: libgegl-devel

%description
With BIMP you can apply a set of GIMP manipulations on groups of images.


%prep
%setup
%autopatch

%build
%make_build

%install
%makeinstall_std

%files
%gimppluginsdir/*
%doc CHANGELOG.md README.md


%changelog
* Mon Jan 02 2023 Pavel Skrylev <majioa@altlinux.org> 2.6-alt1
- initial build for Sisyphus
