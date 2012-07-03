Name: fish
Version: 1.23.1
Release: alt2

Summary: A friendly interactive shell
License: GPLv2+
Group: Shells

URL:                    http://www.fishshell.org

Source: %name-%version.tar

Requires: bc man

BuildRequires: libncurses-devel doxygen
BuildRequires: xorg-proto-devel libX11-devel libXt-devel libXext-devel

%set_compress_topdir %_mandir

%description
fish is a shell geared towards interactive use. Its features are
focused on user friendliness and discoverability. The language syntax
is simple but incompatible with other shell languages.

%prep
%setup -q

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%post
grep -q %_bindir/fish %_sysconfdir/shells ||
	echo %_bindir/fish >>%_sysconfdir/shells

%postun
. shell-quote
if [ "$1" = 0 ]; then
	sed -i "/^$(quote_sed_regexp %_bindir/fish)$/ d" %_sysconfdir/shells
fi

%files
%_bindir/fish
%_bindir/fish_indent
%_bindir/fish_pager
%_bindir/fishd
%_bindir/mimedb
%_bindir/set_color
%_bindir/xsel
%dir %_sysconfdir/fish
%config %_sysconfdir/fish/config.fish
%dir %_datadir/fish
%_datadir/fish/config.fish
%dir %_datadir/fish/completions
%_datadir/fish/completions/*.fish
%dir %_datadir/fish/functions
%_datadir/fish/functions/*.fish
%dir %_datadir/fish/man
%_datadir/fish/man/*.1
%doc %_datadir/doc/%name
%_mandir/man1/fish.1*
%_mandir/man1/fish_pager.1*
%_mandir/man1/fish_indent.1*
%_mandir/man1/fishd.1*
%_mandir/man1/mimedb.1*
%_mandir/man1/set_color.1*
%_mandir/man1/xsel.1x*

%changelog
* Sun Mar 06 2011 Kirill A. Shutemov <kas@altlinux.org> 1.23.1-alt2
- Do not compress /usr/share/fish/man/*

* Sat Mar 05 2011 Kirill A. Shutemov <kas@altlinux.org> 1.23.1-alt1
- Initial build
