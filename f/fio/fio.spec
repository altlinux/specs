Name: fio
Version: 2.0.7
Release: alt1

Summary: IO testing tool
License: GPLv2
Group: System/Kernel and hardware

Url: http://git.kernel.dk/?p=fio.git;a=summary
Source0: http://brick.kernel.dk/snaps/fio-%version.tar.bz2

# Automatically added by buildreq on Sun Jun 12 2011
BuildRequires: libaio-devel

%description
fio is a tool that will spawn a number of threads or processes doing a
particular type of io action as specified by the user. fio takes a
number of global parameters, each inherited by the thread unless
otherwise parameters given to them overriding that setting is given.
The typical use of fio is to write a job file matching the io load
one wants to simulate.

%prep
%setup

%build
%make_build V=1 EXTFLAGS="%optflags"

%install
%make_install DESTDIR=%buildroot install prefix=/usr mandir=/usr/share/man

%files
%doc HOWTO README REPORTING-BUGS examples
%_bindir/*
%_man1dir/*

%changelog
* Sun Apr 15 2012 Victor Forsiuk <force@altlinux.org> 2.0.7-alt1
- 2.0.7

* Sun Mar 25 2012 Victor Forsiuk <force@altlinux.org> 2.0.6-alt1
- 2.0.6

* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 1.59-alt1
- 1.59

* Fri Jul 22 2011 Victor Forsiuk <force@altlinux.org> 1.57-alt1
- 1.57

* Sun Jun 12 2011 Victor Forsiuk <force@altlinux.org> 1.55-alt1
- 1.55

* Sun Mar 14 2010 Igor Zubkov <icesik@altlinux.org> 1.37-alt1
- 1.36 -> 1.37

* Wed Dec 16 2009 Igor Zubkov <icesik@altlinux.org> 1.36-alt1
- 1.34 -> 1.36

* Thu Oct 01 2009 Igor Zubkov <icesik@altlinux.org> 1.34-alt1
- 1.24 -> 1.34

* Wed Mar 25 2009 Igor Zubkov <icesik@altlinux.org> 1.24-alt1
- 1.23 -> 1.24

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 1.23-alt1
- 1.21 -> 1.23

* Sat Jul 19 2008 Igor Zubkov <icesik@altlinux.org> 1.21-alt1
- 1.17.2 -> 1.21

* Thu Nov 01 2007 Igor Zubkov <icesik@altlinux.org> 1.17.2-alt1
- build for Sisyphus

