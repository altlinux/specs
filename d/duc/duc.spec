%define _unpackaged_files_terminate_build 1

Name: duc
Version: 1.4.6
Release: alt1

Summary: Collection of tools for inspecting and visualizing disk usage
License: LGPL-3.0-or-later
Group: File tools
Url: http://duc.zevv.nl
VCS: https://github.com/zevv/duc

Source: %name-%version.tar

BuildRequires: pkgconfig(tokyocabinet)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(ncurses)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(glfw3)

%description
Dude, where are my bytes: Duc, a library and suite of tools for
inspecting disk usage.

Duc is a collection of tools for indexing, inspecting and visualizing
disk usage. Duc maintains a database of accumulated sizes of directories
of the file system, and allows you to query this database with some
tools, or create fancy graphs showing you where your bytes are.

%prep
%setup
sed -i "s|/img/||" README.md

%build
%autoreconf
%configure \
           --with-db-backend=tokyocabinet \
           --enable-dependency-tracking \
           --enable-opengl \
           --disable-x11
%make_build

%install
%makeinstall_std

%check
%make_build check
./test.sh

%files
%doc LICENSE README.md img/palette-rainbow.png
%doc examples
%_bindir/duc
%_man1dir/duc.1.*

%changelog
* Mon Feb 03 2026 Nikolay Strelkov <snk@altlinux.org> 1.4.6-alt1
- Initial build for Sisyphus
