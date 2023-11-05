Name:           wf-recorder
Version:        0.4.1
Release:        alt1
Summary:        Utility program for screen recording of wlroots-based compositors
License:        MIT
Group:          Video
URL:            https://github.com/ammen99/wf-recorder
Source0:        %{name}-%{version}.tar
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.54.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14

%description
Utility program for screen recording of wlroots-based compositors
(more specifically, those that support wlr-screencopy-v1 and xdg-output).

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md LICENSE
%attr(0755,root,root) /usr/bin/wf-recorder
%{_mandir}/man?/%{name}*

%changelog
* Sun Nov  5 2023 Artyom Bystrov <arbars@altlinux.org> 0.4.1-alt1
- Initial commit for Sisyphus