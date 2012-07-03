Name: tvmet
Version: 1.7.2
Release: alt5
Summary: Tiny Vector Matrix library using Expression Templates
License: LGPL v2.1
Group: Sciences/Mathematics
Url: http://tvmet.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# cvs -z3 -d:pserver:anonymous@tvmet.cvs.sourceforge.net:/cvsroot/tvmet co -P tvmet
Source: %name-%version.tar.gz

BuildPreReq: gcc-c++ cppunit-devel doxygen graphviz
#BuildPreReq: /usr/bin/pdflatex /usr/bin/epstopdf
BuildPreReq: /usr/bin/epstopdf

%description
TVMET - Tiny Vector Matrix library using Expression Templates.
This tiny vector and matrix template libary uses meta templates and
template expressions to evaluate results at compile time - to make
it fast for low order systems. Temporaries are kicked off. 

%package -n lib%name-devel
Summary: Development files of TVMET
Group: Development/C++

%description -n lib%name-devel
TVMET - Tiny Vector Matrix library using Expression Templates.
This tiny vector and matrix template libary uses meta templates and
template expressions to evaluate results at compile time - to make
it fast for low order systems. Temporaries are kicked off. 

This package contains development files of TVMET.

%package -n lib%name-devel-doc
Summary: Documentation for TVMET
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
TVMET - Tiny Vector Matrix library using Expression Templates.
This tiny vector and matrix template libary uses meta templates and
template expressions to evaluate results at compile time - to make
it fast for low order systems. Temporaries are kicked off. 

This package contains development documentation for TVMET.

%prep
%setup

%build
cp ChangeLog.1 ChangeLog
%autoreconf
%configure \
	--enable-optimize \
	--enable-docs

sed -i 's|^\(CXX\ \=.*\)|\1 -g|' Makefile examples/Makefile
%make_build
pushd examples
%make_build examples
popd

%install
sed -i 's|@\$(INSTALL_DATA)|cp -fR|' doc/Makefile
%makeinstall_std

mv %buildroot%_docdir/%name-%version %buildroot%_docdir/%name
install -d %buildroot%_docdir/%name/examples
pushd examples
install -p -m644 *.cc %buildroot%_docdir/%name/examples
rm -f *.cc *.o Makefile*
for i in $(ls); do
	mv $i %{name}_$i
done
install -m755 * %buildroot%_bindir
popd

%files
%doc AUTHORS COPYING ChangeLog LICENSE NEWS README THANKS
%_bindir/*
%exclude %_bindir/%name-config

%files -n lib%name-devel
%_bindir/%name-config
%_includedir/*
%_aclocaldir/*
%_man1dir/*

%files -n lib%name-devel-doc
%_docdir/%name

%changelog
* Sat Apr 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2-alt5
- Fixed build

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2-alt4
- Rebuilt for debuginfo

* Mon Oct 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2-alt3
- Rebuilt without rpm-build-compat

* Thu May 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2-alt2
- Set lib%name-devel-doc as noarch package

* Tue May 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2-alt1
- Initial build for Sisyphus

