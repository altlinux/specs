%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname js.html5shiv

%def_with python3

Name: python-module-%oname
Version: 3.7.3
#Release: alt1.dev0.hg20130504.1
Summary: Fanstatic packaging of html5shiv
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.html5shiv/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/fanstatic/js.html5shiv
Source0: https://pypi.python.org/packages/de/dc/b051382290657f45a311681753b649e4d1670627596bc33a0e5d278cb31f/%{oname}-%{version}.tar.gz

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

%if "%_libexecdir" != "%_libdir"
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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.7.3-alt1
- automated PyPI update

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.6.2.2-alt1.dev0.hg20130504.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.6.2.2-alt1.dev0.hg20130504.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2.2-alt1.dev0.hg20130504
- Initial build for Sisyphus

