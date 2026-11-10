%define soname 1
%def_enable ssl
%def_enable zlib
%def_enable lua
%def_enable duktape
%def_with scripting_tests
%def_disable server_stats
%def_disable http2
%def_disable x_dom_socket

Name: civetweb
Version: 1.16
Release: alt4.git588860e

Summary: Embedded C/C++ web server
License: MIT
Group: Networking/WWW

Url: https://github.com/civetweb/civetweb
VCS: https://github.com/civetweb/civetweb
Source: %name-%version.tar
Patch0: %name-%version-upstream.patch
Patch1: %name-%version-%release.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: /proc /dev/pts
BuildRequires: rpm-build-vm iproute2
BuildRequires: ctest libcheck-devel

%if_enabled zlib
BuildRequires: zlib-devel
%endif
%if_enabled ssl
BuildRequires: openssl-devel
%endif
%if_enabled duktape
BuildRequires: libduktape-devel
%endif
%if_enabled lua
BuildRequires: liblua5.3-devel libsqlite3-devel
%endif

%description
Civetweb is an easy to use, powerful, C (C/C++) embeddable web server
with optional CGI, SSL and Lua support.

CivetWeb can be used by developers as a library, to add web server
functionality to an existing application. It can also be used by end
users as a stand-alone web server running on a Windows or Linux PC.
It is available as single executable, no installation is required.

%package devel
Summary: Civetweb C/C++ header files
Group: Development/C
Requires: lib%name%soname = %EVR

%description devel
Civetweb associated header files

%package -n lib%name%soname
Summary: Civetweb shared library
Group: System/Libraries

%description -n lib%name%soname
This package contains the Civetweb shared libraries (C API and C++ wrapper)
used by applications that embed the Civetweb web server.

%prep
%setup
%patch0 -p1
%patch1 -p1

# Strip bundled third-party sources the ALT build does not compile: the
# sqlite3 amalgamation, and the vendored lua/duktape trees (system
# libsqlite3/lua5.3/duktape are used instead). Removing bundled sqlite3.h
# also makes lsqlite3.c compile against the system <sqlite3.h> instead of the
# shadowed 3.50.4 copy, keeping header and library in sync. The compiled Lua
# bindings (lfs, lsqlite3, LuaXML, lua_struct) are kept - they have no system
# package and are embedded into libcivetweb by design.
rm -rf src/third_party/sqlite3.c src/third_party/sqlite3.h \
       src/third_party/lua-5.* src/third_party/duktape-1.*

%build
%cmake . \
    -G "Unix Makefiles" \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_CONFIG=rpmbuild \
    -DCIVETWEB_ENABLE_CXX:BOOL=ON \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DCIVETWEB_BUILD_TESTING:BOOL=ON \
    -DCIVETWEB_ENABLE_WEBSOCKETS:BOOL=ON \
    -DCIVETWEB_THREAD_STACK_SIZE=0 \
    -DCIVETWEB_ENABLE_ASAN:BOOL=OFF \
%if_enabled lua
    -DCIVETWEB_ENABLE_LUA:BOOL=ON \
    -DCIVETWEB_ENABLE_LUA_SHARED:BOOL=ON \
%endif
%if_enabled ssl
    -DCIVETWEB_ENABLE_SSL:BOOL=ON \
    -DCIVETWEB_ENABLE_SSL_DYNAMIC_LOADING:BOOL=OFF \
%endif
%if_enabled zlib
    -DCIVETWEB_ENABLE_ZLIB:BOOL=ON \
%endif
%if_enabled duktape
    -DCIVETWEB_ENABLE_DUKTAPE:BOOL=ON \
%endif
%if_enabled server_stats
    -DCIVETWEB_ENABLE_SERVER_STATS:BOOL=ON \
%endif
%if_enabled http2
    -DCIVETWEB_ENABLE_HTTP2:BOOL=ON \
%endif
%if_enabled x_dom_socket
    -DCIVETWEB_ENABLE_UNIX_DOMAIN_SOCKETS:BOOL=ON \
%endif
%nil

%cmake_build

%check
# Excluded: minimal-http(s)-client connect to github.com/google.com (external DNS unavailable)
# IPv6 loopback: iproute2 in BuildRequires; ip link set lo up then ::1 becomes reachable
# SSL cert tests fixed: WORKING_DIRECTORY=${CMAKE_SOURCE_DIR} + LOCAL_TEST (patch 0004)
# init-library fixed: NO_SSL_DL (direct OpenSSL linking, no dlopen)
# server-requests needs cgi_test.cgi pre-built (not a CMake target)
# scripting tests (lua-script, sqlite-script, lua-extras-script, duktape-script): enabled by default, skip with --without scripting_tests
mkdir -p output
%__cc %optflags -o output/cgi_test.cgi unittest/cgi_test.c
# The installed CMake package must work for C and C++ consumers
cmake -S test/cmake-consumer -B consumer-build \
    -DCMAKE_PREFIX_PATH=%buildroot%_prefix
cmake --build consumer-build
LD_LIBRARY_PATH=%buildroot%_libdir \
    ctest --test-dir consumer-build --output-on-failure
