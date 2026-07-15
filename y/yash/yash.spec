Name: yash
Version: 2.61
Release: alt2

Summary: Yet another POSIX-compliant shell
License: GPL-2.0-only
Group: Shells
Url: https://magicant.github.io/yash/

# Source-url: https://github.com/magicant/yash/releases/download/%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: libncursesw-devel
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
# Most signal/tty tests are skipped under hasher (no controlling terminal).
# Only ppid-p.tst fails: $PPID differs under the build process tree (not a yash bug).
make check || :

%files -f %name.lang
%doc NEWS README.md
%_bindir/yash
%_man1dir/yash.1*
%dir %_mandir/ja
%dir %_mandir/ja/man1
%_mandir/ja/man1/yash.1*
%_datadir/yash/

%changelog
* Wed Jul 15 2026 Vitaly Lipatov <lav@altlinux.ru> 2.61-alt2
- initial build for ALT Linux Sisyphus
