%define _unpackaged_files_terminate_build 1

Name: python3-module-admix
Version: 0.1.1
Release: alt1

Summary: Python bindings for the admix Group Policy editing library
License: MIT
Group: Development/Python
Url: https://git.wetgrape.su/kiper220/libadmix
Vcs: https://git.wetgrape.su/kiper220/libadmix.git

Source: admix-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-maturin
BuildRequires: /proc

%description
Python 3 bindings for the admix library for reading and editing
Microsoft-compatible Group Policy files. It supports Administrative Templates,
Group Policy Preferences, Registry.pol, security templates and GPO metadata.

%prep
%setup -n admix-%version
%rust_prep

%build
export CARGO_NET_OFFLINE=true
export RUSTFLAGS="-g"
%pyproject_build

%install
%pyproject_install

%check
export CARGO_NET_OFFLINE=true
export RUSTFLAGS="-g"
%rust_test --locked
%pyproject_run -- python3 -c 'import admix; assert admix.HighLevelApi'

%files
%doc LICENSE README.md docs/
%python3_sitelibdir/admix/
%python3_sitelibdir/admix-%version.dist-info/

%changelog
* Fri Jul 31 2026 Korney Gedert <kiper@altlinux.org> 0.1.1-alt1
- Added browser-selected localization for built-in strings.
- Added typed language choices and preserved unknown policy values.
- Reworked internal architecture and hardened storage and API boundaries.

* Mon Jul 13 2026 Korney Gedert <kiper@altlinux.org> 0.1.0-alt1
- Initial build.
