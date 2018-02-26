Name:		libev4
Version:	4.04
Release:	alt1
Summary:	libev - an event notification library
License:	BSD or GPL v2+
URL:		http://software.schmorp.de/pkg/libev
Group:		System/Libraries
Source:		%name-%version.tar
Source1:	libev.pc.in

%description
The libev API provides a mechanism to execute a callback function when
a specific event occurs on a file descriptor or after a timeout has
been reached. It is meant to replace the asynchronous event loop found
in event-driven network servers.

%package -n libev-devel
Summary:	Header files for libev library
Group:		Development/C
Requires:	%name = %version-%release

%description -n libev-devel
Header files for libev library.

%package -n libev-devel-static
Summary:	Static libev library
Group:		Development/C
Requires:	libev-devel = %version-%release

%description -n libev-devel-static
Static libev library.

%prep
%setup
# Add pkgconfig support
cp -p %{SOURCE1} .
sed -i.pkgconfig -e 's|Makefile|Makefile libev.pc|' configure.ac configure
sed -i.pkgconfig -e 's|lib_LTLIBRARIES|pkgconfigdir = $(libdir)/pkgconfig\n\npkgconfig_DATA = libev.pc\n\nlib_LTLIBRARIES|' Makefile.am Makefile.in

%build
aclocal
automake
%autoreconf
%configure --with-pic
#--disable-static
%make_build

%install
%makeinstall

# move to libev and create compat symlinks
pushd %buildroot%_includedir/
mkdir libev
mv *.h libev/
ln -s libev/ev.h libev/ev++.h .
popd

%files
%doc Changes LICENSE README
%_libdir/libev.so.*

%files -n libev-devel
%_libdir/libev.so
%_includedir/ev.h
%_includedir/ev++.h
%_includedir/libev
%_libdir/pkgconfig/libev.pc
%_man3dir/*

%files -n libev-devel-static
%_libdir/libev.a

%changelog
* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 4.04-alt1
- 4.04

* Mon Dec 06 2010 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- 4.0.1

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.43-alt3
- Rebuilt for soname set-versions

* Tue Mar 09 2010 Timur Batyrshin <erthad@altlinux.org> 3.43-alt2
- removed obsolete %post/%postun sections

* Tue Aug 26 2008 Kirill A. Shutemov <kas@altlinux.ru> 3.43-alt1
- First build for ALT Linux
