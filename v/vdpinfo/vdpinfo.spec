Name: vdpinfo
Version: 0.0.4
Summary: VDPAU acceleration information utility
Release: alt1
License: MIT/X Consortium
Group: System/X11
URL: http://www.nvnews.net/vbulletin/showthread.php?t=124978
Source: %name-%version.tar

BuildRequires: gcc-c++ libvdpau-devel %__python
BuildRequires: libX11-devel xorg-xproto-devel

%description
Simple utility that queries and displays the VDPAU capabilities of your X display
and prints them in tabular format.


%prep
%setup -q -n %name
sed -i -r '/^[[:blank:]]+for\(int[[:blank:]]+[xy][[:blank:]]*=[[:blank:]]*0/s/for\(int/for(size_t/' %name.cpp


%build
%add_optflags -Wno-strict-aliasing
%__python functions.py > VDPDeviceImpl.h
%make_build CXXFLAGS="%optflags"


%install
install -pD -m 0755 {,%buildroot%_bindir/}%name


%files
%doc LICENSE
%_bindir/*


%changelog
* Wed May 29 2013 Led <led@altlinux.ru> 0.0.4-alt1
- initial build
