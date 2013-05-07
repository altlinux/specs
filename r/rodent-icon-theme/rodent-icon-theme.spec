Name: rodent-icon-theme
Version: 5.0
Release: alt1

Summary: Rodent is a svg (scalable) icon theme
License: %gpl2plus
Url: http://sourceforge.net/projects/xffm/files/rodent-icon-theme/
Group: Graphical desktop/XFce

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

Obsoletes: xfce4-icon-theme <= 4.4.3
Provides: xfce4-icon-theme = %version-%release

%description
Rodent-icon-theme (was xfce4-icon-theme) is a svg (scalable) icon theme
created by Francois L Clainche and augmented by Pablo Morales Romero.
It is freedesktop compatible and works with most mayor Linux/BSD desktop
environments.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc README INSTALL AUTHORS
%_datadir/icons/Rodent

%changelog
* Tue May 07 2013 Mikhail Efremov <sem@altlinux.org> 5.0-alt1
- Return 'Inherits' in the index.theme.
- Renamed to rodent-icon-theme.
- Updated to 5.0.

* Sat Nov 07 2009 Repocop Q. A. Robot <repocop@altlinux.org> 4.4.3-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-gtk-update-icon-cache for xfce4-icon-theme
  * postclean-05-filetriggers for spec file

* Sun Nov 09 2008 Eugene Ostapets <eostapets@altlinux.ru> 4.4.3-alt1
- Xfce 4.4.3 release

* Mon Nov 19 2007 Eugene Ostapets <eostapets@altlinux.org> 4.4.2-alt1
- Xfce 4.4.2 release

* Sat Apr 14 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.1-alt1
- Xfce 4.4.1 release

* Mon Jan 22 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.0-alt0.1
- Xfce 4.4 release

* Sun Nov 05 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.2-alt1
- Xfce 4.4rc2

* Sun Oct 01 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.1-alt1
- 4.4rc1

* Wed May 18 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.2-alt1
- 4.2.2

* Thu Mar 17 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.1-alt1
- 4.2.1

* Sat Jan 15 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.0-alt1
- First version of RPM package for Sisyphus.
