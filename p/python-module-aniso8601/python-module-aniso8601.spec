%define oname aniso8601

Summary: Another ISO 8601 parser for Python
Name: python-module-%oname
Version: 4.0.1
Release: alt1
Url: https://bitbucket.org/nielsenb/aniso8601
Source: https://pypi.python.org/packages/source/a/%oname/%oname-%version.tar.gz
License: BSD
Group: Development/Python

BuildArch: noarch

BuildRequires: python-devel python-module-setuptools

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
This is a Python library for parsing date strings
in ISO 8601 format into datetime format.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Another ISO 8601 parser for Python
Group: Development/Python3

%description -n python3-module-%oname
This is a Python library for parsing date strings
in ISO 8601 format into datetime format.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version

cp -fR . ../python3

%build
%python_build


pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc README.rst LICENSE
%python_sitelibdir/*
#%exclude %python_sitelibdir/*/tests

#%files tests
#%python_sitelibdir/*/tests

%files -n python3-module-%oname
%doc README.rst LICENSE
%python3_sitelibdir/*
#%exclude %python3_sitelibdir/*/tests

#%files -n python3-module-%oname-tests
#%python3_sitelibdir/*/tests

%changelog
* Thu Dec 13 2018 Alexey Shabalin <shaba@altlinux.org> 4.0.1-alt1
- initial build

