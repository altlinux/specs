%define plugname po
%define plugtype after-ftplugin
%define plugver  1.20

Name: vim-plugin-%plugname-%plugtype
Version: %plugver
Release: alt1

Summary: FtPlugin for easier editing of po files
Group: Editors
License: Distributable
Url: %vim_script_url 695
BuildArch: noarch

Source: %plugname.vim
Patch: %name-1.11-alt-disable-default.patch

PreReq: vim-common >= 4:6.3.007-alt1
BuildPreReq: vim-devel

Packager: VIm Plugins Development Team <vim-plugins@packages.altlinux.org>

%description
This is a ftplugin for editing PO files (GNU Gettext -- the GNU i18n
and l10n system). It automates over a dozen of frequent tasks that 
occur while editing files of this type (such as quick jumping to next/prev
untranslated or fuzzy entries and browsing through msgfmt errors).

To enable this plugin define "use_po_after_ftplugin" variable somewhere
in your .vimrc file.

%description -l ru_RU.CP1251
ѕлагин дл€ редактировани€ .po файлов. ќн позвол€ет автоматизировать более
дес€тка операций, таких, как быстрое перемещение к следующей/предыдущей
непереведенной или черновой записи и удобный просмотр ошибок msgfmt.

„тобы включить этот плагин, определите переменную use_po_after_ftplugin в
своем файле .vimrc.

%prep
%setup -cT
%__cp %SOURCE0 .
%patch -p0

%install
%__mkdir_p %buildroot%vim_after_ftplugin_dir
%__install -m644 %plugname.vim %buildroot%vim_after_ftplugin_dir

%files
%vim_after_ftplugin_dir/%plugname.vim

%changelog
* Sat May 28 2005 Andrey Rahmatullin <wrar@altlinux.ru> 1.20-alt1
- 1.2
- fix Url:

* Mon Dec 13 2004 Andrey Rahmatullin <wrar@altlinux.ru> 1.11-alt2
- fix encoding specification in %%description
- change Packager:

* Tue Aug 17 2004 Andrey Rahmatullin <wrar@altlinux.ru> 1.11-alt1
- initial build
