Name: showmesh
Version: 1.0
Release: alt3
Summary: Mesh visualisation tool for X Windows
License: Free for non-commertial using
Group: Sciences/Mathematics
Url: http://www-dinma.univ.trieste.it/nirftc/research/easymesh/showmesh.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://www-dinma.univ.trieste.it/nirftc/research/easymesh/showmesh_1_0.c
Source: %name-%version.tar
Source1: Makefile

BuildPreReq: libX11-devel

%description
ShowMesh is a mesh visualisation tool for X Windows.

%prep
%setup
install -p -m644 %SOURCE1 .

%build
%make_build

%install
%makeinstall_std

%files
%_bindir/*

%changelog
* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- Rebuilt for debuginfo

* Tue Jan 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Fixed using of fonts

* Mon Jan 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

