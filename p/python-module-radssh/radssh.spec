%define oname radssh

%def_with python3

Name: python-module-%oname
Version: 1.1.1
Release: alt1
Summary: RadSSH Module
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/radssh/

# https://github.com/radssh/radssh.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-docs.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-paramiko python-module-netaddr
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-paramiko python3-module-netaddr
%endif

%py_provides %oname
%py_requires paramiko netaddr
%add_python_req_skip genders

%description
High level Paramiko-based toolkit, with an extensible parallel cluster
"shell".

%if_with python3
%package -n python3-module-%oname
Summary: RadSSH Module
Group: Development/Python3
%py3_provides %oname
%py3_requires paramiko netaddr
%add_python3_req_skip genders

%description -n python3-module-%oname
High level Paramiko-based toolkit, with an extensible parallel cluster
"shell".
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

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

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
PYTHONPATH=%buildroot%python_sitelibdir python tests/dispatcher.py
%if_with python3
pushd ../python3
PYTHONPATH=%buildroot%python3_sitelibdir python3 tests/dispatcher.py
popd
%endif

%files
%doc README *.md api_sample
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc README *.md api_sample
%python3_sitelibdir/*
%endif

%changelog
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

