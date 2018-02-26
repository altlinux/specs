# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: fdupes
Version: 1.40
Release: alt2

Summary: Identifies duplicate files within given directories
License: %mit
Group: File tools
Url: http://netdial.caribe.net/~adrian2/fdupes.html

Packager: Artem Zolochevskiy <azol@altlinux.ru>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

%description
FDUPES is a program for identifying or deleting duplicate files
residing within specified directories.

%prep
%setup

%build
%make_build --silent

%install
%define INSTALLDIR %buildroot%_bindir
%define MANPAGEDIR %buildroot%_mandir
mkdir -p %INSTALLDIR
mkdir -p %buildroot%_man1dir
%makeinstall INSTALLDIR=%INSTALLDIR MANPAGEDIR=%MANPAGEDIR install --silent

%files
%doc CHANGES CONTRIBUTORS INSTALL README TODO testdir/
%_bindir/*
%_man1dir/*

%changelog
* Wed Oct 01 2008 Artem Zolochevskiy <azol@altlinux.ru> 1.40-alt2
- fixed manpage name (#17404)

* Sun Aug 26 2007 Artem Zolochevskiy <azol@altlinux.ru> 1.40-alt1
- initial build for Sisyphus


