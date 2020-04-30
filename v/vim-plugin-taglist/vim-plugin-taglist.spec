%define plugname taglist

Name: vim-plugin-%plugname
Version: 4.6
Release: alt1

Summary: Source code browser for Vim
Group: Editors
License: BSD-2-Clause

Url: https://www.vim.org/scripts/script.php?script_id=273
BuildArch: noarch

Source: taglist-%version.tar.gz
Patch: %name-4.6-alt-tag_list.patch

Requires: ctags
BuildPreReq: vim-devel

Packager: VIm Plugins Development Team <vim-plugins@packages.altlinux.org>

%description
This plugin can help you to browse through your source files.
It uses ctags(1), but doesn't need tags files to be built.

Use ":help taglist.txt" to get help

%description -l ru_RU.UTF-8
Этот плагин поможет вам при просмотре исходников. Он использует ctags(1),
но не требует создания файла с тэгами.

Для просмотра справки используйте команду «:help taglist.txt»

%prep
%setup -n taglist-%version
%patch -p2

%install
mkdir -p %buildroot%vim_runtime_dir
cp -a {doc,plugin} %buildroot%vim_runtime_dir

%files
%vim_doc_dir/*
%vim_plugin_dir/*

%changelog
* Thu Apr 30 2020 Fr. Br. George <george@altlinux.ru> 4.6-alt1
- Version update
- New upstream
- Drop no_default patch

* Wed Oct 24 2018 Grigory Ustinov <grenka@altlinux.org> 4.5-alt1.1
- Replace %%vim_script_url macro on real url.

* Fri Feb 22 2008 Andrey Rahmatullin <wrar@altlinux.ru> 4.5-alt1
- 4.5

* Tue Jul 31 2007 Andrey Rahmatullin <wrar@altlinux.ru> 4.4-alt1
- 4.4

* Fri Apr 20 2007 Andrey Rahmatullin <wrar@altlinux.ru> 4.3-alt1
- 4.3
- fix patch (vsu@)

* Wed Dec 13 2006 Andrey Rahmatullin <wrar@altlinux.ru> 4.2-alt1
- 4.2

* Sun Jul 02 2006 Andrey Rahmatullin <wrar@altlinux.ru> 4.0-alt0.4
- 4.0b4

* Fri Feb 10 2006 Andrey Rahmatullin <wrar@altlinux.ru> 4.0-alt0.3
- 4.0b3

* Sun Aug 28 2005 Andrey Rahmatullin <wrar@altlinux.ru> 4.0-alt0.2
- 4.0b2

* Sat May 28 2005 Andrey Rahmatullin <wrar@altlinux.ru> 4.0-alt0.1
- 4.0b1

* Thu Sep 2 2004 Andrey Rahmatullin <wrar@altlinux.ru> 3.4-alt1
- new version
- add Packager:
- add Russian description
- minor spec cleanup

* Thu Aug 19 2004 Andrey Rahmatullin <wrar@altlinux.ru> 3.3-alt1.1
- fix buildreqs

* Wed Aug 18 2004 Andrey Rahmatullin <wrar@altlinux.ru> 3.3-alt1
- initial build
