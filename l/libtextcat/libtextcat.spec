Name: libtextcat
Version: 2.2
Release: alt4

Summary: Text categorisation library
License: BSD
Group: Development/Other

URL: http://software.wise-guys.nl/libtextcat/
Source: http://software.wise-guys.nl/download/libtextcat-%version.tar.gz

%description
Libtextcat is a library with functions that implement the classification
technique described in Cavnar & Trenkle, "N-Gram-Based Text Categorization".
It was primarily developed for language guessing, a task on which it is known
to perform with near-perfect accuracy.

%package devel
Summary: Support files necessary to compile applications with libtextcat
Group: Development/C
Requires: libtextcat = %version-%release

%description devel
Libraries, headers, and support files necessary to compile applications using
libtextcat.

%prep
%setup

%build
subst 's@"conf.txt"@"%_datadir/libtextcat/conf.txt"@' src/testtextcat.c
subst 's@LM@%_datadir/libtextcat/LM@' langclass/conf.txt
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

# make install forgot about header file :\
install -pD -m644 src/textcat.h %buildroot%_includedir/textcat.h
# we also want to have testtextcat installed
install -m755 src/.libs/testtextcat %buildroot%_bindir/textcat

mkdir -p %buildroot%_datadir/libtextcat/LM
cd langclass
cp -R LM %buildroot%_datadir/libtextcat/
cp -a conf.txt %buildroot%_datadir/libtextcat/

%files
%_libdir/*.so.*
%_datadir/*

%files devel
%doc README
%_bindir/*
%_libdir/*.so
%_includedir/*

%changelog
* Thu Jan 27 2011 Victor Forsiuk <force@altlinux.org> 2.2-alt4
- Rebuilt for soname set-versions.

* Wed Nov 18 2009 Victor Forsyuk <force@altlinux.org> 2.2-alt3
- Fix testtextcat to find installed conf.txt.
- Package testtextcat as textcat.
- Sample texts does not needed to be installed, drop it.
- Remove excessive path element from language data location. Fixes ALT #20722.

* Wed Jul 08 2009 Victor Forsyuk <force@altlinux.org> 2.2-alt2
- Split devel subpackage.

* Tue Apr 05 2005 Victor Forsyuk <force@altlinux.ru> 2.2-alt1
- In fact license is BSD.
- Package shared libraries instead of static.

* Sun Jul 13 2003 Ott Alex <ott@altlinux.ru> 2.1-alt1
- Initial build for ALTLinux
