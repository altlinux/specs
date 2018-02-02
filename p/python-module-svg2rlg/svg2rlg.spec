%define oname svg2rlg

%def_without python3

Name: python-module-%oname
Version: 0.3
Release: alt2.svn20110403.1
Summary: Convert SVG to Reportlab drawing
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/svg2rlg/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svg2rlg.googlecode.com/svn/trunk/
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-Reportlab python-module-wx
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-Reportlab
BuildRequires: python3-module-pytest
%endif

%py_provides %oname

%description
svg2rlg is a python tool to convert SVG files to reportlab graphics.

The tool can be used as a console application to convert SVG to PDF
files.

%if_with python3
%package -n python3-module-%oname
Summary: Convert SVG to Reportlab drawing
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
svg2rlg is a python tool to convert SVG files to reportlab graphics.

The tool can be used as a console application to convert SVG to PDF
files.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install
install -d %buildroot%_bindir
ln -s %python_sitelibdir/%oname.py %buildroot%_bindir/%oname

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
py.test
%if_with python3
pushd ../python3
py.test-%_python3_version
popd
%endif

%files
%doc *.txt
%_bindir/*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3-alt2.svn20110403.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2.svn20110403
- Fixed build

* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.svn20110403
- Initial build for Sisyphus

