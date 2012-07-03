%def_enable static

Name: libgpg-error
Version: 1.10
Release: alt2

Group: System/Libraries
Summary: Error library for GnuPG and related projects
License: LGPL
URL: http://www.gnupg.org/

Packager: Sergey V Turchin <zerg@altlinux.org>

Source: %name-%version.tar.bz2
Source1: version-script.map
Source2: compat.lds
# PLD
Patch1: libgpg-error-am18.patch
# ALT
Patch10: libgpg-error-1.8-alt-version-script.patch

# Automatically added by buildreq on Wed Jun 02 2010 (-bi)
#BuildRequires: cvs glibc-devel-static libsubversion-auth-gnome-keyring libsubversion-auth-kwallet rpm-build-qt4 subversion
BuildRequires: cvs glibc-devel
%if_enabled static
BuildRequires: glibc-devel-static
%endif

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
#%patch1 -p1
%patch10 -p1

install -m 0644 %SOURCE1 src/
install -m 0644 %SOURCE2 src/
%autoreconf

%build
%configure %{subst_enable static} --disable-rpath
%make_build
%make check

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%_libdir/lib*.so.*
%_bindir/gpg-error
%doc AUTHORS ChangeLog NEWS README

%files devel
%_bindir/*-config
%_libdir/*.so
%_includedir/*
%_datadir/aclocal/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
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
