Name: libaff
Version: 3.7.20
Release: alt1

Summary: A set of programs for creating and manipulating AFF files

Group: System/Libraries
License: BSD
Url: https://github.com/sshock/AFFLIBv3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/sshock/AFFLIBv3/archive/v%version.tar.gz
Source: %name-%version.tar

# Automatically added by buildreq on Wed Mar 30 2011
BuildRequires: gcc-c++ glibc-devel libcurl-devel libexpat-devel libfuse-devel libncurses-devel libreadline-devel libssl-devel zlib-devel

%description
AFFLIB is an open source library developed by Simson Garfinkel and Basis
Technology that implements the AFF standard. AFFLIB is distributed under
4-clause Berkeley License and may be freely incorporated into both Open
Source and Proprietary software.

In addition to the library, AFFLIB also comes with the AFF Tools,
a set of programs for creating and manipulating AFF files.

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

%package -n aff-tools
Summary: AFFLIB tools
Group: File tools
Requires: %name = %version-%release

%description -n aff-tools
AFFLIB is an open source library developed by Simson Garfinkel and Basis
Technology that implements the AFF standard. AFFLIB is distributed under
4-clause Berkeley License and may be freely incorporated into both Open
Source and Proprietary software.

This package contains AFF Tools.

%prep
%setup

%build
mkdir -p m4
%autoreconf

# EWF support has been dropped upstream
%configure \
    --enable-s3=yes \
    --enable-fuse=yes \
    --with-curl=%prefix \
    --enable-qemu=no \
    --disable-static

# Remove rpath from libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# clean unused-direct-shlib-dependencies
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*

%files -n aff-tools
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

%files devel
%dir %_includedir/afflib/
%_includedir/afflib/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 3.7.20-alt1
- new version 3.7.20 (with rpmrb script)

* Mon Aug 10 2020 Vitaly Lipatov <lav@altlinux.ru> 3.7.19-alt1
- new version 3.7.19 (with rpmrb script)

* Tue Mar 05 2019 Vitaly Lipatov <lav@altlinux.ru> 3.7.18-alt1
- new version 3.7.18 (with rpmrb script)

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 3.7.17-alt1
- new version 3.7.17 (with rpmrb script)

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 3.7.16-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 3.7.16-alt1
- new version 3.7.16 (with rpmrb script)

* Sat Apr 08 2017 Vitaly Lipatov <lav@altlinux.ru> 3.7.15-alt1
- new version 3.7.15 (with rpmrb script)

* Sat Sep 24 2016 Vitaly Lipatov <lav@altlinux.ru> 3.7.10-alt1
- new version 3.7.10 (with rpmrb script)

* Tue Jul 26 2016 Vitaly Lipatov <lav@altlinux.ru> 3.7.7-alt1
- new version 3.7.7 (with rpmrb script)

* Sat Apr 19 2014 Michael Shigorin <mike@altlinux.org> 3.7.4-alt1
- 3.7.4
  + borrowed rpath cleanup from fedora's 3.7.3-1 spec
- NB: utilities moved from libaff to aff-tools

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 3.7.2-alt1
- new version 3.7.2 (with rpmrb script)

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
