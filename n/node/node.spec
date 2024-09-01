%define _unpackaged_files_terminate_build 1

%define major 20.17

%define nodejs_soversion 115
%define nodejs_abi %nodejs_soversion

# there are both 6 and 7 provided (https://github.com/nodejs/node/pull/35199), see napi using
%define napi 7

# TODO: really we have no configure option to build with shared libv8
# V8 presently breaks ABI at least every x.y release while never bumping SONAME,
# so we need to be more explicit until spot fixes that
%define v8_version 10.2
%def_without systemv8


# check deps/npm/package.json for it
%define npm_version 10.8.2
# separate build npm
%def_with npm
# in other case, note: we will npm-@npmver-@release package! fix release if npmver is unchanged

# check deps/corepack/package.json
%define corepackver 0.29.3
%def_without corepack

# check deps/zlib/zlib.h
%define zlib_version 1.3.0.1

# check deps/cares/include/ares_version.h
%define c_ares_version 1.32.3

# check deps/llhttp/include/llhttp.h
%define llhttp_version 9.2.1
# to use internal llhttp
%def_without systemhttpparser

# check: openssl 3.0 inside (TODO: QUIC support, FIPS support)
#define openssl_version 1.1.1s
%define openssl_version 3.0.8
%def_with systemssl

# check deps/uv/include/uv/version.h
%define libuv_version 1.48.0
%def_with systemuv

# check deps/nghttp2/lib/includes/nghttp2/nghttp2ver.h
%define libnghttp2_version 1.60.0
%def_with systemnghttp2

# see deps/v8/src/objects/intl-objects.h for V8_MINIMUM_ICU_VERSION
# check tools/icu/current_ver.dep
%define libicu_abi 7.4
# see rpm-macros-features
%if_feature icu %libicu_abi
%def_with systemicu
%endif

# TODO: some strange build error
%ifarch armh
%global optflags_lto %nil
%endif

# minimalize memory using
%ifarch armh
%define optflags_debug -g0
%endif

# need OpenSSL + QUIC build from https://github.com/quictls/openssl/tree/OpenSSL_1_1_1t+quic
%define libngtcp2_version 0.8.1
%define libnghttp3_version 0.7.0
%def_without systemngtcp2


%def_disable check

# https://nodejs.org/api/n-api.html
# https://github.com/nodejs/abi-stable-node
%def_with nodejs_abi

Name: node
Version: %major.0
Release: alt1

Summary: Evented I/O for V8 Javascript

Group: Development/Tools
License: MIT
Url: http://nodejs.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

##Source-git: https://github.com/nodejs/node.git
# Source-url: https://nodejs.org/dist/v%version/node-v%version.tar.gz
Source: %name-%version.tar
Source7: nodejs_native.req.files

Patch1: node18-system-openssl.patch
Patch2: npm-disable-internal-node-gyp.patch
Patch3: npm-disable-update-notifier.patch

BuildRequires(pre): rpm-macros-nodejs
BuildRequires(pre): rpm-build-intro >= 2.1.14
BuildRequires(pre): rpm-macros-features

BuildRequires: python3-devel gcc-c++
BuildRequires: zlib-devel >= %zlib_version
BuildRequires: libbrotli-devel

BuildRequires: gyp >= 0.14.0
BuildRequires: python3-module-simplejson

%if_with systemv8
%define libv8_package libv8-nodejs
BuildRequires: %libv8_package-devel >= %v8_version-devel
%endif

%if_with systemssl
BuildRequires: openssl-devel >= %openssl_version openssl
# for require strict library version
Requires: openssl >= %openssl_version
%endif

%if_with systemuv
BuildRequires: libuv-devel >= %libuv_version
%endif

%if_with systemicu
BuildRequires: libicu-devel >= %libicu_abi
%endif

%if_with systemnghttp2
BuildRequires: libnghttp2-devel >= %libnghttp2_version
%endif

%if_with systemngtcp2
BuildRequires: libngtcp2-devel >= %libngtcp2_version
BuildRequires: libnghttp3-devel >= %libnghttp3_version
%endif

%if_with systemhttpparser
BuildRequires: libhttp-parser-devel >= 2.9.2-alt2
%endif

BuildRequires: libcares-devel >= %c_ares_version

BuildRequires: curl

%if_without npm
Requires: npm >= %npm_version
%endif

# this corresponds to the "engine" requirement in package.json
Provides: nodejs(engine) = %version

Provides: nodejs = %version-%release
Provides: node.js = %version-%release
Obsoletes: nodejs < %version-%release
Obsoletes: node.js < %version-%release

Provides: nodejs(abi) = %nodejs_abi
Provides: nodejs(abi%major) = %nodejs_abi

Provides: nodejs(v8-abi) = %v8_version

#Provides: nodejs(napi) = 6
#Provides: nodejs(napi) = %{napi}

Provides: bundled(llhttp) = %llhttp_version
Provides: bundled(uvwasi) = 0.0.18

# Node.js is closely tied to the version of v8 that is used with it. It makes
# sense to use the bundled version because upstream consistently breaks ABI
# even in point releases. Node.js upstream has now removed the ability to build
# against a shared system version entirely.
# See https://github.com/nodejs/node/commit/d726a177ed59c37cf5306983ed00ecd858cfbbef
Provides: bundled(v8) = %v8_version

# /usr/bin/ld.default: failed to set dynamic section sizes: memory exhausted
%ifarch %ix86
%define optflags_debug -g0
%endif

# use no more than system_memory/1400 build procs (see https://bugzilla.altlinux.org/show_bug.cgi?id=35112)
%_tune_parallel_build_by_procsize 1400

