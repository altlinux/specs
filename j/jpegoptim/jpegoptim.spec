Name: jpegoptim
Version: 1.4.7
Release: alt1

Summary: Utility to optimize jpeg files
Group: Graphics
License: GPL-2.0-or-later
Url: https://github.com/tjko/jpegoptim

Vcs: https://github.com/tjko/jpegoptim.git
Source: %url/archive/RELEASE.%version/%name-%version.tar.gz

BuildRequires: libjpeg-devel

%description
Utility to optimize jpeg files. Provides lossless optimization (based on
optimizing the Huffman tables) and "lossy" optimization based on setting
maximum quality factor.

%prep
%setup -n %name-RELEASE.%version

%build
%add_optflags %(getconf LFS_CFLAGS)
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*
%doc README

%changelog
* Tue Apr 19 2022 Yuri N. Sedunov <aris@altlinux.org> 1.4.7-alt1
- 1.4.7 (new GitHub homepage)

* Wed Apr 18 2018 Yuri N. Sedunov <aris@altlinux.org> 1.4.6-alt1
- 1.4.6

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
