%define oname twine

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.3.1
Release: alt2.git20140815
Summary: Collection of utilities for interacting with PyPI
License: ASL
Group: Development/Python
Url: https://pypi.python.org/pypi/twine/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pypa/twine.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-module-chardet python-module-ndg-httpsclient python-module-nose python-module-ntlm python-module-pkginfo python-module-pytest 
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-chardet python3-module-nose python3-module-pkginfo python3-module-pytest python3-module-urllib3
%endif

%py_provides %oname

%description
Twine is a utility for interacting with PyPI.

Currently it only supports uploading distributions.

%package -n python3-module-%oname
Summary: Collection of utilities for interacting with PyPI
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Twine is a utility for interacting with PyPI.

Currently it only supports uploading distributions.

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

%check
export PYTHONPATH=$PWD
python setup.py test
py.test
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
python3 setup.py test
py.test-%_python3_version
popd
%endif

%files
%doc AUTHORS *.rst docs/*.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst docs/*.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Wed Feb 03 2016 Sergey Alembekov <rt@altlinux.ru> 1.3.1-alt2.git20140815
- cleanup buildreqs
- disable check

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.git20140815
- Initial build for Sisyphus

