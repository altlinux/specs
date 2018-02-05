Name: vdpauinfo
Version: 1.0
Summary: VDPAU acceleration information utility
Release: alt1
License: MIT/X Consortium
Group: System/X11
URL: https://www.freedesktop.org/wiki/Software/VDPAU/
#https://anongit.freedesktop.org/git/vdpau/vdpauinfo.git
Source: %name-%version.tar

BuildRequires: gcc-c++ libvdpau-devel
BuildRequires: libX11-devel xorg-xproto-devel

%description
Tool to query the capabilities of a VDPAU implementation.


%prep
%setup -q -n %name-%version

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
* Wed Jan 11 2018 Alexandr Antonov <aas@altlinux.org> 1.0-alt1
- initial build for ALT
