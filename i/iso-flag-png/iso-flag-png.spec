Summary: A collection of flags
Name: iso-flag-png
Version: 1.0.1
Release: alt1
License: Public Domain
Group: Graphical desktop/GNOME
BuildArch: noarch
URL: https://github.com/linuxmint/flags
Packager: Vladimir Didenko <cow@altlinux.ru>

Source: %name-%version.tar

%description
A collection of flags

%prep
%setup -n %name-%version

%build

%install
install -m 0755 -d %buildroot%_datadir
cp -Rp usr/share/%name %buildroot%_datadir

%files
%defattr(-,root,root)
%_datadir/%name

%doc debian/copyright debian/changelog

%changelog
* Wed May 23 2017 Vladimir Didenko <cow@altlinux.org> 1.0.1-alt1
- initial build for Sisyphus
