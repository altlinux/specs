%def_disable static

Name: libksba
Version: 1.2.0
Release: alt1

Group: System/Libraries
Summary: X.509 library
URL: http://www.gnupg.org/
License: GPL

Requires: libgpg-error >= 0.6


Source0: %name-%version.tar.bz2
Patch1:		%{name}-info.patch
Patch2:		%{name}-link.patch
# ALT
Patch10: libksba-1.0.2-alt-dont-req-new-tools.patch

# Automatically added by buildreq on Tue Apr 06 2004 (-bi)
#BuildRequires: gcc-c++ gcc-g77 libgcrypt-devel libgpg-error-devel libstdc++-devel
BuildRequires: gcc-c++ libgcrypt-devel libstdc++-devel
BuildRequires: libgpg-error-devel >= 0.6

%description
KSBA is a library designed to build software based
on the X.509 and CMS protocols.

%package -n %name-devel
Summary: Development files for the %name package
Group: Development/Other
Requires: %name = %version-%release
%description -n %name-devel
Development files for the %name package

%package -n %name-devel-static
Summary: Static libraries for the %name-devel package
Group: Development/Other
Requires: %name-devel = %version-%release
Requires: glibc-devel-static
%description -n %name-devel-static
Static libraries for the %name-devel package

%prep
%setup -q
%patch1 -p1
#%patch2 -p1
%patch10 -p1

#__aclocal
#__autoconf
#__automake
./autogen.sh

%build
%configure \
    %{subst_enable static} \
    --enable-ld-version-script
%make_build

%install
%makeinstall
#rm -fv %buildroot/usr/share/info/dir


%files
%doc AUTHORS NEWS README 
%_libdir/*.so.*

%files -n %name-devel
%doc TODO ChangeLog
%_bindir/*
%prefix/share/aclocal/*
%prefix/include/*.h
#%_libdir/*.la
%_libdir/*.so
%_infodir/*.info*

%if_enabled static
%files -n %name-devel-static
%_libdir/*.a
%endif

%changelog
* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt1
- new version

* Mon Dec 06 2010 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt1
- new version

* Fri Jul 23 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.8-alt0.M51.1
- built for M51

* Wed Jul 21 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.8-alt1
- new version

* Sun Jan 11 2009 Sergey V Turchin <zerg at altlinux dot org> 1.0.5-alt1
- new version
- remove deprecated macroses from specfile

* Tue Sep 23 2008 Sergey V Turchin <zerg at altlinux dot org> 1.0.4-alt1
- new version

* Thu Feb 14 2008 Sergey V Turchin <zerg at altlinux dot org> 1.0.3-alt1
- new version

* Tue Jul 10 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0.2-alt1
- new version

* Tue Jan 30 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0.1-alt1
- new version

* Fri Sep 01 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.0-alt1
- new version

* Fri Jan 20 2006 Sergey V Turchin <zerg at altlinux dot org> 0.9.13-alt1
- new version

* Tue Jun 21 2005 Sergey V Turchin <zerg at altlinux dot org> 0.9.11-alt1
- new version

* Mon Oct 11 2004 Sergey V Turchin <zerg at altlinux dot org> 0.9.9-alt1
- new version

* Fri Apr 16 2004 Sergey V Turchin <zerg at altlinux dot org> 0.9.5-alt1
- new version

* Mon Apr 05 2004 Sergey V Turchin <zerg at altlinux dot org> 0.9.4-alt1
- new version
- sync patches with PLD

* Fri Nov 28 2003 Sergey V Turchin <zerg at altlinux dot org> 0.4.7-alt2
- remove *.la files

* Wed Sep 03 2003 Sergey V Turchin <zerg at altlinux dot org> 0.4.7-alt1
- new version

* Fri Feb 07 2003 Sergey V Turchin <zerg@altlinux.ru> 0.4.6-alt2
- fix requires

* Fri Feb 07 2003 Sergey V Turchin <zerg@altlinux.ru> 0.4.6-alt1
- build for ALT

* Wed Dec 11 2002 Fabrice MARIE <fabrice-marie-sec@ifrance.com> 0.4.6-1mdk
- update to version 0.4.6

* Sat Oct 19 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 0.4.5-1mdk
- First package

