Name: cplay-ng
Version: 5.2.0
Release: alt1

Summary: A simple curses audio player
License: GPL-2.0
Group: Sound
Url: https://pypi.org/project/cplay-ng/
Vcs: https://github.com/xi/cplay-ng.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

Requires: mpv

%description
cplay is a minimalist music player with a textual user interface written
in Python. It aims to provide a power-user-friendly interface with simple
filelist and playlist control.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc AUTHORS ChangeLog README.rst LICENSE
%_bindir/*
%python3_sitelibdir/*


%changelog
* Sat Apr 01 2023 Anton Vyatkin <toni@altlinux.org> 5.2.0-alt1
- (NMU) New version 5.2.0.

* Mon Feb 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.0.0-alt1
- Version updated to 3.0.0
- porting to python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.3-alt1.git20150320.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Mar 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt1.git20150320
- Initial build for Sisyphus

