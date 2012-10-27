Name: libmatio
Version: 1.5.0
Release: alt1
Summary: Library for reading/writing Matlab MAT files

Group: Development/Other
License: LGPLv2+
Url: http://sourceforge.net/projects/matio
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: http://downloads.sourceforge.net/matio/matio-%version.tar.gz
Patch: matio-1.3.3-zlibldflag.patch
Patch1: matio-1.3.3-fortranpath.patch
Patch2: matio-1.3.3-fortranpath2.patch
Patch3: matio-1.3.3-automake.patch

BuildRequires: doxygen
BuildRequires: gcc-fortran
#According to the README - zlib 1.2.2 is possible but require a patch
BuildRequires: zlib-devel >= 1.2.3

%description
matio is an open-source library for reading/writing Matlab MAT files.  This
library is designed for use by programs/libraries that do not have access or
do not want to rely on Matlab's libmat shared library.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release
Requires: zlib-devel

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q -n matio-%version
#To fix matio.x86_64: W: undefined-non-weak-symbol /usr/lib64/libmatio.so.0.0.0 inflateEnd, etc.
#patch0 -p1 -b .zlibldflag
#patch1 -p1 -b .fortranpath
#patch2 -p1 -b .fortranpath2
#patch3 -p1 -b .automake

#Doxygen
#pushd doxygen
#  doxygen -u doxygen.config
  #Fake the pdf creation
#  mkdir -p latex
#  touch latex/refman.pdf
#popd

#Prevent some files to be missed at -debuginfo extraction
#mv src/fortran/* src

%build
export FCFLAGS=$RPM_OPT_FLAGS
./autogen.sh
%configure \
  --enable-shared \
  --disable-static \
  --enable-fortran \
  --enable-extended-sparse=yes \
  --enable-test=no \
  --enable-docs=yes

# remove rpath from libtool
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make
#Parallele make fails with
#make[2]: *** No rule to make target `../src/matio.mod', needed by `all-am'.  Stop.
#{?_smp_mflags}

%install
%makeinstall_std INSTALL="install -p"
find %buildroot -name '*.la' -exec rm -f {} ';'

#Remove pdf - really needed along with doxygen ?
rm -rf %buildroot%_docdir/matio/libmatio.pdf

#Fix html docs timestramps generation.
#for f in $(find doxygen/html -type f); do
#  touch -r doxygen/Makefile.am ${f}
#done

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%make -C test check

%files
%doc COPYING NEWS README
%_bindir/*
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Sun Oct 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1
- Version 1.5.0 (ALT #27897)

* Wed Aug 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.3-alt3
- rebuild for debuginfo

* Tue Dec 14 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.3-alt2
- rebuild for soname set-version

* Thu Jul 16 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.3-alt1
- initial
