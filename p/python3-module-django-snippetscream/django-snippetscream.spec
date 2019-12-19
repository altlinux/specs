%define oname django-snippetscream

Name: python3-module-%oname
Version: 0.0.7
Release: alt4

Summary: Django app packaging the best snippets found on http://djangosnippets.org
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-snippetscream/
BuildArch: noarch

# https://github.com/shaunsephton/django-snippetscream.git
Source: %name-%version.tar
Patch0: port-on-new-django.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
Django app packaging the best snippets found on
http://djangosnippets.org

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Django app packaging the best snippets found on
http://djangosnippets.org

This package contains tests for %oname.

%prep
%setup
%patch0 -p1

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests


%changelog
* Thu Dec 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.7-alt4
- build for python2 disabled

* Sun May 20 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.0.7-alt3
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.7-alt2.git20110919.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt2.git20110919
- Additional fix for Python 3

* Wed Oct 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1.git20110919
- Initial build for Sisyphus

