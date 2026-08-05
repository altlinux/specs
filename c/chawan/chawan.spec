%define _unpackaged_files_terminate_build 1
%define _libexec %_prefix/libexec

Name: chawan
Version: 0.4.4
Release: alt1

Summary: TUI web browser
License: ISC
Group: Networking/WWW
Url: https://chawan.net/
Vcs: https://git.sr.ht/~bptato/chawan

Source: %name-%version.tar

BuildRequires: libssl-devel
BuildRequires: libssh2-devel
BuildRequires: libbrotli-devel
BuildRequires: pkg-config
BuildRequires: nim

%description
Chawan is a text-mode web browser. It displays websites in your
terminal and allows you to navigate on them. It can also be used
as a terminal pager

%prep
%setup

%build
%make_build

%install
%makeinstall_std PREFIX=%_prefix

%files
%doc README.md
%_bindir/cha
%_bindir/mancha
%_libexec/%name
%_mandir/man1/cha.1*
%_mandir/man1/mancha.1*
%_mandir/man5/cha-*.5*
%_mandir/man7/cha-*.7*

%changelog
* Wed Aug 05 2026 Mikhail Nogin <joycap@altlinux.org> 0.4.4-alt1
- Initial built for Sisyphus.
