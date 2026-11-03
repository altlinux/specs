%define pypi_name etebase

Name: python3-module-%pypi_name
Version: 0.32.0
Release: alt1

Summary: Python client library for Etebase

License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/etesync/etebase-py

# Source-url: https://github.com/etesync/etebase-py/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
# Cargo crates for the Rust extension
Source1: %name-development-%version.tar
Source2: config.toml
BuildRequires: rpm-build-python3
BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust /proc
BuildRequires: python3-module-maturin
BuildRequires: pkgconfig(libsodium) pkgconfig(openssl)
# for %%check
BuildRequires: python3-module-msgpack

%description
Etebase is an end-to-end encrypted backend as a service: it allows
to sync contacts, calendars, tasks, notes and other data securely.

This package contains the Python client library (bindings to
etebase-rs), used for example by etesync-dav.

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml

%build
# use system libraries instead of the bundled OpenSSL/libsodium
export OPENSSL_NO_VENDOR=1
export SODIUM_USE_PKG_CONFIG=1
export CARGO_NET_OFFLINE=true
export CARGO_PROFILE_RELEASE_DEBUG=true
%pyproject_build

%install
%pyproject_install

%check
# tests/test_smoketest.py needs a running etebase server, do offline checks
cd tests
PYTHONPATH=%buildroot%python3_sitelibdir %__python3 - <<'EOF'
import etebase
client = etebase.Client("alt-check", "http://localhost:8033")
raw = bytes(etebase.random_bytes(32))
assert len(raw) == 32
assert etebase.Base64Url.from_base64(etebase.Base64Url.to_base64(raw)) == raw
print(etebase.pretty_fingerprint(raw))
user = etebase.User("alt", "alt@localhost")
assert (user.username, user.email) == ("alt", "alt@localhost")
EOF

%files
%doc README.md LICENSE
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Nov 03 2026 Vitaly Lipatov <lav@altlinux.ru> 0.32.0-alt1
- new version 0.32.0
- replaced BuildRequires: python3-module-setuptools, python3-module-wheel,
  python3-module-setuptools_rust and /usr/bin/rustfmt with
  python3-module-maturin
- dropped obsolete rust-cpython Python 3.14 patch

* Mon Oct 05 2026 Vitaly Lipatov <lav@altlinux.ru> 0.31.8-alt1
- initial build for Sisyphus

