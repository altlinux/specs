%define _unpackaged_files_terminate_build 1

# Node.js 24 LTS, installed side by side with the default node package:
# only versioned names (/usr/bin/node24, /usr/bin/npm24, /usr/include/node24),
# the private prefix /usr/lib/node24 with unversioned node/npm/npx in bin/
# (PATH=/usr/lib/node24/bin:$PATH selects Node.js 24 as node), no alternatives.
%define major 24

%define node_prefix %_prefix/lib/node%major

%define nodejs_soversion 137
%define nodejs_abi %nodejs_soversion

%define v8_version 13.6

# check deps/npm/package.json for it
%define npm_version 11.19.1

# check deps/zlib/zlib.h (chromium fork 1.3.2.1-motley)
%define zlib_version 1.3.1

# check deps/cares/include/ares_version.h
%define c_ares_version 1.34.8

# check deps/llhttp/include/llhttp.h
%define llhttp_version 9.4.3

# check deps/openssl/openssl/include/openssl/opensslv.h
%define openssl_version 3.5

# check deps/uv/include/uv/version.h
%define libuv_version 1.52.1

# check deps/nghttp2/lib/includes/nghttp2/nghttp2ver.h
%define libnghttp2_version 1.70.0

# check tools/icu/icu_versions.json (minimum_icu)
%define libicu_version 7.3

# check deps/ada/ada.h
%define ada_version 4.0.0

# check deps/zstd/lib/zstd.h
%define zstd_version 1.5.7

# check deps/sqlite/sqlite3.h (bundled 3.53.4)
%define sqlite_version 3.53

# bundled: simdjson 4.6.11 (Sisyphus libsimdjson is older),
# simdutf 6.4.0 (Sisyphus simdutf 9.x has another API), uvwasi 0.0.23,
# ngtcp2/nghttp3 (QUIC is experimental), nbytes, merve, hdr-histogram

# TODO: some strange build error
%ifarch armh
%global optflags_lto %nil
%endif

# minimalize memory using (V8 turboshaft units need several GB with full -g)
%ifarch armh
%define optflags_debug -g0
%else
%define optflags_debug -g1
%endif

%def_disable check

Name: node%major
Version: %major.22.0
Release: alt1

Summary: Evented I/O for V8 Javascript (Node.js %major LTS)

Group: Development/Tools
License: MIT
Url: https://nodejs.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# bundled histogram uses 64-bit only SSE4.1 intrinsics, V8 is not supported on i686 (as in Fedora)
ExcludeArch: %ix86

# Source-url: https://nodejs.org/dist/v%version/node-v%version.tar.gz
Source: %name-%version.tar
Source7: nodejs_native.req.files
Source8: nodejs_native.req

Patch1: node24-system-openssl.patch
Patch2: npm-disable-internal-node-gyp.patch
Patch3: npm-disable-update-notifier.patch

BuildRequires(pre): rpm-macros-nodejs
BuildRequires(pre): rpm-build-intro >= 2.1.14

BuildRequires: python3-devel gcc-c++
BuildRequires: gyp >= 0.22
BuildRequires: zlib-devel >= %zlib_version
BuildRequires: libbrotli-devel
BuildRequires: openssl-devel >= %openssl_version
BuildRequires: libuv-devel >= %libuv_version
BuildRequires: libicu-devel >= %libicu_version
BuildRequires: libnghttp2-devel >= %libnghttp2_version
BuildRequires: libcares-devel >= %c_ares_version
BuildRequires: libada-devel >= %ada_version
BuildRequires: libzstd-devel >= %zstd_version
BuildRequires: libsqlite3-devel >= %sqlite_version

Provides: nodejs%major = %EVR
Provides: nodejs%major(engine) = %version
Provides: nodejs(abi%major) = %nodejs_abi
Provides: nodejs%major(v8-abi) = %v8_version

Provides: bundled(llhttp) = %llhttp_version
Provides: bundled(uvwasi) = 0.0.23
Provides: bundled(simdjson) = 4.6.11
Provides: bundled(simdutf) = 6.4.0
Provides: bundled(v8) = %v8_version

# use no more than system_memory/3000 build procs (V8 13.6 turboshaft units
# are killed with 1400 and 1800, see https://bugzilla.altlinux.org/show_bug.cgi?id=35112)
%_tune_parallel_build_by_procsize 3000

