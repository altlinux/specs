%define oname hotqueue

%def_with python3

Name: python-module-%oname
Version: 0.2.7
Release: alt1.git20120412
Summary: Simple library that allows to use Redis as a message queue.
Group: Development/Python
License: MIT
Url: https://github.com/richardhenry/hotqueue
Packager: Mikhail Pokidko <pma@altlinux.org>
Source: %name-%version-%release.tar
Patch: hotqueye-alt-docs.patch
Patch1: hotqueye-alt-setuptools.patch
BuildArch:      noarch
BuildRequires:  python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel python-module-redis-py
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
HotQueue is a Python library that allows you to use Redis as a message
queue within your Python programs.

%package -n python3-module-%oname
Summary: Simple library that allows to use Redis as a message queue
Group: Development/Python3

%description -n python3-module-%oname
HotQueue is a Python library that allows you to use Redis as a message
queue within your Python programs.

%prep
%setup
%patch -p1
%patch1 -p1

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html

%files
%doc REQUIREMENTS LICENSE README.rst docs/_build/html
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc REQUIREMENTS LICENSE README.rst docs/_build/html
%python3_sitelibdir/*
%endif

%changelog
* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.7-alt1.git20120412
- Version 0.2.7
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.3-alt1.1
- Rebuild with Python-2.7

* Thu Jan 20 2011 Mikhail Pokidko <pma@altlinux.org> 0.2.3-alt1
- initial build

