%define _unpackaged_files_terminate_build 1
%define oname ujson

%def_with python3

Name: python-module-%oname
Version: 1.35
Release: alt1
Summary: Ultra fast JSON encoder and decoder for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/ujson/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/esnme/ultrajson.git
Source0: https://pypi.python.org/packages/16/c4/79f3409bc710559015464e5f49b9879430d8f87498ecdc335899732e5377/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
UltraJSON is an ultra fast JSON encoder and decoder written in pure C
with bindings for Python 2.5+ and 3.

%package -n python3-module-%oname
Summary: Ultra fast JSON encoder and decoder for Pytho
Group: Development/Python3

%description -n python3-module-%oname
UltraJSON is an ultra fast JSON encoder and decoder written in pure C
with bindings for Python 2.5+ and 3.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%install
%add_optflags -fno-strict-aliasing
%python_build_install

%if_with python3
pushd ../python3
%python3_build_install
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.35-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.34-alt1.git20140416.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.34-alt1.git20140416
- Initial build for Sisyphus