cd %_cmake__builddir
%if_with scripting_tests
CTEST_EXCLUDE='test-publicserver-minimal-https?-client|test-publicserver-start-stop-http-server-ipv6'
%else
CTEST_EXCLUDE='test-publicserver-minimal-https?-client|test-publicserver-start-stop-http-server-ipv6|test-publicserver-lua-script|test-publicserver-sqlite-script|test-publicserver-lua-extras-script|test-publicserver-duktape-script'
%endif
CTEST_OUTPUT_ON_FAILURE=1 ctest -E "$CTEST_EXCLUDE"
vm-run --kvm=cond --sbin \
    "ip link set lo up; cd $PWD && CTEST_OUTPUT_ON_FAILURE=1 ctest -R test-publicserver-start-stop-http-server-ipv6"

%install
%cmake_install

%files
%_bindir/civetweb
%doc README.md RELEASE_NOTES.md SECURITY.md

%files -n lib%name%soname
%_libdir/libcivetweb.so.%soname.*
%_libdir/libcivetweb-cpp.so.%soname.*

%files -n %name-devel
%_includedir/*.h
%_libdir/cmake/civetweb
%_libdir/libcivetweb.so
%_libdir/libcivetweb-cpp.so
%_pkgconfigdir/*.pc

%changelog
* Mon Nov 09 2026 Andrey Kuznetcov <morgonf@altlinux.org> 1.16-alt4.git588860e
- fix request handling bugs, sent upstream:
  * multipart file names with spaces, broken by the CVE-2025-9648 fix
    (PR #1447)
  * more than 64 request headers silently dropped (PR #1448)
  * chunk sizes overflowing the request content length (PR #1449)
  * request bytes echoed in the response status line (PR #1457)
  * websocket frames with reserved opcodes or long control frames
    (PR #1458)
  * read errors in the Duktape conn.read() binding (PR #1459)
  * websocket connection kept open after a partial frame write
    (PR #1460)
  * Content-Length near INT64_MAX keeping a keep-alive connection
    with an unread body (PR #1461)
  * uninitialised length in the Lua mg.base64_decode() (PR #1462)
  * unchecked hash and lost :include= lines when modifying the
    passwords file (PR #1463)
  * endless loop in mg_get_cookie() with an empty name (PR #1467)
  * crash on an empty Lua server page (PR #1466)
  * unchecked allocation in WebDAV MOVE and COPY (PR #1468)
- backport upstream PRs #1443, #1451 (httpoxy), #1454, #1455, #1414,
  PR #1442 and PR #1415
- fix the installed CMake package: pkg-config targets of the system Lua,
  SQLite and Duktape leaked into civetweb::civetweb and broke every
  consumer since 1.16-alt2; %%check now builds C and C++ consumers
  (test from PR #1465)
- %%check now runs 69 tests

* Mon Jul 20 2026 Andrey Kuznetcov <morgonf@altlinux.org> 1.16-alt3.git588860e
- fix remote stack-buffer-overflow in mg_handle_form_request() multipart
  preamble scan (upstream issue #1404); add a regression test
- fix integer underflow in mg_handle_form_request() multipart field value
  length: a boundary located before the part body made (size_t)(next - hend)
  wrap, causing an out-of-bounds stack read (remote DoS); add a regression test
- fix infinite loop in mg_handle_form_request() URL-encoded body loop: a
  truncated body ending in a non-consumable fragment kept the loop spinning
  after EOF, burning CPU (remote DoS, distinct from CVE-2025-9648)
- the multipart field value and URL-encoded loop fixes sent upstream as
  PR #1411
- build LuaSQLite3 against the system libsqlite3 instead of the bundled
  amalgamation (BuildRequires: libsqlite3-devel)
- register the bundled Lua modules (sqlite3, lfs, LuaXML, struct) into the Lua
  state at Makefile parity; harden the LuaXML parser for static analysis
- add sqlite and lua-extras integration tests; %%check now runs 55 tests
- keep the upstream 1.16 tarball and ship the post-1.16 upstream delta as a
  separate patch, so the source archive stays the released version
- drop redundant BuildRequires on make

* Tue Jun 09 2026 Andrey Kuznetcov <morgonf@altlinux.org> 1.16-alt2.git588860e
- update to upstream git snapshot 588860e (post-1.16 master)
- Fixes:
  * CVE-2026-5789: unquoted search path in Windows service installer
  * CVE-2025-55763: heap overflow in URI directory slash redirection
  * CVE-2025-9648: infinite loop on NUL byte in POST form data (CPU DoS)
- fix get_request() compile error in the snapshot: broken if condition and
  undeclared 'cl' introduced by the chunked encoding refactoring commit
  (sent upstream as PR #1400)
- fix svace null-after-deref and use-after-free in civetweb.c; http2.inl
  single-argument variadic macros and static globals for LTO; worker thread
  stack size 100 KB -> system default (sent upstream as PR #1396, PR #1397
  and PR #1398; not merged yet)
- build against system libraries (libcheck, Lua 5.3, Duktape) instead of
  bundled GitHub downloads
- enable Lua and Duktape scripting and WebSocket; add cmake options for
  HTTP/2 and Unix domain sockets (off by default)
- add %%check: 51 unit and integration tests (Lua, Duktape, WebSocket,
  OpenSSL 3.x); IPv6 server test via vm-run

* Sun Jul 02 2023 Andrey Kuznetcov <morgonf@altlinux.org> 1.16-alt1
- Initial build for Sisyphus (based on fedora spec)
  + patch CmakeLists.txt to add project version explicitly
