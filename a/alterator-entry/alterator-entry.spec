%define _unpackaged_files_terminate_build 1
%define mod_name alterator_entry

Name: alterator-entry
Version: 0.2.3
Release: alt1

Summary: Common files for Alterator Entry specification
License: GPLv3+
Group: Other
URL: https://gitlab.basealt.space/alt/alterator-entry

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

BuildArch: noarch

BuildRequires(pre): rpm-macros-alterator
BuildRequires: python3-module-alterator-entry

%description
Common files for Alterator Entry specification:
- specification documents
- TOML schemas for Alterator Entry types
- alterator-entry script to validate Alterator Entry files and extract data

%package -n python3-module-alterator-entry
Summary: Python3 module to validate and extract fields from Alterator Entry
Group: Development/Python3

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description -n python3-module-alterator-entry 
%summary.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install
install -D -m 755 alterator_entry/cli %buildroot%_bindir/%name
mkdir -p %buildroot%_alterator_datadir
cp -r ./schemas %buildroot%_alterator_datadir/schemas 

%check
export ALTERATOR_SCHEMAS_DIR=./schemas
find examples -type f | xargs ./alterator_entry/cli validate

%files
%doc COPYING
%doc %_alterator_datadir/schemas/
%_bindir/alterator-entry

%files -n python3-module-alterator-entry
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Mon Mar 03 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.2.3-alt1
- Update enum with needed desktops in schemas
- Fix properties definition in object schema

* Mon Feb 17 2025 Michael Chernigin <chernigin@altlinux.org> 0.2.2-alt1
- Update deps to use tomlkit
- Add overrides key to object (thx Алексеев Андрей Михайлович)
- Add %check section validating examples

* Mon Feb 03 2025 Michael Chernigin <chernigin@altlinux.org> 0.2.1-alt2
- Remove feature filtering for toml and tompllib as it is no longer needed.

* Sun Feb 02 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.2.1-alt1
- Build with oldest rpm-build-pyproject and python3-module-pyproject-installer
  (which not support of using default pyproject.toml if it not found).
- Avoid of using special release for python3-module-alterator-entry.

* Thu Jan 30 2025 Michael Chernigin <chernigin@altlinux.org> 0.2.0-alt1
- Switch from using bash and taplo to python tool for validating files
- Schema changes in components and editions
  + Add supported arches to components
  + Remove region from editions

* Tue Dec 24 2024 Andrey Limachko <liannnix@altlinux.org> 0.1.2-alt1
- Make stub to build package for all architectures

* Tue Dec 03 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.1-alt1
- Switch to using toml instead of ini files for Alterator Entry.
- Add json schemas to validate Alterator Entry files.

* Tue Nov 21 2023 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0-alt3
- alterator-entry: fix version printing.

* Tue Nov 21 2023 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0-alt2
- alterator-entry: fix debug source and missed help about verbose mode.

* Tue Nov 21 2023 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus.
