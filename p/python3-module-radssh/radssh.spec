%define oname radssh

Name: python3-module-%oname
Version: 1.1.1
Release: alt2

Summary: RadSSH Module
License: BSD
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/radssh/

# https://github.com/radssh/radssh.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-docs.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-paramiko python3-module-netaddr
BuildRequires: python3-module-sphinx

%py3_provides %oname
%py3_requires paramiko netaddr
%add_python3_req_skip genders


%description
High level Paramiko-based toolkit, with an extensible parallel cluster
"shell".

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
High level Paramiko-based toolkit, with an extensible parallel cluster
"shell".

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
High level Paramiko-based toolkit, with an extensible parallel cluster
"shell".

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python3_sitelibdir/%oname/

%check
PYTHONPATH=%buildroot%python3_sitelibdir python3 tests/dispatcher.py

%files
%doc README *.md api_sample
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*


%changelog
* Fri Dec 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1.1-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt1
- Updated to upstream version 1.1.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.5-alt1.git20150714.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.5-alt1.git20150714.1
- NMU: Use buildreq for BR.

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1.git20150714
- Version 1.0.5

* Thu Feb 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20150203
- Initial build for Sisyphus

