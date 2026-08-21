%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: zmap
Version: 4.4.0
Release: alt1

Summary: Fast single packet network scanner
License: Apache-2.0
Group: Networking/Other
Url: https://zmap.io
Vcs: https://github.com/zmap/zmap

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake
BuildRequires: bison
BuildRequires: flex
BuildRequires: gengetopt
BuildRequires: libgmp-devel
BuildRequires: libjson-c-devel
BuildRequires: libjudy-devel
BuildRequires: libpcap-devel
BuildRequires: libunistring-devel

%description
ZMap is a fast single packet network scanner designed for Internet-wide
network surveys. On a typical desktop computer with a gigabit Ethernet
connection, ZMap is capable of scanning the entire public IPv4 address
space in under 45 minutes.

%prep
%setup

%build
# CMakeLists.txt looks for a program named byacc; point it at bison's yacc
mkdir -p tools
ln -sf /usr/bin/yacc tools/byacc
export PATH="$PWD/tools:$PATH"
%cmake -DFORCE_CONF_INSTALL:BOOL=ON
%cmake_build

%install
%cmake_install

%check
make -C test/unit run

%files
%doc README.md AUTHORS CHANGELOG.md LICENSE
%_sbindir/zmap
%_sbindir/zblocklist
%_sbindir/ziterate
%_sbindir/ztee
%dir %_sysconfdir/zmap
%config(noreplace) %_sysconfdir/zmap/zmap.conf
%config(noreplace) %_sysconfdir/zmap/blocklist.conf
%_man1dir/zmap.1*
%_man1dir/zblocklist.1*
%_man1dir/ziterate.1*
%_man1dir/ztee.1*

%changelog
* Fri Aug 21 2026 Denis Rastyogin <gerben@altlinux.org> 4.4.0-alt1
- Initial build for ALT Linux.
