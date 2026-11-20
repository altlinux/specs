%def_with check

Name: sblg
Version: 0.6.1
Release: alt2

Summary: sblg is a utility for creating static blogs
License: ISC
Group: Networking/Other
URl: https://kristaps.bsd.lv/sblg/
VCS: https://github.com/kristapsdz/sblg.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%if_with check
BuildRequires: jq
%endif

BuildRequires: libexpat-devel
BuildRequires: libbsd-devel

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
%autopatch -p1

%build
cat <<EOF > configure.local
CC="cc -std=c99"
CFLAGS="%optflags -Wall -Wextra -Wno-error=incompatible-pointer-types"
INSTALL="%__install"
PREFIX="%prefix"
BINDIR="%_bindir"
SHAREDIR="%_datadir"
SBINDIR="%_sbindir"
INCLUDEDIR="%_includedir"
LIBDIR="%_libdir"
MANDIR="%_mandir"
EOF

unset MAKEFLAGS
./configure
%make_build

%install
%makeinstall_std

%check
%make regress

%files
%_bindir/%name
%_man1dir/%name.1.xz
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Fri Nov 20 2026 Ulysses Apokin <ulysses@altlinux.org> 0.6.1-alt2
- Fix time indication for ALT.

* Fri Feb 21 2025 Ulysses Apokin <ulysses@altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus.
