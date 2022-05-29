%define git da66af2

Name: vdpauinfo
Version: 1.4
Summary: VDPAU acceleration information utility
Release: alt1.g%{git}
License: MIT/X Consortium
Group: System/X11
URL: https://www.freedesktop.org/wiki/Software/VDPAU/
#https://anongit.freedesktop.org/git/vdpau/vdpauinfo.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ libvdpau-devel
BuildRequires: libX11-devel xorg-xproto-devel

%description
Tool to query the capabilities of a VDPAU implementation.


%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure
%make_build


%install
%makeinstall_std


%files
%doc COPYING
%_bindir/*


%changelog
* Sun May 29 2022 L.A. Kostis <lakostis@altlinux.ru> 1.4-alt1.gda66af2
- 1.4-1-gda66af2.

* Wed Aug 19 2020 Alexandr Antonov <aas@altlinux.org> 1.3-alt1
- update to current version

* Wed Jan 11 2018 Alexandr Antonov <aas@altlinux.org> 1.0-alt1
- initial build for ALT
