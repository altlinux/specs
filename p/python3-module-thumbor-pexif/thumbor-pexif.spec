%define oname thumbor-pexif

Name: python3-module-%oname
Version: 0.14.1
Release: alt3

Summary: A module for editing JPEG EXIF data
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/thumbor-pexif/
BuildArch: noarch

# https://github.com/thumbor/pexif.git
Source: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3
BuildRequires: python3-module-nose

%py3_provides pexif


%description
This module allows you to parse and edit the EXIF data tags in a JPEG
image.

%prep
%setup
%patch0 -p1

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%if 0
nosetests3
%endif

%files
%doc README examples
%_bindir/*
%python3_sitelibdir/*


%changelog
* Wed Jan 15 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.14.1-alt3
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.14.1-alt2.git20141001.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.1-alt2.git20141001
- Fixed build

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.1-alt1.git20141001
- Initial build for Sisyphus

