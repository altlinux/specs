%define oname pydot

%def_with python3

Name: python-module-%oname
Version: 1.0.29
Release: alt1.git20140730.1

Summary: Python interface to Graphiz's Dot

License: MIT
Group: Development/Python
Url: http://pydot.googlecode.com

Source: %oname-%version.tar.bz2

BuildArch: noarch

%setup_python_module %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-devel python-module-pyparsing python3-module-pyparsing rpm-build-python3

#BuildPreReq: python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python3-module-pyparsing
#BuildPreReq: python3-module-setuptools-tests
%endif

Requires: %_bindir/dot

%description
An interface for creating both directed and non directed graphs from
Python. Currently all attributes implemented in the Dot language are
supported (up to Graphviz 1.16).

Output can be inlined in Postscript into interactive scientific
environments like TeXmacs, or output in any of the format's supported
by the Graphviz tools dot, neato, twopi.

%package -n python3-module-%oname
Summary: Python interface to Graphiz's Dot
Group: Development/Python3
Requires: %_bindir/dot

%description -n python3-module-%oname
An interface for creating both directed and non directed graphs from
Python. Currently all attributes implemented in the Dot language are
supported (up to Graphviz 1.16).

Output can be inlined in Postscript into interactive scientific
environments like TeXmacs, or output in any of the format's supported
by the Graphviz tools dot, neato, twopi.

%prep
%setup -n %oname-%version

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc ChangeLog README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog README
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.29-alt1.git20140730.1
- NMU: Use buildreq for BR.

* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.29-alt1.git20140730
- Version 1.0.29

* Thu May 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.28-alt1
- Version 1.0.28

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt1.1.1
- Rebuild with Python-2.7

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.1
- Rebuilt with python 2.6

* Thu Jun 19 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- new version 1.0.2 (with rpmrb script)

* Sun Sep 16 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.10-alt1
- initial build for ALT Linux Sisyphus
