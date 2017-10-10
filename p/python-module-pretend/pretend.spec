%define oname pretend

%def_with python3

Name: python-module-%oname
Version: 1.0.8
Release: alt1%ubt
Summary: A library for stubbing in Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pretend
BuildArch: noarch

# https://github.com/alex/pretend.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: python-dev python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-pytest
%endif

%description
Pretend is a library to make stubbing with Python easier.

%package -n python3-module-%oname
Summary: A library for stubbing in Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Pretend is a library to make stubbing with Python easier.

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
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%check
py.test -v
%if_with python3
pushd ../python3
py.test3 -v
popd
%endif

%files
%doc LICENSE.rst README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE.rst README.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Oct 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.8-alt1%ubt
- Initial build for ALT.
