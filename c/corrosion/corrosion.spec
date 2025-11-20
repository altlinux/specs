%def_with check

Name:    corrosion
Version: 0.5.2
Release: alt1

Summary: Marrying Rust and CMake - Easy Rust and C/C++ Integration!
License: MIT
Group:   Development/Tools

URL: https://corrosion-rs.github.io/corrosion
VCS: https://github.com/corrosion-rs/corrosion.git

Source0: %name-%version.tar
Source1: vendor.tar
Source2: config.toml

# https://github.com/corrosion-rs/corrosion/pull/605
Patch0: corrosion-0.5.2-upstream-fix-tests.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires: rust-cargo
%if_with check
BuildRequires: ctest gcc-c++ cbindgen
%endif

%description
Corrosion, formerly known as cmake-cargo, is a tool for integrating Rust into an
existing CMake project. Corrosion is capable of automatically importing
executables, static libraries, and dynamic libraries from a workspace or package
manifest (Cargo.toml file).

%prep
%setup -a1
install -vpD %SOURCE2 .cargo/config.toml
# Check for non-source files
find vendor \( -name '*.a' -o -name '*.lib' -o -name '*.dll' \) | grep . && exit 1
%patch0 -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
export CARGO_HOME="./.cargo"
%ctest

%files
%doc *.md LICENSE
%_libdir/cmake/Corrosion
%_datadir/cmake/*

%changelog
* Tue Nov 18 2025 Ilya Sorochan <k0tran@altlinux.org> 0.5.2-alt1
- Initial build.
