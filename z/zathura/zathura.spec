%define gtk_ver 2

Name: zathura
Version: 0.2.0
Release: alt1

Summary: A lightweight document viewer
License: %bsdstyle
Group: Office
Url: https://zathura.pwmt.org/
# git://pwmt.org/zathura.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires: intltool libgtk+%{gtk_ver}-devel libgirara-devel libsqlite3-devel python-module-docutils

Conflicts: zatura-pdf-poppler < 0.1.1-alt2
Conflicts: zatura-djvu < 0.1.1-alt1
Conflicts: zatura-ps < 0.1.0-alt2

%description
zathura is a highly customizable and functional document viewer based on
the girara user interface library and several document libraries.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release
Requires: libgtk+%{gtk_ver}-devel libgirara-devel

%description devel
This package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch -p1

%build
export CFLAGS="%optflags"
%make VERBOSE=1 LIBDIR=%_libdir ZATHURA_GTK_VERSION=%gtk_ver SFLAGS='' RSTTOMAN=/usr/bin/rst2man.py

%install
%makeinstall_std PREFIX=%prefix LIBDIR=%_libdir RSTTOMAN=/usr/bin/rst2man.py
mkdir -p %buildroot%_libdir/zathura
%find_lang %name

%files -f %name.lang
%_bindir/%name
%dir %_libdir/%name
%_desktopdir/*
%_man1dir/*
%_man5dir/*

%files devel
%_includedir/*
%_libdir/pkgconfig/*.pc

%changelog
* Wed Jun 13 2012 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Enable strict aliasing rules.
- Updated to 0.2.0.

* Thu Mar 29 2012 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1
- Updated to 0.1.2.
- Disable strict aliasing rules.

* Fri Mar 16 2012 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- Updated to 0.1.1.

* Wed Mar 09 2011 Kirill A. Shutemov <kas@altlinux.org> 0.0.8.2-alt1
- 0.0.8.2-26-ga01ab17

* Tue Aug 10 2010 Kirill A. Shutemov <kas@altlinux.org> 0.0.8.1-alt1
- 0.0.8.1

* Mon Aug 02 2010 Sergey V Turchin <zerg@altlinux.org> 0.0.7-alt1.1
- rebuilt with new poppler

* Tue Jun 22 2010 Kirill A. Shutemov <kas@altlinux.org> 0.0.7-alt1
- 0.0.7

* Thu Jun 03 2010 Kirill A. Shutemov <kas@altlinux.org> 0.0.5-alt1
- First build for ALT Linux Sisyphus

