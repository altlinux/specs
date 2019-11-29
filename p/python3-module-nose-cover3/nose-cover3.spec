%define oname nose-cover3

Name: python3-module-%oname
Version: 0.1.0
Release: alt2

Summary: Coverage 3.x support for Nose
License: LPGLv2.1
Group: Development/Python3
Url: https://pypi.python.org/pypi/nose-cover3/
BuildArch: noarch

# https://github.com/ask/nosecover3.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
Coverage 3.x support for Nose.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.0-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.0-alt1.git20110913.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.git20110913.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20110913
- Initial build for Sisyphus

