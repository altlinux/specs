%define modname twitter

Name: python3-module-%modname
Version: 3.5
Release: alt1

Summary: Python Interface for Twitter API
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/bear/python-twitter
BuildArch: noarch

Source: twitter-%version.tar
Patch0: fix-build-for-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest-runner python3-module-sphinx
BuildRequires: python3-module-sphinx_rtd_theme

%py3_requires rfc822py3 requests requests_oauthlib
%add_python3_req_skip rfc822
%py3_provides %modname


%description
This library provides a pure python interface for the Twitter API.

%prep
%setup -n twitter-%version
%patch0 -p1

sed -i 's|#!/usr/bin/env python.*|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

export PYTHONPATH=%buildroot%python3_sitelibdir
sphinx-build-3 doc/ _build/ doc/*.rst
mkdir man
cp -fR doc/_build/html/* man/

%install
%python3_install

%files
%doc AUTHORS.* CHANGES COPYING LICENSE README.*
%doc examples/ man/
%python3_sitelibdir/*


%changelog
* Fri Dec 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.5-alt1
- Version updated to 3.5
- build for python2 disabled

* Fri Mar 23 2018 Andrey Bychkov <mrdrew@altlinux.org> 3.4.1-alt1
- Version 3.4.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2
- Added %%py3_provides for Python 3 module

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1
- Version 2.0
- Added module for Python 3

* Tue Feb 07 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.1-alt2
- Rebuild with Python-2.7

* Sun Mar 13 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Wed Apr 14 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6-alt1
- Initial
