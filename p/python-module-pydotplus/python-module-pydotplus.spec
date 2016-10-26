%define oname pydotplus

%def_with python3

Name: python-module-%oname
Version: 2.0.2
Release: alt1
Summary: Python interface to Graphviz Dot language
License: MIT
Group: Development/Python
Url: https://github.com/carlos-jenkins/pydotplus

Source: %name-%version.tar

BuildArch: noarch

%setup_python_module %oname
BuildRequires: python-devel python-module-setuptools python-module-pyparsing
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-pyparsing
%endif

Requires: %_bindir/dot

%description
PyDotPlus is an improved version of the old pydot project that provides a Python Interface to Graphviz Dot language.

%package -n python3-module-%oname
Summary: Python interface to Graphviz Dot language
Group: Development/Python3
Requires: %_bindir/dot

%description -n python3-module-%oname
PyDotPlus is an improved version of the old pydot project that provides a Python Interface to Graphviz Dot language.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

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

%files
%doc README.rst LICENSE
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.rst LICENSE
%python3_sitelibdir/*
%endif

%changelog
* Wed Oct 26 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.2-alt1
- Initial build
