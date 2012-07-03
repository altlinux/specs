Name: archiveopteryx
Version: 3.1.3
Release: alt2

Summary: %name stores email in a database and provides access to it through IMAP and more.
Group: System/Servers
License: BSD

Url: http://www.archiveopteryx.org

Packager: Denis Baranov <baraka@altlinux.org>

Source: %name-%version.tar

# Manual removed MySQL-server 
# Automatically added by buildreq on Mon Sep 06 2010
BuildRequires: gcc-c++ jam libssl-devel zlib-devel

%description
Archiveopteryx is an Internet mail server, optimised to support long-term archival storage.
It seeks to make it practical not only to manage large archives, but to use the information 
therein on a daily basis instead of relegating it to offline storage.

%prep
%setup

%build
%__subst "s|\$(PREFIX)/lib/%name|%_libdir/%name|g" Jamsettings
jam -sPREFIX=%_prefix -sPIDFILEDIR=%_runtimedir -j%__nprocs

%install
jam -sINSTALLROOT=%buildroot -sPREFIX=%_prefix -sPIDFILEDIR=%_runtimedir install
mkdir -p %buildroot/var/lib/%name/

%files
%_docdir/archiveopteryx/
%_bindir/aox
%_bindir/aoximport
%_bindir/deliver
%_bindir/aoxexport
%_libdir/archiveopteryx/
%_man5dir/*
%_man8dir/*
/var/lib/%name/
%_sbindir/archiveopteryx
%_sbindir/logd
%_sbindir/recorder
#%_sbindir/tlsproxy

%changelog
* Thu Nov 18 2010 Denis Baranov <baraka@altlinux.org> 3.1.3-alt2
- fix build on 64bit platform

* Mon Sep 06 2010 Denis Baranov <baraka@altlinux.org> 3.1.3-alt1
- version with all information

* Fri Sep 03 2010 Denis Baranov <baraka@altlinux.org> 3.1.3-alt0.1
- initial build for ALT Linux Sisyphus
