%define oname linkedin

Name: python3-module-%oname
Version: 4.2
Release: alt2

Summary: Python Interface to the LinkedIn API
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/python-linkedin/
BuildArch: noarch

# https://github.com/ozgur/python-linkedin.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-requests-oauthlib python-tools-2to3

%py3_provides %oname
%py3_requires requests requests_oauthlib json


%description
This library provides a pure Python interface to the LinkedIn Profile,
Group, Company, Jobs, Search, Share, Network and Invitation REST APIs.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.md *.rst examples/
%python3_sitelibdir/*


%changelog
* Fri Dec 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.2-alt2
- build for python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2-alt1.git20150625.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.2-alt1.git20150625.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.2-alt1.git20150625.1
- NMU: Use buildreq for BR.

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt1.git20150625
- New snapshot

* Thu Apr 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt1.git20150214
- Initial build for Sisyphus

