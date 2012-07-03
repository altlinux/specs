Name: gsasl
%define libname lib%name
Version: 1.6.1
Release: alt1

Summary: GNU SASL implementation
Group: System/Libraries
License: GPLv3+
Url: http://www.gnu.org/software/gsasl/
# ftp://ftp.gnu.org/gnu/%name/%name-%version.tar.gz
Source: %name-%version.tar

Requires: lib%name = %version-%release

# Automatically added by buildreq on Thu Dec 08 2011
BuildRequires: gtk-doc libgnutls-devel libidn-devel libkrb5-devel libntlm-devel libreadline-devel

%description
GNU SASL is an implementation of the Simple Authentication and
Security Layer framework and a few common SASL mechanisms.

%package -n lib%name
Summary: GNU SASL library
Group: System/Libraries
License: LGPLv2+

%description -n lib%name
GNU SASL is an implementation of the Simple Authentication and
Security Layer framework and a few common SASL mechanisms.

This package contains lib%name runtime library.

%package -n lib%name-devel
Summary: Files for development of lib%name-based applications
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains files for development of applications
which will use lib%name.

%prep
%setup
sed -i 's/^AM_CPPFLAGS =/& \$(GSS_CFLAGS)/' lib/gl/Makefile.*

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
%find_lang lib%name

%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

%check
%make_build -k check

%files -f %name.lang
%_bindir/*
%_man1dir/*
%doc lib/AUTHORS lib/NEWS lib/README lib/THANKS

%files -n lib%name -f lib%name.lang
%doc AUTHORS NEWS README THANKS
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*.h
%_pkgconfigdir/*.pc
%_infodir/*
%_man3dir/*

%changelog
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

