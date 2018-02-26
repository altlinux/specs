Name: libnewmat
Version: 11beta
Release: alt4
Summary: Newmat C++ matrix library

Group: System/Libraries
License: Public Use
Url: http://www.robertnz.net/nm_intro.htm
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.robertnz.net/ftp/newmat11.tar.gz
Source1: http://people.mech.kuleuven.be/~tdelaet/Makefile.Newmat
Source2: http://people.mech.kuleuven.be/~tdelaet/include.h.newmat11
Patch: newmat-11-beta-alt-version.patch

BuildPreReq: gcc-c++

%description
This C++ library is intended for scientists and engineers who need to
manipulate a variety of types of matrices using standard matrix
operations. Emphasis is on the kind of operations needed in statistical
 calculations such as least squares, linear equation solve and
eigenvalues.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
install -p -m644 %SOURCE1 .
install -p -m644 %SOURCE2 .
%patch -p0
%setup -n newmat
mv ../Makefile.Newmat Makefile
mv -f ../include.h.newmat11 include.h

%build
echo 'libnewmat.so.11.0:   $(newmat_lobj)' >> nm_gnu.mak
echo '	$(CXX) $(LDFLAGS) -shared -Wl,-soname,libnewmat.so.11 -o $@ $^' >> \
	nm_gnu.mak

%make_build -f nm_gnu.mak %{?_smp_mflags} CXXFLAGS="%optflags -fPIC" \
	libnewmat.so.11.0

%install

install -p -D libnewmat.so.11.0 %buildroot/%_libdir/libnewmat.so.11.0

pushd  %buildroot/%_libdir
ln -s libnewmat.so.11.0 libnewmat.so.11
ln -s libnewmat.so.11.0 libnewmat.so
popd

install -d %buildroot/%_includedir/newmat
install -m 0644 -p *.h %buildroot/%_includedir/newmat

%files
%doc nm11.htm readme.txt
%_libdir/libnewmat.so.*

%files devel
%doc
%dir %_includedir/newmat/
%_includedir/newmat/*.h
%_libdir/libnewmat.so

%changelog
* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 11beta-alt4
- Rebuilt for debuginfo

* Fri Dec 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 11beta-alt3
- Added operator>> for GeneralMatrix
- Fixed newmat.h

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 11beta-alt2
- Rebuilt for soname set-versions

* Sun Mar 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 11beta-alt1
- Initial build for Sisyphus

* Fri Feb 06 2009 Pascal < pascal22p at parois.net > - 10D-2
- Correction of soname.
* Sat Jan 10 2009 Pascal < pascal22p at parois.net > - 10D-1
- Fisrt spec file.

