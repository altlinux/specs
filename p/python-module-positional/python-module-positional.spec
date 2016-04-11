%define modulename positional

%def_with python3

Name: python-module-%modulename
Version: 1.0.1
Release: alt1

%setup_python_module %modulename

Summary: Library to enforce positional or key-word arguments
License: ASL 2.0
Group: Development/Python

Url: https://github.com/morganfainberg/positional
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pbr
%endif

%description
`positional` provides a decorator which enforces only some args may be passed
positionally. The idea and some of the code was taken from the oauth2 client
of the google-api client.

%package -n python3-module-%modulename
Summary: Library to enforce positional or key-word arguments
Group: Development/Python3

%description -n python3-module-%modulename
`positional` provides a decorator which enforces only some args may be passed
positionally. The idea and some of the code was taken from the oauth2 client
of the google-api client.


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
# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%modulename
%doc README.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Apr 12 2016 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt1
- initial build
