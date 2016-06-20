%def_with python3

Name: python-module-remoto
Version: 0.0.28
Release: alt1
Summary: Execute remote commands or processes
Group: Development/Python

License: MIT
Url: https://github.com/alfredodeza/remoto

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: python-module-pytest
BuildRequires: rpm-build-python
BuildRequires: python-module-execnet >= 1.2.0
BuildRequires: python-module-mock
BuildRequires: python-module-setuptools
%if_with python3
BuildRequires: python3-devel
BuildRequires: python3-module-pytest
BuildRequires: python3-module-execnet >= 1.2.0
BuildRequires: python3-module-mock
BuildRequires: python3-module-setuptools
%endif

Requires: python-module-execnet >= 1.2.0

%description
Execute remote commands or processes.

%if_with python3
%package -n python3-module-remoto
Summary: Execute remote commands or processes
Group: Development/Python
Requires: python3
Requires: python3-module-execnet >= 1.2.0

%description -n python3-module-remoto
Execute remote commands or processes.
%endif

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
export REMOTO_NO_VENDOR=1
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
export REMOTO_NO_VENDOR=1
%python_install -O1

%if_with python3
pushd ../python3
%python3_install -O1
popd
%endif

%check
export REMOTO_NO_VENDOR=1
export PYTHONPATH=$(pwd)

py.test-%__python_version -v remoto/tests

%if_with python3
pushd ../python3
py.test-%__python3_version -v remoto/tests
popd
%endif

%files
%doc LICENSE README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-remoto
%python3_sitelibdir/*
%doc LICENSE README.rst
%endif

%changelog
* Mon Jun 20 2016 Lenar Shakirov <snejok@altlinux.ru> 0.0.28-alt1
- First build for Sisyphus (based on 0.0.28-1.fc25)

