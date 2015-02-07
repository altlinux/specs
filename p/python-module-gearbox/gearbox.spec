%define oname gearbox

%def_with python3

Name: python-module-%oname
Version: 0.0.7
Release: alt1.git20150205
Summary: Toolkit born as a PasteScript replacement for the TurboGears2 web framework
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/gearbox/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/TurboGears/gearbox.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-cliff python-module-tempita
BuildPreReq: python-module-PasteDeploy
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-cliff python3-module-tempita
BuildPreReq: python3-module-PasteDeploy
%endif

%py_provides %oname
%py_requires cliff tempita paste.deploy

%description
gearbox is a paster command replacement for TurboGears2. It has been
created during the process of providing Python3 support to the
TurboGears2 web framework, while still being backward compatible with
the existing TurboGears projects.

%package -n python3-module-%oname
Summary: Toolkit born as a PasteScript replacement for the TurboGears2 web framework
Group: Development/Python3
%py3_provides %oname
%py3_requires cliff tempita paste.deploy

%description -n python3-module-%oname
gearbox is a paster command replacement for TurboGears2. It has been
created during the process of providing Python3 support to the
TurboGears2 web framework, while still being backward compatible with
the existing TurboGears projects.

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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1.git20150205
- Initial build for Sisyphus

