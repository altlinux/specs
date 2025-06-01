%define _unpackaged_files_terminate_build 1
%def_without check

Name: reptyr
Version: 0.10.0
Release: alt1

Summary: Tool for moving running programs between ptys
License: MIT
Group: Terminals
Url: https://github.com/nelhage/reptyr

Source: %name-%version.tar

%if_with check
BuildRequires: /usr/bin/python3
BuildRequires: python3(pexpect)
BuildRequires: /dev
%endif

%description
reptyr is a utility for taking an existing running program and
attaching it to a new terminal, and is particularly useful for moving
a long-running process into a GNU screen session.

reptyr does a more thorough job of transferring programs than many
other tools, including the popular "screenify" shell script, because
it changes the program's controlling terminal. This means that
actions such as window resizes and interrupts are sent to the process
from the new terminal.

%prep
%setup
%__subst 's/python2/python3/g' Makefile

%build
%make_build

%install
%makeinstall_std PREFIX="%{_prefix}"

%find_lang %name --with-man

%check
%make_build test

%files -f %name.lang
%doc COPYING ChangeLog NOTES README.md
%config %_sysconfdir/bash_completion.d/*
%_bindir/*
%_man1dir/*

%changelog
* Sun Jun 01 2025 Nikolay Strelkov <snk@altlinux.org> 0.10.0-alt1
- Initial build for Sisyphus
