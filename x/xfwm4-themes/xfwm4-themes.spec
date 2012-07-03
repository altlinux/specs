Name: xfwm4-themes
Version: 4.9.0
Release: alt1.git20111213

Summary: Additional themes for xfwm4
Summary (ru): Темы для менеджера окон среды Xfce - xfwm4
License: %gpl3plus, %bsdstyle
Group: Graphical desktop/XFce
Url: http://www.xfce.org/
Packager: XFCE Team <xfce@packages.altlinux.org>
Source: %name-%version.tar

Requires: xfwm4
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4
BuildRequires: xfce4-dev-tools

Conflicts: xfwm4 < 4.9

%description
A set of additionnal themes for the xfwm4 window manager.

%description -l ru
Данный пакет содержит в себе дополнительные темы для менеджера
окон xfwm4 используемом в окружении рабочего стола Xfce.

%prep
%setup

%build
%xfce4reconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc README AUTHORS
%_datadir/themes/*

%changelog
* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 4.9.0-alt1.git20111213
- Drop obsoleted patch.
- Upstream git snapshot.

* Mon Feb 21 2011 Mikhail Efremov <sem@altlinux.org> 4.6.0-alt3
- Sources: tar.bz2 -> tar.
- Fix License.
- Really fix build with current autotools.

* Mon May 25 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.0-alt2
- Fix build with new toolchain. Added autoconf and audomake version requiremens. 

* Sun Apr 12 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.0-alt1
Xfce 4.6.0

* Tue Jan 27 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.99.1-alt1
- Xfce 4.6rc1

* Thu Jan 22 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.93-alt1
- Xfce 4.6 beta 3

* Fri Oct 24 2008 Eugene Ostapets <eostapets@altlinux.org> 4.5.91-alt1
- Xfce 4.6 beta1

* Mon Nov 19 2007 Eugene Ostapets <eostapets@altlinux.org> 4.4.2-alt1
- Xfce 4.4.2 release

* Sat Apr 14 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.1-alt1
- Xfce 4.4.1 release

* Mon Jan 29 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.0-alt0.2
- fix typo in Summary

* Mon Jan 22 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.0-alt0.1
- Xfce 4.4 release

* Sun Nov 05 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.2-alt1
- Xfce 4.4rc2

* Sat Sep 30 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.1-alt1
- 4.4rc1

* Fri Nov 18 2005 Eugene Ostapets <eostapets@altlinux.ru> 4.2.3-alt1
- 4.2.3

* Wed May 18 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.2-alt1
- 4.2.2

* Thu Mar 17 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.1-alt1
- 4.2.1

* Sat Jan 15 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.0-alt1
- 4.2.0

* Fri Dec 24 2004 Andrey Astafiev <andrei@altlinux.ru> 4.1.99.3-alt1
- 4.1.99.3

* Mon Nov 01 2004 Andrey Astafiev <andrei@altlinux.ru> 4.1.91-alt1
- 4.1.91

* Wed Jul 21 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.6-alt1
- 4.0.6

* Sat Apr 17 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.5-alt1
- 4.0.5

* Tue Mar 16 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.4-alt1
- 4.0.4

* Wed Jan 21 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.3-alt1
- 4.0.3

* Tue Nov 18 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.0-alt2
- Changed Group tag.

* Fri Sep 26 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.0-alt1
- 4.0.0

* Fri Sep 12 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.4-alt1
- 3.99.4

* Fri Aug 29 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.3-alt0.9
- 3.99.3

* Sun Aug 17 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.2-alt0.9
- 3.99.2

* Mon Jul 14 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.1-alt0.9
- 3.99.1

* Fri Jun 13 2003 Andrey Astafiev <andrei@altlinux.ru> 3.90.0-alt0.9
- First version of RPM package for Sisyphus.
- Spec derived from original version.
