%define oname jsontest

%def_with python3

Name: python-module-%oname
Version: 1.3
Release: alt1
Summary: Automatically generate Python tests from JSON files
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/JsonTest
BuildArch: noarch

# https://github.com/Fizzadar/JsonTest.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%description
A tiny metaclass for autogenerating tests from JSON files.

%if_with python3
%package -n python3-module-%oname
Summary: Automatically generate Python tests from JSON files
Group: Development/Python3

%description -n python3-module-%oname
A tiny metaclass for autogenerating tests from JSON files.
%endif

%prep
%setup

%if_with python3
cp -a . ../python3
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
%python3_build_install
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Tue Mar 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3-alt1
- Initial build for ALT.
