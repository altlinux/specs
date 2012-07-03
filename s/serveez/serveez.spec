Name:		serveez
Version:	0.1.5
Release:	alt3.qa2
License:	GPL
Group:		System/Servers
Summary:	A server framework.
Source:		http://ftp.gnu.org/gnu/serveez/%name-%version.tar.gz
URL:		http://www.gnu.org/software/serveez/index.html
Packager:	Stanislav Yadykin <tosick@altlinux.ru>

# Automatically added by buildreq on Thu Dec 11 2008
BuildRequires: gcc-c++ guile18-devel rpm-build-java rpm-macros-fillup tetex-core zlib-devel

%description
Serveez is a server framework.  It provides routines and help for
implementing IP based servers (currently TCP, UDP and ICMP).  It is also
possible to use named pipes for all connection oriented protocols.

We think it is worth the effort because many people need server functionality 
within their applications.  However, many people experience problems 
with select()- or poll()-loops, and with non-blocking operations.

This application demonstrates various aspects of advanced network
programming in a portable manner.  It is known to compile and run on 
GNU/Linux systems, as well as on other 32-bit and 64-bit flavours of Unix 
and on Microsoft Windows (9x/ME/NT/2000/XP).

You can use it for implementing your own servers or for understanding how
certain network services and operations work.

The package includes a number of servers that work already: an HTTP server,
an IRC server, a Gnutella spider and some others.  One of the highlights is
that you can run all protocols on the same port.  The application itself is
single threaded but it uses helper processes for concurrent name resolution
and ident lookups.

%package -n %name-devel
Requires:	%name guile18-devel
Summary:	Headers and libraries for Serveez server framework development
License:	GPL
Group:		Development/C
Packager:	Stanislav Yadykin <tosick@altlinux.ru>

%description -n %name-devel
This package contains headers and libraries needed to compile serveez-based
applications

%package -n %name-devel-static
Requires:	%name-devel
Summary:	Static libraries for Serveez server framework development
License:	GPL
Group:		Development/C
Packager:	Stanislav Yadykin <tosick@altlinux.ru>

%description -n %name-devel-static
This package contains static libraries needed to static compilation of
serveez-based applications

%prep
%setup

%build
%configure --enable-maintainer-mode

%__subst 's|\/\* \#undef HAVE_BZ2LIB_PREFIX \*\/|#define HAVE_BZ2LIB_PREFIX 1|' config.h

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make

%install
%makeinstall install

%files
%doc AUTHORS BUGS COPYING ChangeLog README* RELEASE THANKS TODO
%_bindir/serveez
%_bindir/mkpassword
%_infodir/serveez.*
%_man1dir/serveez.*
%dir %_datadir/serveez
%_datadir/serveez/*
%_libdir/libserveez-%version.so

%files -n %name-devel
%_bindir/serveez-config
%_libdir/libserveez.so
%_includedir/libserveez.h
%_includedir/svzconfig.h
%dir %_includedir/libserveez
%_includedir/libserveez/*
%_datadir/aclocal/serveez.m4
%_infodir/serveez-api.*
%_man1dir/serveez-config.*

%files -n %name-devel-static
%_libdir/libserveez.a

%changelog
* Tue Feb 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt3.qa2
- Removed bad RPATH

* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.1.5-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for serveez
  * obsolete-call-in-post-install-info for serveez-devel
  * postclean-05-filetriggers for spec file

* Thu Jan 15 2009 Stanislav Yadykin <tosick@altlinux.org> 0.1.5-alt3
- spec improvements

* Thu Dec 11 2008 Stanislav Yadykin <tosick@altlinux.ru> 0.1.5-alt2
- Packager: tag has been added
- devel package has been split into devel and devel-static pakages

* Thu Jan 06 2005 Stanislav Yadykin <tosick@altlinux.ru> 0.1.5-alt1
- 0.1.5

