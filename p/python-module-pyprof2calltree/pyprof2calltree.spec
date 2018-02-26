%define oname pyprof2calltree
Name: python-module-%oname
Version: 1.1.0
Release: alt1.1
Summary: Help visualize profiling data from cProfile with kcachegrind
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyprof2calltree/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%description
Script to help visualize profiling data collected with the cProfile
python module with the kcachegrind (screenshots) graphical calltree
analyser.

This is a rebranding of the venerable
http://www.gnome.org/~johan/lsprofcalltree.py script by David Allouche
et Al. It aims at making it easier to distribute (e.g. through pypi) and
behave more like the scripts of the debian kcachegrind-converters
package. The final goal is to make it part of the official upstream
kdesdk package.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%_bindir/*
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

