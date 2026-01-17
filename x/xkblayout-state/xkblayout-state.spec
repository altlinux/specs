Name:           xkblayout-state
Version:        1.1
Release:        alt1
VCS:            https://github.com/nonpop/xkblayout-state
License:        GPLv2+
Source:         %name-%version.tar

Summary:        A command-line program to get/set the current XKB keyboard layout
Group:          System/X11

# Automatically added by buildreq on Sat Jan 17 2026
# optimized out: bash5 glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libstdc++-devel python3 python3-base python3-dev sh5 xorg-proto-devel
BuildRequires: gcc-c++ libX11-devel

%description
%summary

%prep
%setup

%build
%make CXXFLAGS="%optflags"

%install
%makeinstall_std PREFIX=%_prefix

%files
%doc *.md
%_bindir/%name

%changelog
* Sat Jan 17 2026 Fr. Br. George <george@altlinux.org> 1.1-alt1
- Initial build for ALT
