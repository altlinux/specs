%define _unpackaged_files_terminate_build 1

%define oname imageio

Name: python3-module-%oname
Version: 2.9.0
Release: alt1
Summary: Python library for reading and writing image data
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/imageio/

BuildArch: noarch

# https://github.com/imageio/imageio.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-Pillow
BuildRequires: libnumpy-py3-devel

%description
Imageio is a Python library that provides an easy interface
to read and write a wide range of image data,
including animated images, video, volumetric data,
and scientific formats.
It is cross-platform, runs on Python 2.7 and 3.4+, and is easy to install.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc LICENSE
%doc README.md CHANGELOG.md CONTRIBUTORS.txt
%_bindir/*
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-*.egg-info

%changelog
* Thu Aug 13 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.9.0-alt1
- Updated to upstream version 2.9.0.

* Tue Apr 09 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2.5.0-alt1
- Initial build for ALT.
