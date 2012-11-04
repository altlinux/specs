%def_disable debug

Name: xautomation
Version: 1.07
Release: alt1
Summary: Control X from the command line
Summary(uk_UA.CP1251): Керування X з командного рядка
License: GPLv2+
Group: System/X11
URL: http://hoopajoo.net/projects/%name.html
Source: http://hoopajoo.net/projects/%name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: imake libICE-devel libXtst-devel libpng-devel xorg-cf-files

%description
Control X from the command line for scripts, and do "visual scraping"
to find things on the screen. The control interface allows mouse
movement, clicking, button up/down, key up/down, etc, and uses the
XTest extension so you don't have the annoying problems that xse has
when apps ignore sent events. The visgrep program finds images inside
of images and reports the coordinates, allowing progams to find
buttons, etc, on the screen to click on.


%prep
%setup -q
%patch -p1


%build
%configure %{subst_enable debug}
%make_build
gzip -9c ChangeLog > ChangeLog.gz


%install
%makeinstall_std


%files
%doc AUTHORS ChangeLog.* README
%_bindir/*
%_man1dir/*
%_man7dir/*


%changelog
* Sun Nov 04 2012 Led <led@altlinux.ru> 1.07-alt1
- 1.07
- cleaned up BuildRequires

* Wed Oct 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.03-alt1.2
- Rebuilt with libpng15

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
