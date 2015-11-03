%global modname cliff-tablib

%def_with python3

Name:             python-module-%modname
Version:          1.1
Release:          alt2
Summary:          tablib formatters for cliff

Group:            Development/Python
License:          ASL 2.0
URL:              https://pypi.python.org/pypi/cliff-tablib
Source0:          %name-%version.tar

BuildArch:        noarch

BuildRequires:    python-devel
BuildRequires:    python-module-setuptools
BuildRequires:    python-module-pbr
BuildRequires:    python-module-cliff
BuildRequires:    python-module-tablib

BuildPreReq: python-module-sphinx-devel python-module-oslosphinx

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires:    python3-devel
BuildRequires:    python3-module-setuptools
BuildRequires:    python3-module-pbr
BuildRequires:    python3-module-cliff
BuildRequires:    python3-module-tablib

%endif

%description
The cliff framework is meant to be used to create multi-level commands
such as subversion and git, where the main program handles some basic
argument parsing and then invokes a sub-command to do the work. This
package adds JSON, YAML, and HTML output formatters to those commands.

%package -n python3-module-%modname
Summary:          tablib formatters for cliff
Group:            Development/Python3

%description -n python3-module-%modname
The cliff framework is meant to be used to create multi-level commands
such as subversion and git, where the main program handles some basic
argument parsing and then invokes a sub-command to do the work. This
package adds JSON, YAML, and HTML output formatters to those commands.

%prep
%setup

# Remove bundled egg info
rm -rf *.egg-info

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
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%modname
%python3_sitelibdir/*
%endif

%changelog
* Tue Nov 03 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1-alt2
- enable python3 package

* Wed Aug 26 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1-alt1
- Initial release for Sisyphus
