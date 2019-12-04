%define oname fbads

Name: python3-module-%oname
Version: 0.3.6
Release: alt2

Summary: Python client for the Facebook Ads API
License: Free
Group: Development/Python3
Url: https://pypi.python.org/pypi/fbads/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
Python client for the Facebook Ads API. Works with the new ads schema
(ad sets). Under development!

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests


%changelog
* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.3.6-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.3.6-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.6-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt1
- Initial build for Sisyphus

