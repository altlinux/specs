%define oname tslib
%define plugindir %_libdir/libts-1.0
%define sover 0

Name: libts
Version: 1.22
Release: alt1

Summary: tslib - touchscreen access library

Url: http://developer.berlios.de/projects/tslib/
License: GPL
Group: System/Libraries

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://download.berlios.de/tslib/%oname-%version.tar

BuildRequires: gcc-c++ glibc-devel libSDL2-devel

%description
Hardware independent touchscreen access library.

%package devel
Summary: Development library and headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files (headers etc.) for %name.

%prep
%setup -n %oname-%version
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

%files
%doc README AUTHORS ChangeLog
%config(noreplace) %_sysconfdir/ts.conf
%_bindir/ts_*
%_libdir/lib*.so.%sover
%_libdir/lib*.so.*
%dir %plugindir
%plugindir/*.so

%files devel
%_libdir/*.so
%_includedir/tslib.h
%_pkgconfigdir/*.pc

%changelog
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

