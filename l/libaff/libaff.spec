%define oname afflib

Name: libaff
Version: 3.6.8
Release: alt1

Summary: A set of programs for creating and manipulating AFF files

Group: System/Libraries
License: BSD
Url: http://www.afflib.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.afflib.org/downloads/%oname-%version.tar
Patch0: afflib-shared.diff
Patch1: afflib-no_win32.diff
Patch2: %name-fix-build.patch

# Automatically added by buildreq on Wed Mar 30 2011
BuildRequires: gcc-c++ glibc-devel libcurl-devel libexpat-devel libfuse-devel libncurses-devel libreadline-devel libssl-devel zlib-devel

%description
AFFLIB is an open source library developed by Simson Garfinkel and Basis
Technology that implements the AFF standard. AFFLIB is distributed under
4-clause Berkeley License and may be freely incorporated into both Open
Source and Proprietary software.

In addition to the library, AFFLIB also comes with the AFF Tools, a set of
programs for creating and manipulating AFF files.

%package devel
Summary: Header files for the afflib library
Group: Development/C
Requires: %name = %version-%release

%description devel
AFFLIB is an open source library developed by Simson Garfinkel and Basis
Technology that implements the AFF standard. AFFLIB is distributed under
4-clause Berkeley License and may be freely incorporated into both Open
Source and Proprietary software.

This package contains the header files.

%prep
%setup -n %oname-%version
#%patch0 -p1
#%patch1 -p0
#%patch2

%build
%__subst "s|-static.*||g" tools/Makefile.am lib/Makefile.am
mkdir -p m4
%autoreconf

%configure \
    --enable-libewf=yes \
    --enable-s3=yes \
    --enable-fuse=yes \
    --with-curl=%prefix \
    --enable-qemu=no \
    --disable-static

%make_build

%install
%makeinstall_std

# install headers as well
#install -d %buildroot%_includedir/afflib
#install -m0644 lib/*.h %buildroot%_includedir/afflib/

%files
%_bindir/affcat
%_bindir/affcompare
%_bindir/affcrypto
%_bindir/affrecover
%_bindir/affsign
%_bindir/affverify
%_bindir/affconvert
%_bindir/affcopy
%_bindir/affix
%_bindir/affuse
%_bindir/affinfo
%_bindir/affsegment
%_bindir/affstats
%_bindir/affxml
%_bindir/affdiskprint
%_man1dir/*
%doc AUTHORS BUGLIST.txt COPYING ChangeLog NEWS README* doc/*
%_libdir/*.so.*

%files devel
%dir %_includedir/afflib/
%_includedir/afflib/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Wed Mar 30 2011 Vitaly Lipatov <lav@altlinux.ru> 3.6.8-alt1
- new version (3.6.8) import in git

* Fri Nov 26 2010 Igor Vlasenko <viy@altlinux.ru> 3.5.3-alt1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Sun Dec 13 2009 Vitaly Lipatov <lav@altlinux.ru> 3.5.3-alt1
- new version 3.5.3 (with rpmrb script)

* Fri Aug 28 2009 Vitaly Lipatov <lav@altlinux.ru> 3.3.7-alt1
- new version 3.3.7 (with rpmrb script)

* Fri Nov 07 2008 Vitaly Lipatov <lav@altlinux.ru> 3.3.4-alt1
- initial build for ALT Linux Sisyphus

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 2.3.0-1mdv2008.1
+ Revision: 135817
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 07 2007 Oden Eriksson <oeriksson@mandriva.com> 2.3.0-1mdv2008.0
+ Revision: 81864
- Import afflib

* Fri Sep 07 2007 Oden Eriksson <oeriksson@mandriva.com> 2.3.0-1mdv2008.0
- initial Mandriva package
