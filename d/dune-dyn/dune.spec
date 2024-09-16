# subpackages build order
# - bootstrap
# - ordering
# - configurator
# - dyn
# - stdune
# - private-libs
# - site

%define dune_pkg dyn
%if "%dune_pkg" != "bootstrap"
%define subpackagename -%dune_pkg
%def_with subpackage
%def_without check
%else
%define subpackagename %nil
%def_without subpackage
%def_with check
%endif

Name: dune%subpackagename
Version: 3.16.0
Release: alt1
Summary: A composable build system for OCaml
Group: Development/ML
License: MIT
Url: https://github.com/ocaml/dune
Source0: dune-%version.tar
Patch0: dune-%version-%release.patch
Provides: ocaml-dune = %EVR

BuildRequires: ocaml >= 4.14.0
BuildRequires: rpm-build-ocaml >= 1.5
%if_with subpackage
BuildRequires: dune
BuildRequires: ocaml-csexp-devel
%endif

%if "%dune_pkg" == "bootstrap"
%package -n emacs-dune
Summary: Emacs support for Ocaml Dune
Requires: %name = %EVR
Requires: emacs-common
BuildRequires: rpm-build-emacs
BuildArch: noarch
Group: Development/ML
%description -n emacs-dune
The %{name}-emacs package contains Emacs integration with the dune build
system, a mode to edit dune files, and flymake support for dune files.
%endif

%description
Dune is a build system designed for OCaml/Reason projects only. It focuses
on providing the user with a consistent experience and takes care of most of
the low-level details of OCaml compilation. All you have to do is provide a
description of your project and Dune will do the rest.

The scheme it implements is inspired from the one used inside Jane Street and
adapted to the open source world. It has matured over a long time and is used
daily by hundred of developers, which means that it is highly tested and
productive.

%if "%dune_pkg" == "configurator"
%define pkgname %name
%package -n ocaml-%name
Group: Development/ML
Summary: Helper dune library for gathering system configuration
Requires: ocaml-result-devel
Requires: dune = %EVR
%description -n ocaml-%name
dune-configurator is a small library that helps writing OCaml scripts that
test features available on the system, in order to generate config.h
files for instance.
Among other things, dune-configurator allows one to:
- test if a C program compiles
- query pkg-config
- import #define from OCaml header files
- generate config.h file
%endif

%if "%dune_pkg" == "private-libs"
%define pkgname %name
%package -n ocaml-%name
Group: Development/ML
Summary: Runtime files for %name
Requires: dune = %EVR
BuildRequires: ocaml-dyn-devel = %version
BuildRequires: ocaml-stdune-devel = %version
%description -n ocaml-%name
This package contains code that is shared between various dune-xxx
packages. However, it is not meant for public consumption and provides
no stability guarantee.
%endif

%if "%dune_pkg" == "site"
%define pkgname %name
%package -n ocaml-%name
Group: Development/ML
Summary: Embed location information inside executables and libraries
Requires: dune = %EVR
BuildRequires: ocaml-dune-private-libs-devel = %version
%description -n ocaml-%name
This library enables embedding location information inside executables
and libraries.
%endif

%if "%dune_pkg" == "ordering"
%define pkgname %dune_pkg
%package -n ocaml-%dune_pkg
Group: Development/ML
Summary: Element ordering
Requires: dune = %EVR
%description -n ocaml-%dune_pkg
Element ordering
%endif

%if "%dune_pkg" == "dyn"
%define pkgname %dune_pkg
%package -n ocaml-%dune_pkg
Group: Development/ML
Summary: Dynamic type
Requires: dune = %EVR
BuildRequires: ocaml-ordering-devel = %version ocaml-pp-devel
%description -n ocaml-%dune_pkg
Dynamic type.
%endif

%if "%dune_pkg" == "stdune"
%define pkgname %dune_pkg
%package -n ocaml-%pkgname
Group: Development/ML
Summary: Dune's unstable standard library
Requires: dune = %EVR
BuildRequires: ocaml-ordering-devel = %version
BuildRequires: ocaml-csexp-devel ocaml-pp-devel ocaml-dyn-devel = %version
%description -n ocaml-%pkgname
This library offers no backwards compatibility guarantees. Use at your own risk.
%endif

