%define        _unpackaged_files_terminate_build 1
%def_disable   check

%ifndef        build_parallel_jobs
%global        build_parallel_jobs %__nprocs
%endif

%global        nodejs_abi 25
%define        major %nodejs_abi.8
%define        npmver 11.11.1
%define        nodegypver 12.2.0
%define        openssl_version 3.0.0

Name:          node-nightly
Version:       %major.2
Release:       alt2
Summary:       Evented I/O for V8 Javascript
Group:         Development/Tools
License:       MIT
Url:           https://nodejs.org/
Vcs:           https://github.com/nodejs/node.git

# https://nodejs.org/api/n-api.html
# https://github.com/nodejs/abi-stable-node

Source:        %name-%version.tar
Source3:       node.macros
Source4:       node.alternatives
Source5:       node-devel.alternatives
Source7:       nodejs_native.req.files
Patch6:        node-nightly.patch
Patch7:        no-ssl2-for-i586.patch

AutoProv:      yes,nopython,noshebang,nopython3,noshell
AutoReq:       yes,nopython,noshebang,nopython3,noshell
BuildRequires(pre): rpm-build-intro >= 2.1.14
BuildRequires(pre): rpm-macros-features
BuildRequires: gcc-c++
BuildRequires: curl
BuildRequires: gyp >= 0.10.0
BuildRequires: openssl
BuildRequires: python3-devel
BuildRequires: libbrotli-devel
BuildRequires: zlib-devel
BuildRequires: python3-module-simplejson
BuildRequires: python3-module-setuptools
BuildRequires: openssl-devel >= %openssl_version
BuildRequires: libcares-devel >= 1.18.1-alt1
BuildRequires: libnghttp2-devel
BuildRequires: libsimdjson-devel

Requires(pre): alternatives >= 0:0.2.0-alt0.12
Provides:      node = %EVR
Provides:      nodejs(engine) = %version
Provides:      nodejs = %EVR
Provides:      node.js = %EVR
Provides:      nodejs(abi) = %{nodejs_abi}
Provides:      npm(npm) = %{npmver}
Provides:      npm(node-gyp) = %{nodegypver}
Requires:      openssl >= %openssl_version

%ifarch        armh %ix86
%global        optflags_lto %nil
%define        optflags_debug -g0
%endif

%global node_patch_version $(echo %version | cut -d. -f3)

# ALT #35112
%_tune_parallel_build_by_procsize 1400

%add_findreq_skiplist %{_datadir}/node-nightly
%add_findreq_skiplist %{_libexecdir}/node-nightly
%add_findprov_skiplist %{_libexecdir}/node-nightly

%description
Node.js is a server-side JavaScript environment that uses an asynchronous
event-driven model.  Node's goal is to provide an easy way to build scalable
network programs.

%package       devel
Summary:       Devel package for Node.js
Group:         Development/Other
License:       MIT

AutoProv:      yes,nopython,noshebang,nopython3,noshell
AutoReq:       yes,nopython,noshebang,nopython3,noshell
Requires(pre): alternatives >= 0:0.2.0-alt0.12
Provides:      nodejs-nightly-devel = %EVR
Requires:      %name = %EVR
Requires:      gcc-c++
Requires:      curl
Requires:      gyp >= 0.10.0
Requires:      openssl
Requires:      python3-devel
Requires:      libbrotli-devel
Requires:      zlib-devel
Requires:      python3-module-simplejson
Requires:      python3-module-setuptools
Requires:      openssl-devel >= %openssl_version
Requires:      libcares-devel >= 1.18.1-alt1
Requires:      libnghttp2-devel

%description   devel
Node.js header and build tools


%package       -n rpm-macros-node-nightly
Epoch:         1
Summary:       rpm macros for Node nightly packages
Group:         Development/Ruby

Conflicts:     rpm-macros-nodejs

%description   -n rpm-macros-node-nightly
rpm macros for Node nightly packages.


%prep
%setup
%autopatch


# disable external libs
#rm -rf tools/gyp
rm -rf deps/zlib deps/cares deps/brotli deps/nghttp2/
# make no sense for a first build
%__subst "s|deps/zlib/zlib.gyp||" Makefile

# use rpm's cflags
%__subst "s|'cflags': \[\],|'cflags': ['%optflags'],|" ./configure.py
# fix cflags wrap in outputted config.json
%ifarch mipsel
%__subst "s|'libraries': \[\],|'libraries': ['-latomic'],|" ./configure.py
%endif

