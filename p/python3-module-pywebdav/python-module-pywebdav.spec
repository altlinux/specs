%define srcname PyWebDAV3

Name:       python3-module-pywebdav
Version:    0.9.11
Release:    alt2
Summary:    PyWebDAV is a standards compliant WebDAV server and library written in Python

Group:      Development/Python3
License:    LGPLv2+
URL:        https://github.com/andrewleech/PyWebDAV3
Source0:    %srcname-%version.tar

BuildArch:  noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3 python3-module-six

Provides: pywebdav = %version-%release
Provides: pywebdav3 = %version-%release


%description
WebDAV library for Python. WebDAV is an extension to the normal HTTP/1.1
protocol allowing the user to upload data, create collections of
objects, store properties for objects, etc.

%prep
%setup -n %srcname-%version

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
export LC_ALL=en_US.UTF-8

%python3_build

%install
export LC_ALL=en_US.UTF-8

%python3_install
rm -f %buildroot%_bindir/*
rm -rf %buildroot%python3_sitelibdir/pywebdav/server

%check
%__python3 setup.py test

%files
%doc doc/*
%python3_sitelibdir/pywebdav
%python3_sitelibdir/%{srcname}*.egg-info


%changelog
* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.9.11-alt2
- Build for python2 disabled.

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

