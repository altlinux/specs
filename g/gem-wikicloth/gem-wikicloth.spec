%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname wikicloth

Name:          gem-wikicloth
Version:       0.8.3.17
Release:       alt1
Summary:       Ruby implementation of the MediaWiki markup language
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/nricciar/wikicloth
Vcs:           https://github.com/nricciar/wikicloth.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0
%if_enabled check
BuildRequires: gem(activesupport) >= 0
BuildRequires: gem(builder) >= 0
BuildRequires: gem(expression_parser) >= 0
BuildRequires: gem(htmlentities) >= 0
BuildRequires: gem(i18n) >= 0
BuildRequires: gem(nokogiri) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(twitter-text) >= 2.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names bare
Requires:      gem(builder) >= 0
Requires:      gem(expression_parser) >= 0
Requires:      gem(htmlentities) >= 0
Requires:      gem(nokogiri) >= 0
Requires:      gem(twitter-text) >= 2.1
Provides:      gem(wikicloth) = 0.8.3.17

%description
Ruby implementation of the MediaWiki markup language.


%if_enabled    doc
%package       -n gem-wikicloth-doc
Version:       0.8.3.17
Release:       alt1
Summary:       Ruby implementation of the MediaWiki markup language documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета wikicloth
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(wikicloth) = 0.8.3.17

%description   -n gem-wikicloth-doc
Ruby implementation of the MediaWiki markup language documentation files.

%description   -n gem-wikicloth-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета wikicloth.
%endif


%if_enabled    devel
%package       -n gem-wikicloth-devel
Version:       0.8.3.17
Release:       alt1
Summary:       Ruby implementation of the MediaWiki markup language development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета wikicloth
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(wikicloth) = 0.8.3.17
Requires:      gem(activesupport) >= 0
Requires:      gem(i18n) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(test-unit) >= 0

%description   -n gem-wikicloth-devel
Ruby implementation of the MediaWiki markup language development package.

%description   -n gem-wikicloth-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета wikicloth.
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
%doc MIT-LICENSE README README.textile
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-wikicloth-doc
%doc MIT-LICENSE README README.textile
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-wikicloth-devel
%doc MIT-LICENSE README README.textile
%endif


%changelog
* Sun Jan 26 2025 Pavel Skrylev <majioa@altlinux.org> 0.8.3.17-alt1
- ^ 0.8.3.1 -> 0.8.3.17

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.8.3.1-alt1
- ^ 0.8.3 -> 0.8.3[.1]

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.8.3-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
