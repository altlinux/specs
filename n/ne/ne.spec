# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Summary:  ne, the nice editor

Name:     ne
Version:  3.3.3
Release:  alt1
License:  GPLv3+
Group:    Editors
URL:      https://ne.di.unimi.it/
VCS:      https://github.com/vigna/ne
Packager: Alexey Gladkov <legion@altlinux.org>

Source0: %name-%version.tar

BuildRequires: libncursesw-devel
BuildRequires: makeinfo

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
	LIBS=-lncurses \
	OPTS="%{optflags} -fno-strict-aliasing -Wno-parentheses" \
#
make -C doc \
	ne.info.gz ne.txt html/index.html

%install
mkdir -p -- \
	%buildroot/%_datadir/%name/syntax \
	%buildroot/%_datadir/%name/macros \
#

install -D -m755 src/ne         %buildroot%_bindir/%name
install -D -m644 doc/ne.1       %buildroot%_man1dir/%name.1
install -D -m644 doc/ne.info.gz %buildroot%_infodir/%name.info.gz
install -m 644 syntax/*.jsf     %buildroot%_datadir/%name/syntax/
install -m 644 macros/*         %buildroot%_datadir/%name/macros/
install -m 644 ./extensions     %buildroot%_datadir/ne/extensions

rm INSTALL.md
mv doc/html .

%files
%_bindir/%name
%_datadir/%name
%_man1dir/*
%_infodir/*
%doc doc/default.keys doc/default.menus
%doc ./README.md
%doc ./NEWS
%doc ./CHANGES

%package doc
Group: Editors
Summary: Documentation for ne, the nice editor
BuildArch: noarch

%description doc
Documentation for ne, the nice editor.

%files doc
%doc --no-dereference ./COPYING
%doc html
%doc ./doc/ne.texinfo
#doc ./doc/ne.pdf
%doc ./doc/ne.txt
%doc ./doc/default.*


%changelog
* Sun Nov 12 2023 Igor Vlasenko <viy@altlinux.org> 3.3.3-alt1
- picked up from orphaned
- removed from FTBFS
- New version (3.3.3)

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

