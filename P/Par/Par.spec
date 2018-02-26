# vim: set ft=spec: -*- spec -*-
# $Id: Par,v 1.1 2003/06/18 22:07:36 raorn Exp $

%define name Par
%define ver  1.52
%define tarver 152
%define rel  alt1

Name: %name
Version: %ver
Release: %rel

Summary: Filter for reformatting paragraphs
License: distributable
Group: Text tools
URL: http://www.cs.berkeley.edu/~amc/Par

Source:	%url/%name%tarver.tar.gz

%description
Par is a filter which copies its input to its output, changing all
white characters (except newlines) to spaces, and reformatting each
paragraph. It has some advanced features (see manual page for
examples).

%prep
%setup  -q -n %name%tarver

%build
%make_build \
	CC="gcc %optflags -c" \
	LINK1="gcc" \
	-f protoMakefile

%install
%__mkdir_p %buildroot{%_bindir,%_man1dir}

%__install -p -m755 par %buildroot%_bindir
%__install -p -m644 par.1 %buildroot%_man1dir

%files
%doc par.doc releasenotes
%_bindir/*
%_man1dir/*

%changelog
* Thu Jun 19 2003 Sir Raorn <raorn@altlinux.ru> 1.52-alt1
- Built for Sisyphus (based on PLD's spec)


