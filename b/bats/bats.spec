Name: bats
Version: 1.0
Release: alt2

Summary: Testing framework for Bash
Summary(ru_RU.UTF-8): Набор тестов на Bash

License: Free to copy, develop, use and (re)distribute.
Group: Development/Other
Url: https://github.com/sstephenson/bats

Packager: Anton Agapov (Etersoft) <anton@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch
Requires: bash

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
rm -f %buildroot%_bindir/bats
ln -s ../share/bats/bats %buildroot%_bindir/bats

%files
%doc LICENSE man/*
%_man1dir/*
%_man7dir/*
%_bindir/bats
%_datadir/bats/

%changelog
* Fri Mar 11 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt2
- cleanup spec

* Thu Sep 02 2015 Anton Agapov <anton@altlinux.org> 1.0-alt1
- iinitial build for ALT Linux Sisyphus
