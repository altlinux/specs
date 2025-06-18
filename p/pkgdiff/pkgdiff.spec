%define _unpackaged_files_terminate_build 1

Name: pkgdiff
Version: 1.8
Release: alt1

Summary: A tool for analyzing changes in software packages
License: GPL-2.0-or-later
Group: Development/Tools
Url: https://lvc.github.io/pkgdiff/
Vcs: https://github.com/lvc/pkgdiff.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: help2man

%description
Package Changes Analyzer (pkgdiff) is a tool for analyzing changes in software
packages (RPM, DEB, TAR.GZ, etc). The tool is intended for maintainers who are
interested in ensuring compatibility of old and new versions of packages.

%prep
%setup
chmod 0755 pkgdiff.pl

%install
mkdir -p %buildroot%prefix
perl Makefile.pl -install --prefix=%prefix --destdir=%buildroot

# Generate man page
cp pkgdiff.pl pkgdiff
help2man -N --no-discard-stderr -o pkgdiff.1 ./pkgdiff
sed -i 's/\(.\)/\n\1/' pkgdiff.1
sed -i 's/PACKAGE/PKGDIFF/g' pkgdiff.1
install -Dm 0644 pkgdiff.1 -t %buildroot%_man1dir

%files
%_bindir/pkgdiff
%_datadir/pkgdiff
%_mandir/man1/pkgdiff.1.xz

%changelog
* Wed Jun 18 2025 Constantin Sunzow <protvin@altlinux.org> 1.8-alt1
- Initial build.
