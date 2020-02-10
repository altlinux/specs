# actually provided by tcl 8.6
%add_tcl_req_skip TclOO

Name: tklib
Version: 0.7
Release: alt1

Summary: A Tk standard library
License: BSD
Group: Development/Tcl
Url: https://core.tcl.tk/tklib/
BuildArch: noarch

BuildRequires(pre): rpm-build-tcl >= 0.2.1-alt2
BuildRequires: tcl >= 8.4.0-alt1 tcllib tk

# repacked https://core.tcl-lang.org/tklib/tarball/tklib-%version.tar.gz
Source: %name-%version.tar
Patch1: 0001-ALT-TEA.patch
Patch2: 0002-ALT-fix-shebangs-and-use-unversioned-interpreters.patch

%description
Tklib is a collection of utility modules for tk.

%prep
%setup
%autopatch -p2

%install
%configure
%make_install DESTDIR=%buildroot install
find examples -type f -print0 |xargs -r0 chmod 0644 --

%files
%doc ChangeLog README* license* examples
%_bindir/*
%_tcldatadir/tklib%version
%_mandir/mann/*

%changelog
* Mon Feb 10 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7-alt1
- Updated to 0.7.

* Wed Oct 04 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.6-alt1
- 0.6

* Mon Feb 25 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt1
- first build
