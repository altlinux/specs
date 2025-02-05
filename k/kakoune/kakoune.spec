Name:    kakoune
Version: 2024.05.18
Release: alt1

Summary: Modal editor - Faster as in fewer keystrokes - Multiple selections - Orthogonal design
License: Unlicense
Group:   Editors

URL:     http://kakoune.org/
VCS:     https://github.com/mawww/kakoune/

Source0: %name-%version.tar

BuildRequires: gcc-c++

%description
Kakoune is a code editor that implements Vi's "keystrokes as a text
editing language" model. As it is also a modal editor, it is somewhat
similar to the Vim editor (after which Kakoune was originally inspired).

%prep
%setup

%build
%make_build

%install
%makeinstall_std PREFIX=%prefix

%files
%doc README.asciidoc UNLICENSE VIMTOKAK
%_bindir/kak
%prefix/libexec/kak/kak
%_docdir/kak
%_datadir/kak/*
%_man1dir/kak.1.xz

%changelog
* Wed Jan 29 2025 Ilya Sorochan <k0tran@altlinux.org> 2024.05.18-alt1
- Initial build.
