%define _unpackaged_files_terminate_build 1
%define pypi_name FormEncode

%def_with check

Name: python3-module-%pypi_name
Version: 2.1.0
Release: alt1
Epoch: 1

Summary: HTML form validation, generation, and convertion package for Python
License: MIT
Group: Development/Python3

Url: http://formencode.org
Vcs: https://github.com/formencode/formencode
BuildArch: noarch
Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
FormEncode validates and converts nested structures. It allows for
a declarative form of defining the validation, and decoupled processes
for filling and generating forms.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-test.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra tests

%files
%doc README.rst
%python3_sitelibdir/formencode/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Tue Nov 07 2023 Stanislav Levin <slev@altlinux.org> 1:2.1.0-alt1
- 2.0.1 -> 2.1.0.

* Tue Sep 20 2022 Stanislav Levin <slev@altlinux.org> 1:2.0.1-alt2
- Fixed FTBFS (removed obsoleted setuptools-scm-git-archive).
- Packaged missing i18n data.

* Thu Feb 03 2022 Stanislav Levin <slev@altlinux.org> 1:2.0.1-alt1
- 2.0.0 -> 2.0.1.

* Fri Sep 17 2021 Stanislav Levin <slev@altlinux.org> 1:2.0.0-alt1
- 1.3.1 -> 2.0.0.

* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 1:1.3.1-alt2
- Drop python2 support.

* Fri Dec 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 1:1.3.1-alt1
- Version updated to 1.3.1

* Wed Feb 27 2019 Michael Shigorin <mike@altlinux.org> 1:1.3.0-alt1.git20150207.1.3
- introduce doc knob (on by default)

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1:1.3.0-alt1.git20150207.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.3.0-alt1.git20150207.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 1:1.3.0-alt1.git20150207.1
- NMU: Use buildreq for BR.

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.0-alt1.git20150207
- 1.3.0 released

* Thu Mar 21 2013 Aleksey Avdeev <solo@altlinux.ru> 1:1.3.0-alt1.git20130312
- New snapshot
- Added module for Python 3

* Tue Feb 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.0-alt1.git20130201
- Version 1.3.0

* Fri Sep 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.2.4-alt1.git20120914
- New snapshot

* Thu Dec 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.4-alt1.hg20110930
- Version 1.2.4

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.3-alt2.hg20100922.1
- Rebuild with Python-2.7

* Sat Nov 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt2.hg20100922
- New snapshot (svn -> hg)

* Thu Jul 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.svn20100511
- Version 1.2.3

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt2
- Rebuilt with python 2.6

* Sat Apr 04 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.2.2-alt1
- 1.2.2

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.4-alt2.1.0.1
- Rebuilt with python-2.5.

* Sun Mar 25 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.4-alt2.1.0
- Rebuilt with rpm-build-python-0.30-alt3.

* Thu Mar 02 2006 Maxim Bodyansky <maximbo@altlinux.ru> 0.4-alt2.1
- add_python_req_skip dispatch sqlobject pkg_resources

* Thu Nov 24 2005 Maxim Bodyansky <maximbo@altlinux.ru> 0.4-alt2
- new upstream's version

* Sun Nov 06 2005 Maxim Bodyansky <maximbo@altlinux.ru> 0.2.2-alt1
- Initial build for Sisyphus