%add_findreq_skiplist %{_datadir}/node/sources/*

%description
Node.js is a server-side JavaScript environment that uses an asynchronous
event-driven model.  Node's goal is to provide an easy way to build scalable
network programs.

%package devel
Summary:        Devel package for Node.js
Group:          Development/Other
License:        MIT license
# arch depended info in .gypi
#BuildArch:      noarch
Provides:	nodejs-devel = %EVR
Requires:	%name = %EVR
Requires:       gcc-c++ zlib-devel libbrotli-devel libcares-devel
%if_with systemv8
Requires:	%libv8_package-devel >= %v8_version
%endif
%if_with systemssl
Requires:	openssl-devel >= %openssl_version
%endif
%if_with systemuv
Requires: libuv-devel >= %libuv_version
%else
Conflicts:      libuv-devel
%endif

%description devel
Node.js header and build tools


%package doc
Summary: Documentation files
Group: Development/Other
Requires: %name-devel = %version-%release

BuildArch: noarch

%description doc
Documentation files for %name.

# https://bugzilla.altlinux.org/show_bug.cgi?id=38130
%if_with npm
%package -n npm
Version:	%npm_version
Group:		Development/Tools
Summary:	A package manager for node
License:	MIT License
Requires:	node
BuildArch:	noarch
# https://bugzilla.altlinux.org/show_bug.cgi?id=38130
#%if_with nodejs_abi
#Requires:	nodejs(abi) = %nodejs_abi
#%endif

Requires: bash
Requires: /usr/bin/node

# we do not need any module provides here
AutoProv: no
AutoReq: no

%description -n npm
npm is a package manager for node. You can use it to install and publish your
node programs. It manages dependencies and does other cool stuff.
%endif

%package corepack
Version:	%corepackver
Group:		Development/Tools
Summary:	Bridge between Node projects and their package managers
License:	MIT License
Requires:	node
BuildArch:	noarch
AutoReq:	yes,nopython
#%if_with nodejs_abi
Requires:	nodejs(abi) = %nodejs_abi
#%endif

%description corepack
Corepack is a zero-runtime-dependency Node.js script that acts as a bridge
between Node.js projects and the package managers they are intended to be used
with during development. In practical terms, **Corepack will let you use
Yarn and pnpm without having to install them** - just like what currently
happens with npm, which is shipped by Node.js by default.

**Important:** At the moment, Corepack only covers Yarn and pnpm.
Given that we have little control on the npm project, we prefer to focus
on the Yarn and pnpm use cases.
As a result, Corepack doesn't have any effect at all on the way you use npm.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

%if_with systemv8
# hack against https://bugzilla.altlinux.org/show_bug.cgi?id=32573#c3
cp -a deps/v8/include/libplatform src
rm -rv deps/v8/
%endif

%if_with systemicu
rm -rv deps/icu-small/
%endif

%if_with systemuv
rm -rv deps/uv/
%__subst "s|deps/uv/uv.gyp ||" Makefile
%__subst "s|.*../uv/uv.gyp:libuv.*||" deps/uvwasi/uvwasi.gyp
%endif

%if_with systemnghttp2
rm -rv deps/nghttp2/
%endif

%if_with systemngtcp2
rm -rv deps/ngtcp2/
%endif

%if_with systemssl
rm -rv deps/openssl
%endif

# disable external libs
# TODO:
# deps/gtest
rm -rv tools/gyp
rm -rv deps/zlib deps/cares deps/brotli
# make no sense for a first build
%__subst "s|deps/zlib/zlib.gyp||" Makefile

#rm -rv deps/v8/third_party/jinja2
#rm -rv tools/inspector_protocol/jinja2


%if_with npm
# fix https://bugzilla.altlinux.org/43430
subst 's|// obj\[key\] = flatOptions.userAgent|obj[key] = flatOptions.userAgent|' deps/npm/node_modules/@npmcli/config/lib/definitions/definitions.js

# remove all node-gyp deps
rm -rv deps/npm/node_modules/node-gyp/
%else
# don't use: keep internal npm (used for doc build)
rm -rv deps/npm/
ln -s %_libexecdir/node_modules/npm deps/npm


# Workaround for https://github.com/npm/cli/issues/780
cd man
local f name sec title
rm -v man5/install.5 
for f in man5/folders.5 man7/*.7; do
  sec=${f##*.}
  name=$(basename "$f" ."$sec")
  title=$(echo "$name" | tr '[:lower:]' '[:upper:]')

  sed -Ei "s/^\.TH \"$title\"/.TH \"NPM-$title\"/" "$f"
  mv "$f" "${f%/*}/npm-$name.$sec"
done
cd - >/dev/null

%endif

# use rpm's cflags
%__subst "s|'cflags': \[\],|'cflags': ['%optflags'],|" ./configure.py
# fix cflags wrap in outputted config.json
#__subst "s|indent=2|indent=2,width=160|" ./configure.py
# TODO: move to upstream?
%ifarch mipsel
%__subst "s|'libraries': \[\],|'libraries': ['-latomic'],|" ./configure.py
%endif

# override detected dir (detection via process.execPath does not work without /proc) with corect path
%__subst "s|path.resolve(prefixDir, 'lib', 'node')|'%nodejs_sitelib'|" lib/internal/modules/cjs/loader.js

%build
# hack against
# gyp: Error importing pymod_do_mainmodule (GN-scraper): No module named GN-scraper while loading dependencies of /tmp/.private/lav/RPM/BUILD/node-12.14.1/node.gyp
export PYTHONPATH=$(pwd)/tools/v8_gypfiles

./configure \
    --prefix=%_prefix \
    --enable-lto \
    --shared-zlib \
    --shared-brotli \
%if_with systemicu
    --with-intl=system-icu \
%endif
%if_with systemhttpparser
    --shared-http-parser \
%endif
    --shared-cares \
%if_with systemssl
    --shared-openssl \
    --shared-openssl-includes=%_includedir \
%endif
    --openssl-use-def-ca-store \
    --openssl-conf=%{_sysconfdir}/openssl/openssl.cnf \
%if_without npm
    --without-npm \
%endif
%if_without corepack
   --without-corepack \
%endif
%if_with systemuv
    --shared-libuv \
%endif
%if_with systemnghttp2
    --shared-nghttp2 \
%endif
%if_with systemngtcp2
    --shared-ngtcp2 \
    --shared-nghttp3 \
%endif
%if_with systemv8
    --without-bundled-v8 \
%endif
    %nil

%make_build BUILDTYPE=Release
# skip internal doc build (uses external modules)
#make doc
#%make jslint

%check
%make_build test

%install
mkdir -p %buildroot%nodejs_sitelib/

%makeinstall_std

%if_without systemuv
#install development headers
mkdir -p %{buildroot}%{_includedir}/node/
cp -p src/*.h %{buildroot}%{_includedir}/node
cp -p deps/uv/include/*.h %{buildroot}%{_includedir}/node
#cp -p deps/uv/include/uv-private/*.h %{buildroot}%{_includedir}/node/uv-private
%endif

%if_with npm
rm -rv %buildroot%nodejs_sitelib/npm/bin/node-gyp-bin/

# remove all node-gyp deps
rm -rv %buildroot%nodejs_sitelib/npm/node_modules/@npmcli/run-script/lib/node-gyp-bin

cat <<EOF >> %buildroot%nodejs_sitelib/npm/.npmrc
globalconfig=/etc/npmrc
update-notifier=false
EOF

%endif

%if_with nodejs_abi
# ensure Requires are added to every native module that match the Provides from
# the nodejs build in the buildroot
install -Dpm0755 %{SOURCE7} %buildroot%_rpmlibdir/nodejs_native.req.files
cat << EOF > %buildroot%_rpmlibdir/nodejs_native.req
#!/bin/sh
echo 'nodejs(abi) = %nodejs_abi'
#echo 'nodejs(v8-abi) = %v8_version'
EOF
chmod 0755 %buildroot%_rpmlibdir/nodejs_native.req
%endif

rm -rv %buildroot/usr/share/doc/node/gdbinit
rm -rv %buildroot/usr/share/doc/node/lldb_commands.py


%files
%doc CHANGELOG.md LICENSE README.md
%_bindir/node
%dir %nodejs_sitelib
#_prefix/lib/node
#%_datadir/systemtap/tapset/node.stp
%_man1dir/*

%files doc
%doc README.md
#out/doc/api

%files devel
%dir %_includedir/node/
#%_datadir/%name/%name-v%version-headers.tar.gz
%if_without systemuv
%_includedir/node/uv*
%endif
%if_without systemv8
%_includedir/node/v8*
%endif
%_includedir/node/node*
%_includedir/node/js_native_api*
# deps/cares
#_includedir/node/ares*
%_includedir/node/common.gypi
%_includedir/node/config.gypi
%_includedir/node/libplatform/
%_includedir/node/cppgc/
%if_without systemssl
%_includedir/node/openssl/
%endif
# deps/http_parser
#_includedir/node/nameser.h
#_datadir/node/common.gypi
%if_with nodejs_abi
%_rpmlibdir/nodejs_native.req
%_rpmlibdir/nodejs_native.req.files
%endif
#%_datadir/node/sources

%if_with npm
%files -n npm
%_bindir/npm
%_bindir/npx
%nodejs_sitelib/npm/
%endif

%if_with corepack
%files corepack
%_bindir/corepack
%nodejs_sitelib/corepack
%endif

%changelog
* Sun Sep 01 2024 Vitaly Lipatov <lav@altlinux.ru> 20.17.0-alt1
- 2024-08-21, Version 20.17.0 'Iron' (LTS), @marco-ippolito
- set npm >= 10.8.2, c-ares >= 1.32.3

* Sun Jul 07 2024 Vitaly Lipatov <lav@altlinux.ru> 20.15.0-alt1
- 2024-06-20, Version 20.15.0 'Iron' (LTS), @marco-ippolito
- npm updated to 10.7.0

* Fri May 17 2024 Vitaly Lipatov <lav@altlinux.ru> 20.13.1-alt1
- 2024-05-09, Version 20.13.1 'Iron' (LTS), @marco-ippolito
- npm updated to 10.5.2

* Sat Apr 27 2024 Vitaly Lipatov <lav@altlinux.ru> 20.12.2-alt1
- 2024-04-10, Version 20.12.2 'Iron' (LTS), @RafaelGSS
- CVE-2024-27980: Command injection via args parameter of child_process.spawn without shell option enabled on Windows
- npm: disable update notifier

* Thu Apr 04 2024 Vitaly Lipatov <lav@altlinux.ru> 20.12.1-alt1
- 2024-04-03, Version 20.12.1 'Iron' (LTS), @RafaelGSS
- CVE-2024-27983 - Assertion failed in node::http2::Http2Session::~Http2Session() leads to HTTP/2 server crash- (High)
- CVE-2024-27982 - HTTP Request Smuggling via Content Length Obfuscation - (Medium)

* Thu Mar 28 2024 Vitaly Lipatov <lav@altlinux.ru> 20.12.0-alt1
- 2024-03-26, Version 20.12.0 'Iron' (LTS), @richardlau
- set npm >= 10.5.0, c-ares >= 1.27.0, zlib >= 1.3.01
- set libnghttp2 >= 1.60.0, libicu >= 7.4

* Fri Mar 01 2024 Vitaly Lipatov <lav@altlinux.ru> 20.11.1-alt2
- fix npm config get user-agent output again (ALT bug 43430)

* Sun Feb 18 2024 Vitaly Lipatov <lav@altlinux.ru> 20.11.1-alt1
- new version 20.11.1 (with rpmrb script)
- enable build npm subpackage
- CVE-2024-21892: Code injection and privilege escalation through Linux capabilities- (High)
- CVE-2024-22019: http: Reading unprocessed HTTP request with unbounded chunk extension allows DoS attacks- (High)
- CVE-2024-21896: Path traversal by monkey-patching Buffer internals- (High)
- CVE-2024-22017: setuid() does not drop all privileges due to io_uring - (High)
- CVE-2023-46809: Node.js is vulnerable to the Marvin Attack (timing variant of the Bleichenbacher attack against PKCS#1 v1.5 padding) - (Medium)
- CVE-2024-21891: Multiple permission model bypasses due to improper path traversal sequence sanitization - (Medium)
- CVE-2024-21890: Improper handling of wildcards in --allow-fs-read and --allow-fs-write (Medium)
- CVE-2024-22025: Denial of Service by resource exhaustion in fetch() brotli decoding - (Medium)
- libuv >= 1.48.0

* Mon Feb 05 2024 Vitaly Lipatov <lav@altlinux.ru> 20.11.0-alt1
- new version 20.11.0 (with rpmrb script)
- set npm >= 10.2.4, c-ares >= 1.20.1

* Thu Nov 02 2023 Vitaly Lipatov <lav@altlinux.ru> 20.9.0-alt1
- 2023-10-24, Version 20.9.0 'Iron' (LTS)
- set npm >= 10.1.0, libuv >= 1.46.0, libicu >= 7.3, libnghttp2 >= 1.57.0

* Thu Nov 02 2023 Vitaly Lipatov <lav@altlinux.ru> 18.18.2-alt1
- new version 18.18.2 (with rpmrb script)
- note: libuv reverted to 1.44.2 in upstream due some regressions

* Thu Oct 12 2023 Vitaly Lipatov <lav@altlinux.ru> 18.18.1-alt1
- new version 18.18.1 (with rpmrb script)

* Sat Jul 29 2023 Vitaly Lipatov <lav@altlinux.ru> 18.17.0-alt1
- new version 18.17.0 (with rpmrb script)
- set npm >= 9.6.7
- CVE-2023-30581: mainModule.__proto__ Bypass Experimental Policy Mechanism (High)
- CVE-2023-30585: Privilege escalation via Malicious Registry Key manipulation during Node.js installer repair process (Medium)
- CVE-2023-30588: Process interuption due to invalid Public Key information in x509 certificates (Medium)
- CVE-2023-30589: HTTP Request Smuggling via Empty headers separated by CR (Medium)
- CVE-2023-30590: DiffieHellman does not generate keys after setting a private key (Medium)

* Mon Mar 13 2023 Vitaly Lipatov <lav@altlinux.ru> 18.15.0-alt1
- new LTS version 18.15.0
- build with OpenSSL 3, ngtcp2, nghttp3
- set npm >= 9.5.0, libuv >= 1.44.2, libicu >= 7.2, libnghttp2 >= 1.51.0

* Mon Mar 13 2023 Vitaly Lipatov <lav@altlinux.ru> 16.19.1-alt1
- new version 16.19.1 (with rpmrb script)
- CVE-2023-23918: Node.js Permissions policies can be bypassed via process.mainModule (High)
- CVE-2023-23919: Node.js OpenSSL error handling issues in nodejs crypto library (Medium)
- CVE-2023-23920: Node.js insecure loading of ICU data through ICU\_DATA environment variable (Low)
- CVE-2023-23936: Fetch API in Node.js did not protect against CRLF injection in host headers (Medium)
- CVE-2023-24807: Regular Expression Denial of Service in Headers in Node.js fetch API (Low)
- set openssl >= 1.1.1s
- set npm >= 8.19.3

* Wed Nov 23 2022 Vitaly Lipatov <lav@altlinux.ru> 16.18.1-alt1
- new version 16.18.1 (with rpmrb script)
- CVE-2022-43548: DNS rebinding in --inspect via invalid octal IP address (Medium)

* Sun Oct 16 2022 Vitaly Lipatov <lav@altlinux.ru> 16.18.0-alt1
- new version 16.18.0 (with rpmrb script)
- set npm >= 8.19.2

* Fri Sep 30 2022 Vitaly Lipatov <lav@altlinux.ru> 16.17.1-alt1
- new version 16.17.1 (with rpmrb script)
- set npm >= 8.15.0
- CVE-2022-32212: DNS rebinding in --inspect on macOS (High)
- CVE-2022-32213: bypass via obs-fold mechanic (Medium)
- CVE-2022-35255: Weak randomness in WebCrypto keygen
- CVE-2022-35256: HTTP Request Smuggling - Incorrect Parsing of Header Fields (Medium)

* Tue Jul 12 2022 Vitaly Lipatov <lav@altlinux.ru> 16.16.0-alt1
- new version 16.16.0 (with rpmrb script)
- set openssl >= 1.1.1q
- set npm >= 8.11.0

* Wed Apr 27 2022 Vitaly Lipatov <lav@altlinux.ru> 16.15.0-alt1
- new version 16.15.0 (with rpmrb script)
- set npm >= 8.5.5

* Tue Apr 26 2022 Alexey Shabalin <shaba@altlinux.org> 16.14.2-alt2
- build with system brotli
- add corepack package, but build without

* Sat Apr 23 2022 Vitaly Lipatov <lav@altlinux.ru> 16.14.2-alt1
- new version 16.14.2 (with rpmrb script)
- set openssl >= 1.1.1n
- CVE-2022-0778: Infinite loop in BN_mod_sqrt() reachable when parsing certificates (High)

* Sat Apr 23 2022 Vitaly Lipatov <lav@altlinux.ru> 16.14.1-alt1
- new version 16.14.1 (with rpmrb script)
- set npm >= 8.5.0

* Fri Mar 18 2022 Vitaly Lipatov <lav@altlinux.ru> 16.13.2-alt1
- new version 16.13.2 (with rpmrb script)
- set npm >= 8.3.1
- set libuv >= 1.43.0
- CVE-2021-44531: Improper handling of URI Subject Alternative Names (Medium)
- CVE-2021-44532: Certificate Verification Bypass via String Injection (Medium)
- CVE-2021-44533: Incorrect handling of certificate subject and issuer fields (Medium)
- CVE-2022-21824: Prototype pollution via console.table properties (Low)

* Fri Dec 17 2021 Vitaly Lipatov <lav@altlinux.ru> 16.13.1-alt1
- new LTS version 16.13.1 (with rpmrb script)

* Fri Dec 17 2021 Vitaly Lipatov <lav@altlinux.ru> 14.18.2-alt1
- new version 14.18.2 (with rpmrb script)
- CVE-2021-22959: HTTP Request Smuggling due to spaced in headers
- CVE-2021-22960: HTTP Request Smuggling when parsing the body
- python 3.10 support
- set c-ares >= 1.18.1

* Thu Sep 30 2021 Vitaly Lipatov <lav@altlinux.ru> 14.18.0-alt2
- use rpm-macros-features to check icu version

* Tue Sep 28 2021 Vitaly Lipatov <lav@altlinux.ru> 14.18.0-alt1
- new version 14.18.0 (with rpmrb script)
- disable LTO on armh
- set libuv >= 1.42.0

* Wed Sep 01 2021 Vitaly Lipatov <lav@altlinux.ru> 14.17.6-alt1
- new version 14.17.6 (with rpmrb script)
- set npm >= 6.14.15
- set openssl >= 1.1.1l
- CVE-2021-32803, CVE-2021-32804, CVE-2021-37701, CVE-2021-37712, CVE-2021-37713, CVE-2021-39134, CVE-2021-39135

* Wed Aug 11 2021 Vitaly Lipatov <lav@altlinux.ru> 14.17.5-alt1
- new version 14.17.5 (with rpmrb script)
- set c-ares >= 1.17.2
- CVE-2021-3672, CVE-2021-22931: Improper handling of untypical characters in domain names
- CVE-2021-22930: Use after free on close http2 on stream canceling
- CVE-2021-22939: Incomplete validation of rejectUnauthorized parameter

* Fri Jul 30 2021 Vitaly Lipatov <lav@altlinux.ru> 14.17.4-alt1
- new version 14.17.4 (with rpmrb script)
- CVE-2021-22930: Use after free on close http2 on stream canceling (High)
- set npm >= 6.14.14
- restore minimum ICU version to 65

* Thu Jul 01 2021 Vitaly Lipatov <lav@altlinux.ru> 14.17.2-alt1
- new version 14.17.2 (with rpmrb script)
- CVE-2021-22918: Out of bounds read (set libuv >= 1.41.0-alt3)

* Wed Jun 16 2021 Vitaly Lipatov <lav@altlinux.ru> 14.17.1-alt1
- new version 14.17.1 (with rpmrb script)

* Mon Jun 07 2021 Vitaly Lipatov <lav@altlinux.ru> 14.17.0-alt1
- new version 14.17.0 (with rpmrb script)
- set libuv >= 1.41.0

* Sun Apr 11 2021 Vitaly Lipatov <lav@altlinux.ru> 14.16.1-alt1
- new version 14.16.1 (with rpmrb script)
- set openssl >= 1.1.1k
- set npm >= 6.14.12

* Tue Feb 23 2021 Vitaly Lipatov <lav@altlinux.ru> 14.16.0-alt1
- new version 14.16.0 (with rpmrb script)
- CVE-2021-22883: HTTP2 'unknownProtocol' cause Denial of Service by resource exhaustion
- CVE-2021-22884: DNS rebinding in --inspect

* Fri Feb 05 2021 Vitaly Lipatov <lav@altlinux.ru> 14.15.4-alt1
- new version 14.15.4 (with rpmrb script)
- CVE-2020-1971: OpenSSL - EDIPARTYNAME NULL pointer de-reference (High)
- CVE-2020-8265: use-after-free in TLSWrap (High)
- CVE-2020-8287: HTTP Request Smuggling in nodejs (Low)

* Mon Nov 16 2020 Vitaly Lipatov <lav@altlinux.ru> 14.15.1-alt1
- new version 14.15.1 (with rpmrb script)
- set c-ares >= 1.16.1-alt2
- CVE-2020-8277: Denial of Service through DNS request (High)

* Tue Oct 27 2020 Vitaly Lipatov <lav@altlinux.ru> 14.15.0-alt1
- new version 14.15.0 (with rpmrb script)
- 2020-10-27, Version 14.15.0 'Fermium' (LTS), @richardlau
  This release marks the transition of Node.js 14.x into Long Term Support (LTS)

* Fri Oct 16 2020 Vitaly Lipatov <lav@altlinux.ru> 14.14.0-alt1
- new version 14.14.0 (with rpmrb script)

* Thu Oct 08 2020 Vitaly Lipatov <lav@altlinux.ru> 14.13.1-alt1
- new version 14.13.1 (with rpmrb script)
- internal update llhttp to 2.1.3

* Tue Oct 06 2020 Vitaly Lipatov <lav@altlinux.ru> 14.13.0-alt1
- new version 14.13.0 (with rpmrb script)
- set libuv >= 1.40.0
- set c-ares >= 1.16.1

* Fri Sep 18 2020 Vitaly Lipatov <lav@altlinux.ru> 14.11.0-alt2
- set libicu >= 6.7 (missed since 14.6.0), use packaged icu only on Sisyphus

* Wed Sep 16 2020 Vitaly Lipatov <lav@altlinux.ru> 14.11.0-alt1
- new version 14.11.0 (with rpmrb script)
- CVE-2020-8251: Denial of Service by resource exhaustion CWE-400 due to unfinished HTTP/1.1 requests (Critical)
- CVE-2020-8201: HTTP Request Smuggling due to CR-to-Hyphen conversion (High)

* Wed Sep 02 2020 Vitaly Lipatov <lav@altlinux.ru> 14.9.0-alt1
- new version 14.9.0 (with rpmrb script)
- libuv >= 1.39.0
- npm >= 6.14.8

* Sat Aug 01 2020 Vitaly Lipatov <lav@altlinux.ru> 14.7.0-alt1
- new version 14.7.0 (with rpmrb script)
- npm >= 6.14.7

* Sat Aug 01 2020 Vitaly Lipatov <lav@altlinux.ru> 14.6.0-alt1
- new version 14.6.0 (with rpmrb script)
- libuv >= 1.38.1
- npm >= 6.14.6

* Fri Jun 19 2020 Vitaly Lipatov <lav@altlinux.ru> 14.4.0-alt1
- new version 14.4.0 (with rpmrb script)
- set libicu >= 6.5
- set libnghttp2 >= 1.41.0
- CVE-2020-8172, CVE-2020-11080, CVE-2020-8174

* Fri May 22 2020 Vitaly Lipatov <lav@altlinux.ru> 14.3.0-alt1
- new version 14.3.0 (with rpmrb script)
- npm >= 6.14.5

* Thu May 07 2020 Vitaly Lipatov <lav@altlinux.ru> 14.2.0-alt1
- new version 14.2.0 (with rpmrb script)
- set node ABI to 14
- libuv >= 1.37.0

* Sun Mar 29 2020 Vitaly Lipatov <lav@altlinux.ru> 13.12.0-alt1
- new version 13.12.0 (with rpmrb script)
- npm >= 6.14.4
- libuv >= 1.35.0

* Thu Mar 19 2020 Vitaly Lipatov <lav@altlinux.ru> 13.11.0-alt1
- new version 13.11.0

* Tue Mar 10 2020 Vitaly Lipatov <lav@altlinux.ru> 13.10.1-alt1
- new version 13.10.1
- set node ABI to 13

* Tue Mar 03 2020 Vitaly Lipatov <lav@altlinux.ru> 13.9.0-alt3
- use direct /usr/lib/node_modules instead of detected prefix/lib/node

* Fri Feb 28 2020 Vitaly Lipatov <lav@altlinux.ru> 13.9.0-alt2
- drop profile with broken obsoleted NODE_PATH
- add /usr/lib/node symlink to /usr/lib/node_modules

* Thu Feb 20 2020 Vitaly Lipatov <lav@altlinux.ru> 13.9.0-alt1
- new version 13.9.0 (security fixes)
- set libicu >= 5.6

* Tue Feb 11 2020 Vitaly Lipatov <lav@altlinux.ru> 13.8.0-alt1
- new version 13.8.0 (with rpmrb script)
- CVE-2019-15606, CVE-2019-15605, CVE-2019-15604

* Mon Jan 20 2020 Vitaly Lipatov <lav@altlinux.ru> 13.6.0-alt2
- make node-devel as arch
- drop tarball with node include headers (see ALT bug 36349)
- add fixes for ix86 build

* Thu Jan 16 2020 Vitaly Lipatov <lav@altlinux.ru> 13.6.0-alt1
- new version 13.6.0 (with rpmrb script)
- libuv >= 1.34.0
- switch to python3

* Thu Jan 16 2020 Vitaly Lipatov <lav@altlinux.ru> 12.14.1-alt1
- new version 12.14.1 (with rpmrb script)
- build without system http-parser (use bundled llhttp 2.0.1)

* Thu Jan 16 2020 Pavel Skrylev <majioa@altlinux.org> 10.18.0-alt2
- added (+) tarball for node include headers to devel package

* Thu Dec 26 2019 Vitaly Lipatov <lav@altlinux.ru> 10.18.0-alt1
- new version 10.18.0 (with rpmrb script)
- npm >= 6.13.4 (security fix)

* Sat Oct 26 2019 Vitaly Lipatov <lav@altlinux.ru> 10.17.0-alt1
- new version 10.17.0 (with rpmrb script)
- npm >= 6.11.3

* Fri Aug 30 2019 Vitaly Lipatov <lav@altlinux.ru> 10.16.3-alt1
- new version 10.16.3 (with rpmrb script)
- libnghttp2 >= 1.39.2
- CVE-2019-9511, CVE-2019-9511, CVE-2019-9513, CVE-2019-9514
- CVE-2019-9515, CVE-2019-9516, CVE-2019-9517, CVE-2019-9518

* Thu Jun 06 2019 Vitaly Lipatov <lav@altlinux.ru> 10.16.0-alt1
- new version 10.16.0 (with rpmrb script)
- 2019-05-28, Version 10.16.0 'Dubnium' (LTS), @BethGriggs
- use npm 6.9, ICU >= 6.4, libuv >= 1.28.0

* Sat Mar 09 2019 Vitaly Lipatov <lav@altlinux.ru> 10.15.3-alt1
- new version 10.15.3 (with rpmrb script)
- 2018-03-05, Version 10.15.3 'Dubnium' (LTS), @BethGriggs
- CVE-2019-5737
- fix rpm's cflags using, add -latomic on mipsel
- use external gyp

* Thu Jan 17 2019 Vitaly Lipatov <lav@altlinux.ru> 10.15.0-alt1
- new version 10.15.0 (with rpmrb script)
- 2018-12-26, Version 10.15.0 'Dubnium' (LTS), @MylesBorins
- rebuild with http-parser 2.9.0

* Fri Dec 14 2018 Vitaly Lipatov <lav@altlinux.ru> 10.14.2-alt1
- new version 10.14.2 (with rpmrb script)
- 2018-12-11, Version 10.14.2 'Dubnium' (LTS), @MylesBorins prepared by @codebytere

* Fri Nov 30 2018 Vitaly Lipatov <lav@altlinux.ru> 10.14.1-alt1
- new version 10.14.1 (with rpmrb script)
- disable internal doc
- 2018-11-27, Version 10.14.0 'Dubnium' (LTS), @rvagg
- CVE-2018-12121, CVE-2018-12122, CVE-2018-12123

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 10.13.0-alt1
- new version 10.13.0 (with rpmrb script)
- 2018-10-30, Version 10.13.0 'Dubnium' (LTS), @MylesBorins

* Sat Oct 06 2018 Vitaly Lipatov <lav@altlinux.ru> 8.12.0-alt1
- new version 8.12.0 (with rpmrb script)
- 2018-09-11, Version 8.12.0 'Carbon' (LTS)

* Wed Aug 29 2018 Vitaly Lipatov <lav@altlinux.ru> 8.11.4-alt1
- new version 8.11.4 (with rpmrb script)
- 2018-08-15, Version 8.11.4 'Carbon' (LTS), @rvagg
- CVE-2018-0732, CVE-2018-12115
- build with external libnghttp2
- fix build with ICU >= 61 (add -DU_USING_ICU_NAMESPACE=1)

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 8.11.3-alt1
- new version (8.11.3) with rpmgs script
- 2018-06-12, Version 8.11.3 'Carbon' (LTS), @evanlucas
- CVE-2018-7167, CVE-2018-7161, CVE-2018-1000168

* Tue May 22 2018 Vitaly Lipatov <lav@altlinux.ru> 8.11.2-alt1
- new version (8.11.2) with rpmgs script
- 2018-05-15, Version 8.11.2 'Carbon' (LTS)

* Mon May 21 2018 Vitaly Lipatov <lav@altlinux.ru> 6.14.2-alt1
- new version 6.14.2 (with rpmrb script)
- 2018-04-30 Node.js v6.14.2 'Boron' (LTS) Release

* Tue Feb 27 2018 Alexey Shabalin <shaba@altlinux.ru> 6.13.0-alt1
- new version 6.13.0
- 2018-02-13, Version 6.13.0 'Boron' (LTS)
- fixed CVE-2017-15896, CVE-2017-3738

* Sat Oct 07 2017 Vitaly Lipatov <lav@altlinux.ru> 6.11.4-alt1
- new version 6.11.4 (with rpmrb script)
- 2017-10-03, Version 6.11.4 'Boron' (LTS)

* Fri Jul 14 2017 Vitaly Lipatov <lav@altlinux.ru> 6.11.1-alt1
- new version 6.11.1 (with rpmrb script)
- 2017-07-11 v6.11.1 'Boron' (LTS) Release

* Mon May 08 2017 Vitaly Lipatov <lav@altlinux.ru> 6.10.3-alt1
- new version 6.10.3 (with rpmrb script)
- 2017-05-02, Version 6.10.3 'Boron' (LTS)

* Sat Apr 08 2017 Vitaly Lipatov <lav@altlinux.ru> 6.10.2-alt1
- new version 6.10.2 (with rpmrb script)
- 2017-04-04, Version 6.10.2 'Boron' (LTS), @MylesBorins

* Sat Mar 11 2017 Vitaly Lipatov <lav@altlinux.ru> 6.10.0-alt1
- new version 6.10.0 (with rpmrb script)
- 2017-02-21 Node.js v6.10.0 'Boron' (LTS) Release

* Thu Feb 02 2017 Vitaly Lipatov <lav@altlinux.ru> 6.9.3-alt1
- new version 6.9.3 (with rpmrb script)
- 2017-01-03, Version 6.9.3 'Boron' (LTS)

* Sun Dec 18 2016 Vitaly Lipatov <lav@altlinux.ru> 6.9.2-alt2
- build without npm subpackage

* Wed Dec 07 2016 Vitaly Lipatov <lav@altlinux.ru> 6.9.2-alt1
- new version 6.9.2 (with rpmrb script)
- 2016-12-06 Node.js v6.9.2 'Boron' (LTS) Release

* Wed Nov 30 2016 Vitaly Lipatov <lav@altlinux.ru> 6.9.1-alt1
- new version 6.9.1 (with rpmrb script)
- 2016-10-19 Node.js v6.9.1 'Boron' (LTS) Release

* Wed Oct 05 2016 Vitaly Lipatov <lav@altlinux.ru> 6.7.0-alt6
- new version 6.7.0 (with rpmrb script)

* Fri Sep 02 2016 Vitaly Lipatov <lav@altlinux.ru> 6.5.0-alt5
- new version 6.5.0 (with rpmrb script)

* Wed Aug 24 2016 Vitaly Lipatov <lav@altlinux.ru> 6.4.0-alt4
- build 2016-08-15 Node.js v6.4.0 (Current) Release

* Wed Aug 03 2016 Vitaly Lipatov <lav@altlinux.ru> 6.3.1-alt3
- build 2016-07-21 Node.js v6.3.1 (Current) Release
- build with system libicu, libhttp_parser, c-ares

* Fri Jul 15 2016 Vitaly Lipatov <lav@altlinux.ru> 6.3.0-alt2
- cleanup spec

* Thu Jul 14 2016 Evgeny Bovykin <missingdays@etersoft.ru> 6.3.0-alt1
- build 2016-07-06 Node.js v6.3.0 Release

* Thu Jun 16 2016 Vitaly Lipatov <lav@altlinux.ru> 4.4.5-alt1
- build 2016-05-24 Version 4.4.5 'Argon' (LTS)

* Wed Apr 13 2016 Vitaly Lipatov <lav@altlinux.ru> 4.4.3-alt1
- build 2016-04-12, Version 4.4.3 'Argon' (LTS)
- drop gnuplot and convert reqs from npm
- disable python reqs for npm package

* Wed Feb 10 2016 Vitaly Lipatov <lav@altlinux.ru> 4.2.6-alt2
- build with system libuv-devel 1.8.0
- fix include packing

* Tue Feb 09 2016 Vitaly Lipatov <lav@altlinux.ru> 4.2.6-alt1
- 2016-01-21 Node.js v4.2.6 "Argon" (LTS) Release (ALT bug #30191)
- build with system openssl 1.0.2
- split doc subpackage

* Mon Nov 23 2015 Vitaly Lipatov <lav@altlinux.ru> 4.2.2-alt1
- build 4.2.2 LTS version
- build with static v8 4.5 and static openssl 1.0.2

* Wed Oct 02 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.20-alt1
- new version
- npm 1.3.8

* Sun Sep 15 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.18-alt1
- new version

* Sat Aug 17 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.16-alt1
- new version
- npm 1.3.8

* Sat Jul 27 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.15-alt2.1
- libv8 requires

* Sat Jul 27 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.15-alt2
- nodejs(engine) should be = %%version
- added explicit abi autorequires for binary packages
- fix for %ix86 compilation w/o -fPIC
- explicit linkage with libv8

* Fri Jul 26 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.15-alt1
- new version
- npm 1.3.5

* Sat Jul 13 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.13-alt1
- 0.10.13
- npm 1.3.2
- added node-devel (ALT #29182)

* Wed Jun 26 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.12-alt1
- 0.10.12
- npm 1.2.32
- Provides: nodejs(engine) by viy@

* Wed May 29 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.8-alt1
- 0.10.8
- npm 1.2.23

* Tue May 07 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.5-alt1
- 0.10.5

* Thu Apr 18 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.4-alt1
- 0.10.4
- npm 1.2.18

* Sat Apr 06 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.3-alt1
- 0.10.3
- npm 1.2.17
- Build with shared libuv

* Fri Mar 29 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.2-alt1
- 0.10.2
- npm 1.2.15

* Sun Feb 10 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.8.19-alt1
- 0.8.19
- nmp 1.2.10

* Fri Jan 25 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.8.18-alt1.1
- Fix spec
  + non-strict dependency on node
  + added %optflags on build

* Sun Jan 20 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.8.18-alt1
- 0.8.18
- npm 1.2.2

* Sat Oct 27 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.8.14-alt1
- v0.8.14
- npm v1.1.65

* Mon Jul 23 2012 Mikhail Pokidko <pma@altlinux.org> 0.8.3-alt1
- v0.8.3

* Tue Jun 26 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.8.0-alt1
- 0.8.0

* Thu Jun 21 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.6.19-alt4
- Fix BuildRequires
- Added rpm-build-node subpackage
- Provides nodejs node.js
- Separate package devel

* Sun Jun 17 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.6.19-alt3.1
- Conflicts with node.js

* Sun Jun 17 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.6.19-alt3
- Declare NODE_PATH

* Sun Jun 17 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.6.19-alt2
- npm is noarch package

* Sun Jun 17 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.6.19-alt1
- v0.6.19
- Separate npm package

* Sat May 05 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.17-alt1
- v0.6.17

* Tue Apr 10 2012 Mikhail Pokidko <pma@altlinux.org> 0.6.15-alt1
- v0.6.15

* Mon Feb 06 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.10-alt1
- v0.6.10

* Sun Jan 29 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.9-alt1
- v0.6.9

* Fri Dec 02 2011 Mikhail Pokidko <pma@altlinux.org> 0.6.4-alt1
- v0.6.4

* Mon Nov 28 2011 Mikhail Pokidko <pma@altlinux.org> 0.6.3-alt1
- v0.6.3

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.11-alt1.1
- Rebuild with Python-2.7

* Mon Aug 22 2011 Mikhail Pokidko <pma@altlinux.org> 0.4.11-alt1
- v0.4.11

* Tue Jun 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.8-alt1
- initial

