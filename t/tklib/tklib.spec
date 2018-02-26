Name: tklib
Version: 0.4.1
Release: alt1

Summary: A Tk standard library
License: BSD
Group: Development/Tcl
Url: http://tcllib.sourceforge.net/
BuildArch: noarch

BuildRequires(pre): rpm-build-tcl >= 0.2.1-alt2
BuildRequires: tcl >= 8.4.0-alt1 tcllib tk

Source: %name-%version-%release.tar

%description
Tklib is a collection of utility modules for tk.

%prep
%setup

%install
%configure
%make_install DESTDIR=%buildroot install
find examples -type f -print0 |xargs -r0 chmod 0644 --

%files
%doc ChangeLog PACKAGES README* license* examples
%_tcldatadir/tklib0.4
%_mandir/mann/*

%changelog
* Mon Feb 25 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt1
- first build
