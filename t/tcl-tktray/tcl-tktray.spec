Name: tcl-tktray
Version: 1.3.9
Release: alt1

Summary: FreeDesktop dock plugin for Tk apps
License: GPL
Group: Development/Tcl
Url: http://code.google.com/p/tktray/
Provides: tcl-tksystray = %version-%release
Obsoletes: tcl-tksystray

Source: %name-%version-%release.tar

BuildRequires: rpm-build >= 4.0.4-alt41 rpm-build-tcl >= 0.2-alt1 tcl-devel >= 8.4.0 tk-devel >= 8.4.0

%description
%name is a freedesktop dock plugin for Tk apps,

%prep
%setup
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
%_tcllibdir/libtktray%version.so
%_tcldatadir/tktray%version/
%_mandir/mann/tktray.n*

%changelog
* Mon Jun 25 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.9-alt1
- 1.3.9
