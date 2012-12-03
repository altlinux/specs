# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%define oname quazip
Name:		lib%oname
Version:	0.5
Release:	alt1_1.2
Summary:	Qt/C++ wrapper for the minizip library
License:	GPLv2+ or LGPLv2+
Group:		System/Libraries
URL:		http://quazip.sourceforge.net/
Source0:	%name-%version.tar
BuildRequires:	libqt4-devel
BuildRequires:	doxygen graphviz
Source44: import.info

%description
QuaZIP is a simple C++ wrapper over Gilles Vollant's ZIP/UNZIP package that
can be used to access ZIP archives. It uses Trolltech's Qt toolkit.

QuaZIP allows you to access files inside ZIP archives using QIODevice API,
and - yes! - that means that you can also use QTextStream, QDataStream or
whatever you would like to use on your zipped files.

QuaZIP provides complete abstraction of the ZIP/UNZIP API, for both reading
from and writing to ZIP archives.

%package devel
Summary:		Development files for %oname
Group:			Development/C
Requires:		%name%{?_isa} = %version-%release
Requires:		libqt4-devel%{?_isa}

%description devel
The %name-devel package contains libraries, header files and documentation
for developing applications that use %oname. 

%prep
%setup -q

# Fixes build and install
sed -i 's\PREFIX/lib\PREFIX/%_lib\' %oname/%oname.pro

%build
export PATH=%_qt4_bindir:$PATH
qmake-qt4 \
	PREFIX=%_prefix \
	-after QMAKE_CXXFLAGS+="%optflags" \
	-after QMAKE_CFLAGS+="%optflags"
#do not build in parallel - there are race conditions in 
#qmake-generated makefiles
%make V=1

doxygen Doxyfile
for file in doc/html/*; do
	touch -r Doxyfile $file
done

%install
%make INSTALL="install -p" INSTALL_ROOT=%buildroot install

%files
%doc COPYING NEWS.txt README.txt
%_libdir/*.so.*

%files devel
%doc doc/html
%_includedir/%oname
%_libdir/*.so

%changelog
* Mon Dec 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1_1.2
- Rebuilt with optflags

* Mon Dec 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1_1.1
- Built for Sisyphus

* Sat Dec 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_1
- converted for ALT Linux by srpmconvert tools

