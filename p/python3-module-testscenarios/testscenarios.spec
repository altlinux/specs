%define oname testscenarios

Name: python3-module-%oname
Version: 0.6.2
Release: alt1

Summary: Testscenarios, a pyunit extension for dependency injection

License: Apache-2.0 and BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/testscenarios/

BuildArch: noarch

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-testtools >= 2.8.7
BuildRequires: python3-module-hatchling python3-module-hatch-vcs

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

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
# Upstream 0.6.2 sdist omits the tests directory; exercise documented API examples.
%pyproject_run -- python -m doctest -o ELLIPSIS -v README.rst

%files
%doc Apache-2.0 BSD COPYING GOALS HACKING NEWS README.rst doc
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Thu Oct 08 2026 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt1
- New version 0.6.2.
- Build with hatchling and hatch-vcs; drop obsolete compatibility patches.
- Run upstream README doctests because the release tarball omits the test suite.

* Wed Mar 04 2026 Grigory Ustinov <grenka@altlinux.org> 0.5.0-alt6
- Fixed compatibility with newer testtools again.

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
