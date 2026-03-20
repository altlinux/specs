%define _unpackaged_files_terminate_build 1

%define pypi_name pysdl3

%def_with check

Name: python3-module-%pypi_name
Version: 0.9.11b0
Release: alt1

Summary: Pure Python wrapper for SDL3
License: MIT
Group: Development/Python3
URL: https://github.com/Aermoss/PySDL3

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

Requires: libSDL3
Requires: libSDL3_image
Requires: libSDL3_ttf

%if_with check
BuildRequires: python3(aiohttp)
BuildRequires: python3(requests)
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
PySDL3 is a pure Python wrapper around the SDL3, SDL3_image, SDL3_mixer,
SDL3_ttf, SDL3_rtf, SDL3_net and SDL3_shadercross libraries. It uses the
built-in ctypes library to interface with SDL3 while providing an
understandable function definition with docstrings

%prep
%setup -n %pypi_name-%version
sed -i "s|https://github.com/Aermoss/PySDL3/blob/main/res/logo.png?raw=true|logo.png|" README.md
sed -i "s|https://github.com/Aermoss/PySDL3/blob/main/res/snippet.png?raw=true|snippet.png|" README.md

rm -rfv sdl3/bin

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE README.md res/logo.png res/snippet.png
%python3_sitelibdir/sdl3/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Mar 20 2026 Nikolay Strelkov <snk@altlinux.org> 0.9.11b0-alt1
- New version 0.9.11b0.

* Wed Feb 25 2026 Nikolay Strelkov <snk@altlinux.org> 0.9.10b0-alt1
- Initial build for Sisyphus
