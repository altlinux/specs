# Generated File.
%setup_docs_module linux_intro ru
Name: %packagename
Version: 0.1
Release: alt2

Summary: Introduction into Linux
Summary(ru_RU.KOI8-R): Введение в ОС Linux
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-LinuxIntro-george
Provides: docs-LinuxIntro-george
Obsoletes: docs-LinuxIntro-george

Source: %name-%version.tar

%description 
Free textbook on Linux. Basic level. Examples based on ALT Linux Master 2.4.

%description -l ru_RU.KOI8-R
Учебник по азам работы с Linux: командная строка, процессы и права доступа, диски и файловые системы, сеть, X11, пакеты и дистрибутивы, программное наполнение. Написан на материале ALT Linux Master 2.4. Рассчитан на начинающего пользователя. В настоящее время используется несколькими ВУЗами в учебном процессе.

%prep
%setup

%build
%docs_module_build "html" "Application.html Boot.html Editors.html Etc.html Filesystem.html Filesystem_use.html Linux.html Mount.html Net.html Package.html Permissions.html Pipeline.html Preface.html Processes.html Service.html Session.html Shell.html Terminal.html X11.html index.html"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Sun Jun 01 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-LinuxIntro-george
  + added Provides/Obsoletes

* Fri Jan 25 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-LinuxIntro-george package

* Wed Mar 22 2006 Kirill Maslinsky <kirill@altlinux.ru> 060320-alt1
- Auto rebuild with new version.

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 051103-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Thu Nov 10 2005 Kirill Maslinsky <kirill@altlinux.ru> 051103-alt1
- Auto rebuild with new version.

* Tue Oct 25 2005 Kirill Maslinsky <kirill@altlinux.ru> 051023-alt1
- Auto build with new version.

