Name: tcl-tkXwin
Version: 1.0
Release: alt5

Summary: TkXwin autoaway support for Tcl/Tk aplication.
License: GPL
Group: Development/Tcl
Url: http://beepcore-tcl.sourceforge.net/

Source: %name-%version.tar.gz

BuildRequires: rpm-build >= 4.0.4-alt41 rpm-build-tcl >= 0.2-alt1 tcl-devel >= 8.4.0 tk-devel >= 8.4.0
BuildRequires: libXScrnSaver-devel libXt-devel libXext-devel

%description
TkXwin autoaway support for Tcl/Tk aplication.

%prep
%setup -qc
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
%doc AUTHORS README
%_tcllibdir/libtkXwin%version.so
%_tcldatadir/tkXwin%version

%changelog
* Sat Jun 18 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt5
- buildreqs reordered

* Sat Nov  4 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt4
- moved to TEA-compliant build

* Fri Aug  6 2004 Sergey Kalinin <banzaj@altlinux.ru> 1.0-alt3
- Symlink removed

* Thu Jul 15 2004 Sergey Kalinin <banzaj@altlinux.ru> 1.0-alt2
- *.la files remove

* Tue May 13 2004 Sergey Kalinin <banzaj@altlinux.ru> 1.0-alt1
- initial release
