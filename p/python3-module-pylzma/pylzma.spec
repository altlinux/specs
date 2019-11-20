%define oname pylzma

Name: python3-module-%oname
Version: 0.4.6.2
Release: alt2

Summary: Python bindings for the LZMA library by Igor Pavlov
License: LGPLv2.1+
Group: Development/Python
Url: https://pypi.python.org/pypi/pylzma/
# https://github.com/fancycode/pylzma.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname


%description
PyLZMA provides a platform independent way to read and write data that
has been compressed or can be decompressed by the LZMA library by Igor
Pavlov.

%prep
%setup

sed -i 's|@VERSION@|%version|' version.py

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')
sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')


%build
%add_optflags -fno-strict-aliasing

%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.md doc/*
%python3_sitelibdir/*


%changelog
* Wed Nov 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.6.2-alt2
- disable python2

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.6.2-alt1.git20141116.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.6.2-alt1.git20141116.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.6.2-alt1.git20141116.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6.2-alt1.git20141116
- Initial build for Sisyphus

