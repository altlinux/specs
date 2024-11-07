%define        gimppluginsdir %(gimptool-2.0 --gimpplugindir)/plug-ins/

Name:          gimp-plugin-bimp
Version:       2.6.17
Release:       alt1
Summary:       BIMP - Batch Image Manipulation Plugin for GIMP
License:       %gpl2plus
Group:         Graphics
Url:           https://alessandrofrancesconi.it/projects/bimp/
Vcs:           https://github.com/alessandrofrancesconi/gimp-plugin-bimp.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-licenses
BuildRequires: libgimp-devel
BuildRequires: libgegl-devel

%description
With BIMP you can apply a set of GIMP manipulations on groups of images.


%prep
%setup

%build
%make_build

%install
%makeinstall_std

%files
%gimppluginsdir/*
%doc CHANGELOG.md README.md


%changelog
* Thu Nov 07 2024 Pavel Skrylev <majioa@altlinux.org> 2.6.17-alt1
- ^ 2.6 -> 2.6p17
- ! fixed type conversions when compilation

* Fri Mar 17 2023 Pavel Skrylev <majioa@altlinux.org> 2.6-alt2
- fix installation of the plugin (closes #45572)

* Mon Jan 02 2023 Pavel Skrylev <majioa@altlinux.org> 2.6-alt1
- initial build for Sisyphus
