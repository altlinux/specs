# Generated File.
%setup_docs_module cmc_communication_stand ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Development of public communication center with integrated authentication system
Summary(ru_RU.KOI8-R): Разработка публичного коммуникационного центра с единой системой авторизации доступа
License: %fdl
Url: http://heap.altlinux.ru/HeapLinks/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-CMC_Communication_Stand-george
Provides: docs-CMC_Communication_Stand-george
Obsoletes: docs-CMC_Communication_Stand-george

Source: %name-%version.tar

%description
Report on work at CS department of Moscow State University: sendmail, ClamAV, SpamAssassin, SquirrelMail, Jabberd2, Samba and OpenLDAP on a single unit or several units; recommendations on changing of client software and extending functionality. 

%description -l ru_RU.KOI8-R
Отчёт о проделанной на ф-те ВМиК МГУ работе: sendmail, ClamAV, SpamAssassin, SquirrelMail, Jabberd2, Samba и OpenLDAP на одной стендовой машине либо на нескольких; рекомендации по выбору клиентского ПО и наращиванию дополнительных возможностей. Выполнено на FreeBSD5.

%prep
%setup

%build
%docs_module_build "m-k" "index.m-k"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Mon Nov 10 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- fixed typo in Summary

* Sun Jun 01 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- package renamed: docs-CMC_Communication_Stand-george -> docs-cmc_communication_stand
- build with rpm-build-docs-experimental
- used macro for License tag (rpm-build-licenses)

* Thu Feb 02 2006 Kirill Maslinsky <kirill@altlinux.ru> 060201-alt1
- Auto build with new version.

