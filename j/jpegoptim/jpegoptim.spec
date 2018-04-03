Name: jpegoptim
Version: 1.4.5
Release: alt1

Summary: Utility to optimize jpeg files
License: GPLv2+
Group: Graphics

Url: http://www.kokkonen.net/tjko/projects.html
Source: http://www.kokkonen.net/tjko/src/jpegoptim-%version.tar.gz

BuildRequires: libjpeg-devel

%description
Utility to optimize jpeg files. Provides lossless optimization (based on
optimizing the Huffman tables) and "lossy" optimization based on setting
maximum quality factor.

%prep
%setup

%build
libtoolize -i
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*

%changelog
* Tue Apr 03 2018 Yuri N. Sedunov <aris@altlinux.org> 1.4.5-alt1
- 1.4.5

* Sat Oct 08 2016 Yuri N. Sedunov <aris@altlinux.org> 1.4.4-alt1
- 1.4.4

* Wed May 27 2015 Yuri N. Sedunov <aris@altlinux.org> 1.4.3-alt1
- 1.4.3

* Fri Dec 26 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Fri Jul 04 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Mon Apr 11 2011 Victor Forsiuk <force@altlinux.org> 1.2.4-alt1
- 1.2.4

* Thu Oct 01 2009 Victor Forsyuk <force@altlinux.org> 1.2.3-alt1
- Initial build.
