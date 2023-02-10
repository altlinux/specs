%global pxbu_major_minor 80

%define optflags_lto %nil

Summary: Online backup for InnoDB/XtraDB in MySQL, Percona Server and MariaDB
Name: percona-xtrabackup%pxbu_major_minor
Version: 8.0.31
Release: alt1
License: GPLv2 and LGPLv2
Url: http://www.percona.com/software/percona-xtrabackup/
Group: Databases
Source: %name-%version.tar
Source1: boost_1_77_0.tar.bz2
Source2: libkmip.tar
Patch0: percona-xtrabackup-8.0.28-missing-memory-header.patch
Patch2000: percona-xtrabackup-e2k.patch

Obsoletes: xtrabackup < 2.0.0
Obsoletes: percona-xtrabackup < 8.0.30-alt3
Conflicts: percona-xtrabackup24
# Automatically added by buildreq on Mon Jul 25 2022
# optimized out: alt-os-release cmake-modules glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libgpg-error-devel libncurses-devel libprotobuf-devel libprotobuf27-lite libsasl2-3 libstdc++-devel libtinfo-devel mpdecimal pkg-config python3 python3-base python3-module-Pygments python3-module-alabaster python3-module-babel python3-module-charset-normalizer python3-module-docutils python3-module-idna python3-module-imagesize python3-module-jinja2 python3-module-markupsafe python3-module-packaging python3-module-pytz python3-module-requests python3-module-sphinx python3-module-urllib3 sh4 xz
BuildRequires: cmake gcc-c++ libaio-devel libcurl-devel libev-devel libgcrypt-devel libicu-devel
BuildRequires: libldap-devel libprocps-devel libprotobuf-lite-devel libsasl2-devel libssl-devel libudev-devel
BuildRequires: protobuf-compiler python3-dev python3-module-sphinx-sphinx-build-symlink
BuildRequires: python3-module-sphinxcontrib-applehelp python3-module-sphinxcontrib-devhelp
BuildRequires: python3-module-sphinxcontrib-htmlhelp python3-module-sphinxcontrib-qthelp
BuildRequires: python3-module-sphinxcontrib-serializinghtml python3-tools xxd
BuildRequires: zlib-devel libzstd-devel

ExcludeArch: ppc64le %ix86 %arm %mips32 ppc

%description
Online backup for InnoDB/XtraDB in MySQL, MariaDB and Percona Server.

%prep
%setup -n %name-%version
%patch0 -p1

%ifarch %e2k
%patch2000 -p1
sed -i "/using __base/{N;N;s/^.*using __base.*EncodeBase.*friend __base.*$/EncodeBase_EDG/}" router/src/mysql_protocol/include/mysqlrouter/classic_protocol_codec_*.h
%endif

mkdir -p %_build/../libboost
cp %SOURCE1 %_build/../libboost/
tar xfv %SOURCE2 -C extra
pathfix.py -pni "%__python3 -s" . ./storage/innobase/xtrabackup/test/subunit2junitxml

%build
%cmake -DWITH_BOOST=libboost -DBUILD_CONFIG=xtrabackup_release -DWITH_PROTOBUF=system \
  -DCMAKE_INSTALL_PREFIX=%prefix -DWITH_SSL=system -DINSTALL_MANDIR=%_mandir -DWITH_MAN_PAGES=1 \
  -DINSTALL_MYSQLTESTDIR=%_datadir/percona-xtrabackup-test-%pxbu_major_minor \
  -DINSTALL_PLUGINDIR="%_lib/xtrabackup/plugin" -DFORCE_INSOURCE_BUILD=1 \
  -DWITH_ZLIB=system -DWITH_ZSTD=system \
  -DWITH_ICU=system

%cmake_build

%install
%cmake_install
rm -rf %buildroot/usr/docs/INFO_SRC
rm -rf %buildroot/usr/lib/private/libprotobuf*
rm -rf %buildroot/usr/lib/libmysqlservices.a
rm -rf %buildroot%_datadir/percona-xtrabackup-test-%pxbu_major_minor
rm -rf %buildroot%_libdir/libmysqlservices.a
rm -rf %buildroot%_mandir/man8
rm -rf %buildroot%_mandir/man1/c*
rm -rf %buildroot%_mandir/man1/m*
rm -rf %buildroot%_mandir/man1/i*
rm -rf %buildroot%_mandir/man1/l*
rm -rf %buildroot%_mandir/man1/p*
rm -rf %buildroot%_mandir/man1/z*
rm -rf %buildroot%_libdir/private
rm -rf %buildroot%_libdir/debug/usr/lib64/xtrabackup/plugin

