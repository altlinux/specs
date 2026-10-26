%define oname tslib
%define plugindir %_libdir/libts-1.0
%define sover 0
%define libts libts%sover

Name: libts
Version: 1.24
Release: alt1

Summary: tslib - touchscreen access library

Url: https://github.com/libts/tslib
License: GPL
Group: System/Libraries

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: %url/releases/download/%version/%oname-%version.tar.xz
Source: %oname-%version.tar
Patch0: tslib-fix-getopt-long-option-terminators.patch

BuildRequires: gcc-c++ glibc-devel libSDL2-devel

%description
Hardware independent touchscreen access library.

%package -n tslib
Group: System/Libraries
Summary: %name library
#Requires: %name-common = %EVR
Provides: libts = %EVR
Obsoletes: libts < %EVR
%description -n tslib
Hardware independent touchscreen access library utils.

%package -n %libts
Group: System/Libraries
Summary: %name library
#Requires: %name-common = %EVR
%description -n %libts
%name library.

%package devel
Summary: Development library and headers for %name
Group: Development/C
%description devel
Development files (headers etc.) for %name.

%prep
%setup -n %oname-%version
%patch0 -p1
%__subst 's,^# module_raw input$,module_raw input,' etc/ts.conf
# For quick verification during building:
grep "module_raw input" etc/ts.conf

%build
./autogen.sh
%configure --with-plugindir=%plugindir --with-sdl2
%make_build

%install
%makeinstall_std
rm -f %buildroot%plugindir/*.la

%files -n tslib
%doc README AUTHORS ChangeLog
%config(noreplace) %_sysconfdir/ts.conf
%_bindir/ts_*
%dir %plugindir
%plugindir/*.so
%_man1dir/*
%_man5dir/*

%files -n %libts
%doc README AUTHORS ChangeLog
%_libdir/libts.so.%sover
%_libdir/libts.so.*

%files devel
%_libdir/*.so
%_includedir/tslib.h
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Fri Oct 09 2026 Vitaly Lipatov <lav@altlinux.ru> 1.24-alt1
- new version 1.24
- update project and source URLs after the Berlios closure.
- include upstream fixes for dejitter error cleanup and ts_conf input bounds.
- fix SIGSEGV on unrecognised long options (getopt_long terminator).

* Tue Oct 06 2020 Sergey V Turchin <zerg@altlinux.org> 1.22-alt3
- fix requires

* Tue Oct 06 2020 Sergey V Turchin <zerg@altlinux.org> 1.22-alt2
- split library to separate package
- package manpages

* Wed Sep 23 2020 Sergey V Turchin <zerg@altlinux.org> 1.22-alt1
- new version

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Jan 10 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus (thanks, Mandriva)

* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0-5mdv2010.0
+ Revision: 445562
- rebuild

* Sat Feb 28 2009 Anssi Hannula <anssi@mandriva.org> 1.0-4mdv2009.1
+ Revision: 346002
- fix build with glibc 2.8 (patch from debian)
- spec file cleaning

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Jul 16 2007 Anssi Hannula <anssi@mandriva.org> 1.0-1mdv2008.0
+ Revision: 52350
- initial Mandriva Linux release based on .spec from Gary Greene
  <greeneg@tolharadys.net>

