%define oname jq

Name: python3-module-%oname
Version: 0.1.6
Release: alt2

Summary: Lightweight and flexible JSON processor
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/jq/

# https://github.com/mwilliamson/jq.py.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Cython python3-module-nose
BuildRequires: python3-module-tox
BuildRequires: python3-module-html5lib python3-module-notebook
BuildRequires: libjq-devel

%py3_provides %oname


%description
jq is a lightweight and flexible JSON processor.

This project contains Python bindings for jq.

%prep
%setup
%patch1 -p1

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
cython3 jq.pyx
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
%__python3 setup.py build_ext -i
nosetests3 tests -v

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Fri Dec 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.6-alt2
- build for python2 disabled

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.6-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.6-alt1
- Updated to upstream version 0.1.6.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt1.git20150118.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1.git20150118.1
- NMU: Use buildreq for BR.

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20150118
- Initial build for Sisyphus

