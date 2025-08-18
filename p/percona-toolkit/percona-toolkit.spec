%define _unpackaged_files_terminate_build 1
%define import_path github.com/golang/dep

Name: percona-toolkit
Version: 3.7.0.1
Release: alt1.1

Summary: Advanced MySQL and system command-line tools

License: GPL-2.0
Group: Databases
Url: http://www.percona.com/software/percona-toolkit
Vcs: https://github.com/percona/percona-toolkit.git

ExclusiveArch: %go_arches

Source: %name-%version.tar
Source1: %name-vendor.tar
Patch: alt-go-build.patch
Patch1: alt-portable.patch

BuildRequires: perl-devel perl-podlators
# golang part
BuildRequires(pre): rpm-build-golang 
BuildRequires: golang /proc

Requires: %name-common = %version-%release

%description
Percona Toolkit is a collection of advanced command-line tools used by
Percona (http://www.percona.com/) support staff to perform a variety of
MySQL and system tasks that are too difficult or complex to perform manually.

These tools are ideal alternatives to private or "one-off" scripts because
they are professionally developed, formally tested, and fully documented.
They are also fully self-contained, so installation is quick and easy and
no libraries are installed.

Percona Toolkit is developed and supported by Percona.  For more
information and other free, open-source software developed by Percona,
visit http://www.percona.com/software/.

%package common
Summary: arch agnostic part of %name
Group: Databases
BuildArch: noarch

# tools are "fat"-packed with all perl packages built-it:
AutoReq: yes, noperl

Requires: perl-DBI, perl-DBD-mysql

%description common
%name tools written in Perl and arch agnostic (mostly).

%prep
%setup -n %name-%version -a1
%patch -p1
%patch1 -p1

%build
%perl_vendor_build
%ifarch %go_arches
pushd src/go
export BIN_DIR=${PWD}/../../bin
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
pkgs=$(find . -type d -name "pt-*" -exec basename {} \;)
for pkg in $pkgs; do
pushd "$pkg"
	%golang_prepare
	%golang_build .
popd
done
popd
%endif

%check
make test

%install
%perl_vendor_install
mkdir -p %buildroot%_man1dir
cp -p blib/man1/*.1p %buildroot%_man1dir
[ -s .installed-common ] && rm .installed-common ||:
pkgs_common=$(find %buildroot%_bindir -type f -exec basename {} \;)
for f in $pkgs_common; do
printf '%_bindir/%%s\n' "$f" >> .installed-common
done
%ifarch %go_arches
pushd src/go
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
export GO111MODULE="auto"
[ -s $BUILDDIR/.installed ] && rm $BUILDDIR/.installed ||:
pkgs=$(find . -type d -name "pt-*" -exec basename {} \;)
for pkg in $pkgs; do
pushd "$pkg"
	%golang_install
popd
[ -s $BUILDDIR/bin/"$pkg" ] && printf '%_bindir/%%s\n' "$pkg" >> $BUILDDIR/.installed
done
popd
%endif

%files common -f .installed-common
%_man1dir/*.1p.*
%perl_vendor_privlib/*
%doc Changelog README.md

%ifarch %go_arches
%files -f src/go/.build/.installed
%doc src/go/README.md
%endif

%changelog
* Fri Aug 15 2025 L.A. Kostis <lakostis@altlinux.ru> 3.7.0.1-alt1.1
- Update to 3.7.0-2:
  This release addresses multiple security vulnerabilities reported in Percona
  Toolkit version 3.7.0. No further details available.
- Build: added golang binaries.
- Build: split out perl packages to -common pkg due golang binaries.

* Sun Oct  7 2018 Terechkov Evgenii <evg@altlinux.org> 3.0.12-alt1
- 3.0.12

* Tue Jul  4 2017 Terechkov Evgenii <evg@altlinux.org> 3.0.3-alt1
- 3.0.3

* Sun Nov  6 2016 Terechkov Evgenii <evg@altlinux.org> 2.2.19-alt1
- 2.2.19
- Build from upstream git repo

* Sat Apr 25 2015 Terechkov Evgenii <evg@altlinux.org> 2.2.14-alt1
- 2.2.14

* Mon Feb 10 2014 Evgenii Terechkov <evg@altlinux.org> 2.2.6-alt1
- 2.2.6

* Wed Nov 20 2013 Terechkov Evgenii <evg@altlinux.org> 2.2.5-alt1
- 2.2.5

* Tue Aug 20 2013 Evgenii Terechkov <evg@altlinux.org> 2.2.4-alt1
- initial build for ALT Linux Sisyphus
