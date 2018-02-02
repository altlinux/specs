%define srcname PyWebDAV3

Name:           python-module-pywebdav
Version:        0.9.11
Release:        alt1.1
Summary:        PyWebDAV is a standards compliant WebDAV server and library written in Python

Group:          Development/Python
License:        LGPLv2+
URL:            https://github.com/andrewleech/PyWebDAV3
Source0:        %srcname-%version.tar

BuildArch:      noarch
BuildRequires(pre): rpm-build-python
BuildRequires:  python-devel
BuildRequires:  python-module-distribute
BuildRequires:  python-module-six
BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-devel
BuildRequires:  python3-module-distribute
BuildRequires: python-module-setuptools python3-module-setuptools time

Provides:       pywebdav = %version-%release
Provides:       pywebdav3 = %version-%release

%description
WebDAV library for Python. WebDAV is an extension to the normal HTTP/1.1
protocol allowing the user to upload data, create collections of
objects, store properties for objects, etc.

%package -n python3-module-pywebdav
Summary:        PyWebDAV is a standards compliant WebDAV server and library written in Python3
Group:          Development/Python3

%description -n python3-module-pywebdav
WebDAV library for Python. WebDAV is an extension to the normal HTTP/1.1
protocol allowing the user to upload data, create collections of
objects, store properties for objects, etc.

This module built for Python3.

%prep
%setup -n %srcname-%version
rm -f doc/INSTALL
mkdir ../python3
cp -a * ../python3

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
export LC_ALL=en_US.UTF-8

%python_build
pushd ../python3
%python3_build
popd

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
pushd ../python3
%python3_install
rm -f %buildroot%_bindir/*
rm -rf %buildroot%python3_sitelibdir/pywebdav/server
popd

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

%files -n python3-module-pywebdav
%doc doc/*
%python3_sitelibdir/pywebdav
%python3_sitelibdir/%{srcname}*.egg-info

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.11-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sat Aug 13 2016 Andrey Cherepanov <cas@altlinux.org> 0.9.11-alt1
- New version

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.8-alt1.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.8-alt1.1.1
- NMU: Use buildreq for BR.

* Mon Oct 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1.1
- Added module for Python 3

* Wed Jan 16 2013 Andrey Cherepanov <cas@altlinux.org> 0.9.8-alt1
- Initial build in Sisyphus

