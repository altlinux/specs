# Generated File.
%setup_docs_module shell_intro ru

Name: %packagename
Version: 0.1.1
Release: alt1

Summary: Command line interpreter (shell)
Summary(ru_RU.KOI8-R): Интерпретатор командной строки (shell)
License: %fdl
Url: http://heap.altlinux.ru/HeapLinks/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-shell_intro-kirill
Provides: docs-shell_intro-kirill
Obsoletes: docs-shell_intro-kirill

Source: %name-%version.tar

%description
Short intro into command line interface: what is shell and what it is for, command line syntax (parameters, options, synopsis), the answer to the ``all Linux commands list'' request, survey of documentation subsistem and environment variables. Not included: terminal and its relation to command line interface, input/output redirection, command line candies and shell scripting.

%description -l ru_RU.KOI8-R
Краткое введение в работу с командной строкой: что такое shell и зачем он нужен, синтаксис командной строки (параметры, ключи, синопсис), ответ на вопрос о ``списке всех команд Linux'', обзор подсистемы документации и работы с переменными окружения. Не рассматриваются: понятие терминал и его связь  с командной строкой, перенаправление ввода/вывода, удобства для работы с командной строкой и программирование на shell.

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
* Mon Jun 16 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt1
- updated date & cal command examples

* Sat Apr 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-shell_intro-kirill
  + added Provides/Obsoletes

* Sun Jan 13 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-shell_intro-kirill package

* Mon Mar 13 2006 Kirill Maslinsky <kirill@altlinux.ru> 060313-alt1
- Auto rebuild with new version.

* Wed Jan 11 2006 Kirill Maslinsky <kirill@altlinux.ru> 060108-alt1
- Auto build with new version.

