%define oname tornado-facebook-sdk

Name: python3-module-%oname
Version: 0.1.0
Release: alt2

Summary: A tornado based facebook graph api wrapper
License: OSI
Group: Development/Python3
Url: https://pypi.python.org/pypi/tornado-facebook-sdk/
BuildArch: noarch

# https://github.com/pauloalem/tornado-facebook-sdk.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
The tornado-facebook-sdk is a library that aims to ease the task of
writing non-blocking, server side, facebook social graph accessing code.
It's built using tornado. This makes tornado-facebook-sdk a perfect fit
if you're developing an application using tornado.

%prep
%setup

sed -i 's|graphapi|facebook.graphapi|' facebook/__init__.py

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.TXT *.rst docs/*.rst
%python3_sitelibdir/*


%changelog
* Mon Dec 09 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.0-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.0-alt1.git20121001.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.git20121001.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20121001
- Initial build for Sisyphus

