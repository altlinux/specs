%define _unpackaged_files_terminate_build 1

Name: uxplay
Version: 1.68.3
Release: alt1

Summary: AirPlay Unix mirroring server
License: GPL-3.0
Group: Video
URL: https://github.com/FDH2/UxPlay
Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libplist-devel
BuildRequires: libavahi-devel
BuildRequires: libssl-devel
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)

Requires: avahi
Requires: gst-libav
Requires: gst-plugins-bad1.0
Requires: gst-plugins-good1.0
Requires: gst-plugins-base1.0
Requires: gstreamer-vaapi

%description
This project is a unix AirPlay2 Mirror server that provides screen-mirroring
(with audio) of iOS/MacOS clients in a display window on the server host.

%description -l ru_RU.UTF-8
Этот проект представляет собой зеркальный сервер AirPlay2 Mirror, который
обеспечивает зеркальное отображение экрана (со звуком) клиентов iOS/MacOS
в окне отображения на хосте сервера.

%prep
%setup

%build
%cmake -DNO_MARCH_NATIVE=ON
%cmake_build

%install
%cmake_install

# Remove duplicate docs
rm -rf %buildroot%_defaultdocdir

%files
%_bindir/%name
%_man1dir/%name.1*

%doc README.md LICENSE

%changelog
* Wed Jun 26 2024 Anastasia Osmolovskaya <lola@altlinux.org> 1.68.3-alt1
- Initial build for ALT.
