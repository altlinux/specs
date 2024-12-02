%define pypi_name imageio-ffmpeg
%define mod_name imageio_ffmpeg

%def_with check

Name: python3-module-%pypi_name
Version: 0.5.1
Release: alt1

Summary: FFMPEG wrapper for Python

License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/imageio-ffmpeg
Vcs: https://github.com/imageio/imageio-ffmpeg

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-psutil
%endif

Requires: ffmpeg

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# Tests that require an Internet connection are excluded
%pyproject_run_pytest \
    --ignore 'tests/test_io.py' \
    --ignore 'tests/test_special.py' \
    --ignore 'tests/test_terminate.py'

%files
%doc LICENSE *.md
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Tue Nov 26 2024 Alexander Kovalev <alexvk@altlinux.org> 0.5.1-alt1
- Initial build for ALT.
