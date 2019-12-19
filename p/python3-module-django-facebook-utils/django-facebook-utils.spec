%define oname django-facebook-utils

Name: python3-module-%oname
Version: 1.0.4
Release: alt2

Summary: Some Facebook utilities to use in Django projects
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-facebook-utils/
BuildArch: noarch

# https://github.com/caioariede/django-facebook-utils.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
The intent of this project is to provide some very basic utilities
related to Facebook.

At the moment there are only two features:

* An utility that forces the update of an URL in the Facebook's share
  cache.
* A Context Processor that allows you to hide Facebook Open Graph
  Protocol <meta> tags from other User Agents.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%files
%doc README.markdown example
%python3_sitelibdir/*


%changelog
* Thu Dec 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.4-alt2
- build for python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.4-alt1.git20130201.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.4-alt1.git20130201.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.4-alt1.git20130201.1
- NMU: Use buildreq for BR.

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1.git20130201
- Initial build for Sisyphus

