%define _unpackaged_files_terminate_build 1
%define _localstatedir %{_var}

Name: fdm
Version: 2.2
Release: alt1

Summary: fdm is a mail delivery agent and email filtering software
License: ISC
Group: Networking/Mail
Url: https://github.com/nicm/fdm
VCS: https://github.com/nicm/fdm

Source0: %{name}-%{version}.tar
Patch0: fdm-2.2-alt-fix-lockfile-dir.patch

BuildRequires: make gcc
BuildRequires: libtdb-devel zlib-devel libssl-devel

%description
fdm is a program designed to fetch mail from POP3 or IMAP servers, or receive
local mail from stdin, and deliver it in various ways.

%prep
%setup -q
%autopatch -p1
%autoreconf

%build
%configure
%make_build

%install
%makeinstall_std
install -pm0755 %name-sanitize %buildroot%_bindir/
install -pm0644 %name.1 %buildroot%_man1dir/
install -pm0644 %name.conf.5 %buildroot%_man5dir/

%files
%doc README  examples
%_bindir/*
%_man1dir/*
%_man5dir/*

%changelog
* Thu Apr 10 2025 Andrew Guschin <guschin@altlinux.org> 2.2-alt1
- Initial build for Sisyphus
