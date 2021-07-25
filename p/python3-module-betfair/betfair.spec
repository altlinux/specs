%define oname betfair

Name: python3-module-%oname
Version: 0.1.1
Release: alt2
Summary: Betfair Next Generation asyncio API
License: Free
Group: Development/Python3
Url: https://pypi.python.org/pypi/betfair/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname

%description
Betfair Next Generation asyncio API.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc PKG-INFO
%python3_sitelibdir/*

%changelog
* Sun Jul 25 2021 Grigory Ustinov <grenka@altlinux.org> 0.1.1-alt2
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.1-alt1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1.1
- NMU: Use buildreq for BR.

* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus

