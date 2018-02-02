%define oname rcssmin

%def_with python3

Name: python-module-%oname
Version: 1.0.6
Release: alt1.1
Summary: CSS Minifier
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/%oname

# https://github.com/ndparker/rcssmin.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-epydoc python-modules-xml
BuildPreReq: python-modules-logging python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
rCSSmin is a CSS minifier written in python.

%package -n python3-module-%oname
Summary: CSS Minifier
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
rCSSmin is a CSS minifier written in python.

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

export PYTHONPATH=%buildroot%python_sitelibdir
pushd docs
epydoc --config=epydoc.conf
popd

%files
%doc %_docdir/%oname
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc %_docdir/%oname
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 24 2016 Alexey Shabalin <shaba@altlinux.ru> 1.0.6-alt1
- Initial build for Sisyphus

