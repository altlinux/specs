%define _unpackaged_files_terminate_build 1
%define oname django-sortedm2m

Name: python3-module-%oname
Version: 3.0.0
Release: alt1.1

Summary: Drop-in replacement for django's many to many field with sorted relations
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-sortedm2m/
BuildArch: noarch

# https://github.com/gregmuellegger/django-sortedm2m.git
Source0: %name-%version.tar.gz

BuildRequires(pre): rpm-build-python3

%add_python3_self_prov_path %buildroot%python3_sitelibdir/sortedm2m/test_project


%description
sortedm2m is a drop-in replacement for django's own ManyToManyField. The
provided SortedManyToManyField behaves like the original one but
remembers the order of added relations.

%package tests
Summary: Tests for %name
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description tests
sortedm2m is a drop-in replacement for django's own ManyToManyField. The
provided SortedManyToManyField behaves like the original one but
remembers the order of added relations.

This package contains tests for %name.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

mv sortedm2m_tests/ test_project/ %buildroot%python3_sitelibdir/sortedm2m/

%files
%doc *.rst example/
%python3_sitelibdir/*
%exclude %python3_sitelibdir/sortedm2m/sortedm2m_tests
%exclude %python3_sitelibdir/sortedm2m/test_project

%files tests
%python3_sitelibdir/sortedm2m/sortedm2m_tests
%python3_sitelibdir/sortedm2m/test_project


%changelog
* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 3.0.0-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Wed Dec 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.0.0-alt1
- Version updated to 3.0.0
- build for python2 disabled

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.1-alt1.git20140923.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.git20140923
- Initial build for Sisyphus

