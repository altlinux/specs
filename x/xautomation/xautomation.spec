Name: xautomation
Version: 1.03
Release: alt1.1

Summary: Control X from the command line
Summary(uk_UA.CP1251): Керування X з командного рядка
License: %gpl2plus
Group: System/X11

URL: http://hoopajoo.net/projects/%name.html

Source: %name-%version.tar
Patch: xautomation-1.03-alt-DSO.patch

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: imake libICE-devel libX11-devel libXtst-devel
BuildRequires: libpng-devel xorg-cf-files xorg-inputproto-devel
BuildRequires: xorg-xextproto-devel

%description
Control X from the command line for scripts, and do "visual scraping"
to find things on the screen. The control interface allows mouse
movement, clicking, button up/down, key up/down, etc, and uses the
XTest extension so you don't have the annoying problems that xse has
when apps ignore sent events. The visgrep program finds images inside
of images and reports the coordinates, allowing progams to find
buttons, etc, on the screen to click on.


%prep
%setup
%patch -p0


%build
%configure
%make_build


%install
%make_install DESTDIR=%buildroot install


%files
%doc AUTHORS ChangeLog README
%_bindir/*
%_man1dir/*
%_man7dir/*


%changelog
* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.03-alt1.1
- Fixed build

* Sun Apr 26 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.03-alt1
- 1.03

* Tue Dec 02 2008 Led <led@altlinux.ru> 1.02-alt2
- updated BuildRequires

* Fri Mar 21 2008 Led <led@altlinux.ru> 1.02-alt1
- 1.02

* Sun Jan 27 2008 Led <led@altlinux.ru> 1.01-alt1
- 1.01:
  + added man pages

* Sat Jan 12 2008 Led <led@altlinux.ru> 1.00-alt1
- 1.00

* Sat Dec 08 2007 Led <led@altlinux.ru> 0.99-alt1
- 0.99

* Mon Nov 12 2007 Led <led@altlinux.ru> 0.98-alt1
- 0.98
- fixed License
- updated BuildRequires

* Thu Jun 01 2006 Led <led@altlinux.ru> 0.96-alt1
- initial build for Sisyphus

* Tue Nov 04 2003 - James Oakley <jfunk@funktronics.ca> - 0.92-3
- Build for SUSE 9.0

* Mon Jun 02 2003 - James Oakley <jfunk@funktronics.ca> - 0.92-2
- Build for SuSE 8.2

* Mon Apr 07 2003 - James Oakley <jfunk@funktronics.ca> - 0.92-1
- Update to 0.92

* Sun Dec 29 2002 - James Oakley <jfunk@funktronics.ca> - 0.86-1
- Initial Package
