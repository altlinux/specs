Name: vimpager
Version: 2.06
Release: alt1

Summary: Pager using vim and less.vim
License: BSD
Group: Editors

Url: https://github.com/rkitover/vimpager
Packager: Artem Kurashov <saahriktu@altlinux.org>
BuildArch: noarch
Source: %url/archive/%version/vimpager-%version.tar
Patch: vimpager-alt-fixes.patch

BuildRequires: sharutils
BuildRequires: pandoc
Requires: vim-enhanced

# "syntax error" parser crash workaround
%add_findreq_skiplist %_bindir/vimcat

%description
A PAGER using less.vim with support for highlighting of man pages and many
other features. Works on most UNIX-like systems as well as Cygwin and MSYS.

%prep
%setup
%patch -p1
sed \
    -e '/INSTALLBIN/s|555|755|' \
    -e '/INSTALLMAN/s|444|644|' \
    -i Makefile

%build
%make_build vimpager

%install
%makeinstall_std SYSCONFDIR=%_sysconfdir PREFIX=%_usr

%files
%doc LICENSE
%_bindir/vimcat
%_bindir/vimpager
%_man1dir/vimcat.1*
%_man1dir/vimpager.1*
%config(noreplace) %_sysconfdir/vimpagerrc

%changelog
* Fri May 05 2023 Artem Kurashov <saahriktu@altlinux.org> 2.06-alt1
- Initial package
