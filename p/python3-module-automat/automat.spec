%define _unpackaged_files_terminate_build 1
%define pypi_name Automat
%define mod_name automat

%def_with check

Name: python3-module-%mod_name
Version: 24.8.1
Release: alt1
Summary: Self-service finite-state machines for the programmer on the go
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/Automat/
Vcs: https://github.com/glyph/Automat
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%py3_provides %pypi_name
Provides: python3-module-%pypi_name = %EVR
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra visualize
%pyproject_builddeps_check
%endif

%description
Automat is a library for concise, idiomatic Python expression of finite-state
automata (particularly deterministic finite-state transducers).

%package visualize
Summary: %summary
Group: Development/Python3
Requires: %name
%pyproject_runtimedeps_metadata -- --extra visualize
Provides: %name+visualize = %EVR

%description visualize
Extra 'visualize' for %pypi_name.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

rm -r %buildroot%python3_sitelibdir/automat/_test/

%check
%pyproject_run_pytest -ra -Wignore src/automat/_test

%files
%python3_sitelibdir/%mod_name/
%exclude %python3_sitelibdir/%mod_name/_visualize.py
%exclude %python3_sitelibdir/%mod_name/__pycache__/_visualize.*
%python3_sitelibdir/%pypi_name-%version.dist-info/

%files visualize
%_bindir/automat-visualize
%python3_sitelibdir/%mod_name/_visualize.py
%python3_sitelibdir/%mod_name/__pycache__/_visualize.*

%changelog
* Thu Aug 22 2024 Stanislav Levin <slev@altlinux.org> 24.8.1-alt1
- 22.10.0 -> 24.8.1.

* Tue Jun 13 2023 Stanislav Levin <slev@altlinux.org> 22.10.0-alt1
- 20.2.0 -> 22.10.0

* Thu Sep 22 2022 Stanislav Levin <slev@altlinux.org> 20.2.0-alt3
- Modernized packaging.
- Dropped dependency on unmaintained m2r.
- Packaged visualize tool.
- Enabled testing.

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 20.2.0-alt2
- build python3 package separately

* Thu Mar 26 2020 Mikhail Gordeev <obirvalger@altlinux.org> 20.2.0-alt1
- new version (20.2.0) with rpmgs script

* Sun Jun 30 2019 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1
- new version 0.7.0 (with rpmrb script)

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1.qa1
- NMU: applied repocop patch

* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- initial build for ALT Sisyphus

