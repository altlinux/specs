Name: apt-aliases
Version: 0.0.20230829
Release: alt3

Summary: "apt" command in addition to "apt-get" and friends
License: MIT
Group: System/Configuration/Packaging

# initial one: http://interface31.ru/tech_it/files/apt_aliases.sh
Url: http://t.me/interface31/1569
Vcs: http://github.com/oldcopy/apt_aliases_alt
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

Requires: apt < 1.0

BuildArch: noarch

Summary(ru_RU.UTF-8): команда "apt" вдобавок к "apt-get" со товарищи

%define bashrcdir %_sysconfdir/profile.d

%description
ALT is a fairly distinctive distribution, the main difference of which
is that it uses APT to manage RPM packages.  Switching to ALT from Debian
or Ubuntu is thus significantly simplified as one doesn't need to learn
a new package manager.

But there are some inconveniences, the main one is that ALT uses
apt-get command to manage packages while DEB-based distributions use apt.

This is really inconvenient, since you type one command from memory and
only after pressing Enter do you realize that you had to enter another one.
And apt is just shorter.

Therefore, we wrote a small script that adds apt command syntax support
for ALT.

The script is not comprehensive but does support all the basic apt commands.
You can easily expand it yourself if neccessary.

%description -l ru_RU.UTF-8
Альт – достаточно самобытный дистрибутив, главным отличием которого является
то, что он использует APT для управления RPM-пакетами. Таким образом переход
на Альт с Debian или Ubuntu существенно упрощается, так как не нужно изучать
новый менеджер пакетов.

Но есть и некоторые неудобства, основное из них то, что Альт для управления
пакетами использует команду apt-get, в то время как в DEB-based дистрибутивах
везде используется apt.

Это действительно неудобно, так как вы по памяти набираете одну команду и
только после нажатия Enter вспоминаете, что надо было вводить другую.
Ну и apt просто короче.

Поэтому мы написали небольшой скрипт, который добавляет в Альт поддержку команд
в синтаксисе apt.

Скрипт не является всеобъемлющим, но поддерживает все основные команды apt.
При необходимости можно легко расширить его самостоятельно.

%prep
%setup

%build

%install
install -pDm755 apt_aliases.sh %buildroot%bashrcdir/apt_aliases.sh

%files
%config(noreplace) %bashrcdir/apt_aliases.sh
%doc LICENSE README.md

%changelog
* Wed Aug 30 2023 Michael Shigorin <mike@altlinux.org> 0.0.20230829-alt3
- move to /etc/profile.d so zsh gets this too
- ah! (closes: #41660)

* Wed Aug 30 2023 Michael Shigorin <mike@altlinux.org> 0.0.20230829-alt2
- move to upstream git as the source
- added R: apt < 1.0 (where apt utility had appeared)

* Tue Aug 29 2023 Michael Shigorin <mike@altlinux.org> 0.0.20230829-alt1
- initial release (thanks Andrey Uvarov of interface31.ru fame,
  both the blog and telegram channel are highly recommended)
