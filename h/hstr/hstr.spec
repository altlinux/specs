%define _unpackaged_files_terminate_build 1

%define bash_completionsdir %_datadir/bash-completion/completions

Name: hstr
Version: 3.1
Release: alt2

Summary: Suggest box like shell history completion
License: Apache-2.0
Group: Terminals
Url: http://me.mindforger.com/projects/hh.html
Vcs: https://github.com/dvorka/hstr

Source: %name-%version.tar

BuildRequires: automake
BuildRequires: gcc
BuildRequires: bash-completion
BuildRequires: libncurses-devel
BuildRequires: libncursesw-devel
BuildRequires: libreadline-devel

%description
A command line utility that brings improved shell command completion
from the history. It aims to make completion easier and faster than Ctrl-r.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc README.md
%_bindir/hh
%_bindir/%name
%_man1dir/%name.1*
%bash_completionsdir/%name

%changelog
* Fri Mar 07 2025 Denis Sergeev <zeff@altlinux.org> 3.1-alt2
- Bumped release to override autoimport package.

* Wed Mar 05 2025 Denis Sergeev <zeff@altlinux.org> 3.1-alt1
- Initial build for Sisyphus.
