%define _unpackaged_files_terminate_build 1
%define ns_name zope
%define mod_name deferredimport
%define pypi_name %ns_name.%mod_name

%def_with check

Name: python3-module-%pypi_name
Version: 6.1.1
Release: alt1.1
Summary: Allows you to perform imports names that will be resolved when used in the code
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.deferredimport/
Vcs: https://github.com/zopefoundation/zope.deferredimport.git
BuildArch: noarch
Source: %name-%version.tar
# switched to native namespace
Requires: python3-module-zope >= 3.3.0-alt10

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-zope-proxy
BuildRequires: python3-module-zope-testrunner
%endif

%description
Often, especially for package modules, you want to import names for
convenience, but not actually perform the imports until necessary. The
zope.deferredimport package provided facilities for defining names in
modules that will be imported from somewhere else when used. You can
also cause deprecation warnings to be issued when a variable is used.

%prep
%setup
# don't package examples, remove the package *before* run tests to check if it's
# needed or not
rm -r src/zope/deferredimport/samples/

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests.py
%exclude %python3_sitelibdir/%ns_name/%mod_name/__pycache__/tests.*

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 6.1.1-alt1.1
- Demodernized packaging.

* Tue Feb 17 2026 Stanislav Levin <slev@altlinux.org> 6.1.1-alt1
- 6.1 -> 6.1.1.

* Wed Feb 11 2026 Stanislav Levin <slev@altlinux.org> 6.1-alt1
- 5.1 -> 6.1.

* Thu Aug 14 2025 Stanislav Levin <slev@altlinux.org> 5.1-alt1
- 5.0 -> 5.1.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 5.0-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Thu Jun 29 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version 5.0.

* Fri May 19 2023 Anton Vyatkin <toni@altlinux.org> 4.4-alt1
- New version 4.4.

* Wed Dec 25 2019 Nikolai Kostrigin <nickel@altlinux.org> 4.3.1-alt1
- NMU: 4.3 -> 4.3.1
- Remove python2 module build
- Rearrange unittests execution

* Wed Feb 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.3-alt1
- Version updated to 4.3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.1.1-alt1.dev0.git20150402.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools
- Move samples to examples subpackage

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150402.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150402.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.dev0.git20150402
- Version 4.1.1.dev0
- Enabled check

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Version 4.0.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.3-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt1
- Initial build for Sisyphus

