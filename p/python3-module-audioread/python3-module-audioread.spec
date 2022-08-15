%def_enable snapshot
%define pypi_name audioread
%def_enable check

Name: python3-module-%pypi_name
Version: 3.0.1
Release: alt0.1

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
BuildRequires: python3-module-flit python3-module-wheel
%{?_enable_check:BuildRequires: python3-module-tox python3-module-pytest
BuildRequires: python3-module-pygobject3 ffmpeg libgst-plugins1.0-gir}

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
* Mon Aug 15 2022 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt0.1
- updated to v3.0.0-7-gb694c4f
- ported to %%pyproject*/%%tox* macros

* Sat Jun 25 2022 Yuri N. Sedunov <aris@altlinux.org> 2.1.9-alt1
- first build for Sisyphus



