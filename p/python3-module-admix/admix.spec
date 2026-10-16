%define _unpackaged_files_terminate_build 1

Name: python3-module-admix
Version: 0.3.0
Release: alt1

Summary: Python bindings for the admix Group Policy editing library
License: MPL-2.0
Group: Development/Python
Url: https://git.wetgrape.su/kiper220/libadmix
Vcs: https://git.wetgrape.su/kiper220/libadmix.git

Source: admix-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-maturin
BuildRequires: python3-module-pytest
BuildRequires: xml-utils
BuildRequires: sdmx-basealt >= 1.0.0
BuildRequires: sdmx-schemas >= 1.0.0
BuildRequires: /proc

Requires: xml-utils

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
%rust_test --locked --workspace
%pyproject_run -- python3 -c 'import admix; assert admix.GroupPolicyWorkspace; assert admix.Workspace'
%pyproject_run -- python3 -m pytest -q tests/test_python_api.py tests/test_python_native_workflows.py tests/test_python_security_definitions.py tests/test_python_catalog_concurrency.py

%files
%doc LICENSE README.md docs/
%python3_sitelibdir/admix/
%python3_sitelibdir/admix-%version.dist-info/

%changelog
* Thu Oct 01 2026 Korney Gedert <kiper@altlinux.org> 0.3.0-alt1
- Replaced the built-in security settings API with external SDMX/SDML 1.0
  catalogs, typed configuration and validation; this release changes the API.
- Added Administrative Template indexed and key-value collections, IPv6
  targeting, atomic targeting subtree moves and revision-checked script assets.
- Prepared reusable eager catalog indexes, portable normative schema tests,
  and locked offline vendor sources.

* Fri Sep 11 2026 Korney Gedert <kiper@altlinux.org> 0.2.0-alt1
- Added the faceted GroupPolicyWorkspace API and typed Rust/Python contracts.
- Added typed preference, security, script and publication workflows.
- Split large modules, expanded protocol documentation and strengthened checks.

* Mon Aug 17 2026 Korney Gedert <kiper@altlinux.org> 0.1.2-alt1
- Relicensed to MPL-2.0.
- Extracted ADMX/ADML, CMT, PREG and GPP XML engines into dedicated
  format crates (libadmx, libcmt, libpreg, gpreface, anyfs) and retired
  the roxmltree backend.
- Hardened atomic file writes, UTF-16 source handling and MS-ADTS
  conformance of GPT.INI, GptTmpl and Scripts.ini.

* Fri Jul 31 2026 Korney Gedert <kiper@altlinux.org> 0.1.1-alt1
- Added browser-selected localization for built-in strings.
- Added typed language choices and preserved unknown policy values.
- Reworked internal architecture and hardened storage and API boundaries.

* Mon Jul 13 2026 Korney Gedert <kiper@altlinux.org> 0.1.0-alt1
- Initial build.
