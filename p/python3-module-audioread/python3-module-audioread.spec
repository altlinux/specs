%define modname audioread
# no tests
%def_enable check

Name: python3-module-%modname
Version: 2.1.9
Release: alt1

Summary: A python library for decode audio files
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/%modname

Vcs: https://github.com/sampsyo/audioread.git
Source: https://pypi.io/packages/source/a/%modname/%modname-%version.tar.gz

BuildArch: noarch

Requires: ffmpeg

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
%{?_enable_check:BuildRequires: python3-module-pytest python3-module-pygobject3
BuildRequires: ffmpeg libgst-plugins1.0-gir}

%description
Decode audio files using whichever backend is available.
The library currently supports:
Gstreamer via PyGObject.
MAD via the pymad bindings.
FFmpeg or Libav via its command-line interface.
The standard library wave, aifc, and sunau modules (for uncompressed audio formats).

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
py.test3

%files
%python3_sitelibdir_noarch/*
%doc README*


%changelog
* Sat Jun 25 2022 Yuri N. Sedunov <aris@altlinux.org> 2.1.9-alt1
- first build for Sisyphus



