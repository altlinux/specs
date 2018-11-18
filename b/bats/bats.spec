Name: bats
Version: 1.1.0
Release: alt1

Summary: Testing framework for Bash
Summary(ru_RU.UTF-8): Набор тестов на Bash

License: Free to copy, develop, use and (re)distribute.
Group: Development/Other
Url: https://github.com/bats-core/bats-core

# Source-git: https://github.com/bats-core/bats-core.git
Source: %name-%version.tar

BuildArch: noarch
Requires: bash

# due syntax error
AutoReq:yes,noshell

%description
Bats is a testing framework for Bash.
It provides a simple way to verify that the UNIX programs you write behave as expected.

%description -l ru_RU.UTF-8
Bats - вспомогательный фреймворк для Bash'а.
Это простой способ убедиться, что программа, написанная под Unix, будет работать, как ожидается.

%prep
%setup

%install
./install.sh %buildroot%prefix

%files
%doc LICENSE.md AUTHORS man/*
%_man1dir/*
%_man7dir/*
%_bindir/bats
%_datadir/bats-core/

%changelog
* Sun Nov 18 2018 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version

* Fri Mar 11 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt2
- cleanup spec

* Thu Sep 02 2015 Anton Agapov <anton@altlinux.org> 1.0-alt1
- iinitial build for ALT Linux Sisyphus
