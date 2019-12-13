%define oname google.google

Name: python3-module-%oname
Version: 1.05
Release: alt2

Summary: Python bindings to the Google search engine
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/google/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: dos2unix

%py3_requires google


%description
Python bindings to the Google search engine.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

dos2unix google.py

%build
%python3_build

%install
%python3_install

install -d %buildroot%python3_sitelibdir/google
mv %buildroot%python3_sitelibdir/*.py \
    %buildroot%python3_sitelibdir/__pycache__ \
    %buildroot%python3_sitelibdir/google/

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/*


%changelog
* Fri Dec 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.05-alt2
- build for python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.05-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.05-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.05-alt1
- Initial build for Sisyphus

