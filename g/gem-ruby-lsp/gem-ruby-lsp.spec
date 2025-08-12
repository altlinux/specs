%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname ruby-lsp

Name:          gem-ruby-lsp
Version:       0.26.1
Release:       alt1
Summary:       An opinionated language server for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/Shopify/ruby-lsp
Vcs:           https://github.com/shopify/ruby-lsp.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(base64) >= 0
BuildRequires: gem(bundler) >= 2.1.4
BuildRequires: gem(csv) >= 0
BuildRequires: gem(debug) >= 1.9
BuildRequires: gem(jekyll-feed) >= 0.12
BuildRequires: gem(jekyll-redirect-from) >= 0
BuildRequires: gem(just-the-docs) >= 0.10.1
BuildRequires: gem(language_server-protocol) >= 3.17.0
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(mocha) >= 2.0
BuildRequires: gem(prism) >= 1.2
BuildRequires: gem(psych) >= 5.1
BuildRequires: gem(rake) >= 13.1.0
BuildRequires: gem(rbs) >= 3
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-minitest) >= 0.13.0
BuildRequires: gem(rubocop-rake) >= 0.6.0
BuildRequires: gem(rubocop-shopify) >= 2.14.0
BuildRequires: gem(rubocop-sorbet) >= 0.8
BuildRequires: gem(sorbet-static) >= 0
BuildRequires: gem(syntax_tree) >= 6.1.1
BuildRequires: gem(tapioca) >= 0.16
BuildRequires: gem(test-unit) >= 0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(debug) >= 2
BuildConflicts: gem(jekyll-feed) >= 1
BuildConflicts: gem(just-the-docs) >= 0.11
BuildConflicts: gem(language_server-protocol) >= 3.18
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(mocha) >= 3
BuildConflicts: gem(prism) >= 2.0
BuildConflicts: gem(psych) >= 6
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rbs) >= 5
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-minitest) >= 1
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-shopify) >= 3
BuildConflicts: gem(rubocop-sorbet) >= 1
BuildConflicts: gem(syntax_tree) >= 7
BuildConflicts: gem(tapioca) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 2.0,mocha < 3
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency rubocop-minitest >= 0.13.0,rubocop-minitest < 1
%ruby_use_gem_dependency rubocop-rake >= 0.6.0,rubocop-rake < 1
%ruby_use_gem_dependency rubocop-shopify >= 2.14.0,rubocop-shopify < 3
Requires:      ruby >= 3.0
Requires:      gem(bundler) >= 2.1.4
Requires:      gem(language_server-protocol) >= 3.17.0
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(prism) >= 1.2
Requires:      gem(rbs) >= 3
Requires:      gem(test-unit) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(language_server-protocol) >= 3.18
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(prism) >= 2.0
Conflicts:     gem(rbs) >= 5
Provides:      gem(ruby-lsp) = 0.26.1

%ruby_ignore_names jekyll

%description
An opinionated language server for Ruby


%package       -n ruby-lsp 
Version:       0.26.1
Release:       alt1
Summary:       An opinionated language server for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета ruby-lsp
Group:         Other
BuildArch:     noarch

Requires:      gem(ruby-lsp) = 0.26.1
Requires:      gem(bundler) >= 2.1.4
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(test-unit) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(minitest) >= 6

%description   -n ruby-lsp 
An opinionated language server for Ruby executable(s).

%description   -n ruby-lsp  -l ru_RU.UTF-8
Исполнямка для самоцвета ruby-lsp.


%if_enabled    doc
%package       -n gem-ruby-lsp-doc
Version:       0.26.1
Release:       alt1
Summary:       An opinionated language server for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-lsp
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby-lsp) = 0.26.1

%description   -n gem-ruby-lsp-doc
An opinionated language server for Ruby documentation files.

%description   -n gem-ruby-lsp-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby-lsp.
%endif


%if_enabled    devel
%package       -n gem-ruby-lsp-devel
Version:       0.26.1
Release:       alt1
Summary:       An opinionated language server for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-lsp
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-lsp) = 0.26.1
Requires:      gem(debug) >= 1.9
Requires:      gem(mocha) >= 2.0
Requires:      gem(psych) >= 5.1
Requires:      gem(rake) >= 13.1.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-minitest) >= 0.13.0
Requires:      gem(rubocop-rake) >= 0.6.0
Requires:      gem(rubocop-shopify) >= 2.14.0
Requires:      gem(rubocop-sorbet) >= 0.8
Requires:      gem(sorbet-static) >= 0
Requires:      gem(syntax_tree) >= 6.1.1
Requires:      gem(tapioca) >= 0.16
Conflicts:     gem(debug) >= 2
Conflicts:     gem(mocha) >= 3
Conflicts:     gem(psych) >= 6
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-minitest) >= 1
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-shopify) >= 3
Conflicts:     gem(rubocop-sorbet) >= 1
Conflicts:     gem(syntax_tree) >= 7
Conflicts:     gem(tapioca) >= 1

%description   -n gem-ruby-lsp-devel
An opinionated language server for Ruby development package.

%description   -n gem-ruby-lsp-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby-lsp.
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
%doc LICENSE.txt README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n ruby-lsp 
%doc LICENSE.txt README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%_bindir/ruby-lsp
%_bindir/ruby-lsp-check
%_bindir/ruby-lsp-launcher
%_bindir/ruby-lsp-test-exec

%if_enabled    doc
%files         -n gem-ruby-lsp-doc
%doc LICENSE.txt README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ruby-lsp-devel
%doc LICENSE.txt README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%endif


%changelog
* Tue Aug 12 2025 Pavel Skrylev <majioa@altlinux.org> 0.26.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
