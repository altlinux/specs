Name: cplay-ng
Version: 2.0.3
Release: alt1.git20150320.1
Summary: A curses front-end for various audio players
License: GPLv2+
Group: Sound
Url: https://pypi.python.org/pypi/cplay-ng/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/xi/cplay-ng.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools python-modules-curses
BuildPreReq: python-module-babel python-module-libmagic
BuildPreReq: python-module-alsaaudio python-module-mutagen
BuildPreReq: python-module-nose python-module-coverage
BuildPreReq: python-modules-logging

%py_provides cplay
Requires: python-module-libmagic
%py_requires curses alsaaudio mutagen logging

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
%python_build_debug

%install
%python_install

install -d %buildroot%_man1dir
install -p -m644 *.1 %buildroot%_man1dir/

%check
python setup.py test
nosetests -v

%files
%doc AUTHORS ChangeLog TODO *.rst *.list
%_bindir/*
%python_sitelibdir/*
%_man1dir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.3-alt1.git20150320.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Mar 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt1.git20150320
- Initial build for Sisyphus

