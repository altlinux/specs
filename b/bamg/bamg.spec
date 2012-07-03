Name: bamg
Version: 0.60
Release: alt3
Summary: 2D mesh generator
License: Free for non-commertial using
Group: Sciences/Mathematics
Url: http://www.inria.fr/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://dsec.pku.edu.cn/~rli/source_code/bamg.tar.gz
Source: %name-%version.tar
Source1: http://dsec.pku.edu.cn/~rli/source_code/bamg.ps.gz

BuildPreReq: gcc-c++ gcc-fortran libX11-devel

%description
Bamg: Bidimensional Anisotrope Mesh Generator.

%package doc
Summary: Documentation for Bamg
Group: Documentation
BuildArch: noarch

%description doc
Bamg: Bidimensional Anisotrope Mesh Generator.

This package contains documentation for Bamg.

%package examples
Summary: Examples for Bamg
Group: Documentation
BuildArch: noarch
Requires: nsc2ke

%description examples
Bamg: Bidimensional Anisotrope Mesh Generator.

This package contains examples for Bamg.

%prep
%setup
install -p -m644 %SOURCE1 .

%build
%make_build HOSTTYPE=linux world

%install
%makeinstall_std HOSTTYPE=linux install-world

%files
%doc README
%_bindir/*

%files doc
%doc *.ps.gz

%files examples
%doc examples/*

%changelog
* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.60-alt3
- Rebuilt for debuginfo

* Sat Jan 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.60-alt2
- Fixed examples

* Fri Jan 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.60-alt1
- Initial build for Sisyphus

