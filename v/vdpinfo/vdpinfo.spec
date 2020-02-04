Name: vdpinfo
Version: 0.0.4
Release: alt2

Summary: VDPAU acceleration information utility
License: MIT/X Consortium
Group: System/X11
URL: http://www.nvnews.net/vbulletin/showthread.php?t=124978

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ libvdpau-devel
BuildRequires: libX11-devel xorg-xproto-devel python-tools-2to3


%description
Simple utility that queries and displays the VDPAU capabilities of your X display
and prints them in tabular format.


%prep
%setup -q -n %name
sed -i -r '/^[[:blank:]]+for\(int[[:blank:]]+[xy][[:blank:]]*=[[:blank:]]*0/s/for\(int/for(size_t/' %name.cpp

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')

%build
%add_optflags -Wno-strict-aliasing
%__python3 functions.py > VDPDeviceImpl.h
%make_build CXXFLAGS="%optflags"

%install
install -pD -m 0755 {,%buildroot%_bindir/}%name

%files
%doc LICENSE
%_bindir/*


%changelog
* Tue Feb 04 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.0.4-alt2
- Porting to python3.

* Wed May 29 2013 Led <led@altlinux.ru> 0.0.4-alt1
- initial build
