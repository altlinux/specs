Name: minised
Version: 1.14
Release: alt1.svn20130424
Summary: Smaller, cheaper, faster SED implementation
License: GPL
Group: Editors
URL: http://www.exactcode.de/site/open_source/%name/
# http://svn.exactcode.de/minised/trunk/
Source: %name-%version.tar

# Automatically added by buildreq on Fri May 09 2008
BuildRequires: dietlibc

%description
%name smaller, cheaper, faster SED implementation.
Along a lot fixes and cleanups, further speedups, and some missing
features and POSIX conformance.


%prep
%setup


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
* Mon Sep 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14-alt1.svn20130424
- Version 1.14

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.12-alt2.qa1
- NMU: rebuilt for debuginfo.

* Mon Nov 10 2008 Led <led@altlinux.ru> 1.12-alt2
- SVN revision 106

* Sun Sep 14 2008 Led <led@altlinux.ru> 1.12-alt1
- 1.12

* Fri May 09 2008 Led <led@altlinux.ru> 1.11-alt1
- initial build
