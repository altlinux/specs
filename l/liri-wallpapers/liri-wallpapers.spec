Name: liri-wallpapers
Version: 0.10.0
Release: alt1

Summary: Wallpapers for the Liri desktop
License: Distributable
Group: Graphical desktop/Other
Url: https://github.com/lirios/wallpapers

Source: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: cmake cmake-modules-liri

%description
%summary

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc backgrounds/CREDITS.md README.md
%_datadir/backgrounds/liri/*.png
%_datadir/backgrounds/liri/*.jpg

%changelog
* Thu Oct 31 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.0-alt1
- initial
