%define oname testscenarios

Name: python3-module-%oname
Version: 0.5.0
Release: alt5

Summary: Testscenarios, a pyunit extension for dependency injection

License: Apache-2.0 and BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/testscenarios/

BuildArch: noarch

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

# Not full commit, just tests/test_testscenarios.py hunks
# for applying next patches
Patch0: 12250124d11440e94fd30149d1ffed6b1b88f02d.patch
# Not full commit, just tests/test_testcase.py hunks
# for applying next patches
Patch1: 2907ab614964e5838047566c7477b16172717b92.patch
# Fix compatibility with newer testtools
Patch2: 75b76e7d07bc6d415384e668aefb6b887a3aa13d.patch
# s/assertEquals/assertEqual/
Patch3: fd9a58526f1f77c192c129f6e06cb61bf06dfea4.patch
# https://github.com/testing-cabal/testscenarios/pull/1
Patch4: 9e2c6ba88925700a42e46f554419fc1a31fc5f29.patch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-testtools
BuildRequires: python3-module-pytest python3-module-pbr

%py3_provides %oname
%py3_requires testtools

%description
testscenarios provides clean dependency injection for python unittest
style tests. This can be used for interface testing (testing many
implementations via a single test suite) or for classic dependency
injection (provide tests with dependencies externally to the test code
itself, allowing easy testing in different situations).

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- python -m testtools.run -v testscenarios.test_suite

%files
%doc Apache-2.0 BSD COPYING GOALS HACKING NEWS README doc
%doc AUTHORS ChangeLog
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Thu Jan 29 2026 Grigory Ustinov <grenka@altlinux.org> 0.5.0-alt5
- Fixed compatibility with newer testtools.

* Thu Jun 16 2022 Grigory Ustinov <grenka@altlinux.org> 0.5.0-alt4
- Fixed FTBFS.

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt3
- build python3 separately

* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.5.0-alt2.1
- rebuild with all requires

* Mon May 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.5.0-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Aug 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Version 0.5.0

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Initial build for Sisyphus

