%define oname js.typeahead

%def_with python3

Name: python-module-%oname
Version: 0.9.2
Release: alt1
Summary: Fanstatic Package of Twitter's Typeadhead.js
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/js.typeahead/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname
%py_requires js js.jquery

%description
Fanstatic Package of Twitter's Typeadhead.js.

%package -n python3-module-%oname
Summary: Fanstatic Package of Twitter's Typeadhead.js
Group: Development/Python3
%py3_provides %oname
%py3_requires js js.jquery

%description -n python3-module-%oname
Fanstatic Package of Twitter's Typeadhead.js.

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
%doc docs/*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc docs/*
%python3_sitelibdir/*
%endif

%changelog
* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1
- Initial build for Sisyphus

