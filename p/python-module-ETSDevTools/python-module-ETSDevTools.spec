%define oname ETSDevTools

%def_without python3

Name: python-module-%oname
Version: 4.0.1
Release: alt1.git20120221
Summary: Enthought tools to support Python development

Group: Development/Python
License: BSD and GPLv2
URL: http://www.enthought.com/
# https://github.com/enthought/etsdevtools.git
Source: %oname-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

#Requires: python-module-TraitsBackendWX

BuildArch: noarch
BuildPreReq: python-devel, python-module-setuptools
BuildPreReq: python-module-setupdocs libnumpy-devel gcc-c++
BuildPreReq: libX11-devel libXt-devel libXtst-devel libXext-devel
BuildPreReq: xorg-xextproto-devel xorg-inputproto-devel
BuildPreReq: python-module-xlib swig libXi-devel
BuildPreReq: python-module-sphinx python-module-Pygments
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setupdocs
BuildPreReq: libnumpy-py3-devel python-tools-2to3
%endif

%description
The ETSDevTools project includes a set of packages that can be used during the
development of a software project, for understanding, debugging, testing, and
inspecting code.

%if_with python3
%package -n python3-module-%oname
Summary: Enthought tools to support Python 3 development
Group: Development/Python3

%description -n python3-module-%oname
The ETSDevTools project includes a set of packages that can be used during the
development of a software project, for understanding, debugging, testing, and
inspecting code.
%endif

%package doc
Summary: Documentation for Enthought tools to support Python development
Group: Development/Documentation
BuildArch: noarch

%description doc
The ETSDevTools project includes a set of packages that can be used during the
development of a software project, for understanding, debugging, testing, and
inspecting code.

This package contains documentation for ETSDevTools.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
done
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i py3_$i
done
popd
%endif
%python_install -O1

#cp -fR examples/* %buildroot%python_sitelibdir/enthought/

%files
%doc *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/py3_*
%endif
%python_sitelibdir/*/*
%exclude %python_sitelibdir/etsdevtools/developer/vet_plugin_definition.py*

%files doc
%doc examples docs/developer docs/testing docs/endo

%if_with python3
%files -n python3-module-%oname
%_bindir/py3_*
%python3_sitelibdir/*/*
%exclude %python3_sitelibdir/etsdevtools/developer/vet_plugin_definition.py*
%endif

%changelog
* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.git20120221
- New snapshot

* Wed Nov 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.git20110621
- Version 4.0.1

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.2-alt1.svn20110127.2
- Rebuild with Python-2.7
* Mon Oct 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt1.svn20110127.1
- Rebuilt with updated NumPy

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt1.svn20110127
- Version 3.1.2

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1.svn20101101.1
- Rebuilt with NumPy 2.0.0-alt1.svn20100607.7

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1.svn20101101
- Version 3.1.1

* Mon Apr 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.5-alt1.svn20100225.1
- Fixed build

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.5-alt1.svn20100225
- Version 3.0.5

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.4-alt1.svn20090812.2
- Rebuilt with python 2.6

* Sat Oct 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.4-alt1.svn20090812.1
- Extracted documentation into separate package

* Thu Oct 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.4-alt1.svn20090812
- Initial build for Sisyphus

