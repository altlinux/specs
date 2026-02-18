# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: datamash
Version: 1.9
Release: alt1
Summary: Statistical, numerical and textual operations in the command line
License: GPL-3.0-or-later
Group: Sciences/Mathematics
Url: https://www.gnu.org/software/datamash/
Vcs: https://https.git.savannah.gnu.org/git/datamash.git

# Fails a lot on aarch64.
%define valgrind_arches x86_64

Source: %name-%version.tar
BuildRequires: gnulib
BuildRequires: gperf
BuildRequires: makeinfo
BuildRequires: pkgconfig(bash-completion)
BuildRequires: pkgconfig(openssl)
BuildRequires: texinfo
%{?!_without_check:%{?!_disable_check:
BuildRequires: perl(Digest/SHA.pm)
%ifarch %valgrind_arches
BuildRequires: valgrind
%endif
}}

%description
GNU datamash is a command-line program which performs basic numeric, textual
and statistical operations on input textual data files.

%prep
%setup
mkdir .git # for man-pages to trigger BUILD_FROM_GIT
echo -n %version > .tarball-version

%build
./bootstrap \
	--gnulib-srcdir=%_datadir/gnulib \
	--no-bootstrap-sync \
	--no-git \
	--skip-po
%autoreconf
%configure \
	--disable-nls \
	--with-bash-completion-dir=%_datadir/bash-completion/completions \
	--with-openssl=yes \
	--with-packager="%vendor" \
	--with-packager-version="%distribution %version-%release"
%make_build

%install
%makeinstall_std

%check
%buildroot%_bindir/datamash --version | grep -Fx '%name (GNU %name) %version'
%make_build check-expensive || { sed 's/^/> /' test-suite.log; exit 2; }

%files
%define _customdocdir %_docdir/%name
%doc AUTHORS COPYING HACKING.md NEWS README
%_bindir/datamash
%_bindir/decorate
%_datadir/%name
%_man1dir/datamash.1.*
%_man1dir/decorate.1.*
%_infodir/datamash.info.*
%_datadir/bash-completion/completions/%name

%changelog
* Wed Feb 18 2026 Vitaly Chikunov <vt@altlinux.org> 1.9-alt1
- First import v1.9-9-g25ac32e (2025-12-03).
