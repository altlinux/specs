%define userrldp _rldp-http-proxy

Name: ton
Version: 2026.04
Release: alt1

Summary: TON - The Open Network tools

License: GPLv2
Group: Networking/Other
Url: https://github.com/ton-blockchain/ton

Packager: Vitaly Lipatov <lav@altlinux.ru>

# [ppc64le] gmake[3]: *** [crypto/CMakeFiles/gen_fif_smartcont_auto_elector_code.dir/build.make:78: ../crypto/smartcont/auto/elector-code.cpp] Illegal instruction
# [arhm] /usr/src/RPM/BUILD/ton-2022.12/third-party/rocksdb/utilities/transactions/lock/range/range_tree/lib/locktree/../portability/toku_time.h:141:2: error: #error No timer implementation for this platform
ExclusiveArch: x86_64 aarch64

# Source-url: https://github.com/ton-blockchain/ton/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

# Source1-url: https://ton.org/global-config.json
Source1: global.config.json

# Source2-url: https://ton.org/testnet-global.config.json
Source2: testnet-global.config.json

Source3: rldp-http-proxy.service

# instead of .gitmodules
# Source4-url: https://github.com/google/crc32c/archive/refs/tags/1.1.2.tar.gz
Source4: %name-crc32c-%version.tar

# Source5-url: https://github.com/facebook/rocksdb/archive/refs/tags/v8.6.7.tar.gz
Source5: %name-rocksdb-%version.tar

# Source6-url: https://github.com/supranational/blst/archive/refs/tags/v0.3.15.tar.gz
Source6: %name-blst-%version.tar

# TON-specific forks (submodules)
Source7: %name-tl-parser-%version.tar
Source8: %name-libraptorq-%version.tar

Source9: %name-secp256k1-%version.tar

Patch2: ton-use-system-libs.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake >= 3.17
BuildRequires: gcc-c++

BuildRequires: git-core

BuildRequires: zlib-devel libssl-devel libreadline-devel

BuildRequires: libsodium-devel

# for storage-daemon
BuildRequires: libblas-devel libgsl-devel

# for blockchain-explorer
BuildRequires: libmicrohttpd-devel
BuildRequires: liblz4-devel
BuildRequires: libbacktrace-devel

# Unusable -DTON_USE_ROCKSDB=OFF
# due
#$ grep Rocks adnl/adnl-db.cpp 
##include "td/db/RocksDb.h"
#  kv_ = std::make_shared<td::RocksDb>(td::RocksDb::open(path_).move_as_ok());
# TODO: not supported external libs
#BuildRequires: librocksdb-devel

# TODO: use instead of embedded crc32c
#BuildRequires: libcrc32c-devel

BuildRequires: libabseil-cpp-devel

%description
TON - The Open Network.
The next gen network to unite all blockchains and the existing Internet.

%package common
Summary: TON common files
Group: Networking/WWW
BuildArch: noarch
#Requires: %name = %EVR

%description common
TON common files.


%package rldp-http-proxy
Summary: TON RLDP-HTTP Proxy
Group: Networking/WWW
Requires: %name-common = %EVR

%description rldp-http-proxy
The RLDP-HTTP Proxy is a special utility specially designed for accessing and creating TON Sites.


%package crypto
Summary: TON crypto
Group: Networking/WWW
Requires: %name-common = %EVR

%description crypto
TON crypto utils foft and func.


%package cli
Summary: TON tonlib-cli
Group: Networking/WWW
Requires: %name-common = %EVR

%description cli
TON tonlib-cli.


%package lite-client
Summary: TON lite-client
Group: Networking/WWW
Requires: %name-common = %EVR

%description lite-client
TON lite-client.


%package tools
Summary: TON tools
Group: Networking/WWW
Requires: %name-common = %EVR

%description tools
TON tools:
generate-random-id


%package storage-daemon
Summary: TON tools
Group: Networking/WWW
Requires: %name-common = %EVR

%description storage-daemon
TON
storage-daemon
storage-daemon-cli


%prep
%setup -a4 -a5 -a6 -a7 -a8 -a9
%patch2 -p1

# Use system abseil instead of bundled subdirectory build
%__subst 's|add_subdirectory(third-party/abseil-cpp EXCLUDE_FROM_ALL)|find_package(absl REQUIRED)|' CMakeLists.txt

