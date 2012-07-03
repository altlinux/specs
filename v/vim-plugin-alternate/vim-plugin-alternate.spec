Name: vim-plugin-alternate
Version: 2.18
Release: alt1

Summary: Plugin for quick switching between source and header files
Summary(ru_RU.CP1251): Плагин для быстрого переключения между исходными и заголовочными файлами
Group: Editors
License: Distributable
Url: %vim_script_url 31
BuildArch: noarch

Source0: a.vim
Source1: alternate.txt
Patch: %name-2.10-alt-disable-default.patch

PreReq: vim-common >= 4:6.3.007-alt1
BuildPreReq: vim-devel

Packager: VIm Plugins Development Team <vim-plugins@packages.altlinux.org>

%description
This plugin allows quick switching between file pairs with same name
and different extensions (for example, foo.c & foo.h). By default it
supports C, C++ and ADA95.

To enable this plugin define "use_alternate_plugin" variable somewhere
in your .vimrc file.

%description -l ru_RU.CP1251
Этот плагин позволяет быстро переключаться между парами файлов с одним
именем и разными расширениями (например, foo.c и foo.h). По умолчанию он
поддерживает C, C++ и ADA95.

Чтобы включить этот плагин, определите переменную use_alternate_plugin в
своем файле .vimrc.

%prep
%setup -cT
cp %SOURCE0 .
cp %SOURCE1 .
%patch -p0

%install
mkdir -p %buildroot{%vim_plugin_dir,%vim_doc_dir}
install -m644 a.vim %buildroot%vim_plugin_dir
install -m644 alternate.txt %buildroot%vim_doc_dir

%post
%update_vimhelp
%postun
%clean_vimhelp

%files
%vim_plugin_dir/a.vim
%vim_doc_dir/alternate.txt

%changelog
* Tue Jul 31 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.18-alt1
- 2.18

* Tue Apr 17 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.16-alt1
- 2.16

* Mon Dec 04 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.15-alt1
- 2.15

* Sun Jul 02 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.14-alt1
- 2.14

* Sat May 28 2005 Andrey Rahmatullin <wrar@altlinux.ru> 2.12-alt1
- 2.12

* Wed Oct 20 2004 Andrey Rahmatullin <wrar@altlinux.ru> 2.11a-alt1
- new version

* Sun Sep 26 2004 Andrey Rahmatullin <wrar@altlinux.ru> 2.11-alt1
- new version

* Thu Sep 16 2004 Andrey Rahmatullin <wrar@altlinux.ru> 2.10-alt1
- new version

* Sun Sep 12 2004 Andrey Rahmatullin <wrar@altlinux.ru> 2.9-alt1
- new version

* Thu Sep 02 2004 Andrey Rahmatullin <wrar@altlinux.ru> 2.8-alt1.1
- add Packager:
- add Russian summary and description

* Tue Aug 17 2004 Andrey Rahmatullin <wrar@altlinux.ru> 2.8-alt1
- initial build

