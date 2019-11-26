%define oname skosprovider_sqlalchemy

%def_disable check

Name: python3-module-%oname
Version: 0.4.1
Release: alt2

Summary: A SQLAlchemy implementation of the skosprovider interface
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/skosprovider_sqlalchemy/
# https://github.com/koenedaele/skosprovider_sqlalchemy.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose python3-module-pytest-cov
BuildRequires: python3-module-z4r-coveralls

%py3_provides %oname
%py3_requires skosprovider sqlalchemy


%description
An implementation of the skosprovider interface against SQLAlchemy.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst docs/*.rst
%_bindir/*
%python3_sitelibdir/*


%changelog
* Tue Nov 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.1-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.4.1-alt1.git20141218.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.git20141218.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt1.git20141218.1
- NMU: Use buildreq for BR.

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20141218
- Initial build for Sisyphus

