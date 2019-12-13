%define oname googleads

Name: python3-module-%oname
Version: 2.0.2
Release: alt2

Summary: Google Ads Python Client Library
License: ASL v2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/googleads
BuildArch: noarch

# https://github.com/googleads/googleads-python-lib.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
The googleads Python Client Libraries support the following products:

* AdWords API
* DoubleClick for Advertisers API
* DoubleClick for Publishers API

%prep
%setup

sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')


%build
%python3_build_debug

%install
%python3_install

%files
%doc ChangeLog *.md examples
%python3_sitelibdir/*


%changelog
* Fri Dec 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.2-alt2
- build for python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.0.2-alt1.git20140903.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.2-alt1.git20140903.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1.git20140903
- Initial build for Sisyphus

