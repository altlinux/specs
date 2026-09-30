%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname github-markup

Name:          gem-github-markup
Version:       6.0.0
Release:       alt1
Summary:       The code GitHub uses to render README.markup
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/github/markup
Vcs:           https://github.com/github/markup.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(RedCloth) >= 0
BuildRequires: gem(activesupport) >= 7.1
BuildRequires: gem(asciidoctor) >= 2.0.26
BuildRequires: gem(commonmarker) >= 2.8.2
BuildRequires: gem(creole) >= 0.5.0
BuildRequires: gem(github-linguist) >= 7.1.3
BuildRequires: gem(html-pipeline) >= 3.2
BuildRequires: gem(minitest) >= 6.0
BuildRequires: gem(nokogiri) >= 1.18.9
BuildRequires: gem(nokogiri-diff) >= 0.3.0
BuildRequires: gem(org-ruby) = 0.9.12
BuildRequires: gem(rake) >= 13
BuildRequires: gem(rdoc) >= 6.1.1
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(twitter-text) >= 1.14
BuildRequires: gem(wikicloth) >= 0.8.3
BuildConflicts: gem(activesupport) >= 8.2
BuildConflicts: gem(asciidoctor) >= 2.1
BuildConflicts: gem(creole) >= 0.6
BuildConflicts: gem(html-pipeline) >= 4
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(nokogiri-diff) >= 0.4
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency nokogiri >= 1.18.9
%ruby_use_gem_dependency rdoc >= 6.1.1
%ruby_use_gem_dependency simplecov >= 0.17
%ruby_use_gem_dependency activesupport >= 7.1
%ruby_use_gem_dependency wikicloth >= 0.8.3
%ruby_use_gem_dependency commonmarker >= 2.8.2
%ruby_use_gem_dependency twitter-text >= 1.14
Requires:      ruby >= 3.3.0
Provides:      gem(github-markup) = 6.0.0

%description
This gem is used by GitHub to render any fancy markup such as Markdown, Textile,
Org-Mode, etc. Fork it and add your own!


%package       -n github-markup
Version:       6.0.0
Release:       alt1
Summary:       The code GitHub uses to render README.markup executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета github-markup
Group:         Other
BuildArch:     noarch

Requires:      gem(github-markup) = 6.0.0

%description   -n github-markup
The code GitHub uses to render README.markup executable(s).

This gem is used by GitHub to render any fancy markup such as Markdown, Textile,
Org-Mode, etc. Fork it and add your own!

%description   -n github-markup -l ru_RU.UTF-8
Исполнямка для самоцвета github-markup.


%if_enabled    doc
%package       -n gem-github-markup-doc
Version:       6.0.0
Release:       alt1
Summary:       The code GitHub uses to render README.markup documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета github-markup
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(github-markup) = 6.0.0

%description   -n gem-github-markup-doc
The code GitHub uses to render README.markup documentation files.

This gem is used by GitHub to render any fancy markup such as Markdown, Textile,
Org-Mode, etc. Fork it and add your own!

%description   -n gem-github-markup-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета github-markup.
%endif


%if_enabled    devel
%package       -n gem-github-markup-devel
Version:       6.0.0
Release:       alt1
Summary:       The code GitHub uses to render README.markup development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета github-markup
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(github-markup) = 6.0.0
Requires:      gem(RedCloth) >= 0
Requires:      gem(activesupport) >= 7.1
Requires:      gem(asciidoctor) >= 2.0.26
Requires:      gem(commonmarker) >= 2.8.2
Requires:      gem(creole) >= 0.5.0
Requires:      gem(github-linguist) >= 7.1.3
Requires:      gem(html-pipeline) >= 3.2
Requires:      gem(minitest) >= 6.0
Requires:      gem(nokogiri) >= 1.18.9
Requires:      gem(nokogiri-diff) >= 0.3.0
Requires:      gem(org-ruby) = 0.9.12
Requires:      gem(rake) >= 13
Requires:      gem(rdoc) >= 6.1.1
Requires:      gem(redcarpet) >= 0
Requires:      gem(rexml) >= 0
Requires:      gem(simplecov) >= 0.17
Requires:      gem(twitter-text) >= 1.14
Requires:      gem(wikicloth) >= 0.8.3
Conflicts:     gem(activesupport) >= 8.2
Conflicts:     gem(asciidoctor) >= 2.1
Conflicts:     gem(creole) >= 0.6
Conflicts:     gem(html-pipeline) >= 4
Conflicts:     gem(minitest) >= 7
Conflicts:     gem(nokogiri-diff) >= 0.4
Conflicts:     gem(rake) >= 14

%description   -n gem-github-markup-devel
The code GitHub uses to render README.markup development package.

This gem is used by GitHub to render any fancy markup such as Markdown, Textile,
Org-Mode, etc. Fork it and add your own!

%description   -n gem-github-markup-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета github-markup.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md HISTORY.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n github-markup
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md HISTORY.md LICENSE README.md
%_bindir/github-markup

%if_enabled    doc
%files         -n gem-github-markup-doc
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md HISTORY.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-github-markup-devel
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md HISTORY.md LICENSE README.md
%endif


%changelog
* Sun May 31 2026 Pavel Skrylev <majioa@altlinux.org> 6.0.0-alt1
- ^ 4.0.0 -> 6.0.0

* Thu Jun 03 2021 Pavel Skrylev <majioa@altlinux.org> 4.0.0-alt1
- + packaged gem with Ruby Policy 2.0
