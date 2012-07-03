Name: pete
Version: 2.1.0
Release: alt1
Summary: Portable Expression Template Engine
License: ACL/LANL
Group: Sciences/Mathematics
Url: http://www.nongnu.org/freepooma/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

BuildPreReq: gcc-c++

%description
Welcome to PETE, the second public release of the Portable
Expression Template Engine. In 1995, Todd Veldhuizen and David 
Vandevoorde developed the expression-template technique to 
transform arithmetic expressions involving array-like containers into 
efficient loops that rivaled hand-coded C in speed. Expression 
templates are now at the heart of highly efficient scientific 
container libraries including POOMA and Blitz++. Unfortunately, the
technique's perceived complexity and the belief that it is limited 
to evaluating array expressions have deterred many potential 
expression-template users. PETE is therefore designed to easily 
add expression-template functionality to their container classes 
and to simply perform complex expression manipulations.

%package -n lib%name-devel
Summary: Headers of Portable Expression Template Engine (PETE)
Group: Development/C++
Requires: %name = %version-%release

%description -n lib%name-devel
Headers of Portable Expression Template Engine (PETE).

%package -n lib%name-devel-doc
Summary: Documentation for Expression Template Engine (PETE)
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
Documentation for Expression Template Engine (PETE).

%prep
%setup

%build
export PETEARCH=LINUXEGCS
%make_build

%install
export PETEDIR=%buildroot
export PETEARCH=LINUXEGCS
%make install

install -d %buildroot%_bindir
install -d %buildroot%_includedir/%name
install -d %buildroot%_docdir/%name

mv %buildroot/linux/bin/* %buildroot%_bindir/
mv %buildroot/src/PETE/* %buildroot%_includedir/%name/
mv %buildroot/html/* %buildroot%_docdir/%name/

%files
%doc CREDITS LICENSE README
%_bindir/*

%files -n lib%name-devel
%_includedir/*

%files -n lib%name-devel-doc
%_docdir/%name

%changelog
* Sun May 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus
