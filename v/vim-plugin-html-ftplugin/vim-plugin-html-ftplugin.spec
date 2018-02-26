Name: vim-plugin-html-ftplugin
Version: 0.28.2
Release: alt1

Summary: Vim plugin for easy HTML editing
Summary(ru_RU.CP1251): Плагин для простого редактирования файлов HTML
Group: Editors
License: GPL
Url: %vim_script_url 453
BuildArch: noarch

Source: %name-%version.tar.bz2
Patch0: %name-0.28.2-alt-disable-default.patch
Patch1: %name-0.23.2-alt-charsets.patch

PreReq: vim-common >= 4:6.3.007-alt1
BuildPreReq: vim-devel

Packager: VIm Plugins Development Team <vim-plugins@packages.altlinux.org>

%post
%update_vimhelp

%postun
%clean_vimhelp

%description
This is a set of HTML mappings and menus which help with HTML editing.
You can insert HTML tags with menus or key mappings. You can also open
HTML file you edit in your web browser (supports Mozilla, Netscape,
Opera and Lynx).

To enable this plugin define "use_html_ftplugin" variable somewhere
in your .vimrc file.

%description -l ru_RU.CP1251
Этот плагин помогает редактировать HTML-файлы, позволяя вставлять
HTML-теги при помощи меню или клавиатурных привязок. Кроме того, он
позволяет открывать редактируемый файл в браузере (поддерживаются
Mozilla, Netscape, Opera и Lynx).

Чтобы включить этот плагин, определите переменную use_html_ftplugin в
своем файле .vimrc.

%prep
%setup
%patch0 -p1
%patch1 -p1
mkdir plugin
mv *.vim plugin

%install
mkdir -p %buildroot%vim_runtime_dir
cp -a {bitmaps,doc,plugin,ftplugin} %buildroot%vim_runtime_dir

%files 
%vim_runtime_dir/bitmaps/*
%vim_doc_dir/*
%vim_plugin_dir/*
%vim_ftplugin_dir/*

%changelog
* Tue Jul 31 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.28.2-alt1
- 0.28.2

* Wed Dec 13 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.23.2-alt1
- 0.23.2
- add koi8-r and cp1251 to the list of charsets supported by ;ct macro

* Fri Feb 10 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.18-alt1
- 0.18

* Sun Aug 28 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.16-alt1
- 0.16

* Sat May 28 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.15.1-alt1
- 0.15.1

* Wed Oct 13 2004 Andrey Rahmatullin <wrar@altlinux.ru> 0.15-alt1
- initial build
