Name: xvfb-run
Version: 1.4.1
Release: alt1

Summary: xvfb-run - script to run process under Xvfb server
License: GPLv2+
Group: Development/Other
BuildArch: noarch
Packager: Dmitry V. Levin <ldv@altlinux.org>

Source: xvfb-run
Source1: xvfb-run.1

Requires: fakeroot xorg-xvfb

# Automatically added by buildreq on Tue Sep 09 2008
BuildRequires: fakeroot xorg-xvfb xset

%description
xvfb-run - script to run process under Xvfb xserver

%prep
%setup -qcT
install -pm755 %_sourcedir/%name .

%build
./%name -a xset b

%install
install -pD -m755 %name %buildroot%_bindir/%name
install -pD -m644 %_sourcedir/%name.1 %buildroot%_man1dir/%name.1

%files
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Sun Apr 04 2010 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt1
- Updated XVFBARGS (Valery V. Inozemtsev).

* Wed Jun 24 2009 Dmitry V. Levin <ldv@altlinux.org> 1.4-alt1
- Changed to use "xauth source", to avoid placing magic cookie
  on the command line (patch from Debian; closes: #19943).
- Changed default to create temporary file for auth cookie.
- Adopted xvfb-run(1) manpage from Debian.

* Mon Sep 08 2008 Dmitry V. Levin <ldv@altlinux.org> 1.3-alt1
- Updated XVFBARGS (Valery V. Inozemtsev).
- Fixed signal handler exit status.
- Updated package dependencies.

* Wed Aug 30 2006 Dmitry V. Levin <ldv@altlinux.org> 1.2-alt2
- Relocated utility to %_bindir.
- Updated build dependencies.

* Mon Dec 13 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2-alt1
- Terminate Xvfb server when utility gets terminated by signal.

* Thu Oct 07 2004 Dmitry V. Levin <ldv@altlinux.org> 1.1-alt1
- Reworked script.
- Added test during build.
- Relocated script from %_bindir/ to %_x11bindir/.

* Thu Feb 06 2003 Alexander V. Nikolaev  <avn@altlinux.ru> 1.0-alt1
- Initial package
