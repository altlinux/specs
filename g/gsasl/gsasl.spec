Name: gsasl
# Taken from gsasl/configure.ac: LT_CURRENT - LT_AGE.
# Look for `AC_SUBST(LT_CURRENT, *)`, etc. in the source.
%define soversion 18
%define libnso lib%name%soversion
%define libname lib%name
Version: 2.2.1
Release: alt2

Summary: GNU SASL implementation
Group: System/Libraries
License: GPLv3+
Url: http://www.gnu.org/software/gsasl/
# ftp://ftp.gnu.org/gnu/%name/%name-%version.tar.gz
Source: %name-%version.tar

Requires: %libnso = %version-%release

# Automatically added by buildreq on Thu Dec 08 2011
BuildRequires: gtk-doc libgnutls-devel libidn-devel libkrb5-devel libntlm-devel libreadline-devel
BuildRequires: libgcrypt-devel
BuildRequires: texinfo

%description
GNU SASL is an implementation of the Simple Authentication and
Security Layer framework and a few common SASL mechanisms.

%package -n %libnso
Summary: GNU SASL library
Group: System/Libraries
License: LGPLv2+
# The previous versions of this subpackage had non-SLP-compliant names. Make
# apt push them out on upgrades.
Obsoletes: lib%name < 2.2.1-alt1

%description -n %libnso
GNU SASL is an implementation of the Simple Authentication and
Security Layer framework and a few common SASL mechanisms.

This package contains the %libnso runtime library.

%package -n lib%name-devel
Summary: Files for development of lib%name-based applications
Group: Development/C
Requires: %libnso = %version-%release

%description -n lib%name-devel
This package contains files for development of applications
which will use lib%name.

%prep
%setup
sed -i 's/^AM_CPPFLAGS +=/& \$(GSS_CFLAGS)/' lib/gl/Makefile.*

# Use gnulib largefile module in the library as well.
sed -i '/AC_REQUIRE(\[gl_USE_SYSTEM_EXTENSIONS\])/a AC_REQUIRE([AC_SYS_LARGEFILE])' \
	lib/m4/gnulib-comp.m4

%build
%autoreconf
%configure \
	--disable-static \
	--enable-shared \
	--disable-rpath \
	--disable-silent-rules \
	--with-libgcrypt \
	--with-gssapi-impl=mit \
	--disable-obsolete
%make_build

%install
%makeinstall_std
%find_lang %name
sed -i '/libgsasl\.mo/d' %name.lang
%find_lang %libnso

%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

%check
%make_build -k check

%files -f %name.lang
%_bindir/*
%_man1dir/*
%doc AUTHORS NEWS README THANKS

%files -n %libnso -f %libnso.lang
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*.h
%_pkgconfigdir/*.pc
%_infodir/*
%_man3dir/*

%changelog
* Mon Oct 14 2024 Arseny Maslennikov <arseny@altlinux.org> 2.2.1-alt2
- Explicitly push out earlier versions of the libgsasl package. (Closes: 51714)
  Not sure why apt does not deal with this automatically.

* Wed Oct 09 2024 Arseny Maslennikov <arseny@altlinux.org> 2.2.1-alt1
- 2.2.0 -> 2.2.1.
- Moved libgsasl.so to a SharedLibsPolicy-compliant subpackage.

* Sun Oct 29 2023 Arseny Maslennikov <arseny@altlinux.org> 2.2.0-alt1
- 1.8.0 -> 2.2.0.

* Mon Dec 10 2018 Dmitry V. Levin <ldv@altlinux.org> 1.8.0-alt3
- Built the library with LFS support.

* Tue Jan 12 2016 Mikhail Efremov <sem@altlinux.org> 1.8.0-alt2
- Fixed build: disable couple of gnulib tests.

* Wed Nov 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1.1
- Fixed build

* Tue Apr 09 2013 Dmitry V. Levin <ldv@altlinux.org> 1.8.0-alt1
- Updated to 1.8.0.

* Fri Dec 09 2011 Dmitry V. Levin <ldv@altlinux.org> 1.6.1-alt1
- Updated to 1.6.1.

* Mon Oct 04 2010 Sergey V Turchin <zerg@altlinux.org> 1.4.4-alt1
- new version (ALT#24193)

* Mon Mar 02 2009 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt1
- new version

* Mon Nov 17 2008 Sergey V Turchin <zerg at altlinux dot org> 0.2.29-alt1
- new version

* Mon May 26 2008 Sergey V Turchin <zerg at altlinux dot org> 0.2.26-alt2
- fix requires

* Fri May 23 2008 Sergey V Turchin <zerg at altlinux dot org> 0.2.26-alt1
- new version

* Wed Apr 30 2008 Sergey V Turchin <zerg at altlinux dot org> 0.2.25-alt1
- new version
- fix %%license

* Tue Mar 04 2008 Sergey V Turchin <zerg at altlinux dot org> 0.2.24-alt1
- new version

* Fri Jan 11 2008 Sergey V Turchin <zerg at altlinux dot org> 0.2.21-alt2
- remove libkeyutils-devel from BuildRequires (#13977)

* Wed Jan 09 2008 Sergey V Turchin <zerg at altlinux dot org> 0.2.21-alt1
- initial specfile

