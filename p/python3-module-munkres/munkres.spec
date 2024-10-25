%define oname munkres

%def_with check

Name: python3-module-%oname
Version: 1.1.4
Release: alt1
Summary: Munkres algorithm for the Assignment Problem
License: BSD
Group: Development/Python3
URL: https://pypi.org/project/munkres
VCS: https://github.com/bmc/munkres

Source: %name-%version.tar
# Fixes test error on i586
# https://github.com/bmc/munkres/pull/41
Patch: 380a0d593a0569a761c4a035edaa4414c3b4b31d.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

%py3_provides %oname

%description
The Munkres module provides an implementation of the Munkres algorithm
(also called the Hungarian algorithm or the Kuhn-Munkres algorithm),
useful for solving the Assignment Problem.

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%oname.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Fri Oct 25 2024 Grigory Ustinov <grenka@altlinux.org> 1.1.4-alt1
- Build new version.

* Tue Jan 30 2024 Grigory Ustinov <grenka@altlinux.org> 1.0.6-alt4.git20131103.3
- NMU: Added zombie-imp to BuildRequires.

* Sun Jul 25 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.6-alt4.git20131103.2
- Drop python2 support.

* Thu Apr 30 2020 Stanislav Levin <slev@altlinux.org> 1.0.6-alt3.git20131103.2
- Fixed FTBFS.

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.6-alt2.git20131103.2
- Rebuild with python3.7.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.6-alt2.git20131103.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Mar 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.6-alt2.git20131103
- NMU: added python-devel to BRs.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.6-alt1.git20131103.1
- NMU: Use buildreq for BR.

* Sat Nov 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1.git20131103
- Initial build for Sisyphus

