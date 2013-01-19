# spec by Kogan Konstantin <kostyalamer at yandex.ru>

Name: python-module-pywm
Version: 1.0 	
Release: alt1
Summary: Module python for WindowMaker docklets
Summary(ru_RU.UTF-8): Модуль python для написания докапплетов WindowMaker
License: GPL
Group: Development/Python

URL: http://pywmdockapps.sourceforge.net/
Source: %name-%version.tar.gz
Requires: python-devel >= 2.5
# Automatically added by buildreq on Sun Aug 15 2010 (-bi)
BuildRequires: libXext-devel libXpm-devel python-devel

%description
Pywmgeneral is a Python module that will help you develope WindowMaker
dockapps in Python. It is mostly a wrapper around the functions from
the popular wmgeneral.c, but some new functions are added too.

It also contains the Python written module pywmhelpers.py which
contains functions to aid the development of WM dockapps. This module
contains Python functions that wrap up the functions which the
extension module provides. They ease up argument passing and give
nicer return values. Some additional functions, like help for handling
a simple configuration file is also available. This module is better
documented than the pywmgeneral. It is adviced to only use pywmhelpers
and not touch the pywmgeneral module directly at all. For information
about how to use the module, see the documentation in pywmhelpers.py.
It is also possible to import it in the interactive interpreter and
issue 'help(pywmhelpers)'.

%prep
%setup

%build
%python_build_debug

%install
%python_install \
	--record=INSTALLED_FILES

%files
%doc README
%python_sitelibdir/*

%changelog
* Sat Jan 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

