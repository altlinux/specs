# -*- coding: utf-8; mode: rpm-spec -*-

Name: rpm-build-emacs
Version: 0.0.3
Release: alt2

Group: Development/Other
Summary: Helper scripts and RPM macros to build GNU Emacs extensions
License: GPLv2+

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

BuildArch: noarch

Requires: emacs-base >= 0.0.5-alt2
Requires: emacs-nox

Source0: emacs-lisp-pkgutils-0.1.2.tar
Source1: rpm-build-emacs.macros
Source2: README.ALT.ru.txt
Patch: el-pkgutils-pathfix-alt.patch
Requires: rpm-macros-emacs = %EVR
Conflicts: emacs-devel < 0.0.3
Obsoletes: emacs-devel < 0.0.3
Provides: emacs-devel = %EVR

%description
%name is set of scripts and rpm macros to assist in GNU Emacs modules
build process


%package -n rpm-macros-emacs
Summary: Set of RPM macros for packaging emacs-based applications
Group: Development/Other
# helps old apt to resolve file conflict at dist-upgrade (thanks to Stanislav Ievlev)
Conflicts: emacs-devel <= 0.0.1-alt3

%description -n rpm-macros-emacs
Set of RPM macros for packaging emacs-based applications for ALT Linux.
Install this package if you want to create RPM packages that use emacs.

%prep
%setup -q -n el-pkgutils
cp %SOURCE2 .
%patch -p0

%install
mkdir -p %buildroot%_rpmmacrosdir
install -p -m644 %SOURCE1 %buildroot%_rpmmacrosdir/emacs
mkdir -p %buildroot%_emacslispdir
mkdir -p %buildroot%_datadir/emacs/etc/el-pkgutils
# Packager's tools - to be used in this and other pkgs
install -m0755 el-pkgutils.sh %buildroot%_datadir/emacs/etc/el-pkgutils
install -m0644 el-pkgutils.el %buildroot%_emacslispdir

%files
%doc README.ALT.ru.txt
%_emacslispdir/*
%_datadir/emacs/etc/*

%files -n rpm-macros-emacs
%_rpmmacrosdir/emacs

%changelog
* Sun Dec 19 2021 Igor Vlasenko <viy@altlinux.org> 0.0.3-alt2
- added release to emacs-devel provides

* Fri Dec 17 2021 Igor Vlasenko <viy@altlinux.org> 0.0.3-alt1
- renamed to rpm-build-emacs
- added requires on emacs-nox
- dropped provides: el-pkgutils

* Sat Oct 24 2009 Igor Vlasenko <viy@altlinux.ru> 0.0.2-alt1
- rpm macros moved to rpm-macros-emacs subpackage

* Wed Feb 01 2006 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt3
- added patch el-pkgutils-pathfix-alt.patch:
  fixes build of emacs21 with installed emacs22

* Sun Nov 06 2005 Eugene Vlasov <eugvv@altlinux.ru> 0.0.1-alt2
- Now %%byte_compile_file and %%byte_compile_dir run with --no-site-file
- Added %%bc_file_with_site and %%bc_dir_with_site - for byte compiling with
  site-start scripts
- Added %%byte_recompile_dir, %%byte_recompile_lispdir,
  %%brecomp_dir_with_site, %%brecomp_lispdir_with_site
- Fixed using load-path in all byte-compile macro

* Sat Oct 22 2005 Eugene Vlasov <eugvv@altlinux.ru> 0.0.1-alt1
- First build for Sisyphus
- Moved el-pkgutils from emacs-base
- RPM macro %%_emacs_sitestart_dir, %%_emacs_etc_dir, %%byte_compile_file,
  %%byte_compile_dir

