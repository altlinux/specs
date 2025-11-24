%define _unpackaged_files_terminate_build 1
%define mod_name alterator_entry

Name: alterator-entry
Version: 0.4.5
Release: alt1

Summary: Common files for Alterator Entry specification
License: GPLv3+
Group: Other
URL: https://altlinux.space/alterator/alterator-entry

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

BuildArch: noarch

BuildRequires(pre): rpm-macros-alterator

%description
Common files for Alterator Entry specification:
- specification documents
- TOML schemas for Alterator Entry types
- alterator-entry script to validate Alterator Entry files and extract data
- editions2packages script to extract packages from editions

%package -n python3-module-alterator-entry
Summary: Python3 module to validate and extract fields from Alterator Entry
Group: Development/Python3

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: python3-module-tomlkit
BuildRequires: python3-module-jsonschema

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
install -D -m 755 scripts/alterator-entry %buildroot%_bindir/alterator-entry
install -D -m 755 scripts/editions2packages %buildroot%_bindir/editions2packages

mkdir -p %buildroot%_alterator_datadir
cp -r ./schemas %buildroot%_alterator_datadir/schemas 

%check
export ALTERATOR_SCHEMAS_DIR=./schemas
export PYTHONPATH=./alterator_entry:$PYTHONPATH
find examples -type f | xargs ./scripts/alterator-entry validate

%files
%doc COPYING
%doc %_alterator_datadir/schemas/
%_bindir/alterator-entry
%_bindir/editions2packages

%files -n python3-module-alterator-entry
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Tue Sep 30 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.4.5-alt1
- Fix documentation (thx Alexey Saprunov)
- Update service entitys (thx Andrey Alekseev):
  + feat: array label
  + feat: internal parameters
  + change: replace 'exclusive' objects with enum subparameters

* Tue Jul 22 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.4.4-alt1
- Add short_display_name for components and categories (thx Michael Chernigin)

* Tue Jul 22 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.4.3-alt1
- Improve service entry (thx Andrey Alekseev)
- Update documentation for service entry (thx Andrey Alekseev)

* Mon Jul 21 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.4.2-alt1
- Add support for reading key names for tables in get_field()

* Tue Jun 03 2025 Michael Chernigin <chernigin@altlinux.org> 0.4.1-alt1
- Add tags for components and editions

* Fri Mar 28 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.4.0-alt1
- Add new entity for services: examples, schema and docs (thx Evgenii Sozonov)
- Change desktop option in components schema to set of desktops

* Mon Mar 17 2025 Michael Chernigin <chernigin@altlinux.org> 0.3.1-alt1
- Introduce draft flag

* Sat Mar 08 2025 Andrey Limachko <liannnix@altlinux.org> 0.3-alt1
- Add filter by section
- Strip component name in component path

* Wed Mar 05 2025 Michael Chernigin <chernigin@altlinux.org> 0.2.4-alt2
- Fix build dependency of python3-module-alterator-entry on itself.
- Remove duplicate scripts install.
- Add wheel to deps json to build for p11.

* Mon Mar 04 2025 Michael Chernigin <chernigin@altlinux.org> 0.2.4-alt1
- Add editions2packages script to extract packages from editions

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
