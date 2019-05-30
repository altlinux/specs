%define _unpackaged_files_terminate_build 1
%define oname fields

%def_with python3
%def_with full_tests

Name: python-module-%oname
Version: 5.0.0
Release: alt2
Summary: Container class boilerplate killer
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/fields

Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
%if_with full_tests
BuildRequires: python2.7(attr) python2.7(characteristic) python2.7(pytest_benchmark)
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%if_with full_tests
BuildRequires: python3(attr) python3(characteristic) python3(pytest_benchmark)
%endif
%endif

%description
Container class boilerplate killer.

%if_with python3
%package -n python3-module-%oname
Summary: Container class boilerplate killer
Group: Development/Python3

%description -n python3-module-%oname
Container class boilerplate killer.
%endif

%prep
%setup
# Pytest4.x compatibility
grep -qsF '[pytest]' setup.cfg || exit 1
sed -i 's/\[pytest\]/[tool:pytest]/g' setup.cfg

%if_with python3
cp -fR . ../python3
# this file is not needed in python3
rm -f ../python3/src/fields/py2ordereddict.py
%endif

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
%if_with full_tests
py.test
%endif

%if_with python3
pushd ../python3
python3 setup.py test
%if_with full_tests
py.test3
%endif
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
* Thu May 30 2019 Stanislav Levin <slev@altlinux.org> 5.0.0-alt2
- Fixed Pytest4.x compatibility error.

* Fri Nov 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0.0-alt1
- Initial build for ALT.
