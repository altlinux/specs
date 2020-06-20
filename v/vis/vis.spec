Name: vis
Version: 0.6
Release: alt1

Summary: simple yet efficient editor, combining the strengths of both vi(m) and sam

License: ISC and MIT and CC0
Group: Editors
Url: https://github.com/martanne/vis

VCS: https://github.com/martanne/vis
Source: %name-%version.tar

BuildRequires: libtermkey-devel libncursesw-devel liblua5.3-devel
Requires: lua5.3-module-lpeg
Requires: vis-data

%package data
BuildArch: noarch
Group: Editors
Summary: data files for vis editor

%description
Vis aims to be a modern, legacy-free, simple yet efficient editor,
combining the strengths of both vi(m) and sam.

It extends vi's modal editing with built-in support for multiple
cursors/selections and combines it with sam's [1] structural regular
expression [2] based command language [3].

A universal editor, it has decent Unicode support and should cope
with arbitrary files, including large, binary or single-line ones.

[1] http://sam.cat-v.org/
[2] http://doc.cat-v.org/bell_labs/structural_regexps/
[3] http://doc.cat-v.org/bell_labs/sam_lang_tutorial/

%description data
Vis aims to be a modern, legacy-free, simple yet efficient editor,
combining the strengths of both vi(m) and sam.

This package contains data files for vis editor.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

# remove wrong places docs
rm -r -- %buildroot%_datadir/doc/vis/

%files
%doc LICENSE
%_bindir/vis
%_bindir/vis-clipboard
%_bindir/vis-complete
%_bindir/vis-digraph
%_bindir/vis-menu
%_bindir/vis-open

%_man1dir/vis.1*
%_man1dir/vis-clipboard.1*
%_man1dir/vis-complete.1*
%_man1dir/vis-digraph.1*
%_man1dir/vis-menu.1*
%_man1dir/vis-open.1*

%files data
%dir %_datadir/vis
%_datadir/vis/vis.lua
%_datadir/vis/visrc.lua
%_datadir/vis/vis-std.lua

%_datadir/vis/lexer.lua
%dir %_datadir/vis/lexers
%_datadir/vis/lexers/*

%dir %_datadir/vis/plugins
%_datadir/vis/plugins/*

%dir %_datadir/vis/themes
%_datadir/vis/themes/*

%changelog
* Sat Jun 20 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.6-alt1
- 0.6.

* Tue Apr 21 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.5.0.181.08a550d-alt1
- Initial build for ALT Sisyphus.

