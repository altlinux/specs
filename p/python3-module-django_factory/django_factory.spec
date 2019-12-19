%define oname django_factory

Name: python3-module-%oname
Version: 0.11
Release: alt3

Summary: Generic factory for creating instances of Django models in tests
License: ASL v2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/django_factory/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
django_factory is a generic implementation of `Creation Methods` for
Django models.

Using django_factory in your tests means that each test can create
instances of the models, but only has to specify the model attributes
that are germane to that particular test.

Using creation methods usually leads to tests that are easier to read,
and makes it easier to avoid convoluted test setup methods that are
shared, as the pre-conditions for each test are easier to establish.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%files
%doc HACKING README
%python3_sitelibdir/*


%changelog
* Thu Dec 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.11-alt3
- build for python2 disabled

* Mon May 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.11-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1
- Initial build for Sisyphus

