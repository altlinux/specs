%define oname js.html5shiv

%def_with python3

Name: python-module-%oname
Version: 3.6.2.2
Release: alt1.dev0.hg20130504.1
Summary: Fanstatic packaging of html5shiv
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.html5shiv/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/fanstatic/js.html5shiv
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname
%py_requires js

%description
This library packages html5shiv for fanstatic.

%package -n python3-module-%oname
Summary: Fanstatic packaging of html5shiv
Group: Development/Python
%py3_provides %oname
%py3_requires js

%description -n python3-module-%oname
This library packages html5shiv for fanstatic.

%prep
%setup

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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.6.2.2-alt1.dev0.hg20130504.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2.2-alt1.dev0.hg20130504
- Initial build for Sisyphus

