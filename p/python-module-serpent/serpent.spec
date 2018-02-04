%define oname serpent

%def_with python3

Name: python-module-%oname
Version: 1.23
Release: alt1.1
Summary: Serializer for literal Python expressions
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/serpent

# https://github.com/irmen/Serpent.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-module-flake8 python-module-pytz python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flake8 python3-module-pytz python3-module-setuptools
%endif

%py_provides %oname

%description
Serpent is a simple serialization library based on ast.literal_eval.

Because it only serializes literals and recreates the objects using
ast.literal_eval(), the serialized data is safe to transport to other
machines (over the network for instance) and de-serialize it there.

%package -n python3-module-%oname
Summary: Serializer for literal Python expressions
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Serpent is a simple serialization library based on ast.literal_eval.

Because it only serializes literals and recreates the objects using
ast.literal_eval(), the serialized data is safe to transport to other
machines (over the network for instance) and de-serialize it there.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

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

%check
python setup.py test
%make test
%if_with python3
pushd ../python3
python3 setup.py test
sed -i 's|python|python3|g' Makefile
%make test
popd
%endif

%files
%doc LICENSE README.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.23-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Oct 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.23-alt1
- Updated to upstream version 1.23.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.11-alt2.git20150621.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 05 2016 Sergey Alembekov <rt@altlinux.ru> 1.11-alt2.git20150621
- cleanup buildreq

* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11-alt1.git20150621
- Version 1.11

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt1.git20150108
- Version 1.8

* Wed Oct 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1.git20140713
- Initial build for Sisyphus

