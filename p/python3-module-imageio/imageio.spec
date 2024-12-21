%define _unpackaged_files_terminate_build 1

%define oname imageio

Name: python3-module-%oname
Version: 2.36.1
Release: alt1
Summary: Python library for reading and writing image data
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/imageio/
VCS: https://github.com/imageio/imageio.git

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
Imageio is a mature Python library that makes it easy
to read and write image and video data.
This includes animated images, video, volumetric data,
and scientific formats.
It is cross-platform, runs on Python 3.9+, and is easy to install.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE
%doc README.md CHANGELOG.md CONTRIBUTORS.txt
%_bindir/%{oname}_download_bin
%_bindir/%{oname}_remove_bin
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Mon Dec 16 2024 Alexander Kovalev <alexvk@altlinux.org> 2.36.1-alt1
- Updated version to 2.36.1.
- Fixed build requires.

* Tue Oct 17 2023 Elizaveta Morozova <morozovaes@altlinux.org> 2.31.4-alt1
- Updated version to 2.31.4.
- Migrated to pyproject.

* Thu Aug 13 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.9.0-alt1
- Updated to upstream version 2.9.0.

* Tue Apr 09 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2.5.0-alt1
- Initial build for ALT.
