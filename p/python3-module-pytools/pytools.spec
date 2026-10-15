%define oname pytools

Name: python3-module-%oname
Version: 2026.1.1
Release: alt1
Summary: A collection of tools for Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytools

# Source-git: https://github.com/inducer/pytools.git
Source: %oname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
%if_disabled check
%else
BuildRequires: python3-module-pytest
BuildRequires: python3-module-platformdirs
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-siphash24
BuildRequires: python3-module-numpy
BuildRequires: python3-modules-sqlite3
%endif

# platformdirs is a hard upstream dependency imported lazily in persistent_dict
Requires: python3(platformdirs)

%add_python3_req_skip mpi4py.rc

%description
Pytools is a big bag of things that are "missing" from the Python
standard library. This is mainly a dependency of my other software
packages, and is probably of little interest to you unless you use
those.

%package tests
Summary: Test for Pytools
Group: Development/Python3
Requires: %name = %version-%release

%description tests
Pytools is a big bag of things that are "missing" from the Python
standard library. This is mainly a dependency of my other software
packages, and is probably of little interest to you unless you use
those.

This package contains test for Pytools.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# test_xdg_cache_home depends on the XDG cache layout of the build environment;
# test_scalar_hashing hashes np.clongdouble bytes, unstable with x87 padding on i586
%pyproject_run_pytest -v pytools/test -k "not test_xdg_cache_home and not test_scalar_hashing"

%files
%doc README.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{pyproject_distinfo %oname}/
%exclude %python3_sitelibdir/%oname/test/

%files tests
%python3_sitelibdir/%oname/test/

%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 2026.1.1-alt1
- NMU: new version 2026.1.1
- switch to pyproject build
- move tests to pytools/test/ (upstream layout)

* Tue May 25 2021 Grigory Ustinov <grenka@altlinux.org> 2017.4-alt2
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2017.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2017.4-alt1
- Updated to upstream version 2017.4.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2014.3.5-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.3.5-alt1
- Version 2014.3.5

* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.3.4-alt1
- Version 2014.3.4
- Enabled testing

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.3-alt1
- Version 2014.3

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.5.7-alt1
- Version 2013.5.7

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.5.6-alt1
- Version 2013.5.6

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2012.1-alt1
- Version 2012.1

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 2011.5-alt2.1
- Rebuild with Python-3.3

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.5-alt2
- Added module for Python 3

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.5-alt1
- Initial build for Sisyphus

