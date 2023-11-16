%define _unpackaged_files_terminate_build 1

%define oname imageio

Name: python3-module-%oname
Version: 2.31.4
Release: alt1
Summary: Python library for reading and writing image data
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/imageio/
VCS: https://github.com/imageio/imageio.git

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-Pillow
BuildRequires: libnumpy-py3-devel
BuildRequires: python3-module-wheel
# currently unwanted extra dependency
%add_python3_req_skip imageio_ffmpeg

%description
Imageio is a Python library that provides an easy interface
to read and write a wide range of image data,
including animated images, video, volumetric data,
and scientific formats.
It is cross-platform, runs on Python 3.8+, and is easy to install.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE
%doc README.md CHANGELOG.md CONTRIBUTORS.txt
%_bindir/*
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Tue Oct 17 2023 Elizaveta Morozova <morozovaes@altlinux.org> 2.31.4-alt1
- Updated version to 2.31.4.
- Migrated to pyproject.

* Thu Aug 13 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.9.0-alt1
- Updated to upstream version 2.9.0.

* Tue Apr 09 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2.5.0-alt1
- Initial build for ALT.
