%define svnrev 106
Name: minised
Version: 1.12
Release: alt2
Summary: Smaller, cheaper, faster SED implementation
License: GPL
Group: Editors
URL: http://www.exactcode.de/site/open_source/%name/
Source: http://dl.exactcode.de/oss/%name/%name-%version.tar
%{?svnrev:Patch: %name-svn-r%svnrev.patch}
Packager: Led <led@altlinux.ru>

# Automatically added by buildreq on Fri May 09 2008
BuildRequires: dietlibc

%description
%name smaller, cheaper, faster SED implementation.
Along a lot fixes and cleanups, further speedups, and some missing
features and POSIX conformance.


%prep
%setup
%{?svnrev:%patch -p1}


%build
%define _optlevel s
%make_build CC="diet %__cc" CFLAGS="%optflags"


%install
install -D -m 0755 {,%buildroot%_bindir/}%name
install -D -m 0644 {,%buildroot%_man1dir/}%name.1


%files
%doc BUGS README
%_bindir/*
%_man1dir/*


%changelog
* Mon Nov 10 2008 Led <led@altlinux.ru> 1.12-alt2
- SVN revision 106

* Sun Sep 14 2008 Led <led@altlinux.ru> 1.12-alt1
- 1.12

* Fri May 09 2008 Led <led@altlinux.ru> 1.11-alt1
- initial build
