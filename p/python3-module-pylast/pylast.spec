%define oname pylast

%def_with check

Name: python3-module-%oname
Version: 5.3.0
Release: alt1

Summary: A Python interface to Last.fm (and other API compatible social networks)

License: Apache-2.0
Group: Development/Python3
URL: https://pypi.org/project/pylast
VCS: https://github.com/pylast/pylast

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs
BuildRequires: python3-module-setuptools-scm

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-httpx
BuildRequires: python3-module-flaky
%endif

%description
A Python interface to Last.fm and other api-compatible websites such as
Libre.fm.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.yaml *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Sun Jun 02 2024 Grigory Ustinov <grenka@altlinux.org> 5.3.0-alt1
- Automatically updated to 5.3.0.
- Built with check.

* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt1.git20140825.2
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.0-alt1.git20140825.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.git20140825.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1.git20140825.1
- NMU: Use buildreq for BR.

* Fri Oct 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20140825
- Initial build for Sisyphus

