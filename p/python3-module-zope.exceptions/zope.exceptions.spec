%define _unpackaged_files_terminate_build 1
%define pypi_name zope.exceptions
%define ns_name zope
%define mod_name exceptions

%def_with check

Name: python3-module-%pypi_name
Version: 5.1
Release: alt1

Summary: Zope Exceptions
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.exceptions/
Vcs: https://github.com/zopefoundation/zope.exceptions.git
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
# setuptools(pkg_resources) is used by namespace root that is packaged
# separately at python3-module-zope
%add_pyproject_deps_runtime_filter setuptools
%pyproject_runtimedeps_metadata
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
This package contains exception interfaces and implementations which are
so general purpose that they don't belong in Zope application-specific
packages.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
        %buildroot%python3_sitelibdir/
%endif

# don't ship tests
rm -r %buildroot%python3_sitelibdir/%ns_name/%mod_name/tests

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%doc *.txt README.*
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/
%exclude %python3_sitelibdir/*.pth

%changelog
* Fri Jun 07 2024 Stanislav Levin <slev@altlinux.org> 5.1-alt1
- 5.0.1 -> 5.1.

* Thu Aug 03 2023 Stanislav Levin <slev@altlinux.org> 5.0.1-alt2
- Mapped PyPI name to distro's one.

* Wed Jul 12 2023 Anton Vyatkin <toni@altlinux.org> 5.0.1-alt1
- New version 5.0.1.

* Thu Jun 29 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version 5.0.

* Sat May 20 2023 Anton Vyatkin <toni@altlinux.org> 4.6-alt1
- New version 4.6.

* Wed Mar 30 2022 Stanislav Levin <slev@altlinux.org> 4.5-alt1
- 4.4 -> 4.5.

* Thu Apr 15 2021 Grigory Ustinov <grenka@altlinux.org> 4.4-alt1
- Automatically updated to 4.4.

* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.2.0-alt5
- Build for python2 disabled.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt4
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt3
- NMU: remove %%ubt from release

* Wed Feb 14 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt2.S1
- Fix a wrong logic of packaging for non x86_64 arch

* Mon Feb 12 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1.S1
- v4.0.8 -> v4.2.0

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.8-alt1.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.8-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.8-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.8-alt1
- Version 4.0.8

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.7-alt1
- Version 4.0.7

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.6-alt1
- Version 4.0.6

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.7.1-alt1.1
- Rebuild with Python-3.3

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt1
- Version 3.7.1
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Initial build for Sisyphus

