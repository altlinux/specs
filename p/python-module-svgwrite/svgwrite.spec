%define _unpackaged_files_terminate_build 1
%define oname svgwrite

%def_with python3

Name: python-module-%oname
Version: 1.1.9
Release: alt1
Summary: A Python library to create SVG drawings
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/svgwrite/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/27/77/041204e668cdcd305b3366dbf486baa70bfcf40705ed4a658ef4fd3f0a74/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
A Python library to create SVG drawings.

%package -n python3-module-%oname
Summary: A Python library to create SVG drawings
Group: Development/Python3

%description -n python3-module-%oname
A Python library to create SVG drawings.

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.TXT
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.TXT
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.9-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.6-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.6-alt1
- Initial build for Sisyphus

