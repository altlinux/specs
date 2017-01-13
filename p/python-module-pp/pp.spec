%define _unpackaged_files_terminate_build 1
%define oname pp

%def_without python3

Name: python-module-%oname
Version: 1.6.5
Release: alt1
Summary: Parallel and distributed programming for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/14/e9/f69030681985226849becd36b04e2c0cb99babff23c8342bc4e30ded06b2/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python-tools-2to3
%endif

%description
Parallel Python module (PP) provides an easy and efficient way to create
parallel-enabled applications for SMP computers and clusters. PP module
features cross-platform portability and dynamic load balancing. Thus
application written with PP will parallelize efficiently even on
heterogeneous and multi-platform clusters (including clusters running
other application with variable CPU loads).

%package -n python3-module-%oname
Summary: Parallel and distributed programming for Python
Group: Development/Python3

%description -n python3-module-%oname
Parallel Python module (PP) provides an easy and efficient way to create
parallel-enabled applications for SMP computers and clusters. PP module
features cross-platform portability and dynamic load balancing. Thus
application written with PP will parallelize efficiently even on
heterogeneous and multi-platform clusters (including clusters running
other application with variable CPU loads).

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/ppserver.py %buildroot%_bindir/ppserver.py3
%endif

%python_install

%files
%doc AUTHORS CHANGELOG README doc/*.config doc/*.html
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGELOG README doc/*.config doc/*.html
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.6.5-alt1
- automated PyPI update

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.4-alt1
- Initial build for Sisyphus

