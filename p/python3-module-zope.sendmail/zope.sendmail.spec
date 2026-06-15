%define _unpackaged_files_terminate_build 1
%define pypi_name zope.sendmail
%define ns_name zope
%define mod_name sendmail

%def_with check

Name: python3-module-%pypi_name
Version: 7.1.1
Release: alt1
Summary: Zope sendmail
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.sendmail/
Vcs: https://github.com/zopefoundation/zope.sendmail.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
# switched to native namespace
Requires: python3-module-zope >= 3.3.0-alt10
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
zope.sendmail is a package for email sending from Zope 3 applications.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%_bindir/*
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests/

%changelog
* Mon Jun 15 2026 Stanislav Levin <slev@altlinux.org> 7.1.1-alt1
- 7.1 -> 7.1.1

* Mon Apr 27 2026 Stanislav Levin <slev@altlinux.org> 7.1-alt1
- 7.0 -> 7.1.

* Tue Dec 02 2025 Stanislav Levin <slev@altlinux.org> 7.0-alt1
- 6.2 -> 7.0.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 6.2-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Mon Mar 25 2024 Anton Vyatkin <toni@altlinux.org> 6.2-alt1
- New version 6.2.

* Fri Feb 09 2024 Anton Vyatkin <toni@altlinux.org> 6.1-alt1
- New version 6.1.

* Tue Aug 22 2023 Anton Vyatkin <toni@altlinux.org> 6.0-alt1
- New version 6.0.

* Sat May 20 2023 Anton Vyatkin <toni@altlinux.org> 5.3-alt1
- New version 5.3.

* Fri Sep 24 2021 Nikolai Kostrigin <nickel@altlinux.org> 5.2-alt1
- 5.0 -> 5.2

* Tue Dec 24 2019 Nikolai Kostrigin <nickel@altlinux.org> 5.0-alt1
- NMU: 4.0.2 -> 5.0
- Remove python2 module build
- Rearrange unittests execution

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.0.2-alt1.dev0.git20150613.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.2-alt1.dev0.git20150613.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.2-alt1.dev0.git20150613.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1.dev0.git20150613
- Version 4.0.2.dev0
- Enabled check

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt3
- Version 4.0.0

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.a2
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a2
- Version 4.0.0a2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.4-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt1
- Initial build for Sisyphus

