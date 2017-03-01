%global pypi_name betamax
%def_with python3
%def_disable check

Name: python-module-%pypi_name
Version: 0.8.0
Release: alt1
Summary: VCR imitation for python-requests

Group: Development/Python
License: ASL 2.0 or BSD
Url: https://github.com/sigmavirus24/betamax
Source: %pypi_name-%version.tar.gz
Patch: betamax-system-urllib3.patch

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-requests

%if_with python3
BuildRequires(pre):  rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-requests
%endif

%description
Betamax is a VCR_ imitation for requests. This will make mocking out requests\
much easier.

%package -n python3-module-%pypi_name
Summary: VCR imitation for python-requests
Group: Development/Python3
BuildArch: noarch

%description -n python3-module-%pypi_name
Betamax is a VCR_ imitation for requests. This will make mocking out requests\
much easier.

%prep
%setup -n %pypi_name-%version
%patch -p1

%if_with python3
rm -rf ../python3
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
%python3_install
popd
%endif

%check
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc README.rst LICENSE
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%pypi_name
%doc README.rst LICENSE
%python3_sitelibdir/*
%endif

%changelog
* Wed Mar 01 2017 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0
