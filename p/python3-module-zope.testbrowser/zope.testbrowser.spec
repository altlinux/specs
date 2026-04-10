%define _unpackaged_files_terminate_build 1
%define pypi_name zope.testbrowser

%def_with check

Name: python3-module-%pypi_name
Version: 8.0
Release: alt1

Summary: Programmable browser for functional black-box tests
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/zope.testbrowser
VCS: https://github.com/zopefoundation/zope.testbrowser.git
BuildArch: noarch
Source: %name-%version.tar
Source1111: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
AutoReq: yes, nopython3
Requires: python3-module-zope >= 3.3.0-alt10
%add_pyproject_deps_runtime_filter setuptools
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_check
%endif

%description
zope.testbrowser provides an easy-to-use programmable web browser with
special focus on testing. It is used in Zope, but it's not Zope specific
at all. For instance, it can be used to test or otherwise interact with
any web site.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

# don't ship tests
rm -r %buildroot%python3_sitelibdir/zope/testbrowser/tests/

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%python3_sitelibdir/zope/testbrowser/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Apr 09 2026 Stanislav Levin <slev@altlinux.org> 8.0-alt1
- 7.0.1 -> 8.0.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 7.0.1-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Thu Mar 06 2025 Anton Vyatkin <toni@altlinux.org> 7.0.1-alt1
- New version 7.0.1.

* Sat Jun 01 2024 Anton Vyatkin <toni@altlinux.org> 7.0-alt1
- New version 7.0.

* Fri May 19 2023 Anton Vyatkin <toni@altlinux.org> 6.0-alt1
- New version 6.0.

* Mon Feb 06 2023 Stanislav Levin <slev@altlinux.org> 5.6.1-alt1
- 5.0.0 -> 5.6.1.

* Tue Feb 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 5.0.0-alt3
- Build for python2 disabled.

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt2.dev0.git20150220.2
- Rebuild with python3.7.

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 5.0.0-alt2.dev0.git20150220.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 5.0.0-alt2.dev0.git20150220.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 5.0.0-alt2.dev0.git20150220.1
- NMU: Use buildreq for BR.

* Sat Aug 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.0-alt2.dev0.git20150220
- New snapshot

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.0-alt2.dev0.git20140125
- Restored zope.testbrowser.connection

* Wed Oct 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.0-alt1.dev0.git20140125
- Version 5.0.0.dev0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt2
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1
- Version 4.0.4

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.1-alt1.1
- Rebuild with Python-2.7

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Initial build for Sisyphus

