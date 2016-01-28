%define oname fb

%def_with python3

Name: python-module-%oname
Version: 0.4.0
Release: alt1.git20141005.1
Summary: Python SDK for the Facebook Graph Api
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/fb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/blaklites/fb.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python-tools-2to3
%endif

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python3 python3-base
BuildRequires: rpm-build-python3

%description
fb is a python sdk for the Facebook Graph Api. The sdk provides three
methods for interacting largely with facebook. publish(), get_object()
and delete() In addtion to the three, there is one helper method to view
the structure of objects returned from facebook, show_fields()

%package -n python3-module-%oname
Summary: Python SDK for the Facebook Graph Api
Group: Development/Python3

%description -n python3-module-%oname
fb is a python sdk for the Facebook Graph Api. The sdk provides three
methods for interacting largely with facebook. publish(), get_object()
and delete() In addtion to the three, there is one helper method to view
the structure of objects returned from facebook, show_fields()

%prep
%setup

%if_with python3
cp -fR . ../python3
#find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%install
install -d %buildroot%python_sitelibdir
cp -fR %oname %buildroot%python_sitelibdir/

%if_with python3
pushd ../python3
install -d %buildroot%python3_sitelibdir
cp -fR %oname %buildroot%python3_sitelibdir/
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
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1.git20141005.1
- NMU: Use buildreq for BR.

* Wed Oct 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20141005
- Initial build for Sisyphus

