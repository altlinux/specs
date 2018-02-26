%define plugname CRefVIM
%define plugver  1.0.4

Name: vim-plugin-%plugname
Version: %plugver
Release: alt1

Summary: C language reference manual designed for Vim
Summary(ru_RU.CP1251): —правочник по €зыку C дл€ просмотра в Vim
Group: Development/C
License: GPL & FDL
Url: %vim_script_url 614
BuildArch: noarch

Source: crefvim.zip

PreReq: vim-common >= 4:6.3.007-alt1
BuildPreReq: vim-devel unzip

Packager: VIm Plugins Development Team <vim-plugins@packages.altlinux.org>

%post
%update_vimhelp

%postun
%clean_vimhelp

%description
This package contains the C reference manual and Vim plugin to view it
as Vim help. You can also use mappings \cr (opens help for keyword under
cursor) and \cw (opens prompt for keyword to search for).

%description -l ru_RU.CP1251
—правочник по €зыку C и плагин дл€ Vim, позвол€ющий легко просматривать его
при помощи справочной системы Vim. »спользуйте \cr дл€ получени€ справки по
слову под курсором и \cw дл€ ввода интересующего слова вручную.

%prep
%setup -q -n crefvim

%install
%__mkdir_p %buildroot%vim_runtime_dir
%__cp -a {after,doc,plugin} %buildroot%vim_runtime_dir

%files 
%defattr(644,root,root)
%vim_doc_dir/*
%vim_plugin_dir/*
%vim_after_syntax_dir/*

%changelog
* Mon Nov 29 2004 Andrey Rahmatullin <wrar@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Thu Sep 2 2004 Andrey Rahmatullin <wrar@altlinux.ru> 1.0.3-alt2
- enable plugin by default
- add Packager:
- add Russian summary and description
- minor spec cleanup

* Wed Aug 18 2004 Andrey Rahmatullin <wrar@altlinux.ru> 1.0.3-alt1
- initial build
