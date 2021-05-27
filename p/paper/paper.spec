Name: paper
Version: 2.3
Release: alt1
Summary: Query paper size database and retrieve the preferred size
License: GPLv3+
Group: Text tools
Url: https://github.com/rrthomas/paper
Source0: %name-%version.tar
Source1: %name.watch
BuildRequires: gnulib
BuildRequires: help2man
BuildRequires: perl-base
BuildRequires: diffutils

%description
This package enables users to indicate their preferred paper size, provides
the paper(1) utility to find the user's preferred default paper size and give
information about known sizes, and specifies system-wide and per-user paper
size catalogs, which can be can also be used directly (see paperspecs(5)).

%prep
%setup

%build
./bootstrap --gnulib-srcdir=/usr/share/gnulib
%configure --disable-relocatable
%make_build

%check
# No upstream tests
echo "Testing localepaper tool"
locale width height > expected
./src/localepaper | tr ' ' "\n" > got
diff -u expected got
echo "Testing paper tool"
perl -c ./src/paper

%install
%makeinstall_std

%files
%doc AUTHORS README
%_bindir/paper
%config(noreplace) %_sysconfdir/paperspecs
%_libexecdir/localepaper
%_mandir/man1/paper.1*
%_mandir/man5/paperspecs.5*

%changelog
* Tue May 25 2021 Anton Farygin <rider@altlinux.ru> 2.3-alt1
- first build for ALT, based on specfile from Fedora project
