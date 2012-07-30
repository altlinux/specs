Name: glm
Version: 0.9.3.4
Release: alt1
License: MIT
Summary: GLM is a header only C++ mathematics library for graphics software based on the GLSL specification
Group: Development/C++
Url: http://glm.g-truc.net/
BuildArch: noarch

# http://download.sourceforge.net/ogl-math/glm-%version.zip
Source: %name-%version.tar

%package -n lib%name-devel
Summary: GLM is a header only C++ mathematics library for graphics software based on the GLSL specification
Group: Development/C++

%package -n lib%name-devel-doc
Summary: Documentation for OpenGL Mathematics (GLM) library
Group: Development/Documentation
Requires: lib%name-devel = %version-%release

%description
C++ library for OpenGL GLSL type-based mathematics OpenGL Mathematics
(GLM) is a header only C++ mathematics library for graphics software
based on the OpenGL Shading Language (GLSL) specification.

GLM provides classes and functions designed and implemented with the
same naming conventions and functionalities as GLSL, so that when a
programmer knows GLSL, he knows GLM as well, which makes it easy to use.

This project isn't limited to GLSL features. An extension system, based
on the GLSL extension conventions, provides extended capabilities:
matrix transformations, quaternions, half-based types, random nums, etc.

%description -n lib%name-devel
C++ library for OpenGL GLSL type-based mathematics OpenGL Mathematics
(GLM) is a header only C++ mathematics library for graphics software
based on the OpenGL Shading Language (GLSL) specification.

GLM provides classes and functions designed and implemented with the
same naming conventions and functionalities as GLSL, so that when a
programmer knows GLSL, he knows GLM as well, which makes it easy to use.

This project isn't limited to GLSL features. An extension system, based
on the GLSL extension conventions, provides extended capabilities:
matrix transformations, quaternions, half-based types, random nums, etc.

Header files for GLM library.

%description -n lib%name-devel-doc
Documentation for the OpenGL Mathematics (GLM) library.
OpenGL Mathematics (GLM) is a header only C++ mathematics library for
graphics software based on the OpenGL Shading Language (GLSL) specs.

This package contains the GLM in HTML and PDF formats.

%prep
%setup

%install
mkdir -p %buildroot%_includedir
cp -a glm %buildroot%_includedir
rm %buildroot%_includedir/glm/CMakeLists.txt
mkdir -p %buildroot%_docdir/lib%name-devel/
cp -a copying.txt readme.txt doc/*.pdf doc/html/ %buildroot%_docdir/lib%name-devel/

%files -n lib%name-devel
%_includedir/%name/
%dir %_docdir/lib%name-devel/
%_docdir/lib%name-devel/copying.txt
%_docdir/lib%name-devel/readme.txt

%files -n lib%name-devel-doc
%dir %_docdir/lib%name-devel/
%_docdir/lib%name-devel/*.pdf
%_docdir/lib%name-devel/html/

%changelog
* Mon Jul 30 2012 Ivan Ovcherenko <asdus@altlinux.org> 0.9.3.4-alt1
- initial build for ALT Linux Sisyphus
