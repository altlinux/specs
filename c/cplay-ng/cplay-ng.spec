Name: cplay-ng
Version: 3.0.0
Release: alt1

Summary: A curses front-end for various audio players
License: GPLv2+
Group: Sound
Url: https://pypi.python.org/pypi/cplay-ng/
BuildArch: noarch

# https://github.com/xi/cplay-ng.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-modules-curses python3-module-nose


%description
cplay-ng is a curses front-end for various audio players. It aims to
provide a power-user-friendly interface with simple filelist and
playlist control. cplay-ng is written in Python and can use either
pyncurses or the standard curses module.

The original cplay is no longer maintained. This fork aims to
maintaining the original code as well as keeping it up to date with
recent developments (e.g. python3) and adding new features.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
nosetests3 -v

%files
%doc AUTHORS ChangeLog README.rst LICENSE
%_bindir/*
%python3_sitelibdir/*


%changelog
* Mon Feb 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.0.0-alt1
- Version updated to 3.0.0
- porting to python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.3-alt1.git20150320.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Mar 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt1.git20150320
- Initial build for Sisyphus

