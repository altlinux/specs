Name: builder-useradd
Version: 1.6
Release: alt1
Summary: Add user and configure hasher and gear for him/her
License: GPLv2+
Group: System/Configuration/Other
Packager: Dmitry Terekhin <jqt4@altlinux.org>
Requires: git-core gear hasher
Url: https://git.altlinux.org/people/jqt4/packages/builder-useradd.git
BuildArch: noarch
Source0: %name
Source1: README.ru
Source2: README.en

%description
The builder-useradd package installs components of the Alt building environment
into the system, namely, gear and hasher, and the git-core needed for their work.
Also installs the builder-useradd script, which allows you to quickly configure
necessary for working with gear and hasher system parameters and start building
packages.

%description -l ru_RU.UTF-8
Пакет builder-useradd устанавливает в систему компоненты сборочной среды Альт,
а конкретно gear и hasher, и нужный для их работы git-core.
Также устанавливает скрипт builder-useradd, который позволяет быстро настроить
нужные для работы с gear и hasher параметры системы и начать собирать пакеты.

%install
install -Dpm 0755 %SOURCE0 %buildroot%_sbindir/%name
install -m 644 %SOURCE1 ./
install -m 644 %SOURCE2 ./

%files
%doc README.ru README.en
%_sbindir/%name

%changelog
* Sun Dec 04 2022 Anton Midyukov <antohami@altlinux.org> 1.6-alt1
- remove Yandex Mirror from generated apt source lists.
  Yandex Mirror is broken.

* Fri Oct 14 2022 Anton Midyukov <antohami@altlinux.org> 1.5-alt1
- add settings for for comfortable work

* Thu Mar 03 2022 Anton Midyukov <antohami@altlinux.org> 1.4-alt1
- fix $HOME directory definition for not x86 systems

* Wed Mar 02 2022 Anton Midyukov <antohami@altlinux.org> 1.3-alt1
- fix links to repositories for ports Sisyphus in generated source lists

* Tue Jan 18 2022 Anton Midyukov <antohami@altlinux.org> 1.2-alt1
- new version:
  + Add sign repo in generated sources.lists for ports
  + Fix generated sources.lists for ports of stable branches

* Mon Jan 17 2022 Anton Midyukov <antohami@altlinux.org> 1.1-alt1
- new version:
  + Unify code style and set -efu
  + Fix get variables for $USER
  + Fix owner for created files
  + Fix execution for an existing user
  + Do not add everything 'rpm-dir file://$HOME/hasher/repo'
  + Add config for mkimage-profiles
  + Add apt.conf's for supported branches

* Fri Aug 09 2019 Dmitry Terekhin <jqt4@altlinux.org> 1.0-alt1
- Prepared for publication

* Tue Mar 19 2019 Dmitry Terekhin <jqt4@altlinux.org> 0.1-alt1
- Initial build
