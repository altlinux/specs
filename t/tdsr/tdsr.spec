%define _unpackaged_files_terminate_build 1

%def_without check

Name:    tdsr
Version: 20240602
Release: alt1

Summary: A console screen reader for macOS and Linux
License: GPL-3.0
Group:   Development/Python3
URL:     https://github.com/tspivey/tdsr
Source: %name-%version.tar
Patch0: 0001-Fixed-config-path.patch

Requires: python3-module-pyte
Requires: speech-dispatcher

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

%description
This is a console-based screen reader.
It has been tested under macOS, Linux and FreeBSD.
It might also run on other \*nix systems, but this hasn't been tested.

What works
* Reading output
* Reading by line, word and character
* cursor keys (waits some amount of time and speaks)

%prep
%setup
%patch0 -p1

%build

%install
install -D -m 775 %name %buildroot%_bindir/%name
install -D -m 775 speechdispatcher %buildroot%_bindir/speechdispatcher
install -D -m 644 %name.cfg.dist %buildroot%_sysconfdir/%name.cfg
install -D -m 444 COPYING.txt %buildroot%_docdir/%name-%version/COPYING.txt
install -D -m 444 readme.md %buildroot%_docdir/%name-%version/readme.md

%files
%config(noreplace) %_sysconfdir/%name.cfg
%_bindir/%name
%_bindir/speechdispatcher
%_docdir/%name-%version/COPYING.txt
%_docdir/%name-%version/readme.md

%changelog
* Fri Nov 01 2024 Artem Semenov <savoptik@altlinux.org> 20240602-alt1
- Initial build for Sisyphus (ALT bug: 51706)
