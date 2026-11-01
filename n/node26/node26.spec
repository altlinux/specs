%define _unpackaged_files_terminate_build 1
%define major 26
%define node_version 26.13.0
%define node_prefix %_prefix/lib/node%major

%define nodejs_soversion 149
%define nodejs_abi %nodejs_soversion
%define v8_version 14.6
%define npm_version 11.20.0

%define libicu_version 7.8.3
%define libuv_version 1.53.0
%define libnghttp2_version 1.70.0
%define c_ares_version 1.34.9
%define openssl_version 3.5.9
%define ada_version 4.0.0
%define zstd_version 1.5.7
%define sqlite_version 3.54.0
%define brotli_version 1.2.1

# Bundled: llhttp 9.4.3, sqlite 3.54.0 (ALT has 3.53.3),
# simdjson 4.6.11, simdutf 6.4.0,
# uvwasi 0.0.23, ngtcp2/nghttp3, nbytes, merve, hdr-histogram.
%define zlib_version 1.3.1

%ifarch armh
%global optflags_lto %nil
%define optflags_debug -g0
%else
%define optflags_debug -g1
%endif

%def_disable check

Name: node%major
Version: %node_version
Release: alt1

Summary: Evented I/O for V8 Javascript (Node.js %major LTS)

Group: Development/Tools
License: MIT
Url: https://nodejs.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# V8 does not build on i686; hdr_histogram requires 64-bit SSE4.1.
ExcludeArch: %ix86

# Source-url: https://nodejs.org/dist/v%version/node-v%version.tar.gz
Source: %name-%version.tar
Source7: nodejs_native.req.files
Source8: nodejs_native.req
Patch1: node26-system-openssl.patch
Patch2: npm-disable-internal-node-gyp.patch
Patch3: npm-disable-update-notifier.patch

BuildRequires(pre): rpm-macros-nodejs
BuildRequires(pre): rpm-build-intro >= 2.1.14

BuildRequires: python3-devel gcc-c++
BuildRequires: gyp >= 0.22
BuildRequires: zlib-devel >= %zlib_version
BuildRequires: libbrotli-devel >= %brotli_version
BuildRequires: openssl-devel >= %openssl_version
BuildRequires: libuv-devel >= %libuv_version
BuildRequires: libicu-devel >= %libicu_version
BuildRequires: libnghttp2-devel >= %libnghttp2_version
BuildRequires: libcares-devel >= %c_ares_version
BuildRequires: libada-devel >= %ada_version
BuildRequires: libzstd-devel >= %zstd_version

Provides: nodejs%major = %EVR
Provides: nodejs%major(engine) = %version
Provides: nodejs(abi%major) = %nodejs_abi
Provides: nodejs%major(v8-abi) = %v8_version

Provides: bundled(llhttp) = 9.4.3
Provides: bundled(uvwasi) = 0.0.23
Provides: bundled(simdjson) = 4.6.11
Provides: bundled(simdutf) = 6.4.0
Provides: bundled(v8) = %v8_version
Provides: bundled(sqlite) = %sqlite_version

%_tune_parallel_build_by_procsize 3000
%add_findreq_skiplist %_includedir/node%major/*

%description
Node.js is a server-side JavaScript environment that uses an asynchronous
event-driven model. Node's goal is to provide an easy way to build scalable
network programs.

This package contains Node.js %major LTS, installable together with
the default node package: the interpreter is %_bindir/node%major,
use PATH=%node_prefix/bin:$PATH to get it as node.

%package -n lib%name-devel
Summary: Devel package for Node.js %major
Group: Development/Other
Requires: %name = %EVR
Requires: gcc-c++ zlib-devel libbrotli-devel >= %brotli_version libcares-devel >= %c_ares_version
Requires: openssl-devel >= %openssl_version
Requires: libuv-devel >= %libuv_version

%description -n lib%name-devel
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
# npm24 is arch dependent because node24 excludes i586.
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

rm -rv deps/icu-small/ deps/uv/ deps/nghttp2/ deps/openssl tools/gyp
%__subst "s|deps/uv/uv.gyp ||" Makefile
%__subst "s|.*../uv/uv.gyp:libuv.*||" deps/uvwasi/uvwasi.gyp
rm -rv deps/zlib deps/cares deps/brotli deps/ada deps/zstd
%__subst "s|deps/zlib/zlib.gyp||" Makefile

# Remove vendored node-gyp dependencies; use system node-gyp.
rm -rv deps/npm/node_modules/node-gyp/

# Use rpm build flags.
%__subst "s|'cflags': \[\],|'cflags': ['%optflags'],|" configure.py

# Share architecture-independent npm modules with the default node.
%__subst "s|path.resolve(prefixDir, 'lib', 'node')|'%nodejs_sitelib'|" \
    lib/internal/modules/cjs/loader.js
grep -q "'%nodejs_sitelib'" lib/internal/modules/cjs/loader.js

%build
export PYTHONPATH=$(pwd)/tools/v8_gypfiles
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
    --shared-libuv \
    --shared-nghttp2 \
    --shared-ada \
    --shared-zstd \
    %nil

%make_build BUILDTYPE=Release

%install
%makeinstall_std

mkdir -p %buildroot%_bindir
mv -v %buildroot%node_prefix/bin/node %buildroot%_bindir/node%major
ln -s ../../../bin/node%major %buildroot%node_prefix/bin/node

mkdir -p %buildroot%_includedir
mv -v %buildroot%node_prefix/include/node %buildroot%_includedir/node%major
ln -s ../../../include/node%major %buildroot%node_prefix/include/node

mkdir -p %buildroot%_man1dir
mv -v %buildroot%node_prefix/share/man/man1/node.1 %buildroot%_man1dir/node%major.1
rm -v %buildroot%node_prefix/share/doc/node/gdbinit
rm -v %buildroot%node_prefix/share/doc/node/lldb_commands.py
rmdir -v %buildroot%node_prefix/share/doc/node %buildroot%node_prefix/share/doc
rmdir -v %buildroot%node_prefix/share/man/man1 %buildroot%node_prefix/share/man %buildroot%node_prefix/share

mv -v %buildroot%node_prefix/lib/node_modules %buildroot%node_prefix/node_modules
rmdir -v %buildroot%node_prefix/lib
ln -sfv ../node_modules/npm/bin/npm-cli.js %buildroot%node_prefix/bin/npm
ln -sfv ../node_modules/npm/bin/npx-cli.js %buildroot%node_prefix/bin/npx
rm -rv %buildroot%node_prefix/node_modules/npm/bin/node-gyp-bin/
rm -rv %buildroot%node_prefix/node_modules/npm/node_modules/@npmcli/run-script/lib/node-gyp-bin

cat <<EOF > %buildroot%node_prefix/node_modules/npm/npmrc
globalconfig=/etc/npmrc
update-notifier=false
EOF

for i in npm npx ; do
cat <<EOF > %buildroot%_bindir/${i}%major
#!/bin/sh
PATH=%node_prefix/bin:\$PATH
export PATH
exec %_bindir/node%major %node_prefix/node_modules/npm/bin/$i-cli.js "\$@"
EOF
chmod 0755 %buildroot%_bindir/${i}%major
done

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

%files -n lib%name-devel
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
* Sat Oct 31 2026 Vitaly Lipatov <lav@altlinux.ru> 26.13.0-alt1
- initial build for ALT Sisyphus
