%define _unpackaged_files_terminate_build 1
%define oname aspectlib

%def_with python3

Name: python-module-%oname
Version: 1.4.2
Release: alt2
Summary: An aspect-oriented programming, monkey-patch and decorators library
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.org/project/aspectlib/

Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%description
An aspect-oriented programming, monkey-patch and decorators library.
It is useful when changing behavior in existing code is desired.
It includes tools for debugging and testing: simple mock/record and a complete capture/replay framework.

%if_with python3
%package -n python3-module-%oname
Summary: An aspect-oriented programming, monkey-patch and decorators library
Group: Development/Python3

%description -n python3-module-%oname
An aspect-oriented programming, monkey-patch and decorators library.
It is useful when changing behavior in existing code is desired.
It includes tools for debugging and testing: simple mock/record and a complete capture/replay framework.
%endif

%prep
%setup
# false dependency
grep -qsF "'fields'" setup.py || exit 1
sed -i "/'fields'/d" setup.py

%if_with python3
cp -fR . ../python3
# these files are not needed in python3
rm -f ../python3/src/%{oname}/py2*.py
%endif

# these files are not needed in python2
rm -f ./src/%{oname}/py3*.py

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
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
python setup.py test

%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc LICENSE *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu May 30 2019 Stanislav Levin <slev@altlinux.org> 1.4.2-alt2
- Removed false dependency on `fields`.

* Fri Nov 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.2-alt1
- Initial build for ALT.
