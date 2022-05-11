%define modname ExifRead
%define _modname exifread

%def_disable check

Name: python3-module-%_modname
Version: 3.0.0
Release: alt1

Summary: Python3 library to extract Exif metadata
Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.org/project/%modname

Vcs: https://github.com/ianare/exif-py
Source: https://pypi.io/packages/source/E/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
%{?_enable_check:BuildRequires: python3-module-pytest}

%description
Easy to use Python3 module to extract Exif metadata from digital image files.
Supported formats: TIFF, JPEG, PNG, Webp, HEIC.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%check
py.test3

%files
%_bindir/EXIF.py
%python3_sitelibdir_noarch/%_modname/
%python3_sitelibdir_noarch/%modname-*.egg-info/
%doc README* ChangeLog*


%changelog
* Wed May 11 2022 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Wed Jan 05 2022 Yuri N. Sedunov <aris@altlinux.org> 2.3.2-alt1
- first build for Sisyphus




