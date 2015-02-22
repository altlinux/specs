%define mname zopyx.smartprintng
%define oname %mname.client
Name: python-module-%oname
Version: 0.8.5
Release: alt1.git10121018
Summary: Produce & Publish ZIP client
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/zopyx.smartprintng.client/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopyx/zopyx.smartprintng.client.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests

%py_provides %oname
Requires: python-module-%mname = %EVR

%description
The zip-client-side implementation of the Produce & Publish server (aka
zopyx.smartprintng.server).

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires zopyx

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%build
%python_build_debug

%install
install -d %buildroot%python_sitelibdir/zopyx
cp -fR zopyx/smartprintng %buildroot%python_sitelibdir/zopyx/
cp -fR *.egg-info %buildroot%python_sitelibdir/

%check
python setup.py test

%files
%doc *.txt docs/*
%python_sitelibdir/zopyx/smartprintng/client
%python_sitelibdir/*.egg-info

%files -n python-module-%mname
%dir %python_sitelibdir/zopyx/smartprintng
%python_sitelibdir/zopyx/smartprintng/__init__.py*

%changelog
* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.5-alt1.git10121018
- Initial build for Sisyphus

