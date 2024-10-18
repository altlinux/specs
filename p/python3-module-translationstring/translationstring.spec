%define _unpackaged_files_terminate_build 1
%define pypi_name translationstring
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.4
Release: alt4

Summary: Utility library for i18n relied on by various Repoze packages
License: BSD-4-Clause
Group: Development/Python3
Url: https://pypi.org/project/translationstring/
Vcs: https://github.com/Pylons/translationstring
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: python3-module-pytest
%endif

%description
A library used by various Repoze packages for internationalization
(i18n) duties related to translation.

This package provides a translation string class, a translation string
factory class, translation and pluralization primitives, and a utility
that helps Chameleon templates use translation facilities of this
package. It does not depend on Babel, but its translation and
pluralization services are meant to work best when provided with an
instance of the babel.support.Translations class.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%mod_name/tests/

%changelog
* Fri Oct 18 2024 Stanislav Levin <slev@altlinux.org> 1.4-alt4
- Migrated from removed setuptools' test command (see #50996).

* Tue Jun 01 2021 Grigory Ustinov <grenka@altlinux.org> 1.4-alt3
- Fixed Build Requires.
- Fixed license tag.

* Fri Dec 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.4-alt2
- build for python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4-alt1.dev.git20141105.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4-alt1.dev.git20141105.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.4-alt1.dev.git20141105.1
- NMU: Use buildreq for BR.

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.dev.git20141105
- Version 1.4dev
- Enabled testing

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.1-alt1.1
- Rebuild with Python-3.3

* Fri May 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Version 1.1
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Version 0.4

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

