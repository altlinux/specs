%define        gemname jekyll

Name:          gem-jekyll
Version:       4.3.2
Release:       alt1
Summary:       Jekyll is a simple, blog-aware, static site generator
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jekyll/jekyll
Vcs:           https://github.com/jekyll/jekyll.git
Packager:      Dmitriy Voropaev <voropaevdmtr@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(launchy) >= 2.3
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(cucumber) >= 5.1.2
BuildRequires: gem(httpclient) >= 0
BuildRequires: gem(jekyll_test_plugin) >= 0
BuildRequires: gem(jekyll_test_plugin_malicious) >= 0
BuildRequires: gem(memory_profiler) >= 0
BuildRequires: gem(nokogiri) >= 1.7
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rspec-mocks) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-minitest) >= 0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rake) >= 0
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(minitest-profile) >= 0
BuildRequires: gem(minitest-reporters) >= 0
BuildRequires: gem(shoulda) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(jekyll-coffeescript) >= 0
BuildRequires: gem(jekyll-feed) >= 0.9
BuildRequires: gem(jekyll-gist) >= 0
BuildRequires: gem(jekyll-paginate) >= 0
BuildRequires: gem(jekyll-redirect-from) >= 0
BuildRequires: gem(kramdown-syntax-coderay) >= 0
BuildRequires: gem(matrix) >= 0
BuildRequires: gem(mime-types) >= 3.0
BuildRequires: gem(psych) >= 4.0
BuildRequires: gem(rdoc) >= 6.0
BuildRequires: gem(tomlrb) >= 0
BuildRequires: gem(classifier-reborn) >= 2.2
BuildRequires: gem(liquid-c) >= 4.0
BuildRequires: gem(yajl-ruby) >= 1.4
BuildRequires: gem(jekyll-avatar) >= 0
BuildRequires: gem(jekyll-mentions) >= 0
BuildRequires: gem(jekyll-seo-tag) >= 0
BuildRequires: gem(jekyll-sitemap) >= 0
BuildRequires: gem(jemoji) >= 0
BuildRequires: gem(addressable) >= 2.4
BuildRequires: gem(colorator) >= 1.0
BuildRequires: gem(em-websocket) >= 0.5
BuildRequires: gem(i18n) >= 1.0
BuildRequires: gem(jekyll-sass-converter) >= 2.0
BuildRequires: gem(jekyll-watch) >= 2.0
BuildRequires: gem(kramdown) >= 2.3
BuildRequires: gem(kramdown-parser-gfm) >= 1.0
BuildRequires: gem(liquid) >= 4.0
BuildRequires: gem(mercenary) >= 0.3.6
BuildRequires: gem(pathutil) >= 0.9
BuildRequires: gem(rouge) >= 3.0
BuildRequires: gem(safe_yaml) >= 1.0
BuildRequires: gem(terminal-table) >= 1.8
BuildRequires: gem(webrick) >= 1.7
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(launchy) >= 3
BuildConflicts: gem(cucumber) >= 5.2
BuildConflicts: gem(nokogiri) >= 2
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(jekyll-feed) >= 1
BuildConflicts: gem(mime-types) >= 4
BuildConflicts: gem(psych) >= 5
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(classifier-reborn) >= 3
BuildConflicts: gem(liquid-c) >= 5
BuildConflicts: gem(yajl-ruby) >= 2
BuildConflicts: gem(addressable) >= 3
BuildConflicts: gem(colorator) >= 2
BuildConflicts: gem(em-websocket) >= 1
BuildConflicts: gem(i18n) >= 2
BuildConflicts: gem(jekyll-sass-converter) >= 4.0
BuildConflicts: gem(jekyll-watch) >= 3
BuildConflicts: gem(kramdown-parser-gfm) >= 2
BuildConflicts: gem(liquid) >= 6
BuildConflicts: gem(mercenary) >= 0.5
BuildConflicts: gem(pathutil) >= 1
BuildConflicts: gem(rouge) >= 5.0
BuildConflicts: gem(safe_yaml) >= 2
BuildConflicts: gem(terminal-table) >= 4.0
BuildConflicts: gem(webrick) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency kramdown >= 2.3.1,kramdown < 3
%ruby_use_gem_dependency liquid >= 5.0.1,liquid < 6
Requires:      gem(addressable) >= 2.4
Requires:      gem(colorator) >= 1.0
Requires:      gem(em-websocket) >= 0.5
Requires:      gem(i18n) >= 1.0
Requires:      gem(jekyll-sass-converter) >= 2.0
Requires:      gem(jekyll-watch) >= 2.0
Requires:      gem(kramdown) >= 2.3
Requires:      gem(kramdown-parser-gfm) >= 1.0
Requires:      gem(liquid) >= 4.0
Requires:      gem(mercenary) >= 0.3.6
Requires:      gem(pathutil) >= 0.9
Requires:      gem(rouge) >= 3.0
Requires:      gem(safe_yaml) >= 1.0
Requires:      gem(terminal-table) >= 1.8
Requires:      gem(webrick) >= 1.7
Conflicts:     gem(addressable) >= 3
Conflicts:     gem(colorator) >= 2
Conflicts:     gem(em-websocket) >= 1
Conflicts:     gem(i18n) >= 2
Conflicts:     gem(jekyll-sass-converter) >= 4.0
Conflicts:     gem(jekyll-watch) >= 3
Conflicts:     gem(kramdown-parser-gfm) >= 2
Conflicts:     gem(liquid) >= 6
Conflicts:     gem(mercenary) >= 0.5
Conflicts:     gem(pathutil) >= 1
Conflicts:     gem(rouge) >= 5.0
Conflicts:     gem(safe_yaml) >= 2
Conflicts:     gem(terminal-table) >= 4.0
Conflicts:     gem(webrick) >= 2
Provides:      gem(jekyll) = 4.3.2


%description
Jekyll is a simple, blog aware, static site generator.


%package       -n jekyll
Version:       4.3.2
Release:       alt1
Summary:       Jekyll is a simple, blog-aware, static site generator executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета jekyll
Group:         Other
BuildArch:     noarch

Requires:      gem(jekyll) = 4.3.2

%description   -n jekyll
Jekyll is a simple, blog-aware, static site generator executable(s).

Jekyll is a simple, blog aware, static site generator.

%description   -n jekyll -l ru_RU.UTF-8
Исполнямка для самоцвета jekyll.


%package       -n gem-jekyll-doc
Version:       4.3.2
Release:       alt1
Summary:       Jekyll is a simple, blog-aware, static site generator documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета jekyll
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(jekyll) = 4.3.2

%description   -n gem-jekyll-doc
Jekyll is a simple, blog-aware, static site generator documentation
files.

Jekyll is a simple, blog aware, static site generator.

%description   -n gem-jekyll-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета jekyll.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.markdown
%ruby_gemspec
%ruby_gemlibdir

%files         -n jekyll
%doc README.markdown
%_bindir/jekyll

%files         -n gem-jekyll-doc
%doc README.markdown
%ruby_gemdocdir


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 4.3.2-alt1
- ^ 4.2.0 -> 4.3.2 (no devel)

* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 4.2.0-alt1.1
- ! spec

* Wed Mar 03 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 4.2.0-alt1
- initial build
