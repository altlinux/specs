Name:		pick
Version:	4.0.0
Release:	alt2
Summary:	Reads a list of choices from stdin and outputs the selected choice to stdout
Source:		%name-%version.tar.gz
URL:		https://github.com/mptre/pick
Group:		Text tools
License:	MIT

# Automatically added by buildreq on Tue Dec 16 2025
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libncurses-devel libtinfo-devel python3 python3-base sh5
BuildRequires: libncursesw-devel
BuildRequires: /dev/pts

%description
Pick reads a list of choices from stdin and outputs the selected choice to
stdout.  Therefore it is easily used both in pipelines and subshells.

%prep
%setup

%build
MAKEFLAGS="-O" PREFIX="%_prefix" MANDIR="%_mandir" ./configure
%make_build

%install
%makeinstall_std

%files
%doc README*
%_bindir/%name
%_man1dir/%{name}*

%check
make test

%changelog
* Thu Jan 15 2026 Fr. Br. George <george@altlinux.org> 4.0.0-alt2
- Force handmade configure to work

* Tue Dec 16 2025 Fr. Br. George <george@altlinux.org> 4.0.0-alt1
- Initial build for ALT
