%define _unpackaged_files_terminate_build 1
%define pypi_name zope.tal
%define ns_name zope
%define mod_name tal

%def_with check

Name: python3-module-%pypi_name
Version: 6.0
Release: alt1
Summary: Zope3 Template Attribute Languate
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.tal/
VCS: https://github.com/zopefoundation/zope.tal.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
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
The Zope3 Template Attribute Languate (TAL) specifies the custom
namespace and attributes which are used by the Zope Page Templates
renderer to inject dynamic markup into a page. It also includes the
Macro Expansion for TAL (METAL) macro language used in page assembly.

The dynamic values themselves are specified using a companion language,
TALES (see the 'zope.tales' package for more).

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
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests/
%exclude %python3_sitelibdir/%ns_name/%mod_name/runtest.*
%exclude %python3_sitelibdir/%ns_name/%mod_name/__pycache__/runtest.*
%exclude %python3_sitelibdir/%ns_name/%mod_name/benchmark/

%changelog
* Thu Apr 09 2026 Stanislav Levin <slev@altlinux.org> 6.0-alt1
- 5.1.1 -> 6.0.

* Mon Sep 08 2025 Stanislav Levin <slev@altlinux.org> 5.1.1-alt1
- 5.1 -> 5.1.1.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 5.1-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Sun Feb 16 2025 Anton Vyatkin <toni@altlinux.org> 5.1-alt1
- New version 5.1.

* Sat Jan 20 2024 Anton Vyatkin <toni@altlinux.org> 5.0.1-alt2
- Fix FTBFS.

* Wed Feb 22 2023 Anton Vyatkin <toni@altlinux.org> 5.0.1-alt1
- new version 5.0.1

* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.2.0-alt3
- python2 disabled

* Thu Feb 08 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.2.0-alt2
- fix lib/lib64 stupidity

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Aug 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.0-alt1
- Updated to upstream version 4.2.0.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.2-alt1.dev0.git10150605.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt1.dev0.git10150605
- Version 4.1.2.dev0

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.dev0.git10141229
- Version 4.1.1.dev0

* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.dev.git10140113
- Version 4.0.1dev

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- Version 4.0.0

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a1
- Version 4.0.0a1

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.6.1-alt1.1
- Rebuild with Python-3.3

* Tue Apr 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Version 3.6.1
- Added module for Python 3

* Thu Dec 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1
- Version 3.6.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.2-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt3
- Added necesssary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt1
- Initial build for Sisyphus

