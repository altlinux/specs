%define oname pydap3.2

%def_with python3

Name: python-module-%oname
Version: 3.2
Release: alt1.git20121211.1
Summary: A Python library implementing the Data Access Protocol (DAP, aka OPeNDAP or DODS)
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/dap/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/lukecampbell/pydap.git
Source: %oname-%version.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-httplib2
#BuildPreReq: python-module-paste python-module-cheetah
#BuildPreReq: python-module-setuptools-tests libnumpy-devel
#BuildPreReq: python-module-PasteScript python-module-PasteDeploy
#BuildPreReq: python-module-genshi
%setup_python_module %oname
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-httplib2
#BuildPreReq: python3-module-setuptools-tests libnumpy-py3-devel
#BuildPreReq: python3-module-paste python3-module-genshi
#BuildPreReq: python3-module-PasteScript python3-module-PasteDeploy
%endif

Requires: python-modules-email
%py_requires paste.deploy
Conflicts: python-module-pydap

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-numpy python-module-paste python-module-pyparsing python-module-pytz python-module-setuptools python-module-snowballstemmer python-module-sphinx python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-numpy python3-module-paste python3-module-setuptools
BuildRequires: python-module-PasteDeploy python-module-PasteScript python-module-docutils python-module-html5lib python-module-httplib2 python-module-matplotlib python-module-pytest python3-module-PasteDeploy python3-module-PasteScript python3-module-genshi python3-module-httplib2 python3-module-pytest rpm-build-python3 time

%description
Pydap is an implementation of the Opendap/DODS protocol, written from
scratch. You can use Pydap to access scientific data on the internet
without having to download it; instead, you work with special array and
iterable objects that download data on-the-fly as necessary, saving
bandwidth and time. The module also comes with a robust-but-lightweight
Opendap server, implemented as a WSGI application.

%package -n python3-module-%oname
Summary: Python implementation of the Data Access Protocol (DAP)
Group: Development/Python3
%py3_requires paste.deploy rfc822py3
Conflicts: python3-module-pydap

%description -n python3-module-%oname
Pydap is an implementation of the Opendap/DODS protocol, written from
scratch. You can use Pydap to access scientific data on the internet
without having to download it; instead, you work with special array and
iterable objects that download data on-the-fly as necessary, saving
bandwidth and time. The module also comes with a robust-but-lightweight
Opendap server, implemented as a WSGI application.

%prep
%setup

%if_with python3
cp -fR . ../python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
popd
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%files
%doc *.txt *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.2-alt1.git20121211.1
- NMU: Use buildreq for BR.

* Wed Aug 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt1.git20121211
- Initial build for Sisyphus

