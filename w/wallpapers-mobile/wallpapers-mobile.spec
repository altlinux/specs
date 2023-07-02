%define photos_dir %_datadir/wallpapers
%define rname mobile

Name: wallpapers-%rname
Version: 1
Release: alt1

Summary: Backgrounds for mobile screens
License: CC-BY-NC-ND-4.0
Group: Graphics

Source: %name-%version.tar

BuildArch: noarch

%description
Original backgrounds for mobile screens.

%prep
%setup

%build

%install
install -pD -m644 -t %buildroot%photos_dir/%rname/720x1440 720x1440/*

%files
%photos_dir/%rname/

%changelog
* Sun Jul 02 2023 Andrew Savchenko <bircoph@altlinux.org> 1-alt1
- Initial built for ALT Linux.
