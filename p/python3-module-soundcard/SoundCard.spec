%define nameD soundcard

Name: python3-module-%nameD
Version: 0.4.3
Release: alt1

Summary: A Pure-Python Real-Time Audio Library
License: BSD-3-Clause
Group: Development/Python3

Url: https://pypi.org/project/SoundCard/
Vcs: https://github.com/bastibe/SoundCard

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%add_python3_path %python3_sitelibdir/%nameD/

BuildArch: noarch

Source: %name-%version.tar

%description
SoundCard is a library for playing and recording audio without resorting to a 
CPython extension. Instead, it is implemented using the wonderful CFFI and 
the native audio libraries of Linux, Windows and macOS.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install


%files
%doc LICENSE README.rst
%python3_sitelibdir/%nameD/
%python3_sitelibdir/SoundCard-%version.dist-info/

%changelog
* Fri Jan 24 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.3-alt1
- Initial build for Sisyphus
