%define _unpackaged_files_terminate_build 1
%define pypi_name pyenchant
%define mod_name enchant

%def_with check

Name: python3-module-enchant
Version: 3.2.2
Release: alt2
Summary: Python bindings for the Enchant spellchecking system
License: LGPLv2+
Group: Development/Python3
Url: https://pypi.org/project/pyenchant/
Vcs: https://github.com/pyenchant/pyenchant/
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
# used dynamically
Requires: libenchant
%pyproject_runtimedeps_metadata
# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: hunspell-en_US
%endif
BuildRequires: libenchant-devel

%description
PyEnchant combines all the functionality of the underlying Enchant
library with the flexibility of Python and a nice "Pythonic"
object-oriented interface. It also aims to provide some higher-level
functionality than is available in the C API.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%mod_name/checker/*CheckerDialog*

%changelog
* Fri Apr 28 2023 Stanislav Levin <slev@altlinux.org> 3.2.2-alt2
- Modernized packaging.
- Mapped PyPI name to distro's one.

* Wed Mar 08 2023 Vitaly Lipatov <lav@altlinux.ru> 3.2.2-alt1
- new version 3.2.2 (with rpmrb script)

* Fri Aug 13 2021 Vitaly Lipatov <lav@altlinux.ru> 3.2.1-alt2
- NMU: restore missed libenchant

* Fri Aug 13 2021 Vitaly Lipatov <lav@altlinux.ru> 3.2.1-alt1
- NMU: cleanup spec
- NMU: new version 3.2.1 (with rpmrb script)

* Thu Mar 15 2018 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt2
- Add packaging egg-info.

* Wed Mar 14 2018 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- Build new version.
- Get rid of ugly macros.
- Add missing Requires.
- Change url, license.

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6.5-alt5
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6.5-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 25 2014 Fr. Br. George <george@altlinux.ru> 1.6.5-alt4
- Fix build

* Wed May 22 2013 Fr. Br. George <george@altlinux.ru> 1.6.5-alt3
- Change specsubst scheme
- Separate GUI dialogs

* Mon May 13 2013 Fr. Br. George <george@altlinux.ru> 1.6.5-alt2
- Implement specsubst scheme
- Build for python3 also

* Sun Oct 30 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.5-alt1.1
- Rebuild with Python-2.7

* Thu Oct 20 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.5-alt1
- initial build for sisyphus

