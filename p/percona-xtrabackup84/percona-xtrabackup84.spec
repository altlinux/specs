%global pxbu_major_minor 84

%def_with man

Summary: Online backup for InnoDB/XtraDB in MySQL, Percona Server and MariaDB
Name: percona-xtrabackup%pxbu_major_minor
Version: 8.4.0
Release: alt2
License: GPLv2 and LGPLv2
Url: http://www.percona.com/software/percona-xtrabackup/
Group: Databases
Source: %name-%version.tar
Source2: libkmip.tar
Patch0: percona-xtrabackup-8.0.28-missing-memory-header.patch
Patch2000: percona-xtrabackup-e2k.patch

Obsoletes: xtrabackup < 2.0.0
Obsoletes: percona-xtrabackup < 8.0.30-alt3
Conflicts: percona-xtrabackup24
Conflicts: percona-xtrabackup80

# Automatically added by buildreq on Tue Jun 02 2026
BuildRequires: cmake doxygen gcc-c++ libaio-devel libcurl-devel libev-devel libfido2-devel libgcrypt-devel
BuildRequires: libicu-devel libldap-devel liblz4-devel libncurses-devel libproc2-devel libprotobuf-lite-devel
BuildRequires: libsasl2-devel libzstd-devel python3-dev libtirpc-devel python3-module-sphinx
%ifarch x86_64
BuildRequires: libquadmath-devel
%endif

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

tar xfv %SOURCE2 -C extra/libkmip

%build
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%cmake -DWITH_BOOST=libboost -DBUILD_CONFIG=xtrabackup_release -DWITH_PROTOBUF=system \
  -DCMAKE_INSTALL_PREFIX=%prefix -DWITH_SSL=system -DINSTALL_MANDIR=%_mandir -DWITH_MAN_PAGES=1 \
  -DINSTALL_MYSQLTESTDIR=%_datadir/percona-xtrabackup-test-%pxbu_major_minor \
  -DINSTALL_PLUGINDIR="%_lib/xtrabackup/plugin" -DFORCE_INSOURCE_BUILD=1 \
%if_without man
   -DWITH_MAN_PAGES=FALSE \
%endif
  -DWITH_CURL=system \
  -DWITH_FIDO=system \
  -DWITH_ICU=system \
  -DWITH_LZ4=system \
  -DWITH_ZLIB=system \
  -DWITH_ZSTD=system

%cmake_build

%install
%cmake_install
rm -rf %buildroot/usr/docs/INFO_SRC
rm -rf %buildroot/usr/lib/private/libprotobuf*
rm -rf %buildroot/usr/lib/libmysqlservices.a
rm -rf %buildroot%_datadir/percona-xtrabackup-test-%pxbu_major_minor
rm -rf %buildroot%_libdir/libmysqlservices.a
rm -rf %buildroot%_man8dir
rm -rf %buildroot%_man1dir/c*
rm -rf %buildroot%_man1dir/m*
rm -rf %buildroot%_man1dir/i*
rm -rf %buildroot%_man1dir/l*
rm -rf %buildroot%_man1dir/p*
rm -rf %buildroot%_man1dir/z*
rm -rf %buildroot%_libdir/private
rm -rf %buildroot%_libdir/debug/usr/lib64/xtrabackup/plugin

%files
%_bindir/xtrabackup
%_bindir/xbstream
%_bindir/xbcrypt
%_bindir/xbcloud
%_bindir/xbcloud_osenv
%doc README.md XB_VERSION LICENSE
%if_with man
%_man1dir/xtrabackup.1*
%_man1dir/xbstream.1*
%_man1dir/xbcrypt.1*
%endif
%_libdir/xtrabackup

%changelog
* Thu Jun 25 2026 Alexei Takaseev <taf@altlinux.org> 8.4.0-alt2
- 8.4.0-6
- Add BR: libtirpc-devel
- Enable LTO
- Build with manpages

* Tue Jun 02 2026 Alexei Takaseev <taf@altlinux.org> 8.4.0-alt1
- Build for MySQL 8.4

* Mon Jan 26 2026 Alexei Takaseev <taf@altlinux.org> 8.0.35-alt8
- 8.0.35-35

* Sat Oct 11 2025 Alexei Takaseev <taf@altlinux.org> 8.0.35-alt7
- Fix FTBS: add BR libncurses-devel

* Tue Aug 12 2025 Alexei Takaseev <taf@altlinux.org> 8.0.35-alt6
- 8.0.35-34

* Mon May 19 2025 Alexei Takaseev <taf@altlinux.org> 8.0.35-alt5
- 8.0.35-33
- Build with system lz4

* Fri Jan 10 2025 Alexei Takaseev <taf@altlinux.org> 8.0.35-alt4
- 8.0.35-32

* Fri Jun 21 2024 Alexei Takaseev <taf@altlinux.org> 8.0.35-alt3
- 8.0.35-31

* Mon Jan 22 2024 Alexei Takaseev <taf@altlinux.org> 8.0.35-alt2
- Fix build with python 3.12

* Thu Dec 14 2023 Alexei Takaseev <taf@altlinux.org> 8.0.35-alt1
- 8.0.35-30
- Drop percona-xtrabackup80-8.0.33-fix-gcc13.patch fixed in upstream

* Thu Oct 12 2023 Alexei Takaseev <taf@altlinux.org> 8.0.34-alt2
- Change BR: libprocps-devel -> libproc2-devel

* Tue Aug 22 2023 Alexei Takaseev <taf@altlinux.org> 8.0.34-alt1
- 8.0.33-29
- Drop percona-xtrabackup80-8.0.33-fix-zlib.patch fix on upstream

* Thu Jul 20 2023 Alexei Takaseev <taf@altlinux.org> 8.0.33-alt3
- 8.0.33-28

* Thu Jun 22 2023 Alexei Takaseev <taf@altlinux.org> 8.0.33-alt2
- Fix build with GCC 13

* Fri May 26 2023 Alexei Takaseev <taf@altlinux.org> 8.0.33-alt1
- 8.0.33-27

* Fri Apr 21 2023 Alexei Takaseev <taf@altlinux.org> 8.0.32-alt3
- Fix build, disable man files

* Wed Apr 05 2023 Alexei Takaseev <taf@altlinux.org> 8.0.32-alt2
- 8.0.32-26

* Tue Feb 28 2023 Alexei Takaseev <taf@altlinux.org> 8.0.32-alt1
- 8.0.32-25

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
