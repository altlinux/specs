%def_with check

Name: sblg
Version: 0.6.1
Release: alt1

Summary: sblg is a utility for creating static blogs
License: ISC
Group: Networking/Other
Url: https://kristaps.bsd.lv/sblg/
Vcs: https://github.com/kristapsdz/sblg.git

Source0: %name-%version.tar
Source1: Makefile.configure
Source2: config.h

%if_with check
BuildRequires: jq
%endif

BuildRequires: libexpat-devel

%description
sblg is a utility for creating static blogs. It merges articles into templates
to generate static HTML files, Atom feeds, and JSON files. It's built for use
with make. No PHP, no database: just a simple UNIX tool for pulling data from
articles and populating templates. How does it work? You write your HTML
(really XHTML) articles and templates. sblg pulls data from the articles and
merges it into the templates. This is usually orchestrated with a Makefile.
And that's it. You can write articles in any format - like Markdown - so long
it converts into XHTML.

%prep
%setup
cp %SOURCE1 .
cp %SOURCE2 .
# Fix time indication for ALT
# Required for make regress
%if_with check
sed -i -e 's/06\/29\/13/06\/29\/2013/g' \
        -e 's/06\/28\/13/06\/28\/2013/g' ./regress/blog/*
%endif

%build
%make_build

%install
%makeinstall_std \
        PREFIX=%_prefix \
        BINDIR=%_bindir \
        SHAREDIR=%_datadir \
        MANDIR=%_mandir

%check
%make regress

%files
%_bindir/%name
%_man1dir/%name.1.xz
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Fri Feb 21 2025 Ulysses Apokin <ulysses@altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus.
