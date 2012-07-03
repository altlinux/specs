# Generated File.
%setup_docs_module shell_efficiency ru

Name: %packagename
Version: 0.1.1
Release: alt1

Summary: Shell efficiency: economy of gestures
Summary(ru_RU.KOI8-R): Удобство shell: экономия движений
License: %fdl
Url: http://heap.altlinux.ru/HeapLinks/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-shell_efficiency-kirill
Provides: docs-shell_efficiency-kirill 
Obsoletes: docs-shell_efficiency-kirill

Source: %name-%version.tar

%description 
Shell tools for efficient work with command line: command line editing, commands history, completion, patterns and aliases.

%description -l ru_RU.KOI8-R
Описание средств эффективной работы с командной строкой в bash: редактирование ввода, история команд, сокращения (alias), достраивание и шаблоны.

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
* Thu Jun 26 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt1
- tiny punctuation fix (thanks bertis@)

* Sat Apr 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-shell_efficiency-kirill
  + added Provides/Obsoletes

* Sun Jan 13 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-shell_efficiency-kirill package

* Fri Mar 24 2006 Kirill Maslinsky <kirill@altlinux.ru> 060324-alt1
- Auto rebuild with new version.

* Mon Mar 13 2006 Kirill Maslinsky <kirill@altlinux.ru> 060313-alt1
- Auto rebuild with new version.

* Tue Dec 20 2005 Kirill Maslinsky <kirill@altlinux.ru> 051220-alt1
- Auto build with new version.