%files
%_bindir/xtrabackup
%_bindir/xbstream
%_bindir/xbcrypt
%_bindir/xbcloud
%_bindir/xbcloud_osenv
%doc README.md XB_VERSION LICENSE
%_mandir/man1/xtrabackup.1.*
%_mandir/man1/xbstream.1.*
%_mandir/man1/xbcrypt.1.*
%_libdir/xtrabackup

%changelog
* Fri Feb 10 2023 Alexei Takaseev <taf@altlinux.org> 8.0.31-alt1
- 8.0.31-24

* Tue Dec 20 2022 Alexei Takaseev <taf@altlinux.org> 8.0.30-alt3
- Rename to percona-xtrabackup80

* Sun Nov 20 2022 Alexei Takaseev <taf@altlinux.org> 8.0.30-alt2
- Do not pack .gear/ to SRPM tar
- Add e2k patch
- Build with system zlib and libzstd

* Tue Nov 15 2022 Alexei Takaseev <taf@altlinux.org> 8.0.30-alt1
- 8.0.30-23
- Build only 64-bit arch.

* Mon Jul 25 2022 Alexei Takaseev <taf@altlinux.org> 8.0.28-alt1
- Build for ALT Linux Sisyphus

* Sat Jul 31 2021 Sven Lankes <sven@lank.es> - 8.0.25_17-1
- rebase to latest upstream release

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Sven Lankes <sven@lank.es> - 8.0.14-1
- Rebase to new upstream release

* Thu Oct 01 2020 Petr Pisar <ppisar@redhat.com> - 2.3.6-21
- Adapt to new CMake macros (bug #1865206)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-20
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 06 2020 Peter MacKinnon <pmackinn@redhat.com> - 2.3.6-18
- Fixes #1799854

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Carl George <carl@george.computer> - 2.3.6-16
- Remove dependency on python2 rhbz#1738052

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Peter MacKinnon <pmackinn@redhat.com> - 2.3.6-14
- Fixes #1730231

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 2.3.6-12
- Rebuilt for libcrypt.so.2 (#1666033)

* Fri Jan 04 2019 Björn Esser <besser82@fedoraproject.org> - 2.3.6-11
- Add patch to use explicit shebangs, fixes FTBFS for Fedora 30
- Add patch to fix -fpermissive, fixes FTBFS for Fedora 30
- Apply proper buildflags
- Modernize spec-file

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.3.6-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.3.6-7
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 17 2017 Peter MacKinnon <pmackinn@redhat.com> - 2.3.6-3
- Adjustments for GCC 7

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Peter MacKinnon <pmackinn@redhat.com> - 2.3.6-1
- Updated to 2.3.6
- Fixes CVE-2016-6225

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 3 2015 Peter MacKinnon <pmackinn@redhat.com> - 2.2.9-3
- Add an extra provides for version 2.2

* Tue Sep 1 2015 Peter MacKinnon <pmackinn@redhat.com> - 2.2.9-2
- Spec changes from Fedora review

* Fri Jun 12 2015 Peter MacKinnon <pmackinn@redhat.com> - 2.2.9-1
- Updated to 2.2.9 (mariadb 5.5 compatible)

* Thu Oct 31 2013 Stewart Smith <stewart@flamingspork.com> - 2.1.5-1
- Update packaging for Percona XtraBackup 2.1.5 release

* Mon Sep 27 2010 Aleksandr Kuzminsky
- Version 1.4

* Wed Jun 30 2010 Aleksandr Kuzminsky
- Version 1.3 ported on Percona Server 11

* Thu Mar 11 2010 Aleksandr Kuzminsky
- Ported to MySQL 5.1 with InnoDB plugin

* Fri Mar 13 2009 Vadim Tkachenko
- initial release
