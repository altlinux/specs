# TODO:
# * STEMMER: broken build with system libs
# * old home dir in rpm: useradd -M -r -d /var/lib/sphinx
# * JEMALLOC (support in service file?)

# check needs https://github.com/google/googletest/archive/master.zip
# extracted to manticore/googletest
%def_disable check

Name: manticore
Version: 4.0.2
Release: alt1

Summary: Manticore full-text search server

License: GPLv2
Group: Text tools
Url: https://manticoresearch.com

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/manticoresoftware/manticoresearch/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar
Source2: %name-files-%version.tar

Patch: 0001-use-RE2-Options.set_encoding-instead-of-set_utf8.patch
Patch2000: %name-e2k.patch

Conflicts: mnogosearch
Conflicts: sphinx

ExclusiveArch: x86_64

BuildRequires: flex bison
BuildRequires: boost-context-devel boost-devel-headers
BuildRequires: libexpat-devel libmariadb-devel libre2-devel libssl-devel libunixODBC-devel libstemmer-devel postgresql-devel zlib-devel
#BuildRequires: libjemalloc-devel

BuildRequires: libmanticore-columnar-devel

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
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
* Craigslist, Socialgist, PubChem and many others use Manticore
  for efficient searching and stream filtering.

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
#patch -p1
%ifarch %e2k
%patch2000 -p1
%endif
%if_enabled check
mkdir -p ../cache
cp -r googletest ../cache/googletest-src
%endif
subst "s|.*Boost_USE_STATIC_LIBS ON.*||" src/CMakeLists.txt
subst "s|.*Boost_USE_STATIC_RUNTIME ON.*||" src/CMakeLists.txt
# broken usage of CMAKE_INSTALL_PREFIX
subst 's|"/usr"||' CMakeLists.txt
# hack to set correct dirs
#subst 's|SET ( LOCALDATADIR .*|SET ( LOCALDATADIR "/var/lib/manticore" )|' CMakeLists.txt
#subst 's|SET ( FULL_SHARE_DIR .*|SET ( FULL_SHARE_DIR "/usr/share/manticore" )|' CMakeLists.txt

subst "s|find_package(re2|find_package(RE2|" cmake/GetRE2.cmake

# https://github.com/doctest/doctest/issues/473
subst "s|SIGSTKSZ|65635|" src/searchd.cpp

%build
# DISABLE_TESTING=ON need for enable api build
%cmake_insource -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DWITH_GALERA=OFF \
    -DWITH_MYSQL=ON \
    -DWITH_EXPAT=ON \
    -DWITH_POSTGRESQL=ON \
    -DWITH_ICU=OFF \
    -DWITH_ICU_FORCE_STATIC=OFF \
    -DWITH_COLUMNAR=OFF \
    -DWITH_RE2_LIBS=%_libdir \
    -DWITH_RE2_FORCE_STATIC=OFF \
    -DWITH_STEMMER_FORCE_STATIC=OFF \
    -DWITH_STEMMER_LIBS=%_libdir \
    -DWITH_JEMALLOC=OFF \
    -DSYSCONFDIR=/etc/manticoresearch \
    -DLOCALDATADIR=/var/lib/manticore \
    -DFULL_SHARE_DIR=/usr/share/manticore
%make_build

%check
ctest -C Debug

%install
%makeinstall_std
#rm -fv %buildroot%_libdir/debug/usr/bin/*
rm -rv %buildroot/usr/include/manticore/sphinxudf.h
#    /usr/bin/index_converter
rm -rv %buildroot/usr/lib/systemd/system-generators/manticore-search-generator
rm -rv %buildroot/usr/lib/tmpfiles.d/manticore.conf
rm -rv %buildroot/usr/share/doc/%name/
rm -rv %buildroot/%_datadir/%name/api/


cd %buildroot/
tar xfv %SOURCE2

%pre
%_sbindir/groupadd -r -f _%name &>/dev/null
%_sbindir/useradd -r -n -g _%name -d /var/empty -s /bin/false -c "Manticore Searchd pseudo user" _%name >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name


%files
%doc README.md example.sql
%_bindir/indexer
%_bindir/indextool
%_bindir/searchd
%_bindir/spelldump
%_bindir/wordbreaker
#_bindir/manticore_new_cluster
%_datadir/%name/
%_unitdir/*
%dir %_sysconfdir/manticoresearch/
%config(noreplace) %attr(644,root,root) %_sysconfdir/manticoresearch/%name.conf
%_tmpfilesdir/%name.conf
%config(noreplace) %_sysconfdir/logrotate.d/%name
%dir %attr(775,root,_manticore) %_var/log/%name/
%dir %attr(775,root,_manticore) %_var/lib/%name/
%_man1dir/*

%files -n manticore-converter
%_bindir/index_converter

%changelog
* Sat Dec 11 2021 Vitaly Lipatov <lav@altlinux.ru> 4.0.2-alt1
- new version 4.0.2 (with rpmrb script)

* Tue Aug 31 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.6.0-alt2
- added patch for Elbrus
- added check

* Thu May 13 2021 Vitaly Lipatov <lav@altlinux.ru> 3.6.0-alt1
- new version 3.6.0 (with rpmrb script)

* Fri Apr 23 2021 Vitaly Lipatov <lav@altlinux.ru> 3.5.4-alt1
- initial build for ALT Sisyphus
