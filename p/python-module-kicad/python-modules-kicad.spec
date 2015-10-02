%define rev	e565781f
%define modulename kicad

Name: python-module-%modulename
Version: 0.0
Release: alt1.%rev.1

%setup_python_module %modulename

Summary: Development of a new Python scripting API for KiCad
License: GPLv2+
Group: Development/Python

Url: https://github.com/KiCad/kicad-python
Packager: Anton Midyukov <antohami@altlinux.org>
BuildArch: noarch

Source: python-module-kicad-%version.tar
#git clone https://github.com/KiCad/kicad-python.git

#BuildPreReq: %py_dependencies setuptools
BuildRequires: python-module-setuptools

%description
Development of a new Python scripting API for KiCad based on Piers Titus van
der Torren work and comunity feedback to create a less C++ tied API.

A second intention of this new API is also to provide better documentation via
sphinx.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Fri Oct 02 2015 Anton Midyukov <antohami@altlinux.org> 0.0-alt1.e565781f.1
- Initial build for Alt Linux Sisyphus.
