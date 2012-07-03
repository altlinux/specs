%define plugname vimirc

Name: vim-plugin-%plugname
Version: 0.9.28
Release: alt1

Summary: IRC client plugin for VIm
Summary(ru_RU.CP1251): IRC-клиент для VIm

Group: Networking/IRC
License: Same as for Vim
Url: %vim_script_url 931
BuildArch: noarch

Source: %plugname.vim

PreReq: vim-common >= 4:6.3.007-alt1
BuildPreReq: vim-devel

# FIXME
Requires: perl(Encode.pm) perl(Fcntl.pm) perl(IO/Select.pm) perl(IO/Socket.pm)

Packager: VIm Plugins Development Team <vim-plugins@packages.altlinux.org>

%description
This is an IRC client which runs on Vim. It has some of the features IRC
users might expect, such as multiple servers connectivity, DCC SEND/CHAT
features etc. Read the plugin file for more feature info and usage
instructions.

%description -l ru_RU.CP1251
Плагин для VIm с функциональностью IRC-клиента. Информацию о возможностях
и советы по использованию вы можете найти в самом файле плагина.

Быстрый старт: запустите VIm и выполните команду :VimIRC. После подключения
к irc.freenode.net нажмите i, чтобы перейти в режим ввода IRC-команд.
Теперь можно выдавать обычные команды, такие как /join. В окнах каналов
режим ввода сообщения включается также нажатием i.

%prep
%setup -cT
%__cp %SOURCE0 .

%install
%__mkdir_p %buildroot%vim_plugin_dir
%__install -m644 %plugname.vim %buildroot%vim_plugin_dir

%files
%vim_plugin_dir/%plugname.vim

%changelog
* Sat May 28 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.9.28-alt1
- 0.9.28

* Fri Mar 11 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.9.10-alt1
- 0.9.10

* Fri Jan 21 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.8.11-alt1
- 0.8.11

* Thu Jan 20 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.8.10-alt1
- 0.8.10

* Wed Jan 19 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.8.9-alt1
- initial build

