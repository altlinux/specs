%def_disable snapshot
%define pypi_name audioread
%def_disable check

Name: python3-module-%pypi_name
Version: 3.1.0
Release: alt1

Summary: Cross-platform audio decoding python library
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/%pypi_name

Vcs: https://github.com/sampsyo/audioread.git

%if_disabled snapshot
Source: https://pypi.io/packages/source/a/%pypi_name/%pypi_name-%version.tar.gz
%else
Source: %pypi_name-%version.tar
%endif

BuildArch: noarch

Requires: ffmpeg

BuildRequires(pre): rpm-build-python3
BuildRequires:  python3(wheel) python3(poetry-core)
%{?_enable_check:BuildRequires: python3(tox) python3(pytest) python3(mad)
BuildRequires: python3-module-pygobject3 ffmpeg libgst-plugins1.0-gir
# for python >= 3.13
BuildRequires: python3(aifc) python3(sunau)}

%description
Decode audio files using whichever backend is available.
The library currently supports:
Gstreamer via PyGObject.
MAD via the pymad bindings.
FFmpeg or Libav via its command-line interface.
The standard library wave, aifc, and sunau modules (for uncompressed audio formats).

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check

%files
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README*


%changelog
* Mon Oct 27 2025 Yuri N. Sedunov <aris@altlinux.org> 3.1.0-alt1
- 3.1.0

* Thu Dec 26 2024 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt0.2
- prepared for python-3.13 (fc patch) (ALT #52544)

* Mon Aug 15 2022 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt0.1
- updated to v3.0.0-7-gb694c4f
- ported to %%pyproject*/%%tox* macros

* Sat Jun 25 2022 Yuri N. Sedunov <aris@altlinux.org> 2.1.9-alt1
- first build for Sisyphus



