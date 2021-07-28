%define oname pylast

Name: python3-module-%oname
Version: 1.0.0
Release: alt1.git20140825.2
Summary: A Python interface to Last.fm (and other API compatible social networks)
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/pylast/

# https://github.com/pylast/pylast.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
A Python interface to Last.fm and other api-compatible websites such as
Libre.fm.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc *.yaml *.md
%python3_sitelibdir/*

%changelog
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

