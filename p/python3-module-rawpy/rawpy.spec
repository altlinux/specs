%define pypi_name rawpy

%ifarch %ix86
%def_without docs
%else
%def_with docs
%endif

Name: python3-module-%pypi_name
Version: 0.23.2
Release: alt1

Summary: RAW image processing for Python, a wrapper for libraw

License: MIT and LGPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/rawpy
Vcs: https://github.com/letmaik/rawpy

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-numpy
BuildRequires: python3-module-Cython
BuildRequires: libraw-devel gcc-c++
BuildRequires: libnumpy-py3-devel
BuildRequires: libgomp14-devel

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx_rtd_theme
BuildRequires: python3-module-opencv
%endif

%description
rawpy is an easy-to-use Python wrapper for the LibRaw library.
It also contains some extra functionality for finding and
repairing hot/dead pixels.

%package docs
Summary: Documentation for %pypi_name
Group: Development/Documentation

%description docs
rawpy is an easy-to-use Python wrapper for the LibRaw library.
It also contains some extra functionality for finding and
repairing hot/dead pixels.

This package contains documentation for %pypi_name.

%package pickles
Summary: Pickles for %pypi_name
Group: Development/Python3

%description pickles
rawpy is an easy-to-use Python wrapper for the LibRaw library.
It also contains some extra functionality for finding and
repairing hot/dead pixels.

This package contains pickles for %pypi_name.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%if_with docs
export PYTHONPATH=%buildroot%python3_sitelibdir
sphinx-build-3 -b html docs build/html
sphinx-build-3 -b pickle docs build/pickle
sphinx-build-3 -b man docs build/man

# remove the sphinx-build leftovers
rm -rv build/html/{.doctrees,.buildinfo,objects.inv}
rm -rv build/pickle/{.doctrees,.buildinfo,objects.inv}

install -d %buildroot%python3_sitelibdir/%pypi_name
cp -fR build/pickle %buildroot%python3_sitelibdir/%pypi_name
mkdir -p %buildroot%_man1dir
install -m0644 build/man/%pypi_name.1 %buildroot%_man1dir
%endif

%files
%doc LICENSE *.md
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%if_with docs
%_man1dir/*
%exclude %python3_sitelibdir/%pypi_name/pickle

%files docs
%doc build/html

%files pickles
%dir %python3_sitelibdir/%pypi_name
%python3_sitelibdir/%pypi_name/pickle
%endif

%changelog
* Fri Dec 06 2024 Alexander Kovalev <alexvk@altlinux.org> 0.23.2-alt1
- Initial build for ALT.
