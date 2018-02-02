%define _unpackaged_files_terminate_build 1
%define oname faketime

%def_with python3

Name: python-module-%oname
Version: 0.9.6.6
Release: alt1.1
Summary: Python wrapper around libfaketime
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/faketime/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/crdoconnor/faketime.git
Source0: https://pypi.python.org/packages/f2/79/f6344e2acc0735867133f4e5b9e43bd0aaee196f90c192186453ab4d840b/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
Libfaketime is a C library which can fake the passage of time for UNIX
applications, written by Wolfgang Hommel.

%if_with python3
%package -n python3-module-%oname
Summary: Python wrapper around libfaketime
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Libfaketime is a C library which can fake the passage of time for UNIX
applications, written by Wolfgang Hommel.
%endif

%prep
%setup -q -n %{oname}-%{version}

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
%ifarch x86_64
install -d %buildroot%_libdir
%endif

%python_install
pushd %buildroot%python_sitelibdir_noarch/%oname
for i in $(ls *.so.*); do
	mv $i %buildroot%_libdir/
	ln -s %_libdir/$i %buildroot%python_sitelibdir_noarch/%oname/
done
popd

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%ifarch x86_64
mv %buildroot%_libexecdir/* %buildroot%_libdir/
%endif

%check
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%_libdir/*.so.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.6.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.6.6-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.6.3-alt1.git20150622.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6.3-alt1.git20150622
- Initial build for Sisyphus

