Name: tcl-zlib
Version: 2.0.1
Release: alt2

Summary: Zlib support for Tcl
License: BSD
Group: Development/Tcl
Url: http://svn.scheffers.net/zlib

Source: %name-%version-%release.tar

BuildRequires: rpm-build-tcl >= 0.2.1-alt1 tcl-devel >= 8.4.0 zlib-devel

%description
%name adds Zlib support for Tcl, as described in TIP234,
see http://www.tcl.tk/cgi-bin/tct/tip/234

%prep
%setup
%teapatch
sed -i 's,@lib@,%_lib,' pkgIndex.tcl.in

%build
aclocal
%autoreconf
%configure
make

%install
%makeinstall

%files
%doc README ChangeLog
%_tcllibdir/libzlib%version.so
%dir %_tcldatadir/zlib%version
%_tcldatadir/zlib%version/pkgIndex.tcl

%changelog
* Sat Oct 25 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.1-alt2
- fixed build on x86_64

* Thu Oct 23 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.1-alt1
- initial build
