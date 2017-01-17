%define _unpackaged_files_terminate_build 1
%define oname modernize

%def_with python3

Name: python-module-%oname
Version: 0.5
Release: alt1
Summary: A hack on top of 2to3 for modernizing code for hybrid codebases
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/modernize/0.2
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/d5/e7/92d89a6814f52add2c334be42108c4eac8763f8e147716595a55cabd921a/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
This library is a very thin wrapper around lib2to3 to utilize it
to make Python 2 code more modern with the intention of eventually
porting it over to Python 3.

It does not guarantee, but it attempts to spit out a Python 2/3
compatible codebase.  The code that it generates has a runtime
dependency on `six`.

%package -n python3-module-%oname
Summary: A hack on top of 2to3 for modernizing code for hybrid codebases
Group: Development/Python3

%description -n python3-module-%oname
This library is a very thin wrapper around lib2to3 to utilize it
to make Python 2 code more modern with the intention of eventually
porting it over to Python 3.

It does not guarantee, but it attempts to spit out a Python 2/3
compatible codebase.  The code that it generates has a runtime
dependency on `six`.

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
mv %buildroot%_bindir/python-modernize \
	%buildroot%_bindir/python-modernize.py3
%endif

%python_install

%files
%doc PKG-INFO LICENSE README.rst CHANGELOG.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO LICENSE README.rst CHANGELOG.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

