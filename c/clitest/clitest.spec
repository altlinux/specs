Name: clitest
Version: 0.4.0
Release: alt1

Summary: Command Line Tester
License: MIT
Group: Development/Other

Url: https://github.com/aureliojargas/clitest
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: /usr/bin/perl
%{?!_without_check:%{?!_disable_check:BuildRequires: /proc bash ash mksh zsh}}

%description
clitest is a portable POSIX shell script that performs automatic testing in
Unix command lines.

It's the same concept as in Python's doctest module: you document both the
commands and their expected output, using the familiar interactive prompt
format, and a specialized tool tests them.

%prep
%setup

%build

%check
make test docker_run=

%install
install -D -m755 -p clitest %buildroot%_bindir/clitest

%files
%doc README.md LICENSE.txt
%_bindir/clitest

%changelog
* Mon Oct 04 2021 Andrew A. Vasilyev <andy@altlinux.org> 0.4.0-alt1
- Initial build for ALT
