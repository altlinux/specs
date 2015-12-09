Summary:  The Nice Editor

Name:     ne
Version:  3.0.1
Release:  alt1
License:  GPL2
Group:    Editors
Url:      https://github.com/vigna/ne
Packager: Alexey Gladkov <legion@altlinux.org>

Source0: %name-%version.tar

BuildRequires: libncursesw-devel
BuildRequires: texinfo

# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%description
ne is a text editor based on the POSIX standard that runs
on almost any UN*X machine.
Some of the features of ne are:
* is fast, small (~250K), powerful and simple to use;
* syntax highlighting;
* full support for UTF-8;
* unlimited undo/redo capability;
* simple scripting language;
* extended regular expression search and replace;
* editing of binary files.

%prep
%setup

%build
make -C src \
	CC=gcc \
	NE_GLOBAL_DIR=%_datadir/%name \
#
make -C doc \
        ne.info.gz

%install
mkdir -p -- \
	%buildroot/%_datadir/%name/syntax \
#

install -D -m755 src/ne         %buildroot/%_bindir/%name
install -D -m644 doc/ne.1       %buildroot/%_man1dir/%name.1
install -D -m644 doc/ne.info.gz %buildroot/%_infodir/%name.info.gz
install -m644 syntax/*.jsf      %buildroot/%_datadir/%name/syntax/

%files
%_bindir/%name
%_datadir/%name
%_man1dir/*
%_infodir/*
%doc doc/default.keys doc/default.menus

%changelog
* Wed Dec 09 2015 Alexey Gladkov <legion@altlinux.ru> 3.0.1-alt1
- New version (3.0.1)

* Wed Nov 16 2011 Alexey Gladkov <legion@altlinux.ru> 2.3-alt1
- New version (2.3)

* Mon Mar 07 2011 Alexey Gladkov <legion@altlinux.ru> 2.1-alt2
- Add libmagic support.

* Fri Apr 23 2010 Alexey Gladkov <legion@altlinux.ru> 2.1-alt1
- New version.

* Thu Jan 28 2010 Alexey Gladkov <legion@altlinux.ru> 2.0.3-alt1
- First build for sisyphus.

