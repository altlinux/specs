Packager: Repocop Q. A. Robot <repocop@altlinux.org>
%def_enable shared
%def_enable static
%def_with examples

%define bname coredumper
Name: lib%bname
Version: 1.2.1
Release: alt2.1
Summary: Library to create core dumps of the running program
Group: System/Libraries
License: %bsdstyle
URL: http://code.google.com/p/google-%bname/
Source: http://google-%bname.googlecode.com/files/%bname-%version.tar
Patch: %bname-1.2.1-alt-include.patch

# Automatically added by buildreq on Tue Apr 15 2008
BuildRequires: gcc-c++
BuildRequires: rpm-build-licenses

%description
The %bname library can be compiled into applications to create core
dumps of the running program - without terminating. It supports both
single- and multi-threaded core dumps, even if the kernel does not
natively support multi-threaded core files.


%package devel
Summary: Development files of %bname library
Group: Development/C
Requires: %name%{?_disable_shared:-devel-static} = %version-%release

%description devel
The %bname library can be compiled into applications to create core
dumps of the running program - without terminating. It supports both
single- and multi-threaded core dumps, even if the kernel does not
natively support multi-threaded core files.

This package includes the header file needed to develop %name-based
software.



%if_enabled static
%package devel-static
Summary: Static %bname library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
The %bname library can be compiled into applications to create core
dumps of the running program - without terminating. It supports both
single- and multi-threaded core dumps, even if the kernel does not
natively support multi-threaded core files.

This package includes the static library needed to develop
%name-based software.
%endif


%if_with examples
%package devel-examples
Summary: Examples of using %name
Group: Documentation
BuildArch: noarch

%description devel-examples
The %bname library can be compiled into applications to create core
dumps of the running program - without terminating. It supports both
single- and multi-threaded core dumps, even if the kernel does not
natively support multi-threaded core files.

This package includes examples of using %name.
%endif


%prep
%setup -n %bname-%version
%patch -p1


%build
%configure %{subst_enable shared} %{subst_enable static}
%make_build


%install
%make_install DESTDIR=%buildroot docdir=%_docdir/%name-%version install
%if_with examples
install -d -m 0755 %buildroot%_docdir/%name-%version/examples
install -m 0644 examples/* %buildroot%_docdir/%name-%version/examples/
%endif


%if_enabled shared
%files
%_libdir/*.so.*
%endif


%files devel
%dir %_includedir/google
%_includedir/google/*
%_man3dir/*
%{?_enable_shared:%_libdir/*.so}
%_docdir/%name-%version
%{?_with_examples:%exclude %_docdir/%name-%version/examples}



%if_enabled static
%files devel-static
%_libdir/*.a
%endif


%if_with examples
%files devel-examples
%dir %_docdir/%name-%version
%_docdir/%name-%version/examples
%endif


%changelog
* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libcoredumper
  * postun_ldconfig for libcoredumper

* Tue Sep 16 2008 Led <led@altlinux.ru> 1.2.1-alt2
- added %bname-1.2.1-alt-include.patch

* Tue Apr 15 2008 Led <led@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Tue Oct 30 2007 Led <led@altlinux.ru> 1.1-alt1
- initial build
