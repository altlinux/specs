%define oname hotqueue

%def_with python3

Name: python-module-%oname
Version: 0.2.7
Release: alt1.git20120412.1.1
Summary: Simple library that allows to use Redis as a message queue.
Group: Development/Python
License: MIT
Url: https://github.com/richardhenry/hotqueue
Packager: Mikhail Pokidko <pma@altlinux.org>
Source: %name-%version-%release.tar
Patch: hotqueye-alt-docs.patch
Patch1: hotqueye-alt-setuptools.patch
BuildArch:      noarch
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-redis-py python3-module-setuptools rpm-build-python3 time

#BuildRequires:  python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel python-module-redis-py
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.7-alt1.git20120412.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.7-alt1.git20120412.1
- NMU: Use buildreq for BR.

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.7-alt1.git20120412
- Version 0.2.7
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.3-alt1.1
- Rebuild with Python-2.7

* Thu Jan 20 2011 Mikhail Pokidko <pma@altlinux.org> 0.2.3-alt1
- initial build

