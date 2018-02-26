# Generated File.
%setup_docs_module scheme_article1 ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Scheme -- your new language
Summary(ru_RU.KOI8-R): Знакомьтесь -- язык Scheme
License: %fdl
Url: http://heap.altlinux.ru/kirill/scheme_article_1/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-scheme_article_1-kirill
Provides: docs-scheme_article_1-kirill
Obsoletes: docs-scheme_article_1-kirill

Source: %name-%version.tar

%description
Introductary article into Scheme programming language.

%description -l ru_RU.KOI8-R
Вводная статья про язык scheme, ориентированная на школьников (старшеклассников).

%prep
%setup

%build
%docs_module_build "html" "index.html"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Tue Apr 15 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-scheme_article_1-kirill
  + added Provides/Obsoletes

* Tue Apr 15 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-scheme_article_1-kirill package

* Fri Apr 07 2006 Kirill Maslinsky <kirill@altlinux.ru> 060407-alt1
- Initial build for Sisyphus.

