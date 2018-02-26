Name: cilk
Version: 5.4.6
Release: alt8
Summary: Language for multithreaded parallel programming based on ANSI C
License: GPL v2 or later
Group: Development/C
Url: http://supertech.csail.mit.edu/cilk/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://supertech.csail.mit.edu/cilk/cilk-5.4.6.tar.gz

Requires: lib%name-devel = %version-%release
Conflicts: lib%name-devel-static < %version-%release
Obsoletes: lib%name-devel-static < %version-%release

BuildPreReq: flex chrpath

%description
Cilk is a language for multithreaded parallel programming based on ANSI
C. Cilk is designed for general-purpose parallel programming, but it is
especially effective for exploiting dynamic, highly asynchronous
parallelism, which can be difficult to write in data-parallel or
message-passing style. Using Cilk, our group has developed three
world-class chess programs, StarTech, *Socrates, and Cilkchess. Cilk
provides an effective platform for programming dense and sparse
numerical algorithms, such as matrix factorization and N-body
simulations, and we are working on other types of applications. Unlike
many other multithreaded programming systems, Cilk is algorithmic, in
that the runtime system employs a scheduler that allows the performance
of programs to be estimated accurately based on abstract complexity
measures.

%package -n lib%name
Summary: Shared libraries of Cilk
Group: System/Libraries

%description -n lib%name
Cilk is a language for multithreaded parallel programming based on ANSI
C. Cilk is designed for general-purpose parallel programming, but it is
especially effective for exploiting dynamic, highly asynchronous
parallelism, which can be difficult to write in data-parallel or
message-passing style. Using Cilk, our group has developed three
world-class chess programs, StarTech, *Socrates, and Cilkchess. Cilk
provides an effective platform for programming dense and sparse
numerical algorithms, such as matrix factorization and N-body
simulations, and we are working on other types of applications. Unlike
many other multithreaded programming systems, Cilk is algorithmic, in
that the runtime system employs a scheduler that allows the performance
of programs to be estimated accurately based on abstract complexity
measures.

This package contains shared libraries of Cilk.

%package -n lib%name-devel
Summary: Development files of Cilk
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Cilk is a language for multithreaded parallel programming based on ANSI
C. Cilk is designed for general-purpose parallel programming, but it is
especially effective for exploiting dynamic, highly asynchronous
parallelism, which can be difficult to write in data-parallel or
message-passing style. Using Cilk, our group has developed three
world-class chess programs, StarTech, *Socrates, and Cilkchess. Cilk
provides an effective platform for programming dense and sparse
numerical algorithms, such as matrix factorization and N-body
simulations, and we are working on other types of applications. Unlike
many other multithreaded programming systems, Cilk is algorithmic, in
that the runtime system employs a scheduler that allows the performance
of programs to be estimated accurately based on abstract complexity
measures.

This package contains development files of Cilk.

%package -n lib%name-devel-static
Summary: Static libraries of Cilk
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
Cilk is a language for multithreaded parallel programming based on ANSI
C. Cilk is designed for general-purpose parallel programming, but it is
especially effective for exploiting dynamic, highly asynchronous
parallelism, which can be difficult to write in data-parallel or
message-passing style. Using Cilk, our group has developed three
world-class chess programs, StarTech, *Socrates, and Cilkchess. Cilk
provides an effective platform for programming dense and sparse
numerical algorithms, such as matrix factorization and N-body
simulations, and we are working on other types of applications. Unlike
many other multithreaded programming systems, Cilk is algorithmic, in
that the runtime system employs a scheduler that allows the performance
of programs to be estimated accurately based on abstract complexity
measures.

This package contains static libraries of Cilk.

%package examples
Summary: Examples for Cilk
Group: Development/Documentation
Requires: lib%name = %version-%release

%description examples
Cilk is a language for multithreaded parallel programming based on ANSI
C. Cilk is designed for general-purpose parallel programming, but it is
especially effective for exploiting dynamic, highly asynchronous
parallelism, which can be difficult to write in data-parallel or
message-passing style. Using Cilk, our group has developed three
world-class chess programs, StarTech, *Socrates, and Cilkchess. Cilk
provides an effective platform for programming dense and sparse
numerical algorithms, such as matrix factorization and N-body
simulations, and we are working on other types of applications. Unlike
many other multithreaded programming systems, Cilk is algorithmic, in
that the runtime system employs a scheduler that allows the performance
of programs to be estimated accurately based on abstract complexity
measures.

This package contains examples for Cilk.

%package doc
Summary: Documentation for Cilk
Group: Development/Documentation
BuildArch: noarch

%description doc
Cilk is a language for multithreaded parallel programming based on ANSI
C. Cilk is designed for general-purpose parallel programming, but it is
especially effective for exploiting dynamic, highly asynchronous
parallelism, which can be difficult to write in data-parallel or
message-passing style. Using Cilk, our group has developed three
world-class chess programs, StarTech, *Socrates, and Cilkchess. Cilk
provides an effective platform for programming dense and sparse
numerical algorithms, such as matrix factorization and N-body
simulations, and we are working on other types of applications. Unlike
many other multithreaded programming systems, Cilk is algorithmic, in
that the runtime system employs a scheduler that allows the performance
of programs to be estimated accurately based on abstract complexity
measures.

This package contains documentation for Cilk.

%prep
%setup

%build
%add_optflags %optflags_shared
%autoreconf
%configure \
	--with-perfctr=no
%make_build

%install
%makeinstall_std

install -d %buildroot%_infodir
install -m644 FAQ/*.info %buildroot%_infodir

install -d %buildroot%_docdir/%name/FAQ
install -p -m644 doc/*.pdf %buildroot%_docdir/%name
install -m644 FAQ/%name-faq.html/* \
	%buildroot%_docdir/%name/FAQ

cp -fR examples %buildroot%_libdir/%name/
rm -f %buildroot%_libdir/%name/examples/*.o

pushd %buildroot%_libdir/%name/examples
for i in $(ls); do
	TYPE="$(file $i|sed 's|.*\(ELF\).*|\1|')"
	if [ "$TYPE" = "ELF" -a "$(readelf -a $i|grep RPATH)" != "" ]; then
		chrpath -d $i
	fi
done
popd

%files
%doc AUTHORS ChangeLog COPYING NEWS README THANKS
%_bindir/*
%_libdir/%name/*.a
%_libexecdir/%name/cilk2c

%files -n lib%name
%dir %_libdir/%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

#files -n lib%name-devel-static
#_libdir/*.a

%files doc
%_infodir/*
%_docdir/%name

%files examples
%_libdir/%name/examples

%changelog
* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.6-alt8
- Fixed build with new automake

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.6-alt7
- Fixed RPATH
- Disabled devel-static package

* Wed Aug 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.6-alt6
- Rebuilt without perfctr

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.6-alt5
- Rebuilt for debuginfo

* Fri Oct 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.6-alt4
- Rebuilt with set-versioned libperfctr

* Tue Oct 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.6-alt3
- Rebuilt for soname set-versions

* Mon Sep 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.6-alt2
- Fixed packaging errors

* Sun Sep 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.6-alt1
- Initial build for Sisyphus

