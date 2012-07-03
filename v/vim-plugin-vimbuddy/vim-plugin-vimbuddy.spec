%define plugname vimbuddy

Name: vim-plugin-%plugname
Version: 0.9.2
Release: alt1

Summary: An absolutely unuseful Vim plugin
Summary(ru_RU.CP1251): јбсолютно бесполезный плагин дл€ Vim

Group: Editors
License: Distributable
Url: %vim_script_url 8
BuildArch: noarch

Source: %plugname.vim

PreReq: vim-common >= 4:6.3.007-alt1
BuildPreReq: vim-devel

Packager: VIm Plugins Development Team <vim-plugins@packages.altlinux.org>

%description
This little plugin puts an animated smiley on your status line.
To use it put the string "%%{VimBuddy()}" into your 'statusline' variable.

%description -l ru_RU.CP1251
Ётот небольшой плагин добавл€ет в строку состо€ни€ анимированный смайлик.
„тобы использовать его, добавьте строку "%%{VimBuddy()}" в переменную
statusline.

%prep
%setup -cT
cp %SOURCE0 .

%install
mkdir -p %buildroot%vim_plugin_dir
install -m644 %plugname.vim %buildroot%vim_plugin_dir

%files
%vim_plugin_dir/%plugname.vim

%changelog
* Fri Aug 10 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Sat Oct 01 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.9.1-alt2
- fix variable names for vim7 (from Gentoo)

* Thu Sep 02 2004 Andrey Rahmatullin <wrar@altlinux.ru> 0.9.1-alt1.1
- add Packager:
- add Russian summary and description

* Wed Aug 18 2004 Andrey Rahmatullin <wrar@altlinux.ru> 0.9.1-alt1
- initial build