%if "%dune_pkg" == "xdg"
%define pkgname %dune_pkg
%package -n ocaml-%pkgname
Group: Development/ML
Summary: XDG Base Directory Specification
Requires: dune = %EVR
BuildRequires: dune = %version
%description -n ocaml-%pkgname
XDG Base Directory Specification
%endif

%if_with subpackage
%package -n ocaml-%pkgname-devel
Summary: Development files for %name
Group: Development/ML
Requires: ocaml-result-devel
Requires: ocaml-%pkgname = %EVR
%description -n ocaml-%pkgname-devel
The ocaml-%pkgname-devel package contains libraries and signature files for
developing applications that use ocaml-%pkgname.
%endif

%prep
%setup -n dune-%version
%patch0 -p1

%build
sed -i '/^(name/a (version %version)' dune-project
./configure --libdir=%_libdir/ocaml \
	    --mandir=%_mandir  \
	    --datadir=%_datadir \
	    --etcdir %_sysconfdir \
	    --bindir %_bindir \
            --sbindir %_sbindir \
	    --docdir %_docdir \
	    %nil

%if_without subpackage
%make_build release
%else
rm -rf vendor/csexp vendor/pp
%dune_build -p %pkgname
%endif

%install
%if_with subpackage
%dune_install %pkgname
%else
./dune.exe install --destdir=%buildroot dune
%byte_recompile_lispdir
%endif

%check
./dune.exe runtest test/unit-tests

%if_without subpackage
%files
%doc README.md CHANGES.md
%_ocamldir/dune/META
%_ocamldir/dune/dune-package
%_ocamldir/dune/opam
%_bindir/dune
%_man1dir/dune.1*
%_man1dir/dune-describe.1*
%_man1dir/dune-help.1*
%_man1dir/dune-printenv.1*
%_man1dir/dune-promote.1*
%_man1dir/dune-build.1*
%_man1dir/dune-cache.1*
%_man1dir/dune-clean.1*
%_man1dir/dune-exec.1*
%_man1dir/dune-external-lib-deps.1*
%_man1dir/dune-install.1*
%_man1dir/dune-init.1*
%_man1dir/dune-installed-libraries.1*
%_man1dir/dune-ocaml-merlin.1*
%_man1dir/dune-rules.1*
%_man1dir/dune-runtest.1*
%_man1dir/dune-subst.1*
%_man1dir/dune-test.1*
%_man1dir/dune-top.1*
%_man1dir/dune-uninstall.1*
%_man1dir/dune-utop.1*
%_man5dir/dune-config.5*
%_man1dir/dune-format-dune-file.1.*
%_man1dir/dune-upgrade.1.*
%_man1dir/dune-coq.1.*
%_man1dir/dune-diagnostics.1.*
%_man1dir/dune-fmt.1.*
%_man1dir/dune-internal.1.*
%_man1dir/dune-monitor.1.*
%_man1dir/dune-ocaml.1.*
%_man1dir/dune-pkg.1.*
%_man1dir/dune-rpc.1.*
%_man1dir/dune-show.1.*
%_man1dir/dune-shutdown.1.*
%_man1dir/dune-promotion.1.*