# disambiguate co_return {} for Task<Unit> with newer GCC
find adnl overlay -name '*.cpp' -o -name '*.h' | xargs -r %__subst 's|co_return {};|co_return td::Unit{};|'

%build
%cmake -DTON_USE_ROCKSDB=ON -DTON_USE_ABSEIL=ON -DUSE_QUIC=OFF
%cmake_build --target rldp-http-proxy
%cmake_build --target generate-random-id
%cmake_build --target lite-client
%cmake_build --target tonlib-cli
%cmake_build --target fift func
%cmake_build --target storage-daemon storage-daemon-cli

%install
install -m0644 -D %SOURCE1 %buildroot%_sysconfdir/%name/global.config.json
install -m0644 -D %SOURCE2 %buildroot%_sysconfdir/%name/testnet-global.config.json
install -m0644 -D %SOURCE3 %buildroot%_unitdir/rldp-http-proxy.service

cd %_cmake__builddir
mkdir -p %buildroot%_bindir/
install -m0755 rldp-http-proxy/rldp-http-proxy %buildroot%_bindir/
install -m0755 lite-client/lite-client %buildroot%_bindir/
install -m0755 tonlib/tonlib-cli %buildroot%_bindir/
install -m0755 utils/generate-random-id %buildroot%_bindir/
install -m0755 crypto/fift %buildroot%_bindir/
install -m0755 crypto/func %buildroot%_bindir/
install -m0755 storage/storage-daemon/storage-daemon %buildroot%_bindir/
install -m0755 storage/storage-daemon/storage-daemon-cli %buildroot%_bindir/

%pre rldp-http-proxy
%_sbindir/groupadd -r -f %userrldp &>/dev/null
%_sbindir/useradd -r -n -g %userrldp -d /var/empty -s /bin/false -c "%userrldp pseudo user" %userrldp >/dev/null 2>&1 ||:

%post rldp-http-proxy
%post_service rldp-http-proxy

%preun rldp-http-proxy
%preun_service rldp-http-proxy

%files common
%dir %_sysconfdir/%name/
%config(noreplace) %attr(644,root,root) %_sysconfdir/%name/global.config.json
%config(noreplace) %attr(644,root,root) %_sysconfdir/%name/testnet-global.config.json

%files rldp-http-proxy
%_bindir/rldp-http-proxy
%_unitdir/rldp-http-proxy.service

%files crypto
%_bindir/fift
%_bindir/func

%files cli
%_bindir/tonlib-cli

%files lite-client
%_bindir/lite-client

%files tools
%_bindir/generate-random-id

%files storage-daemon
%_bindir/storage-daemon
%_bindir/storage-daemon-cli


%changelog
* Wed May 06 2026 Vitaly Lipatov <lav@altlinux.ru> 2026.04-alt1
- new version 2026.04
- enable libabseil-cpp-devel (now required by upstream)
- drop Patch1 (already applied upstream)

* Wed Mar 11 2026 Vitaly Lipatov <lav@altlinux.ru> 2026.02-alt1
- new version 2026.02 (with rpmrb script)
- add -DUSE_QUIC=OFF (disable bundled ngtcp2/openssl QUIC)
- add patch to use system OpenSSL, libsodium, liblz4, libsecp256k1,
  libbacktrace, libmicrohttpd, zlib instead of bundled third-party builds
- add bundled tl-parser and libraptorq (TON-specific forks)
- update bundled blst to 0.3.15

* Sun Mar 17 2024 Vitaly Lipatov <lav@altlinux.ru> 2024.03-alt1
- new version 2024.03 (with rpmrb script)

* Fri Jul 28 2023 Vitaly Lipatov <lav@altlinux.ru> 2023.06-alt1
- new version 2023.06 (with rpmrb script)
- add BuildRequires: libmicrohttpd-devel
- applied fix for build embedded rocksdb with gcc13

* Fri Jul 28 2023 Vitaly Lipatov <lav@altlinux.ru> 2023.03-alt2
- real build 2023.03 (fix Source URL)

* Mon Mar 13 2023 Vitaly Lipatov <lav@altlinux.ru> 2023.03-alt1
- new version 2023.03 (with rpmrb script)

* Tue Jan 24 2023 Vitaly Lipatov <lav@altlinux.ru> 2022.12-alt1
- initial build for ALT Sisyphus
