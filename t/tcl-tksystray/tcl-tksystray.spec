Name: tcl-tksystray
Version: 0.2
Release: alt2

Summary: FreeDesktop dock plugin for Tk apps
License: GPL
Group: Development/Tcl

Source: %name-%version.tar.gz

BuildRequires: rpm-build >= 4.0.4-alt41 rpm-build-tcl >= 0.2-alt1 tcl-devel >= 8.4.0 tk-devel >= 8.4.0

%description
%name is a freedesktop dock plugin for Tk apps,
initially appeared in amsn ( see www.amsn-project.net )

%prep
%setup -c
%teapatch
sed -i 's,@lib@,%_lib,' pkgIndex.tcl.in

%build
aclocal
autoconf
%configure
%make_build

%install
%makeinstall

%files
%doc README
%_tcllibdir/libtray%version.so
%_tcldatadir/tray%version/

%changelog
* Wed Nov 18 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt2
- support for obsolete KDE_NET_WM_SYSTEM_TRAY dropped

* Sat Nov  4 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt1
- moved to TEA-compliant build
- get rid of imlib

* Thu Aug 25 2005 Sergey Kalinin <banzaj@altlinux.ru> 0.1-alt1
- initial release
