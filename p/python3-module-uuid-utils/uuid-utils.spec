%define _unpackaged_files_terminate_build 1
%define pypi_name uuid-utils
%define module_name uuid_utils

%def_with check

Name: python3-module-%pypi_name
Version: 0.16.1
Release: alt1

Summary: Fast, drop-in replacement for Python's uuid module, powered by Rust
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/uuid_utils/
Vcs: https://github.com/aminalaee/uuid-utils

Source0: %name-%version.tar
Source1: crates.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-maturin
BuildRequires: python3-dev
BuildRequires: rust-cargo
BuildRequires: /proc
%if_with check
BuildRequires: python3-module-pytest
%endif

%description
%summary.

Available UUID versions:
* uuid1 - Version 1 UUIDs using a timestamp and monotonic counter.
* uuid3 - Version 3 UUIDs based on the MD5 hash of some data.
* uuid4 - Version 4 UUIDs with random data.
* uuid5 - Version 5 UUIDs based on the SHA1 hash of some data.
* uuid6 - Version 6 UUIDs using a timestamp and monotonic counter.
* uuid7 - Version 7 UUIDs using a Unix timestamp ordered by time.
* uuid8 - Version 8 UUIDs using user-defined data.

%prep
%setup -a1
%autopatch -p1
mkdir -p .cargo
cat << EOF > .cargo/config.toml
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[install]
root = "%buildroot%prefix"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1", "--cfg=rustix_use_libc"]

[profile.release]
strip = false
EOF

%build
%pyproject_build

%install
%pyproject_install

%check
# tests/test_uuid.py::test_getnode
# --------------------------------
# Exclude the test_getnode test since it uses a MAC address to return an
# integer. However, there're no network interfaces in a Hasher environment,
# so it uses a random MAC address. Therefore, getnode from the standard uuid
# module and getnode from uuid_utils return different values.
%pyproject_run_pytest \
	--deselect="tests/test_uuid.py::test_getnode"

%files
%doc README.md LICENSE.md
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jun 16 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.16.1-alt1
- Updated to 0.16.1.

* Tue Mar 17 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.14.1-alt1
- Initial build for ALT Sisyphus.
