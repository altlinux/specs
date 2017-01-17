%define _unpackaged_files_terminate_build 1
%define oname gearbox

%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt1
Summary: Toolkit born as a PasteScript replacement for the TurboGears2 web framework
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/gearbox/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/TurboGears/gearbox.git
Source0: https://pypi.python.org/packages/01/77/731c12d104a9df980baa4828347882d57a4e39a44d1f5e6c7bd0d627fc11/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-cliff python-module-tempita
#BuildPreReq: python-module-PasteDeploy
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-cliff python3-module-tempita
#BuildPreReq: python3-module-PasteDeploy
%endif

%py_provides %oname
%py_requires cliff tempita paste.deploy

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cmd2 python-module-cssselect python-module-docutils python-module-genshi python-module-jinja2 python-module-paste python-module-pyparsing python-module-pytest python-module-pytz python-module-setuptools python-module-snowballstemmer python-module-sphinx python-module-stevedore python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-Pygments python3-module-babel python3-module-cssselect python3-module-docutils python3-module-genshi python3-module-jinja2 python3-module-paste python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-snowballstemmer python3-module-sphinx python3-module-stevedore python3-module-yaml
BuildRequires: python-module-PasteDeploy python-module-cliff python-module-html5lib python-module-setuptools-tests python3-module-PasteDeploy python3-module-cliff python3-module-html5lib python3-module-setuptools-tests rpm-build-python3

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
%setup -q -n %{oname}-%{version}

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
%doc *.rst PKG-INFO
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst PKG-INFO
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.7-alt1.git20150205.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.7-alt1.git20150205.1
- NMU: Use buildreq for BR.

* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1.git20150205
- Initial build for Sisyphus

