%define oname pywebdav

%def_without check

Name:       python3-module-%oname
Version:    0.10.0
Release:    alt1
Summary:    PyWebDAV is a standards compliant WebDAV server and library written in Python

Group:      Development/Python3
License:    LGPLv2
URL:        https://github.com/andrewleech/PyWebDAV3
Source:     %name-%version.tar

BuildArch:  noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pip
BuildRequires: python3-module-wheel
BuildRequires: python3-module-six

%description
WebDAV library for Python. WebDAV is an extension to the normal HTTP/1.1
protocol allowing the user to upload data, create collections of
objects, store properties for objects, etc.

%prep
%setup
# Upstream has problem with versioning
sed -i "s/__version__ = '0.9.14'/__version__ = '%version'/" pywebdav/__init__.py
# get rid of git-versioner
sed -i '/setup_requires/d' setup.py

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=$PWD
python3 test/test_litmus.py

%files
%doc doc/*
%_bindir/davserver
%python3_sitelibdir/%oname
%python3_sitelibdir/PyWebDAV3-%version-py%_python3_version.egg-info


%changelog
* Tue Feb 21 2023 Anton Vyatkin <toni@altlinux.org> 0.10.0-alt1
- new version 0.10.0.

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