# override detected dir (detection via process.execPath does not work without /proc) with corect path
%__subst "s|path.resolve(prefixDir, 'lib', 'node')|'%nodejs_sitelib'|" lib/internal/modules/cjs/loader.js

%__subst "s|#define NODE_PATCH_VERSION.*|#define NODE_PATCH_VERSION %node_patch_version|" src/node_version.h

%build
export PYTHONPATH=$(pwd)/tools/v8_gypfiles

./configure \
   --prefix=%_prefix \
   --enable-lto \
   --shared-zlib \
   --shared-brotli \
   --shared-cares \
   --shared-openssl \
   --shared-openssl-includes=%_includedir \
   --shared-nghttp2 \
   --shared-simdjson \
   %nil

%make_build BUILDTYPE=Release

grep "^#\!\/usr\/bin\/env pwsh" -r |sed "s,:.*,," |while read -r f; do rm -rf "$f"; done
grep "^#\!\/usr\/bin\/env pwsh" -r |sed "s,:.*,," |while read -r f; do echo "$f"; done

%install
mkdir -p %buildroot%nodejs_sitelib/

%makeinstall_std

mkdir -p %buildroot%_altdir %buildroot%_libdir/%name/bin %buildroot%_libexecdir/%name/ %buildroot%nodejs_sitelib/npm
install -m 644 -D %SOURCE3 %buildroot%_rpmmacrosdir/node-nightly
install -m 644 -D %SOURCE4 %buildroot%_altdir/%name
install -m 644 -D %SOURCE5 %buildroot%_altdir/%name-devel

cat <<EOF >> %buildroot%nodejs_sitelib/npm/.npmrc
globalconfig=/etc/node-nightly/npmrc
update-notifier=false
EOF

mv %buildroot%_includedir/node %buildroot%{_includedir}/node-nightly/
mv %buildroot%_libexecdir/node_modules/ %buildroot%_libexecdir/%name/node_modules
ln -rvs %buildroot%_libexecdir/node-nightly/node_modules/npm/node_modules/node-gyp/ %buildroot%_libexecdir/node-nightly/node_modules/

# ensure Requires are added to every native module that match the Provides from
# the nodejs build in the buildroot
install -Dpm0755 %{SOURCE7} %buildroot%_rpmlibdir/nodejs_nightly_native.req.files
cat << EOF > %buildroot%_rpmlibdir/nodejs_nightly_native.req
#!/bin/sh
echo 'nodejs(abi) = %nodejs_abi'
EOF
chmod 0755 %buildroot%_rpmlibdir/nodejs_nightly_native.req

mv %buildroot%_bindir/node %buildroot%_libdir/%name/bin/

rm -rf %buildroot/usr/bin
rm -rf %buildroot/usr/lib/dtrace/
rm -rf %buildroot/usr/share/doc/node/gdbinit
rm -rf %buildroot/usr/share/doc/node/lldb_commands.py
rm -rf %buildroot/usr/share/doc/node/lldbinit
rm -rf %buildroot/usr/share/man/*

# drop tapset file
rm -rf %buildroot%_datadir/systemtap/tapset


%check
%make_build test


%files
%doc LICENSE README.md CHANGELOG.md
%_libdir/%name/bin/node
%_libexecdir/%name/node_modules
%_altdir/%name

%files         devel
%doc LICENSE README.md SECURITY.md CONTRIBUTING.md CODE_OF_CONDUCT.md BUILDING.md
%dir %_includedir/node-nightly/
%_includedir/node-nightly/v8*
%_includedir/node-nightly/node*
%_includedir/node-nightly/js_native_api*
%_includedir/node-nightly/common.gypi
%_includedir/node-nightly/config.gypi
%_includedir/node-nightly/libplatform/
%_includedir/node-nightly/cppgc/
%_includedir/node-nightly/uv*
%_rpmlibdir/nodejs_nightly_native.req
%_rpmlibdir/nodejs_nightly_native.req.files
%_altdir/%name-devel

%files         -n rpm-macros-node-nightly
%_rpmmacrosdir/node-nightly


%changelog
* Fri May 15 2026 Ilya Sorochan <k0tran@altlinux.org> 25.8.2-alt2
- NMU: switch from vendored simdjson to packaged

* Thu Mar 26 2026 Pavel Skrylev <majioa@altlinux.org> 25.8.2-alt1
- + packaged nightly node for compat purposes
