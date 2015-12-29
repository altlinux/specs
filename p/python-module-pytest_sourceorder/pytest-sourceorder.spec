%define _unpackaged_files_terminate_build 1

%define mname pytest_sourceorder
%def_without python3

Name: python-module-%mname
Version: 0.4
Release: alt1
Summary: Test-ordering plugin for pytest

Group: Development/Python
License: %gpl3plus
Url: https://github.com/encukou/pytest-sourceorder

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildArch: noarch

BuildPreReq: rpm-build-python
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-pytest

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest
%endif

%setup_python_module %mname

%description
Allows tests within a specially marked class to be run in source order,
instead of the "almost alphabetical" order Pytest normally uses.

%if_with python3
%package -n python3-module-%mname
Summary:       Test-ordering plugin for pytest (Python3)
Group:         Development/Python3

%description -n python3-module-%mname
Allows tests within a specially marked class to be run in source order,
instead of the "almost alphabetical" order Pytest normally uses.
This is a Python3 module.
%endif

%prep
%setup
#patch -p1
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

%check
python -m pytest

%if_with python3
pushd ../python3
python3 -m pytest
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
%files -n python3-module-%mname
%python3_sitelibdir/*
%endif

%changelog
* Tue Dec 29 2015 Mikhail Efremov <sem@altlinux.org> 0.4-alt1
- Initial build.

