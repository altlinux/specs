%define _unpackaged_files_terminate_build 1

Name: gcli
Version: 2.9.0
Release: alt1

Group: Development/Other
Summary: Portable CLI tool for interacting with Git(Hub|Lab|Tea) from the command line
License: BSD-2-Clause
Url: https://herrhotzenplotz.de/gcli/
Vcs: https://github.com/herrhotzenplotz/gcli.git
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: flex make
# BuildRequires: bison
BuildRequires: libcurl-devel libssl-devel
BuildRequires: libedit-devel
# For tests
BuildRequires: libatf-c-devel kyua

%description
%summary.

The official GitHub CLI tool only supports GitHub. I wanted a simple unified tool for
various git forges such as GitHub and GitLab because every forge does things differently
yet all build on Git and purposefully break with its philosophy.

Also, the official tool from Github is written in Go, which does manual DNS resolution
which is a massive security vulnerability for people using Tor as it leaks your IP to
the DNS server. This program builds upon libcurl, which obeys the operating system's DNS
resolution mechanisms and thus also works with Tor.

%prep
%setup
%patch0 -p1

%build
./configure --prefix=/usr --debug
%make

%install
%makeinstall_std

%check
make check

%files
%_bindir/%name
%_man1dir/*
%_man5dir/*

%changelog
* Thu Aug 28 2025 Artyom Sinyugin <writers@altlinux.org> 2.9.0-alt1
- New version 2.9.0.

* Thu May 26 2025 Artyom Sinyugin <writers@altlinux.org> 2.8.0-alt1
- Version 2.8.0. Initial build.
