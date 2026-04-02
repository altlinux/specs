# check needs https://github.com/google/googletest/archive/master.zip
# extracted to manticore/googletest
%def_disable check

Name: manticore
Version: 17.5.1
Release: alt1

Summary: Manticore full-text search server

License: GPLv2
Group: Text tools
Url: https://manticoresearch.com

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/manticoresoftware/manticoresearch/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar
Source2: %name-files-%version.tar

Patch1: manticore-system-xxhash-pkgconfig.patch
Patch2: manticore-uni-algo-no-freebsd-ifdef.patch

Conflicts: mnogosearch
Conflicts: sphinx

ExclusiveArch: x86_64

BuildRequires: flex
BuildRequires: boost-context-devel boost-filesystem-devel boost-asio-devel boost-devel-headers
BuildRequires: libexpat-devel libmysqlclient-devel libre2-devel libssl-devel libunixODBC-devel libstemmer-devel postgresql-devel zlib-devel
BuildRequires: nlohmann-json-devel libuni-algo-devel cctz-devel libxxhash-devel libzstd-devel libcurl-devel
BuildRequires: libicu-devel
BuildRequires: libmanticore-columnar-devel >= 10.2.0
BuildRequires: libroaring-devel

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake >= 3.17
BuildRequires: gcc-c++
BuildRequires: /proc

%if_enabled check
BuildRequires: ctest php mysql python3
%endif

%description
Manticore Search is a database designed specifically for search,
including full-text search. What differs it from other solutions is:
* Powerful and fast full-text searching which works fine for small and big datasets
* SQL-first: the native Manticore's syntax is SQL.
  It speaks SQL over HTTP and MySQL protocol (you can use your preferred mysql client)
* JSON over HTTP: to provide more programmatic way to manage your data and
  schemas Manticore provides HTTP JSON protocol. Very similar to the one from Elasticsearch
* Written fully in C++: starts fast, doesn't take much RAM,
  low-level optimizations give good performance
* Real-time inserts: after INSERT is made the document can be read immediately
* Interactive courses for easier learning
* Built-in replication and load balancing
* Can sync from MySQL/PostgreSQL/ODBC/xml/csv out of the box
* Not fully ACID-compliant, but supports transactions and binlog for safe writes

Manticore Search was forked from Sphinx 2.3.2 in 2017.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++

%description -n lib%name-devel
Libraries/include files for development with %name.

%package -n manticore-converter
Summary: Converter from Sphinx 2.x to Manticore Search 3.x format
Group: Text tools

%description -n manticore-converter
This package provides the index_converter tool
for Manticore Search which converts indexes created with Manticore Search 2.x or Sphinx 2.x to
Manticore Search 3.x format.


%prep
%setup
%patch1 -p1
%patch2 -p1
subst 's|#define VERNUMBERS "0.0.0"|#define VERNUMBERS "%version"|' src/sphinxversion.h.in
subst "s|.*Boost_USE_STATIC_LIBS ON.*||" src/CMakeLists.txt
subst "s|.*Boost_USE_STATIC_RUNTIME ON.*||" src/CMakeLists.txt
subst "s|\${CMAKE_INSTALL_LIBDIR}/systemd/system|%_unitdir|g" cmake/builds/CommonRpm.cmake
%if_enabled check
mkdir -p ../cache
cp -r googletest ../cache/googletest-src
%endif

%build
%cmake_insource -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DVERNUMBERS=%version \
    -DWITH_GALERA=OFF \
    -DWITH_MYSQL=ON \
    -DWITH_EXPAT=ON \
    -DWITH_POSTGRESQL=ON \
    -DWITH_ICU=ON \
    -DWITH_ICU_FORCE_STATIC=OFF \
    -DWITH_RE2_FORCE_STATIC=OFF \
    -DWITH_STEMMER_FORCE_STATIC=OFF \
    -DWITH_JEMALLOC=OFF \
    -DWITH_JIEBA=OFF \
    -DSYSCONFDIR=/etc/manticoresearch \
    -DLOCALDATADIR=/var/lib/manticore \
    -DFULL_SHARE_DIR=/usr/share/manticore
%make_build

%check
ctest -C Debug

%install
%makeinstall_std
rm -rv %buildroot/usr/include/manticore/sphinxudf.h 2>/dev/null ||:
rm -rv %buildroot/usr/lib/tmpfiles.d/searchd.conf 2>/dev/null ||:
rm -rv %buildroot/usr/share/doc/%name/ 2>/dev/null ||:
rm -rv %buildroot/%_datadir/%name/api/ 2>/dev/null ||:

# Remove cmake-installed service/tmpfiles - use our own
rm -rf %buildroot%_unitdir/
rm -rf %buildroot/usr/lib/tmpfiles.d/
rm -rf %buildroot%_sysusersdir/

# Install our config, logrotate, service, sysusers
cd %buildroot/
tar xfv %SOURCE2

%pre
%sysusers_create %name.conf

%post
%post_service %name

%preun
%preun_service %name


%files
%doc README.md
%_bindir/indexer
%_bindir/indextool
%_bindir/searchd
%_bindir/spelldump
%_bindir/wordbreaker
%_bindir/manticore_new_cluster
%_datadir/%name/
%_unitdir/*
%dir %_sysconfdir/manticoresearch/
%config(noreplace) %attr(644,root,root) %_sysconfdir/manticoresearch/%name.conf
%_sysusersdir/%name.conf
%_sysconfdir/default/manticore-indexer_global
%_sysconfdir/sysctl.d/70-manticore.conf
%config(noreplace) %_sysconfdir/logrotate.d/%name
%dir %attr(775,root,_manticore) %_var/log/%name/
%dir %attr(775,root,_manticore) %_var/lib/%name/
%_man1dir/*

%files -n lib%name-devel
%_includedir/manticore/

%files -n manticore-converter
%_bindir/index_converter

%changelog
* Tue Mar 31 2026 Vitaly Lipatov <lav@altlinux.ru> 17.5.1-alt1
- new version (17.5.1)
- set correct version via VERNUMBERS
- fix systemd unit: use RuntimeDirectory, correct user _manticore
- replace tmpfiles.d with sysusers.d
- add %%pre with %%sysusers_create to create _manticore user/group before install
- add patch: use system xxhash via pkg-config
- add patch: remove FreeBSD ifdefs around uni-algo calls
- add %%pre with %%sysusers_create to create _manticore user/group before install

* Thu Mar 02 2023 Vitaly Lipatov <lav@altlinux.ru> 6.0.2-alt1
- new version 6.0.2 (with rpmrb script)

* Tue Jul 19 2022 Vitaly Lipatov <lav@altlinux.ru> 5.0.2-alt2
- pack /var/lib/manticore/data dir

* Mon Jun 27 2022 Vitaly Lipatov <lav@altlinux.ru> 5.0.2-alt1
- new version 5.0.2 (with rpmrb script)

* Sat Dec 25 2021 Vitaly Lipatov <lav@altlinux.ru> 4.2.0-alt1
- new version 4.2.0 (with rpmrb script)

* Sat Dec 11 2021 Vitaly Lipatov <lav@altlinux.ru> 4.0.2-alt1
- new version 4.0.2 (with rpmrb script)

* Tue Aug 31 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.6.0-alt2
- added patch for Elbrus
- added check

* Thu May 13 2021 Vitaly Lipatov <lav@altlinux.ru> 3.6.0-alt1
- new version 3.6.0 (with rpmrb script)

* Fri Apr 23 2021 Vitaly Lipatov <lav@altlinux.ru> 3.5.4-alt1
- initial build for ALT Sisyphus
