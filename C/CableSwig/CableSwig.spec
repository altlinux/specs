Name: CableSwig
Version: 3.20.0
Release: alt1
License: BSD
Summary: CableSwig is used to create interfaces (i.e. "wrappers") to interpreted languages such as Tcl and Python
Group: Development/Tools
Url: http://www.itk.org/ITK/resources/CableSwig.html
Source0: %name-ITK-%version.tar.gz

# Automatically added by buildreq on Mon Apr 18 2011
# optimized out: cmake cmake-modules gcc-c++ libstdc++-devel
BuildRequires: ccmake ctest gccxml

%description
It was created to produce wrappers for ITK because the toolkit uses C++ structures that SWIG cannot parse 
(deeply nested template instantiations). CableSwig is a combination tool that uses  GCC_XML as the c++ parser. 
The input files are  Cable style input files. The XML produced from the Cable/GCC_XML input files are then 
parsed and feed into a modified version of  SWIG. SWIG is a software development tool that connects programs 
written in C and C++ with a variety of high-level programming languages. It is used to generate the 
language bindings to the target language.

%prep
%setup

%build
%cmake \
	-DSWIG_BUILD_EXAMPLES:BOOL=OFF \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DBUILD_TESTING:BOOL=OFF \
	-DCMAKE_BUILD_TYPE:STRING=RELEASE \
	-DBUILD_DOXYGEN:BOOL=OFF \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DCSWIG_USE_SYSTEM_GCCXML:BOOL=ON

%make -C BUILD

%install
%make install DESTDIR=%buildroot -C BUILD


%files
%doc SWIG/ANNOUNCE SWIG/CHANGES SWIG/CHANGES.current SWIG/FUTURE SWIG/LICENSE SWIG/README SWIG/SWIG-NEW SWIG/TODO
%_bindir/*
/usr/lib/CableSwig


%changelog
* Mon Apr 18 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 3.20.0-alt1
- Build for ALT
