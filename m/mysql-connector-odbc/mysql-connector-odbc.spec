# TODO: there is exist driver registration utility, add some macros?
# odbcinst -i -d -f template

Name: mysql-connector-odbc
Version: 8.0.37
Release: alt1

Summary: MySQL Connector/ODBC - ODBC driver for MySQL

# exceptions allow library to be linked with most open source SW,
# not only GPL code.
License: %gpl2only
Group: System/Libraries
Url: https://github.com/mysql/mysql-connector-odbc
# https://dev.mysql.com/doc/connector-odbc/en/

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Source1: odbc.ini
Source2: odbcinst.ini

Patch1: %name-8.0.22-alt-rpath.patch
Patch2: %name-8.0.13-fedora-myodbc-64bit.patch
Patch3: %name-8.0.35-libdir-wtf.patch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Wed Aug 08 2018
# optimized out: cmake-modules glibc-kernheaders-generic glibc-kernheaders-x86 libcrypt-devel libncurses-devel libstdc++-devel libtinfo-devel libunixODBC-devel-compat python-base python-modules python3 python3-base python3-dev ruby
BuildRequires: cmake gcc-c++ glibc-devel-static libmysqlclient21-devel libsasl2-devel libssl-devel libunixODBC-devel

%description
MySQL Connector/ODBC   allows you to connect to MySQL database
servers using ODBC, the Open Database Connectivity abstraction
layer which is understood by a variety of database tools that
cannot talk to MySQL databases directly.

Connector/ODBC documentation for detailed installation and
setup instructions can be found at 
  https://dev.mysql.com/doc/connector-odbc/en/


%prep
%setup
%patch0 -p1

%patch1 -p2
%patch2 -p1
%patch3 -p1

%build
%cmake -G "Unix Makefiles" \
    -DCMAKE_BUILD_TYPE=RelWithDebinfo \
    -DWITH_UNIXODBC=1 \
    -DMYSQLCLIENT_STATIC_LINKING=false \
    -DBUNDLE_DEPENDENCIES=false \
    -DHAVE_STRUCT_TIMESPEC=1 \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DDISABLE_GUI=1 \
    -DRPM_BUILD=1 \
    ..

%cmake_build

%install
%cmakeinstall_std

%ifarch %e2k
# no LIB_SUFFIX reaction
mkdir -p %buildroot%_libdir
mv %buildroot{%_prefix/lib/*,%_libdir} ||:
%endif

install -pm 0644 %SOURCE1 odbc.ini
install -pm 0644 %SOURCE2 odbcinst.ini
sed -e 's#@@lib@@#%_libdir#g' -i odbcinst.ini

rm -f %buildroot/%_prefix/{ChangeLog,README.txt,LICENSE.txt,INFO_BIN,INFO_SRC}

%files
%doc ChangeLog README.txt LICENSE.txt odbcinst.ini odbc.ini INFO_BIN INFO_SRC
%_bindir/myodbc-installer
%_libdir/libmyodbc*
%exclude %_prefix/test

%changelog
* Tue May 21 2024 Nikolai Kostrigin <nickel@altlinux.org> 8.0.37-alt1
- New version

* Thu Jan 18 2024 Nikolai Kostrigin <nickel@altlinux.org> 8.0.36-alt1
- New version

* Sat Nov 18 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 8.0.35-alt2
- NMU: fixed FTBFS on LoongArch (and possibly riscv64)

* Sat Nov 18 2023 Nikolai Kostrigin <nickel@altlinux.org> 8.0.35-alt1
- New version

* Sat Nov 18 2023 Nikolai Kostrigin <nickel@altlinux.org> 8.0.33-alt1
- New version

* Wed Jun 14 2023 Nikolai Kostrigin <nickel@altlinux.org> 8.0.32-alt1
- New version (fixes: CVE-2022-24407)

* Tue Nov 15 2022 Nikolai Kostrigin <nickel@altlinux.org> 8.0.31-alt1
- New version (fixes: CVE-2022-2097)

* Wed Aug 24 2022 Nikolai Kostrigin <nickel@altlinux.org> 8.0.30-alt1
- New version

* Thu May 12 2022 Nikolai Kostrigin <nickel@altlinux.org> 8.0.29-alt1
- New version (fixes: CVE-2022-0778)

* Thu Jan 20 2022 Nikolai Kostrigin <nickel@altlinux.org> 8.0.28-alt1
- New version

* Mon Nov 08 2021 Nikolai Kostrigin <nickel@altlinux.org> 8.0.27-alt1
- New version

* Tue Aug 10 2021 Nikolai Kostrigin <nickel@altlinux.org> 8.0.26-alt1
- New version

* Mon Aug 09 2021 Michael Shigorin <mike@altlinux.org> 8.0.25-alt2
- libsuffix installation problem workaround on e2k

* Tue May 25 2021 Nikolai Kostrigin <nickel@altlinux.org> 8.0.25-alt1
- New version

* Wed May 19 2021 Nikolai Kostrigin <nickel@altlinux.org> 8.0.24-alt1
- New version

* Tue Feb 09 2021 Nikolai Kostrigin <nickel@altlinux.org> 8.0.23-alt1
- New version

* Fri Nov 13 2020 Nikolai Kostrigin <nickel@altlinux.org> 8.0.22-alt1
- New version
- Update alt-rpath patch

* Sun May 17 2020 Nikolai Kostrigin <nickel@altlinux.org> 8.0.20-alt1
- New version

* Thu Feb 20 2020 Nikolai Kostrigin <nickel@altlinux.org> 8.0.19-alt1
- New version
- Remove obsolete fedora-fix-build patch
- Remove obsolete fedora-fix-inconsistency patch
- Remove obsolete prevent-i586-libssl-bundling patch

* Mon Dec 09 2019 Nikolai Kostrigin <nickel@altlinux.org> 8.0.18-alt1
- New version
- Update prevent-i586-libssl-bundling patch
- Add patches fixing build from Fedora

* Wed Oct 02 2019 Nikolai Kostrigin <nickel@altlinux.org> 8.0.15-alt1
- New version
  + INFO_BIN & INFO_SRC introduced by upstream to provide build environment info

* Fri Dec 28 2018 Nikolai Kostrigin <nickel@altlinux.org> 8.0.13-alt2
- Prevent undesired libssl bundling for i586

* Mon Dec 03 2018 Nikolai Kostrigin <nickel@altlinux.org> 8.0.13-alt1
- New version

* Wed Aug 15 2018 Nikolay A. Fetisov <naf@altlinux.org> 5.3.11-alt1
- New version
- Restored from orphaned

* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.8-alt1.1
- Fixed build

* Mon Apr 18 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.8-alt1
- 5.1.8

* Mon Oct 11 2010 Vitaly Lipatov <lav@altlinux.ru> 5.1.5-alt2
- fix build

* Sun Jan 18 2009 Vitaly Lipatov <lav@altlinux.ru> 5.1.5-alt1
- new version

* Sat Jul 26 2008 Vitaly Lipatov <lav@altlinux.ru> 5.1.4r1107-alt1
- new version 5.1.4

* Thu Feb 09 2006 Vitaly Lipatov <lav@altlinux.ru> 3.51-alt1
- rebuild with libMySQL 5.0
- add libssl-devel to build requires

* Wed Jan 04 2006 Vitaly Lipatov <lav@altlinux.ru> 3.51-alt0.1
- initial build for ALT Linux Sisyphus
- disable GUI
- build without MULTI_RESULTS support

