%define oname voluptuous

%def_with python3

Name: python-module-%oname
Version: 0.8.11
Release: alt1
Summary: Voluptuous is a Python data validation library
License: BSD
Group: Development/Python
Url:  http://github.com/alecthomas/voluptuous

Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
Voluptuous, *despite* the name, is a Python data validation library. It
is primarily intended for validating data coming into Python as JSON,
YAML, etc.

It has three goals:

1. Simplicity.
2. Support for complex data structures.
3. Provide useful error messages.

%package -n python3-module-%oname
Summary: Voluptuous is a Python data validation library
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Voluptuous, *despite* the name, is a Python data validation library. It
is primarily intended for validating data coming into Python as JSON,
YAML, etc.

It has three goals:

1. Simplicity.
2. Support for complex data structures.
3. Provide useful error messages.

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
%doc COPYING README.md README.rst
%python_sitelibdir/*


%if_with python3
%files -n python3-module-%oname
%doc COPYING README.md README.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 0.8.11-alt1
- Initial build for Sisyphus
