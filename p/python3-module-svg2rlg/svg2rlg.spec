%define oname svg2rlg

# no wx for python3
%def_without check

Name: python3-module-%oname
Version: 0.3
Release: alt3

Summary: Convert SVG to Reportlab drawing
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/svg2rlg/

BuildArch: noarch

# http://svg2rlg.googlecode.com/svn/trunk/
Source: %name-%version.tar
Patch0: port-to-python3.patch

BuildRequires(pre): rpm-build-python3


%description
svg2rlg is a python tool to convert SVG files to reportlab graphics.

The tool can be used as a console application to convert SVG to PDF
files.

%prep
%setup
%patch0 -p1

%build
%python3_build_debug

%install
%python3_install

install -d %buildroot%_bindir
ln -s %python3_sitelibdir/%oname.py %buildroot%_bindir/%oname

%check
py.test-%_python3_version

%files
%doc *.txt
%_bindir/*
%python3_sitelibdir/*


%changelog
* Fri Mar 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.3-alt3
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3-alt2.svn20110403.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2.svn20110403
- Fixed build

* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.svn20110403
- Initial build for Sisyphus

