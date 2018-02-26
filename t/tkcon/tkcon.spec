Name: tkcon
Version: 2.5
Release: alt1

Summary: Enhanced interactive console for developing in Tcl
License: BSD
Group: Development/Tcl
Url: http://%name.sourceforge.net

BuildRequires(pre): rpm-build-tcl
BuildRequires: tcl-devel >= 8.4.0-alt1
BuildArch: noarch

Source: %name-%version-%release.tar

%description
%name is a enhanced interactive console for developing in Tcl
%name is a tcl shell and console, making it ideal for
experimenting with Tcl and Tk programs interactively.

%prep
%setup

%install
mkdir -p %buildroot%_bindir
cat << E_O_F > %buildroot%_bindir/%name
#!%__tclsh
package require %name
eval ::tkcon::Init \$::argv
E_O_F

chmod 0755 %buildroot%_bindir/%name
install -pD -m0644 tkcon.tcl %buildroot%_tcldatadir/%name/tkcon.tcl
install -p -m0644 pkgIndex.tcl %buildroot%_tcldatadir/%name/
install -pD -m0644 tkcon.desktop %buildroot%_desktopdir/%name.desktop

%files
%doc index.html docs README.txt ChangeLog
%_bindir/%name
%_tcldatadir/%name
%_desktopdir/%name.desktop

%changelog
* Wed Nov 21 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5-alt1
- snapshot @ 20070623

* Sat Jul 10 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4-alt3
- snapshot @ 20040624

* Sat Feb 14 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4-alt2
- snapshot @ 20040212

* Fri Dec 12 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4-alt1
- snapshot @ 20031118

