%define srcname PyWebDAV
%define oname pywebdav

%def_with python3

Name:           python-module-%oname
Version:        0.9.8
Release:        alt1.1.1
Summary:        WebDAV library

Group:          Development/Python
License:        LGPLv2+
URL:            http://www.webdav.de/
Source0:        http://pywebdav.googlecode.com/files/%srcname-%version.tar.gz

BuildArch:      noarch
BuildRequires(pre): rpm-build-python
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-setuptools-tests python3-module-setuptools-tests rpm-build-python3 time

#BuildRequires:  python-devel
#BuildRequires:  python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires:  python3-devel
#BuildRequires:  python3-module-setuptools-tests
#BuildPreReq: python-tools-2to3
%endif

Provides:       pywebdav = %version-%release

%description
WebDAV library for Python. WebDAV is an extension to the normal HTTP/1.1
protocol allowing the user to upload data, create collections of objects,
store properties for objects, etc.

%package -n python3-module-%oname
Summary:        WebDAV library
Group:          Development/Python3
Provides:       py3webdav = %version-%release

%description -n python3-module-%oname
WebDAV library for Python. WebDAV is an extension to the normal HTTP/1.1
protocol allowing the user to upload data, create collections of objects,
store properties for objects, etc.

%prep
%setup -n %srcname-%version
rm -f doc/INSTALL

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
export LC_ALL=en_US.UTF-8

%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
export LC_ALL=en_US.UTF-8

%python_install
rm -f %buildroot%_bindir/*
rm -rf %buildroot%python_sitelibdir/pywebdav/server

%if_with python3
pushd ../python3
%python3_install
popd
rm -f %buildroot%_bindir/*
rm -rf %buildroot%python3_sitelibdir/pywebdav/server
%endif

%check
export LC_ALL=en_US.UTF-8
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc doc/*
%python_sitelibdir/pywebdav
%python_sitelibdir/%{srcname}*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc doc/*
%python3_sitelibdir/pywebdav
%python3_sitelibdir/%{srcname}*.egg-info
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.8-alt1.1.1
- NMU: Use buildreq for BR.

* Mon Oct 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1.1
- Added module for Python 3

* Wed Jan 16 2013 Andrey Cherepanov <cas@altlinux.org> 0.9.8-alt1
- Initial build in Sisyphus

