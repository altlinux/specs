%define oname strainer

Name: python3-module-%oname
Version: 0.1.4
Release: alt3

Summary: Tools to allow developers to cleanup web objects (HTML, JSON, XHTML)
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/strainer/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-simplejson python3-module-nose
BuildRequires: python-tools-2to3
BuildRequires: python3-module-lxml

%py3_provides %oname
%py3_requires json


%description
Provides middleware for detecting and correcting errors in web pages
that are served via the standard WSGI protocol used by most Python web
frameworks. By default, validation errors are logged to the
"strainer.middleware" channel using the standard Python logging module.

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

%check
%__python3 setup.py test

%files
%python3_sitelibdir/*


%changelog
* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.4-alt3
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.4-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.4-alt2
- Updated build dependencies.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt1.1
- NMU: Use buildreq for BR.

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1
- Initial build for Sisyphus

