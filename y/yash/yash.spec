Name: yash
Version: 2.61
Release: alt1

Summary: Yet another POSIX-compliant shell
License: GPL-2.0-only
Group: Shells
Url: https://magicant.github.io/yash/

# Source-url: https://github.com/magicant/yash/releases/download/%version/%name-%version.tar.gz
Source: %name-%version.tar.gz

BuildRequires: gcc
BuildRequires: libncursesw-devel
BuildRequires: gettext-tools
BuildRequires: ed

%description
Yash, yet another shell, is a POSIX-compliant command line shell
written in C99. Yash is intended to be the most POSIX-compliant shell
in the world while supporting features for daily interactive and
scripting use.

Notable features:
- Global aliases
- Arrays
- Socket, pipeline, and process redirection
- Brace expansion and extended globbing
- Fractional numbers in arithmetic expansion
- Command line completion with predefined completion scripts
- Command line prediction based on command history

%prep
%setup

%build
./configure \
	--prefix=%prefix \
	--bindir=%_bindir \
	--datadir=%_datadir \
	--mandir=%_mandir
%make_build

%install
%makeinstall_std
%find_lang %name

%check
export LANG=C.UTF-8
# ppid-p.tst fails in hasher (PPID mismatch)
# fc-y.tst fails in hasher (ed output differs)
#make check

%files -f %name.lang
%doc NEWS README.md
%_bindir/yash
%_man1dir/yash.1*
%_mandir/ja/man1/yash.1*
%_datadir/yash/

%changelog
* Tue Jul 15 2026 Lav <lav@altlinux.org> 2.61-alt1
- initial build for ALT Linux Sisyphus
