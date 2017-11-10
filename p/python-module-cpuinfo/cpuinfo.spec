%define _unpackaged_files_terminate_build 1
%define oname cpuinfo

%def_with python3

Name: python-module-%oname
Version: 3.3.0
Release: alt1
Summary: Get CPU info with pure Python 2 & 3
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/py-cpuinfo

Source: py-%oname-%version.tar

BuildRequires: python-devel python-module-setuptools
# /proc is needed for tests
BuildRequires: /proc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%description
Py-cpuinfo gets CPU info with pure Python.
Py-cpuinfo should work without any extra programs or libraries, beyond what your OS provides.
It does not require any compilation(C/C++, assembly, et cetera) to use.

%if_with python3
%package -n python3-module-%oname
Summary: Get CPU info with pure Python 2 & 3
Group: Development/Python3

%description -n python3-module-%oname
Py-cpuinfo gets CPU info with pure Python.
Py-cpuinfo should work without any extra programs or libraries, beyond what your OS provides.
It does not require any compilation(C/C++, assembly, et cetera) to use.
%endif

%prep
%setup -n py-%oname-%version

%if_with python3
cp -fR . ../python3
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
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ${i}.py3
done
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
%doc README.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Nov 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.3.0-alt1
- Initial build for ALT.
