# Spec file for BKY version control system

%define version 1.0.0
%define sub_version pre3
%define release alt1.%sub_version


Name: bky
Version: %version
Release: %release

Summary: a minimalistic distributed Version Control System
Summary(ru_RU.UTF-8): упрощённая распределённая система контроля версий

License: GPL
Group: Development/Other
URL: http://www.triptico.com/software/bky.html

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: %name-%version-%sub_version.tar.gz

Requires: rsync, patch, diffutils

%description
Bky is a minimalistic, distributed Version Control System / Source Code
Management  tool that  uses  rsync as  a backend to  store revisions as
complete trees, optimizing the size by storing unchanged files  as hard
links.

%description -l ru_RU.UTF-8
Bky  -  упрощённая  распределённая  система контроля  версия  /  утилита 
управления исходным кодом, которая использует rsync в качестве механизма 
для хранения  ревизий в виде полных  деревьев,  с оптимизаций по размеру 
путём хранения неизменённых файлов как жестких ссылок.

%prep
%setup -q -n %name-%version-%sub_version

%build
%__subst 's,\/usr\/bin\/env perl,/usr/bin/perl -w,' cvs2bky

%install
%make install PREFIX=%buildroot%_prefix
# Removing installed docs
%__rm -rf -- %buildroot%_datadir

# We don't have in Sisyphus cvsps utility - cvs2bky is unusefull
%__rm -- %buildroot%_bindir/cvs2bky

%files
%doc Changelog README AUTHORS TODO
%_bindir/bky*

%changelog
* Thu Jun 08 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.0-alt1.pre3
- New version 1.0.0-pre3
  * Command line argument bug fix
  * Workaround of unseted $EDITOR variable
  
* Sun Nov 20 2005 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.0-alt1.pre2
- Initial build for ALT Linux

* Mon Sep 05 2005 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.0-alt0.1.pre2
- Adding patch for undefined EDITOR variable under root

* Mon Jun 20 2005 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.0-alt0.pre2
- Initial build