%files -n emacs-dune
%_emacslispdir/*
%endif

%if_with subpackage
%files -n ocaml-%pkgname -f ocaml-files.runtime

%files -n ocaml-%pkgname-devel -f ocaml-files.devel
%endif

%changelog
* Tue Sep 03 2024 Anton Farygin <rider@altlinux.ru> 3.16.0-alt1
- 3.11.1 -> 3.16.0

* Sun Nov 05 2023 Anton Farygin <rider@altlinux.ru> 3.11.1-alt2
- removed ocaml-findlib-devel from BuildRequires
- added emacs-dune subpackage
- built ordering, site, dyn and stdune packages

* Thu Nov 02 2023 Anton Farygin <rider@altlinux.ru> 3.11.1-alt1
- 2.9.3 -> 3.11.1

* Sun Jan 30 2022 Anton Farygin <rider@altlinux.ru> 2.9.3-alt1
- 2.9.1 -> 2.9.3

* Tue Sep 14 2021 Anton Farygin <rider@altlinux.ru> 2.9.1-alt1
- 2.9.1

* Tue Jul 27 2021 Anton Farygin <rider@altlinux.ru> 2.9.0-alt1
- 2.9.0

* Fri Apr 09 2021 Anton Farygin <rider@altlinux.org> 2.8.5-alt1
- 2.8.5
- enabled unit-test

* Tue Mar 09 2021 Anton Farygin <rider@altlinux.org> 2.8.4-alt1
- 2.8.4
- dune package was splitted into subpackages by analogy with upstream packages

* Mon Jan 25 2021 Anton Farygin <rider@altlinux.org> 2.8.2-alt1
- 2.8.2

* Fri Jan 15 2021 Anton Farygin <rider@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Tue Oct 13 2020 Anton Farygin <rider@altlinux.ru> 2.7.1-alt3
- moved all dune-configurator modules to devel package to fix
  cyclic build dependencies with csexp package

* Tue Sep 29 2020 Anton Farygin <rider@altlinux.ru> 2.7.1-alt2
- fixed doc_root and mandir location

* Thu Sep 03 2020 Anton Farygin <rider@altlinux.ru> 2.7.1-alt1
- 2.7.1

* Thu Aug 06 2020 Anton Farygin <rider@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Mon Jul 06 2020 Anton Farygin <rider@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Mon Jun 15 2020 Anton Farygin <rider@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Fri Apr 24 2020 Anton Farygin <rider@altlinux.ru> 2.5.1-alt1
- 2.5.1

* Tue Apr 14 2020 Anton Farygin <rider@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Wed Mar 11 2020 Anton Farygin <rider@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Tue Feb 25 2020 Anton Farygin <rider@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Thu Feb 20 2020 Anton Farygin <rider@altlinux.ru> 2.3.0-alt2
- added information about dune version to dune-project to fix
  dune --version when building without git

* Mon Feb 17 2020 Anton Farygin <rider@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Mon Feb 10 2020 Anton Farygin <rider@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Fri Jan 31 2020 Anton Farygin <rider@altlinux.ru> 2.1.3-alt2
- default mandir changed from /usr/man to /usr/share/man

* Fri Jan 24 2020 Anton Farygin <rider@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Thu Jan 09 2020 Anton Farygin <rider@altlinux.ru> 2.1.2-alt1
- 2.1.2
- added devel package

* Thu Oct 17 2019 Anton Farygin <rider@altlinux.ru> 1.11.4-alt1
- 1.11.4

* Tue Sep 03 2019 Anton Farygin <rider@altlinux.ru> 1.11.3-alt1
- 1.11.3

* Wed Jul 24 2019 Anton Farygin <rider@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Wed Jun 05 2019 Anton Farygin <rider@altlinux.ru> 1.10.0-alt1
- 1.10.0

* Sat May 11 2019 Anton Farygin <rider@altlinux.ru> 1.9.3-alt1
- 1.9.3

* Tue Apr 16 2019 Anton Farygin <rider@altlinux.ru> 1.9.1-alt1
- 1.9.1

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Sun Jan 20 2019 Anton Farygin <rider@altlinux.ru> 1.6.3-alt1
- 1.6.3

* Fri Dec 28 2018 Anton Farygin <rider@altlinux.ru> 1.6.2-alt1
- 1.6.2

* Fri Oct 26 2018 Anton Farygin <rider@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.1.1-alt2
- rebuilt for ocaml-4.07.1

* Sat Aug 11 2018 Anton Farygin <rider@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Wed May 16 2018 Anton Farygin <rider@altlinux.ru> 1.0-alt2.beta20
- update to beta20

* Tue Dec 19 2017 Anton Farygin <rider@altlinux.ru> 1.0-alt1.git4570020
- first build for ALT, based on RH spec


