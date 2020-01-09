%define oname pexif

Name: python3-module-%oname
Version: 0.15
Release: alt2

Summary: A module for editing JPEG EXIF data
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pexif/
BuildArch: noarch

# https://github.com/bennoleslie/pexif.git
Source: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_provides %oname
Conflicts: python3-module-thumbor-%oname


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
export PYTHONPATH=$PWD
%__python3 test/test.py -v
%endif

%files
%doc *.md examples
%_bindir/*
%python3_sitelibdir/*


%changelog
* Thu Jan 09 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.15-alt2
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.15-alt1.git20150205.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Mar 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15-alt1.git20150205
- Initial build for Sisyphus

