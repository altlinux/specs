# Generated File.
%setup_docs_module xterm_class ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Linux class in an hour, or X-terminals, thin and lazy
Summary(ru_RU.KOI8-R): Linux-класс за час, или X-терминалы, тонкие и ленивые
License: distributable
Url: http://heap.altlinux.ru/HeapLinks/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3

# replace docs-XTerm_Class-george
Provides:  docs-XTerm_Class-george
Obsoletes:  docs-XTerm_Class-george

Source: %name-%version.tar

%description
Story about a Linux class where appeared Linux-server, and how administrator got TravelCD with X-terminal mode and what happened next.

%description -l ru_RU.KOI8-R
История о том, как в компьютерном классе появился Linux-сервер, как администратор обзавёлся Travel CD с режимом X-терминала, и что из этого вышло, а что -- нет

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
* Sun Jun 01 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-XTerm_Class-george
  + added Provides/Obsoletes

* Wed Feb 06 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-XTerm_Class-george package

* Mon Mar 20 2006 Kirill Maslinsky <kirill@altlinux.ru> 3.0.007-alt1
- Auto rebuild with new version.

* Thu Feb 16 2006 Kirill Maslinsky <kirill@altlinux.ru> 3.0.004-alt1
- initial build

