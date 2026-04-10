%define _unpackaged_files_terminate_build 1
%define pypi_name zope.structuredtext
%define ns_name zope
%define mod_name structuredtext

%def_with check

Name: python3-module-%pypi_name
Version: 6.0
Release: alt1
Summary: StructuredText parser
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.structuredtext
Vcs: https://github.com/zopefoundation/zope.structuredtext
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
# setuptools(pkg_resources) is used by namespace root which is not used in ALT
%add_pyproject_deps_runtime_filter setuptools
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
This package provides a parser and renderers for the classic Zope
"structured text" markup dialect (STX). STX is a plain text markup in
which document structure is signalled primarily by identation.

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
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests.*
%exclude %python3_sitelibdir/%ns_name/%mod_name/__pycache__/tests.*
%exclude %python3_sitelibdir/%ns_name/%mod_name/regressions/

%changelog
* Fri Mar 27 2026 Stanislav Levin <slev@altlinux.org> 6.0-alt1
- 5.1 -> 6.0.

* Wed Sep 10 2025 Stanislav Levin <slev@altlinux.org> 5.1-alt1
- 5.0 -> 5.1.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 5.0-alt2.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Sun Jan 21 2024 Anton Vyatkin <toni@altlinux.org> 5.0-alt2
- Fixed FTBFS.

* Wed May 10 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version 5.0.

* Mon Mar 20 2023 Anton Vyatkin <toni@altlinux.org> 4.4-alt1
- New version 4.4.

* Wed Jun 29 2022 Grigory Ustinov <grenka@altlinux.org> 4.1.1-alt3
- Fixed BuildRequires.

* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.1.1-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.1.1-alt1.dev0.git20150203.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150203.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150203.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.dev0.git20150203
- Version 4.1.1.dev0
- Enabled check

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Version 4.0.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1
- Initial build for Sisyphus

