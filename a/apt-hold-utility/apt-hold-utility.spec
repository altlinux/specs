Name: apt-hold-utility
Version: 0.1
Release: alt2

Summary(ru_RU.UTF-8): Утилиты для заморозки и разморозки обновления пакетов
Summary: Apt-get hold/unhold packages

License: GPLv3
Group: System/Configuration/Other
Url: http://os.mos.ru
BuildArch: noarch
Requires: apt
Source: %name-%version.tar

%description
%summary.

%description -l ru_RU.UTF-8
Утилиты apt-hold и apt-unhold для быстрого создания файлов заморозки пакетов по правилам:
https://www.altlinux.org/Hold

%prep
%setup

%install
mkdir -p %buildroot%_bindir

install -pm755 apt-hold %buildroot%_bindir/apt-hold
install -pm755 apt-unhold %buildroot%_bindir/apt-unhold

%files
%_bindir/apt-hold
%_bindir/apt-unhold

%changelog
* Fri Jan 20 2023 Artem Proskurnev <tema@altlinux.org> 0.1-alt2
- handling a situation with an empty $EDITOR
- interrupting the script in case of an error
- the tips of the shellcheck have been applied

* Thu Jan 19 2023 Artem Proskurnev <tema@altlinux.org> 0.1-alt1
- Init

