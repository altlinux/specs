Name: metakit
Version: 2.4.9.7
Release: alt1

%define tclpkg Mk4tcl
%define soname libmk4.so.1

Summary: Embeddable database
License: X/MIT-like
Group: System/Libraries
#License: GPL ?? -- at least unix/metakit.spec states so, controversially with docs
Url: http://www.equi4.com/metakit/
Packager: Michael Shigorin <mike@altlinux.ru>

Source: %name-%version.tar.gz
Patch0: metakit-2.4.9.6-alt-soname.patch

# Automatically added by buildreq on Sun Jan 02 2005
BuildRequires: gcc-c++ libstdc++-devel tcl-devel

%def_disable static
%{?_enable_static:BuildPreReq: glibc-devel-static}

%description
MetaKit is an embeddable database which runs on Unix, Windows, Macintosh,
and other platforms.  It lets you build applications which store their
data efficiently, in a portable way, and which will not need a complex
runtime installation.  In terms of the data model, MetaKit takes the
middle ground between RDBMS, OODBMS, and flat-file databases - yet it
is quite different from each of them.

%package -n lib%name
Summary: Main library for %name
Group: System/Libraries

%description -n lib%name
This package contains the library needed to run programs dynamically
linked with %name.

%package -n lib%name-devel
Summary: Files to compile programs that will use %name
Group: Development/Databases
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the headers that programmers will need to develop
applications which will use %name.

%package -n lib%name-devel-static
Summary: Files to link with static programs that use %name
Group: Development/Databases
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package contains static libraries for %name development.

%package -n tcl-%name
Summary: Tcl bindings for the Metakit library
Group: Development/Tcl
Requires: lib%name = %version-%release
Requires: tcl >= 8.4.0-alt1

%description -n tcl-%name
This package contains Tcl bindings for the Metakit library.

%prep
%setup -q
%patch0 -p1

%build
cd builds

%define _configure_script ../unix/configure
# whoever wants python should look at Conectiva package first;
# Tcl extension now builds with some hacks

%configure \
	--disable-python --with-tcl=/usr/include,%buildroot%_tcldatadir \
	--enable-shared %{subst_enable static}

%make_build LINK_SPECIAL_FLAGS="-lpthread -ltcl" MK4_SONAME=%soname
export LD_LIBRARY_PATH=`pwd` 
%make_build test 

pushd ../tcl/test
LD_LIBRARY_PATH=../../builds tclsh all.tcl
popd

%install
%makeinstall -C builds MK4_SONAME=%soname

# fix some permissions
chmod -x CHANGES README *.html
find . -type d -name CVS -print0 |
	xargs -r0 rm -rf --
find doc demos -type f -print0 |
	xargs -r0 chmod 644 --

# move tcl extension library to proper place
%__mkdir_p %buildroot%_tcllibdir
%__mv %buildroot%_tcldatadir/%tclpkg/%tclpkg.so %buildroot%_tcllibdir/%tclpkg.so
%__subst 's|\$dir \(%tclpkg\.so\)|%_libdir/tcl \1|' \
	%buildroot%_tcldatadir/%tclpkg/pkgIndex.tcl

%files -n lib%name
%doc CHANGES README Metakit.html doc/e4s.gif doc/format.html
%_libdir/*.so.*

%files -n lib%name-devel
%doc doc/api demos
%_includedir/*
%_libdir/*.so

%files -n tcl-%name
%doc doc/tcl.html doc/tcl.gif doc/e4s.gif
%_tcldatadir/%tclpkg
%_tcllibdir/%tclpkg.so

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif 

%changelog
* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 2.4.9.7-alt1
- 2.4.9.7
- applied repocop patch

* Mon Jan 29 2007 Damir Shayhutdinov <damir@altlinux.ru> 2.4.9.6-alt1
- New version
- Spec cleanup
- libmk4.so soname changed (incompatible ABI)

* Sat Feb 04 2006 Michael Shigorin <mike@altlinux.org> 2.4.9.3-alt2
- oops, must have noticed #8679 much earlier :-(
  + Sun Dec 18 2005 Sergey Vlasov <vsu@altlinux.ru> 2.4.9.3-alt2
  - Enabled Tcl support.
  - Added patch to fix Tcl extension build:
    + use shared metakit library instead of duplicating its code
    + do not export internal symbols
  - Updated BuildRequires.

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.4.9.3-alt1.1.1
- Rebuilt with libstdc++.so.6.

* Wed Aug 04 2004 Dmitry V. Levin <ldv@altlinux.org> 2.4.9.3-alt1.1
- Minor specfile cleanup.

* Mon Jun 07 2004 Michael Shigorin <mike@altlinux.ru> 2.4.9.3-alt1
- 2.4.9.3
- removed *.la
- updated patch0
- conditional static library build

* Fri Jun 13 2003 Michael Shigorin <mike@altlinux.ru> 2.4.9.2-alt2
- 2.4.9.2, replacing mispackaged alt1
- updated patch

* Sun Jun 8 2003 Andrey Semenov <mitrofan@altlinux.ru> 2.4.9.2-alt1
- First version of RPM package.

* Wed Dec 11 2002 Michael Shigorin <mike@altlinux.ru> 2.4.8-alt1
- built for ALT Linux
- spec and patches adapted from Mandrake and Conectiva
  (latter is definitely cleaner and overall better!)
- credits:
    Lenny Cartier <lenny@mandrakesoft.com>
    Guillaume Cottenceau <gc@mandrakesoft.com>
    Andreas Hasenack <andreas@conectiva.com.br>
    Helio Chissini de Castro <helio@conectiva.com.br>
