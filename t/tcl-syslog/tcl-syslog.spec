Name: tcl-syslog
Version: 2.0
Release: alt5.1

Summary: Syslog tcl lib
Group: Development/Tcl
License: BSD
Url: http://www.45.free.net/tcl/tclsyslog.html

Packager: Denis Smirnov <mithraen@altlinux.ru>

Conflicts: scotty

Source: %name-%version.tar.gz

Patch1: %name.Makefile.patch

# Automatically added by buildreq on Sun Sep 25 2005
BuildRequires: tcl-devel

%description
Writing to syslog from tcl scripts

%prep
%setup -q -c
%patch1 -p1

%build
%make

%install
export PREFIX=%buildroot/usr
sed -i '/PREFIX=/d' Makefile
%makeinstall
cat <<EOF > %buildroot%_datadir/tcl/syslog/pkgIndex.tcl
package ifneeded Syslog 2.0 [list load [file join \$dir .. .. .. lib tcl libsyslog.so.2.0] Syslog]
EOF

mkdir -p %buildroot%_libdir/tcl/
%ifarch x86_64
mv %buildroot/usr/lib/tcl/*.so.* %buildroot%_libdir/tcl/
%endif

%files
%_mandir/mann/*
%_libdir/tcl/*.so.*
%_datadir/tcl/syslog

%changelog
* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 2.0-alt5.1
- rebuild (with the help of girar-nmu utility)

* Sun Dec 14 2008 Denis Smirnov <mithraen@altlinux.ru> 2.0-alt5
- add conflicts to scotty

* Wed Dec 03 2008 Denis Smirnov <mithraen@altlinux.ru> 2.0-alt4
- fixed build on x86_64

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 2.0-alt3
- cleanup spec

* Sun Dec 30 2007 Denis Smirnov <mithraen@altlinux.ru> 2.0-alt2
- Build with tcl 8.5

* Sun Sep 25 2005 Denis Smirnov <mithraen@altlinux.ru> 2.0-alt1
- first build for Sisyphus

