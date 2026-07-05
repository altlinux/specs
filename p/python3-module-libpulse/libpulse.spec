%define pypi_name libpulse

%def_with check
%def_with docs

Name: python3-module-%pypi_name
Version: 0.7.1
Release: alt1

Summary: Asyncio interface to the Pulseaudio and Pipewire pulse library

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/libpulse
VCS: https://gitlab.com/xdegaye/libpulse.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-flit-core
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: libpulseaudio
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx_rtd_theme
%endif

%description
Asyncio interface to the Pulseaudio and Pipewire pulse library.

libpulse is a Python project based on asyncio, that uses ctypes to
interface with the pulse library of the PulseAudio and PipeWire sound
servers. The interface is meant to be complete. That is, all the constants,
structures, plain functions and async functions are made available by importing
the libpulse module of the libpulse package.

%package tests
Summary: Tests for %pypi_name
Group: Development/Python3
Requires: %name = %version-%release

%description tests
Asyncio interface to the Pulseaudio and Pipewire pulse library.

libpulse is a Python project based on asyncio, that uses ctypes to
interface with the pulse library of the PulseAudio and PipeWire sound
servers. The interface is meant to be complete. That is, all the constants,
structures, plain functions and async functions are made available by importing
the libpulse module of the libpulse package.

This package contains tests for %pypi_name.

%package docs
Summary: Documentation for %pypi_name
Group: Development/Documentation

%description docs
Asyncio interface to the Pulseaudio and Pipewire pulse library.

libpulse is a Python project based on asyncio, that uses ctypes to
interface with the pulse library of the PulseAudio and PipeWire sound
servers. The interface is meant to be complete. That is, all the constants,
structures, plain functions and async functions are made available by importing
the libpulse module of the libpulse package.

This package contains documentation for %pypi_name.

%prep
%setup

%build
%pyproject_build

%if_with docs
%make -C docs html

# remove the sphinx-build leftovers
rm -rv docs/build/html/{.buildinfo,objects.inv}
%endif

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE *.rst examples
%_bindir/pactl-py
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/%pypi_name/tests

%files tests
%python3_sitelibdir/%pypi_name/tests

%if_with docs
%files docs
%doc docs/build/html
%endif

%changelog
* Sun Jul 05 2026 Alexander Kovalev <alexvk@altlinux.org> 0.7.1-alt1
- New version 0.7.1.

* Sat Mar 29 2025 Alexander Kovalev <alexvk@altlinux.org> 0.7-alt1
- New version 0.7.

* Fri Dec 06 2024 Alexander Kovalev <alexvk@altlinux.org> 0.6-alt1
- Initial build for ALT.
