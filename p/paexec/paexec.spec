Name: paexec
Version: 1.0.1
Release: alt1

Summary: paexec distributes tasks over network or CPUs
License: MIT
Group: Networking/Other

Url: http://paexec.sourceforge.net/
Source: %name-%version.tar.gz
Packager: Aleksey Cheusov <cheusov@altlinux.org>

BuildRequires: %_bindir/pod2man %_bindir/pod2html
BuildRequires: pkgsrc-mk-files groff-base
BuildRequires: mk-configure >= 0.27.0
BuildRequires: runawk

Requires: runawk

%description
Small program that processes a list of tasks in parallel
on different CPUs, computers in a network or whatever else.

%package examples
Summary: Examples for paexec
Group: Documentation
BuildArch: noarch
Requires: %name = %version-%release

%description examples
Small program that processes a list of tasks in parallel
on different CPUs, computers in a network or whatever else.

This package contains examples for PAEXEC.

%prep
%setup

%define env \
unset MAKEFLAGS \
export PREFIX=%prefix \
export SYSCONFDIR=%_sysconfdir \
export MANDIR=%_mandir

%build
%env
mkcmake

%check
%env
# NB: the test might be a bit stressy, disabled so far
#mkcmake test

%install
%env
export DESTDIR=%buildroot
mkcmake install

%files
%doc doc/NEWS README doc/LICENSE doc/TODO presentation/paexec.pdf
%_bindir/*
%_man1dir/*

%files examples
%doc examples

# TODO:
# - investigate and re-enable tests

%changelog
* Sat Nov 29 2014 Aleksey Cheusov <cheusov@altlinux.org> 1.0.1-alt1
- 1.0.1

* Sat Aug 31 2013 Michael Shigorin <mike@altlinux.org> 0.19.1-alt2
- rebuilt for Sisyphus (thanks upstream; closes: #29308)

* Sat Aug 31 2013 Aleksey Cheusov <vle@gmx.net> 0.19.1-alt1
- 0.19.1

* Sun Mar 10 2013 Michael Shigorin <mike@altlinux.org> 0.18.0-alt1
- 0.18.0

* Mon Nov 07 2011 Michael Shigorin <mike@altlinux.org> 0.16.1-alt1
- NMU: 0.16.1 built with:
  + mk-configure 0.21.2
  + libmaa 1.3.1
  + runawk
- spec cleanup

* Thu Apr 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt2
- Rebuilt with libmaa 1.3.0

* Tue Jun 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus

