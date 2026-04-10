%define _unpackaged_files_terminate_build 1
%define pypi_name zope.tales
%define ns_name zope
%define mod_name tales

%def_with check

Name: python3-module-%pypi_name
Version: 7.0
Release: alt1
Summary: Zope Template Application Language Expression Syntax (TALES)
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.tales
VCS: https://github.com/zopefoundation/zope.tales.git
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
Template Attribute Language - Expression Syntax.

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
%exclude %python3_sitelibdir/%ns_name/%mod_name/tests/

%changelog
* Thu Apr 09 2026 Stanislav Levin <slev@altlinux.org> 7.0-alt1
- 6.1 -> 7.0.

* Tue Sep 09 2025 Stanislav Levin <slev@altlinux.org> 6.1-alt2
- Mapped PyPI name to the RPM one.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 6.1-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Sun Feb 16 2025 Anton Vyatkin <toni@altlinux.org> 6.1-alt1
- New version 6.1.

* Wed Jul 12 2023 Anton Vyatkin <toni@altlinux.org> 6.0-alt1
- New version 6.0.

* Mon Mar 20 2023 Anton Vyatkin <toni@altlinux.org> 5.2-alt1
- New version 5.2.

* Wed Apr 01 2020 Andrey Bychkov <mrdrew@altlinux.org> 5.0.2-alt1
- Version updated to 5.0.2.

* Mon Dec 02 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.2.0-alt4
- python2 disabled

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt2
- NMU: remove %%ubt from release

* Tue Feb 20 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1%%ubt
- 4.1.1 -> 4.2.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.1.1-alt1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1
- Version 4.1.1
- Enabled check

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.5.1-alt4.1
- Rebuild with Python-3.3

* Tue Apr 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.1-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1
- Initial build for Sisyphus

