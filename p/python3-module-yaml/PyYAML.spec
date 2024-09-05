%define _unpackaged_files_terminate_build 1
%define pypi_name PyYAML
%define mod_name yaml

%def_with check

Name: python3-module-%mod_name
Version: 6.0.2
Release: alt1

Summary: PyYAML, a YAML parser and emitter for Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/PyYAML/
Vcs: https://github.com/yaml/pyyaml

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR

BuildRequires: libyaml-devel

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%endif

%description
YAML is a data serialization format designed for human readability
and interaction with scripting languages.

PyYAML is a YAML parser and emitter for the Python programming
language.  PyYAML features a complete YAML 1.1 parser, Unicode
support, and relatively sensible error messages.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%add_optflags -fno-strict-aliasing
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- python3 tests/legacy_tests/test_all.py

%files
%doc CHANGES README*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/_yaml/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 6.0.2-alt1
- 6.0.2 released

* Thu Dec 28 2023 Grigory Ustinov <grenka@altlinux.org> 6.0.1-alt1.1
- NMU: Fix building with cython>3.

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.0.1-alt1
- 6.0.1

* Mon Apr 24 2023 Stanislav Levin <slev@altlinux.org> 6.0-alt2
- Modernized packaging.

* Tue Feb 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.0-alt1
- 6.0 released

* Mon Aug 02 2021 Grigory Ustinov <grenka@altlinux.org> 5.4.1-alt2
- Drop python2 support.

* Fri Feb 19 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.4.1-alt1
- 5.4.1 released

* Mon Jul 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.3.1-alt1
- 5.3.1 released

* Wed Feb 12 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.3-alt1
- 5.3 released

* Wed Dec 11 2019 Grigory Ustinov <grenka@altlinux.org> 5.2-alt1
- Build new version 5.2.

* Mon Aug 05 2019 Grigory Ustinov <grenka@altlinux.org> 5.1.2-alt1
- Build new version.

* Wed Jul 10 2019 Grigory Ustinov <grenka@altlinux.org> 5.1.1-alt1
- Build new version.

* Tue Mar 19 2019 Grigory Ustinov <grenka@altlinux.org> 5.1-alt1
- Build new version.

* Tue Dec 25 2018 Grigory Ustinov <grenka@altlinux.org> 3.13-alt1
- Build new version.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.12-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Sun Oct 22 2017 Vitaly Lipatov <lav@altlinux.ru> 3.12-alt1
- new version 3.12 (with rpmrb script) (ALT bug 34046)

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.11-alt1.hg20141128.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.11-alt1.hg20141128
- New snapshot

* Wed Aug 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.11-alt1.hg20140326
- Version 3.11

* Wed Dec 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10-alt2.hg20121224
- Snapshot from Mercurial

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.10-alt2.1
- Rebuild with Python-3.3

* Sat Apr 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10-alt2
- Dont' rename _yaml.*.so -> _yaml.so

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10-alt1
- Version 3.10
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.05-alt2.1.1
- Rebuild with Python-2.7

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.05-alt2.1
- Rebuilt with python 2.6

* Sun Jul 20 2008 Alexander Myltsev <avm@altlinux.ru> 3.05-alt2
- Fix #16285 (package lost directory).
- Pull a minor bugfix from SVN (a single dot is not a valid float).

* Fri Nov 16 2007 Alex V. Myltsev <avm@altlinux.ru> 3.05-alt1
- Initial build for Sisyphus.

