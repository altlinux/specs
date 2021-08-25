%define _unpackaged_files_terminate_build 1

Name: xpa
Version: 2.1.20
Release: alt2
Summary: The XPA Messaging System
License: MIT
Group: Development/Tools
Url: http://hea-www.harvard.edu/RD/xpa/

Source: %name-%version.tar

#Use install path from configure instead of hardcoded
Patch0: xpa-2.1.20-alt-makefile-path-fix.patch

BuildPreReq: libX11-devel libgtk+2-devel libXt-devel tcl-devel

Requires: lib%name = %EVR

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%description
The XPA messaging system provides seamless communication between many
kinds of Unix programs, including X programs and Tcl/Tk programs. It
also provides an easy way for users to communicate with these
XPA-enabled programs by executing XPA client commands in the shell or by
utilizing such commands in scripts. Because XPA works both at the
programming level and the shell level, it is a powerful tool for
unifying any analysis environment: users and programmers have great
flexibility in choosing the best level or levels at which to access XPA
services, and client access can be extended or modified easily at any
time.

%package -n lib%name
Summary: Shared libraries of the XPA messaging system
Group: System/Libraries

%description -n lib%name
The XPA messaging system provides seamless communication between many
kinds of Unix programs, including X programs and Tcl/Tk programs. It
also provides an easy way for users to communicate with these
XPA-enabled programs by executing XPA client commands in the shell or by
utilizing such commands in scripts. Because XPA works both at the
programming level and the shell level, it is a powerful tool for
unifying any analysis environment: users and programmers have great
flexibility in choosing the best level or levels at which to access XPA
services, and client access can be extended or modified easily at any
time.

This package contains shared libraries of the XPA messaging system.

%package -n lib%name-devel
Summary: Development files of the XPA messaging system
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
The XPA messaging system provides seamless communication between many
kinds of Unix programs, including X programs and Tcl/Tk programs. It
also provides an easy way for users to communicate with these
XPA-enabled programs by executing XPA client commands in the shell or by
utilizing such commands in scripts. Because XPA works both at the
programming level and the shell level, it is a powerful tool for
unifying any analysis environment: users and programmers have great
flexibility in choosing the best level or levels at which to access XPA
services, and client access can be extended or modified easily at any
time.

This package contains development files of the XPA messaging system.

%package -n lib%name-devel-static
Summary: Development files of the XPA messaging system
Group: Development/C
Requires: lib%name-devel = %EVR

%description -n lib%name-devel-static
The XPA messaging system provides seamless communication between many
kinds of Unix programs, including X programs and Tcl/Tk programs. It
also provides an easy way for users to communicate with these
XPA-enabled programs by executing XPA client commands in the shell or by
utilizing such commands in scripts. Because XPA works both at the
programming level and the shell level, it is a powerful tool for
unifying any analysis environment: users and programmers have great
flexibility in choosing the best level or levels at which to access XPA
services, and client access can be extended or modified easily at any
time.

This package contains development files of the XPA messaging system.

%package docs
Summary: Documentation for the XPA messaging system
Group: Documentation
BuildArch: noarch

%description docs
The XPA messaging system provides seamless communication between many
kinds of Unix programs, including X programs and Tcl/Tk programs. It
also provides an easy way for users to communicate with these
XPA-enabled programs by executing XPA client commands in the shell or by
utilizing such commands in scripts. Because XPA works both at the
programming level and the shell level, it is a powerful tool for
unifying any analysis environment: users and programmers have great
flexibility in choosing the best level or levels at which to access XPA
services, and client access can be extended or modified easily at any
time.

This package contains documentation for the XPA messaging system.

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure \
	--enable-shared=link \
	--with-x \
	--with-threads=1 \
	--with-gtk=%_includedir/gtk-2.0
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

rm -f doc/Makefile

%files
%doc README
%_bindir/*
%_man1dir/*
%_datadir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_man3dir/*
%_mandir/mann/*
%_pkgconfigdir/%name.pc

%files -n lib%name-devel-static
%_libdir/*.a

%files docs
%doc doc/*

%changelog
* Wed Aug 25 2021 Egor Ignatov <egori@altlinux.org> 2.1.20-alt2
- add -ffat-lto-objects to build static libs with -flto enabled

* Tue Feb 16 2021 Egor Ignatov <egori@altlinux.org> 2.1.20-alt1
- Version 2.1.20

* Mon Nov 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.15-alt1
- Version 2.1.15

* Tue Aug 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.14-alt1
- Version 2.1.14

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.13-alt1
- Initial build for Sisyphus

