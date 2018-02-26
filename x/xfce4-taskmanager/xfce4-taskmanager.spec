Name: xfce4-taskmanager
Version: 1.0.0
Release: alt2

Summary: Taskmanager for XFce Desktop
Summary(ru_RU.UTF-8): Системный монитор для Xfce
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://goodies.xfce.org/projects/applications/xfce4-taskmanager
Packager: XFCE Team <xfce@packages.altlinux.org>
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-devel libxfcegui4-devel libxfce4util-devel
BuildRequires: glib2-devel libatk-devel intltool libwnck-devel
BuildRequires: libgtk+2-devel libpango-devel libcairo-devel

%description
%name is taskmanager application for XFce desktop environment.

%description -l ru_RU.UTF-8
%name -- Менеджер задач для Xfce.

%prep
%setup

%build
%xfce4reconf
%configure \
    --enable-wnck \
    --enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README ChangeLog AUTHORS
%_bindir/*
%_desktopdir/xfce4-taskmanager.desktop

%changelog
* Wed Feb 09 2011 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt2
- Spec updated, tar.gz -> tar.

* Mon Jun 21 2010 Denis Koryavov <dkoryavov@altlinux.org> 1.0.0-alt1
- New version. 

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.4.1-alt1
- new version

* Mon May 19 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.4.0-alt1
- new version

* Mon Jan 29 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.3.2-alt1
- new version

* Thu Aug 18 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Sun Mar 13 2005 Andrey Astafiev <andrei@altlinux.ru> 0.2.1-alt1
- 0.2.1

* Sat Jan 29 2005 Andrey Astafiev <andrei@altlinux.ru> 0.1.0-alt1
- First build for Sisyphus.


