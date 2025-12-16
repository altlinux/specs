Name:		pick
Version:	4.0.0
Release:	alt1
Summary:	Reads a list of choices from stdin and outputs the selected choice to stdout
Source:		%name-%version.tar.gz
Source1:	Makefile.inc
Source2:	config.h
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
cp %SOURCE1 %SOURCE2 .

%build
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
* Tue Dec 16 2025 Fr. Br. George <george@altlinux.org> 4.0.0-alt1
- Initial build for ALT
