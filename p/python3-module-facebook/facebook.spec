%define oname facebook

Name: python3-module-%oname
Version: 2.3.14
Release: alt2

Summary: Facebook API client for Python
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/Facebook/
BuildArch: noarch

# https://github.com/jgorset/facebook.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

Conflicts: python3-module-facebook-sdk


%description
Facebook makes it even easier to interact with Facebook's Graph API.

%prep
%setup

## py2 -> py3
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')
##

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.3.14-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.3.14-alt1.git20140409.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.14-alt1.git20140409.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.3.14-alt1.git20140409.1
- NMU: Use buildreq for BR.

* Tue Sep 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.14-alt1.git20140409
- Initial build for Sisyphus