# C++20 headers, cpp.req can't preprocess them
%add_findreq_skiplist %_includedir/node%major/*

%description
Node.js is a server-side JavaScript environment that uses an asynchronous
event-driven model.  Node's goal is to provide an easy way to build scalable
network programs.

This package contains Node.js %major LTS, installable together with
the default node package: the interpreter is %_bindir/node%major,
use PATH=%node_prefix/bin:$PATH to get it as node.

%package devel
Summary: Devel package for Node.js %major
Group: Development/Other
Requires: %name = %EVR
Requires: gcc-c++ zlib-devel libbrotli-devel libcares-devel
Requires: openssl-devel >= %openssl_version
Requires: libuv-devel >= %libuv_version

%description devel
Node.js %major header and build tools.

Native addons are built with node-gyp against %node_prefix
(found automatically when node-gyp runs with node%major,
or use --nodedir=%node_prefix).

%package -n npm%major
Version: %npm_version
Group: Development/Tools
Summary: A package manager for Node.js %major
License: Artistic-2.0
Requires: %name
# not noarch: node24 is not built on i586

# we do not need any module provides here
AutoProv: no
AutoReq: no

%description -n npm%major
npm is a package manager for node. You can use it to install and publish your
node programs. It manages dependencies and does other cool stuff.

This package contains npm%major and npx%major commands running with
Node.js %major (also for package scripts).

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

rm -rv deps/icu-small/
rm -rv deps/uv/
%__subst "s|deps/uv/uv.gyp ||" Makefile
%__subst "s|.*../uv/uv.gyp:libuv.*||" deps/uvwasi/uvwasi.gyp
rm -rv deps/nghttp2/
rm -rv deps/openssl
rm -rv tools/gyp
rm -rv deps/zlib deps/cares deps/brotli deps/ada deps/zstd deps/sqlite
# make no sense for a first build
%__subst "s|deps/zlib/zlib.gyp||" Makefile

# fix https://bugzilla.altlinux.org/43430
subst 's|// obj\[key\] = flatOptions.userAgent|obj[key] = flatOptions.userAgent|' deps/npm/node_modules/@npmcli/config/lib/definitions/definitions.js

# remove all node-gyp deps
rm -rv deps/npm/node_modules/node-gyp/

# use rpm's cflags
%__subst "s|'cflags': \[\],|'cflags': ['%optflags'],|" ./configure.py

# override detected dir (detection via process.execPath does not work without /proc) with corect path
# global modules are shared with the default node
%__subst "s|path.resolve(prefixDir, 'lib', 'node')|'%nodejs_sitelib'|" lib/internal/modules/cjs/loader.js
grep -q "'%nodejs_sitelib'" lib/internal/modules/cjs/loader.js

%build
export PYTHONPATH=$(pwd)/tools/v8_gypfiles

# prefix %node_prefix: node-gyp finds the headers in it (use_prefix_to_find_headers)
./configure \
    --prefix=%node_prefix \
    --use-prefix-to-find-headers \
    --enable-lto \
    --shared-zlib \
    --shared-brotli \
    --with-intl=system-icu \
    --shared-cares \
    --shared-openssl \
    --shared-openssl-includes=%_includedir \
    --openssl-use-def-ca-store \
    --openssl-conf=%{_sysconfdir}/openssl/openssl.cnf \
    --without-corepack \
    --shared-libuv \
    --shared-nghttp2 \
    --shared-ada \
    --shared-zstd \
    --shared-sqlite \
    %nil

%make_build BUILDTYPE=Release

%check
%make_build test

%install
%makeinstall_std

# node%major in %_bindir, unversioned node in %node_prefix/bin
mkdir -p %buildroot%_bindir
mv -v %buildroot%node_prefix/bin/node %buildroot%_bindir/node%major
ln -s ../../../bin/node%major %buildroot%node_prefix/bin/node

# headers in %_includedir/node%major, %node_prefix/include/node for node-gyp
mkdir -p %buildroot%_includedir
mv -v %buildroot%node_prefix/include/node %buildroot%_includedir/node%major
ln -s ../../../include/node%major %buildroot%node_prefix/include/node

mkdir -p %buildroot%_man1dir
mv -v %buildroot%node_prefix/share/man/man1/node.1 %buildroot%_man1dir/node%major.1
rm -v %buildroot%node_prefix/share/doc/node/gdbinit
rm -v %buildroot%node_prefix/share/doc/node/lldb_commands.py
rmdir -v %buildroot%node_prefix/share/doc/node %buildroot%node_prefix/share/doc
rmdir -v %buildroot%node_prefix/share/man/man1 %buildroot%node_prefix/share/man %buildroot%node_prefix/share

# npm in %node_prefix/node_modules/npm
mv -v %buildroot%node_prefix/lib/node_modules %buildroot%node_prefix/node_modules
rmdir -v %buildroot%node_prefix/lib
ln -sfv ../node_modules/npm/bin/npm-cli.js %buildroot%node_prefix/bin/npm
ln -sfv ../node_modules/npm/bin/npx-cli.js %buildroot%node_prefix/bin/npx

# remove all node-gyp deps
rm -rv %buildroot%node_prefix/node_modules/npm/bin/node-gyp-bin/
rm -rv %buildroot%node_prefix/node_modules/npm/node_modules/@npmcli/run-script/lib/node-gyp-bin

# npm builtin config
cat <<EOF > %buildroot%node_prefix/node_modules/npm/npmrc
globalconfig=/etc/npmrc
update-notifier=false
EOF

# npm%major and npx%major run with node%major, package scripts too
for i in npm npx ; do
cat <<EOF > %buildroot%_bindir/${i}%major
#!/bin/sh
PATH=%node_prefix/bin:\$PATH
export PATH
exec %_bindir/node%major %node_prefix/node_modules/npm/bin/$i-cli.js "\$@"
EOF
chmod 0755 %buildroot%_bindir/${i}%major
done

# Requires nodejs(abi%major) for native addons built against Node.js %major
install -Dpm0755 %SOURCE7 %buildroot%_rpmlibdir/nodejs%{major}_native.req.files
sed -e 's|@MAJOR@|%major|g' -e 's|@ABI@|%nodejs_abi|g' %SOURCE8 > %buildroot%_rpmlibdir/nodejs%{major}_native.req
chmod 0755 %buildroot%_rpmlibdir/nodejs%{major}_native.req

%files
%doc CHANGELOG.md LICENSE README.md
%_bindir/node%major
%dir %node_prefix/
%dir %node_prefix/bin/
%node_prefix/bin/node
%_man1dir/node%major.1*

%files devel
%_includedir/node%major/
%node_prefix/include/
%_rpmlibdir/nodejs%{major}_native.req
%_rpmlibdir/nodejs%{major}_native.req.files

%files -n npm%major
%_bindir/npm%major
%_bindir/npx%major
%node_prefix/bin/npm
%node_prefix/bin/npx
%node_prefix/node_modules/

%changelog
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 24.22.0-alt1
- initial build for Sisyphus
- ExcludeArch: i586 (bundled hdr_histogram does not build on 32-bit x86),
  npm24 is arch dependent therefore
