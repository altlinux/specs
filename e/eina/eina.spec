%def_enable tests
%def_disable static

Name: eina
Version: 1.2.1
%ifdef beta
Release: alt1.%beta
%else
Release: alt1
%endif

Summary: Enlightenment Data Type Library
License: LGPLv2.1+
Group: System/Libraries
Url: http://www.enlightenment.org/

# http://svn.enlightenment.org/svn/e/trunk/%name
Source: http://download.enlightenment.org/releases/%name-%version.tar.bz2

%{?_enable_static:BuildPreReq: glibc-devel-static}

%description
 Eina is a multi-platform library that provides optimized data types and a few
 tools. It supports the following data types:
 Containers:
  o Array: an array
  o Hash Table: a hash table
  o Inlined List: an list with functions inlined
  o List: a single-linked list
  o Red-Black Tree: a tree
  o Access Content types
    + Accessor: can access items of a container randomly
    + Iterator: can access items of a container sequentially.
 Stringshare.

%package -n lib%name
Summary: Enlightenment Data Type Library
Group: System/Libraries

%description -n lib%name
 Eina is a multi-platform library that provides optimized data types and a few
 tools. It supports the following data types:
 Containers:
  o Array: an array
  o Hash Table: a hash table
  o Inlined List: an list with functions inlined
  o List: a single-linked list
  o Red-Black Tree: a tree
  o Access Content types
    + Accessor: can access items of a container randomly
    + Iterator: can access items of a container sequentially
 Stringshare.

This package contains shared Eina library.

%package -n lib%name-devel
Summary: Enlightenment Data Type Library development files
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
 Eina is a multi-platform library that provides optimized data types and a few
 tools. It supports the following data types:
 Containers:
  o Array: an array
  o Hash Table: a hash table
  o Inlined List: an list with functions inlined
  o List: a single-linked list
  o Red-Black Tree: a tree
  o Access Content types
    + Accessor: can access items of a container randomly
    + Iterator: can access items of a container sequentially
 Stringshare.

This package contains headers, development libraries, test programs and
documentation for Eina

%prep
%setup -q -n %name-%version

%build
%configure \
	%{subst_enable static} \
	%{subst_enable tests}

%make_build

%check
%{?_enable_tests:%make check}

%install
%make DESTDIR=%buildroot install

%files -n lib%name
%_libdir/*.so.*
%doc AUTHORS README

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%changelog
* Mon Jun 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Fri May 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Mon Dec 05 2011 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Sat May 28 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Wed Mar 09 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt5
- rebuilt for debuginfo

* Sun Jan 30 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt4
- 1.0.0 release

* Thu Nov 18 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt3.beta2
- 1.0.0.beta2

* Tue Nov 09 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt2.beta
- rebuild for update dependencies

* Fri Oct 29 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1.beta
- 1.0.0.beta

* Mon Jun 07 2010 Yuri N. Sedunov <aris@altlinux.org> 0.9.9.49539-alt1
- 0.9.9.49539

* Sun Jan 03 2010 Yuri N. Sedunov <aris@altlinux.org> 0.9.9.063-alt1
- 0.9.9.063

* Tue Nov 10 2009 Yuri N. Sedunov <aris@altlinux.org> 0.0.2.062-alt1
- new version

* Fri Jul 24 2009 Yuri N. Sedunov <aris@altlinux.org> 0.0.2.061-alt1.20081020
- new version
- removed obsolete %%post{,un}_ldconfig calls

* Wed Oct 29 2008 Yuri N. Sedunov <aris@altlinux.org> 0.0.1-alt1.20081020
- first build for Sisyphus

