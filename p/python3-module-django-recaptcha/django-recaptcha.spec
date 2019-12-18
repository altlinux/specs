%define _unpackaged_files_terminate_build 1
%define oname django-recaptcha

Name: python3-module-%oname
Version: 2.0.5
Release: alt1

Summary: Django recaptcha form field/widget app
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-recaptcha/
BuildArch: noarch

# https://github.com/praekelt/django-recaptcha.git
Source0: %name-%version.tar.gz

BuildRequires(pre): rpm-build-python3


%description
django-recaptcha uses a modified version of the Python reCAPTCHA client
which is included in the package as client.py.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
django-recaptcha uses a modified version of the Python reCAPTCHA client
which is included in the package as client.py.

This package contains tests for %oname.

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
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*


%changelog
* Wed Dec 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.5-alt1
- Version updated to 2.0.5
- build for python2 disabled

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt1.git20140916.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20140916
- Initial build for Sisyphus

