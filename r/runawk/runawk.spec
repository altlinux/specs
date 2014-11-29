Name: runawk
Version: 1.5.1
Release: alt2

Summary: Wrapper for AWK providing modules
License: MIT
Group: Development/Other

Url: http://runawk.sourceforge.net
Source: %name-%version.tar
Packager: Aleksey Cheusov <cheusov@altlinux.org>

BuildRequires: mk-configure >= 0.26.0

%description
RUNAWK is a small wrapper for AWK interpreter that helps to write
the standalone programs in AWK. It provides MODULES for AWK
similar to PERL's "use" command and other powerful features.
Dozens of ready to use modules are also provided.

%package examples
Summary: Examples for RunAWK
Group: Documentation
BuildArch: noarch
Requires: %name = %version-%release

%description examples
This package contains examples for RunAWK.

%prep
%setup

%define env \
unset MAKEFLAGS \
export PREFIX=%prefix \
export SYSCONFDIR=%_sysconfdir \
export MANDIR=%_mandir

%build
%env
mkcmake all
#mkcmake a_getopt

%check
%env
export TMPDIR=/tmp
mkcmake test

%install
%env
export DESTDIR=%buildroot
mkcmake install
#mkcmake install-a_getopt

%files
%doc doc/LICENSE doc/NEWS doc/TODO README
%_bindir/*
%_man1dir/*
%_man3dir/*
%_datadir/%name/

%files examples
%doc examples

# TODO:
# - consider packaging alt_getopt as a subpackage
#   (uses runawk, isn't used by runawk)

%changelog
* Mon Dec  1 2014 Aleksey Cheusov <cheusov@altlinux.org> 1.5.1-alt2
- Fix in .gear/rules

* Sat Nov 29 2014 Aleksey Cheusov <cheusov@altlinux.org> 1.5.1-alt1
- 1.5.1

* Sun Mar 10 2013 Michael Shigorin <mike@altlinux.org> 1.4.4-alt1
- 1.4.4
- added man3

* Sat Apr 21 2012 Michael Shigorin <mike@altlinux.org> 1.4.0-alt1
- 1.4.0

* Mon Nov 21 2011 Michael Shigorin <mike@altlinux.org> 1.3.2-alt2
- fixed name spelling

* Mon Nov 07 2011 Michael Shigorin <mike@altlinux.org> 1.3.2-alt1
- built for ALT Linux (new paexec dependency)
  + thanks Aleksey Cheusov for outstanding upstream support

