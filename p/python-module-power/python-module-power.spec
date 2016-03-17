%def_with python3
%define   pypi_name power
%define   py3dir ../py3build

Name:           python-module-%{pypi_name}
Version:        1.4
Release:        alt1

Summary:        Cross-platform system power status information
License:        MIT
Group:          Development/Python
URL:            https://github.com/Kentzo/Power
Source0:        %name-%version.tar
BuildArch:      noarch

BuildRequires(pre): rpm-build-python
BuildRequires:  python-devel
BuildRequires:  python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-devel
BuildRequires:  python3-module-setuptools
%endif

%description
Python module that allows you to get power and battery status of the
system.

%if_with python3
%package -n python3-module-%{pypi_name}
Group:          Development/Python3
Summary:        Cross-platform system power status information

%description -n python3-module-%{pypi_name}
Python module that allows you to get power and battery status of the
system.
%endif

%prep
%setup -q

# Remove Mac-specific file
rm -f power/darwin.py

%if_with python3
mkdir %py3dir
cp -a . %py3dir
find %py3dir -name '*.py' | xargs sed -i '1s|^#!%{__python}|#!%{__python3}|'
%endif

%build
%python_build
%if_with python3
pushd %py3dir
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd %py3dir
%python3_install
%endif

%check
python -m unittest -v power.tests
%if_with python3
pushd %py3dir
python3 -m unittest -v power.tests
popd
%endif

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%{pypi_name}
%python3_sitelibdir/*
%endif

%changelog
* Thu Mar 17 2016 Andrey Cherepanov <cas@altlinux.org> 1.4-alt1
- Initail build in Sisyphus

