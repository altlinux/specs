%def_enable static

Name: libgpg-error
Version: 1.29
Release: alt1%ubt

Group: System/Libraries
Summary: Error library for GnuPG and related projects
License: LGPL
URL: http://www.gnupg.org/

Packager: Sergey V Turchin <zerg@altlinux.org>

Source: %name-%version.tar.bz2

BuildRequires(pre): rpm-build-ubt
BuildRequires: glibc-devel
%if_enabled static
BuildRequires: glibc-devel-static
%endif
# explicitly added texinfo for info files
BuildRequires: texinfo

%package devel
Summary: Development files for the %name package
Group: Development/C
Requires: %name = %version-%release

%package devel-static
Summary: Static libraries for the %name-devel package
Group: Development/C
Requires: %name-devel = %version-%release

%description
This is a library that defines common error values for all GnuPG
components.  Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt,
pinentry, SmartCard Daemon and possibly more in the future.

%description devel
This package contains files needed to develop
applications using the GnuPG error library.

%description devel-static
Static build of the GnuPG error library.

%prep
%setup -q

%build
%autoreconf
%configure %{subst_enable static} --disable-rpath
%make_build

%install
%makeinstall

# relocate shared libraries from %_libdir/ to /%_lib/.
mkdir -p %buildroot/%_lib
mv -f %buildroot%_libdir/libgpg-error.so.* %buildroot/%_lib
ln -sf ../../%_lib/libgpg-error.so.0 %buildroot%_libdir/libgpg-error.so

%find_lang %name

%check
%make check

%files -f %name.lang
/%_lib/lib*.so.*
%_bindir/gpg-error
%_datadir/libgpg-error/
%doc AUTHORS ChangeLog NEWS README

%files devel
%_bindir/*-config
%_libdir/*.so
%_includedir/*
%_datadir/aclocal/*
%_man1dir/gpg-error-config.*
%_infodir/gpgrt.*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Thu Apr 19 2018 Sergey V Turchin <zerg@altlinux.org> 1.29-alt1%ubt
- new version

* Mon Apr 17 2017 Sergey V Turchin <zerg@altlinux.org> 1.27-alt1%ubt
- new version

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1.1
- NMU: added BR: texinfo

* Wed Aug 26 2015 Sergey V Turchin <zerg@altlinux.org> 1.20-alt1
- new version

* Wed Jun 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.19-alt1
- 1.19
- relocate shared libraries from %_libdir/ to /%_lib/.

* Tue Nov 25 2014 Sergey V Turchin <zerg@altlinux.org> 1.17-alt0.M70P.1
- built for M70P

* Tue Nov 25 2014 Sergey V Turchin <zerg@altlinux.org> 1.17-alt1
- new version

* Thu Jun 19 2014 Sergey V Turchin <zerg@altlinux.org> 1.13-alt0.M70P.1
- built for M70P

* Thu Jun 05 2014 Sergey V Turchin <zerg@altlinux.org> 1.13-alt1
- new version

* Thu Jun 05 2014 Sergey V Turchin <zerg@altlinux.org> 1.12-alt0.M70P.1
- built for M70P

* Thu Dec 19 2013 Sergey V Turchin <zerg@altlinux.org> 1.12-alt1
- new version

* Mon Feb 25 2013 Sergey V Turchin <zerg@altlinux.org> 1.11-alt1
- new version

* Fri Feb 25 2011 Sergey V Turchin <zerg@altlinux.org> 1.10-alt2
- add old versioned symbols to library

* Fri Feb 25 2011 Sergey V Turchin <zerg@altlinux.org> 1.10-alt1
- new version
- clean version script

* Mon Oct 25 2010 Sergey V Turchin <zerg@altlinux.org> 1.9-alt1
- new version

* Mon Jun 07 2010 Sergey V Turchin <zerg@altlinux.org> 1.8-alt0.M51.1
- built for M51

* Wed Jun 02 2010 Sergey V Turchin <zerg@altlinux.org> 1.8-alt1
- new version

* Mon Apr 27 2009 Sergey V Turchin <zerg@altlinux.org> 1.7-alt1
- new version
- remove deprecated macroses from specfile
- built static library

* Tue Sep 16 2008 Sergey V Turchin <zerg at altlinux dot org> 1.6-alt1
- new version

* Tue Dec 26 2006 Sergey V Turchin <zerg at altlinux dot org> 1.5-alt1
- new version

* Fri Sep 15 2006 Sergey V Turchin <zerg at altlinux dot org> 1.4-alt1
- new version

* Fri Apr 14 2006 Sergey V Turchin <zerg at altlinux dot org> 1.3-alt1
- new version

* Tue Jun 21 2005 Sergey V Turchin <zerg at altlinux dot org> 1.1-alt1
- new version

* Mon Oct 11 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt1
- new version

* Mon Apr 05 2004 Sergey V Turchin <zerg at altlinux dot org> 0.7-alt1
- rebuild

* Wed Mar 24 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.7-alt0.1
- New upstream release
- Spec cleanup
- Added /usr/bin/gpg-error to the filelist
- Brushed up descriptions

* Thu Feb 05 2004 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt2
- rebuild

* Mon Feb 02 2004 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt1
- new version
- don't build static libs by default

* Thu Sep 04 2003 Sergey V Turchin <zerg at altlinux dot org> 0.4-alt1
- initial spec
