Summary: A program for mount Symbian OS file system using blutooth, irda and NFS
Name: p3nfs
Version: 5.19
Release: alt1.qa1
Group: Communications
License: GPL
Packager: Dmitri Kuzishchin <dim@altlinux.ru>
URL: http://www.koeniglich.de/p3nfs.html

Source: %name-%version.tar.gz
Source2: %name-doc-1.tar.bz2

Patch0:	%name-%version-alt-configure.patch
Patch1:	%name-%version-alt-Makefile.patch

BuildRequires: linux-libc-headers

%description
Mount Symbian OS file system over NFS

%description -l ru_RU.KOI8-R
Подключение файловой системы ОС Symbian по протоколу NFS

%prep
%setup -q
%setup -q -D -T -b 2
%patch0 -p1
%patch1 -p1

%build
%__autoconf
%configure
%make_build
%install

mkdir -p $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/share/man/man1

install server/p3nfsd $RPM_BUILD_ROOT/usr/bin

mkdir -p $RPM_BUILD_ROOT/usr/share/man/man1
cp doc/p3nfsd.1 $RPM_BUILD_ROOT/usr/share/man/man1

mkdir -p $RPM_BUILD_ROOT/usr/share/doc/p3nfs-5.19

#cp README CHANGES LICENCE $RPM_BUILD_ROOT/usr/share/doc/p3nfs-5.19

cp doc/* $RPM_BUILD_ROOT/usr/share/doc/p3nfs-5.19

cp bin/*.sis client/*/opl/*.opl client/epoc16/nfsc/nfsc.app $RPM_BUILD_ROOT/usr/share/doc/p3nfs-5.19

#cp %SOURCE2 $RPM_BUILD_ROOT/usr/share/doc/p3nfs-5.19
cp ../p3nfs-doc-1/*  $RPM_BUILD_ROOT/usr/share/doc/p3nfs-5.19

%clean

%files

%{_prefix}/bin/*
%{_mandir}/man1/*
%{_docdir}/p3nfs-%{version}/*

#mkdir -p //usr/bin
#install server/p3nfsd //usr/bin
#mkdir -p //usr/share/man/man1
#cp doc/p3nfsd.1 //usr/share/man/man1
#mkdir -p //usr/share/doc/p3nfs-5.19
#cp doc/* //usr/share/doc/p3nfs-5.19
#cp bin/*.sis client/*/opl/*.opl client/epoc16/nfsc/nfsc.app //usr/share/doc/p3nfs-5.19
# The package does not own its own docdir subdirectory.
# The line below is added by repocop to fix this bug in a straightforward way. 
# Another way is to rewrite the spec to use relative doc paths.
%dir %_docdir/p3nfs-%version 


%changelog
* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 5.19-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * docdir-is-not-owned for p3nfs
  * postclean-05-filetriggers for spec file

* Fri May 05 2006 Dmitri Kuzishchin <dim@altlinux.ru> 5.19-alt1
- Update to 5.19 
- Add russian documentation

* Mon May 02 2005 Dmitri Kuzishchin <dim@altlinux.ru> 5.17-alt1
- first build for ALT
