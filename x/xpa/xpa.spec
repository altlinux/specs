Name: xpa
Version: 2.1.13
Release: alt1
Summary: The XPA Messaging System
License: LGPLv2.1
Group: Development/Tools
Url: http://hea-www.harvard.edu/RD/xpa/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: libX11-devel libgtk+2-devel libXt-devel

Requires: lib%name = %version-%release

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
Requires: lib%name = %version-%release

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

%build
%autoreconf
%configure \
	--enable-shared=link \
	--with-x \
	--with-threads \
	--with-gtk=%_includedir/gtk-2.0
%make_build

%install
%makeinstall_std

install -d %buildroot%_libdir
cp -P *.so* %buildroot%_libdir/

install -d %buildroot%_man1dir
install -p -m644 man/man1/* %buildroot%_man1dir
install -d %buildroot%_man3dir
install -p -m644 man/man3/* %buildroot%_man3dir
install -d %buildroot%_mandir/mann
install -p -m644 man/mann/* %buildroot%_mandir/mann

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

%files docs
%doc doc/*

%changelog
* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.13-alt1
- Initial build for Sisyphus

