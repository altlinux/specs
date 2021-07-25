%define oname munkres

Name: python3-module-%oname
Version: 1.0.6
Release: alt4.git20131103.2
Summary: Munkres algorithm for the Assignment Problem
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/munkres/

# https://github.com/bmc/munkres.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname

%description
The Munkres module provides an implementation of the Munkres algorithm
(also called the Hungarian algorithm or the Kuhn-Munkres algorithm),
useful for solving the Assignment Problem.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
%__python3 %oname.py

%files
%doc CHANGELOG *.md
%python3_sitelibdir/*

%changelog
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

