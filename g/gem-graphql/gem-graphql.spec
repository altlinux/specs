%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname graphql

Name:          gem-graphql
Version:       1.13.23
Release:       alt1
Summary:       A plain-Ruby implementation of GraphQL
License:       MIT
Group:         Development/Ruby
Url:           https://graphql-ruby.org/
Vcs:           https://github.com/rmosolgo/graphql-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(base64) >= 0
BuildRequires: gem(bootsnap) >= 0
BuildRequires: gem(capybara) = 3.34.0
BuildRequires: gem(evt) >= 0
BuildRequires: gem(graphql-batch) >= 0
BuildRequires: gem(libev_scheduler) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(pry-stack_explorer) >= 0
BuildRequires: gem(puma) >= 0
BuildRequires: gem(rails) >= 5.2.1
BuildRequires: gem(selenium-webdriver) >= 3.0
BuildRequires: gem(stackprof) >= 0
BuildRequires: gem(webdrivers) >= 4.1
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(concurrent-ruby) >= 1.0
BuildRequires: gem(jekyll) >= 0
BuildRequires: gem(jekyll-algolia) >= 0
BuildRequires: gem(listen) >= 0
BuildRequires: gem(m) >= 1.5.0
BuildRequires: gem(memory_profiler) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(minitest-focus) >= 0
BuildRequires: gem(minitest-reporters) >= 0
BuildRequires: gem(parser) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(rubocop) >= 1.12
BuildRequires: gem(webrick) >= 0
BuildRequires: gem(yard) >= 0
BuildConflicts: gem(concurrent-ruby) >= 2
BuildConflicts: gem(jekyll-algolia) >= 2
BuildConflicts: gem(m) >= 1.6
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rails) >= 7
BuildConflicts: gem(selenium-webdriver) >= 4
BuildConflicts: gem(webdrivers) >= 5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      ruby >= 2.4.0
Requires:      gem(base64) >= 0
Provides:      graphql = %EVR
Provides:      gem(graphql) = 1.13.23

%description
Ruby implementation of GraphQL.

* Implement the GraphQL spec & support a Relay front end
* Provide idiomatic, plain-Ruby API with similarities to reference
implementation where possible
* Support Ruby on Rails and Relay


%if_enabled    doc
%package       -n gem-graphql-doc
Version:       1.13.23
Release:       alt1
Summary:       A plain-Ruby implementation of GraphQL documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета graphql
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(graphql) = 1.13.23

%description   -n gem-graphql-doc
A plain-Ruby implementation of GraphQL documentation files.

%description   -n gem-graphql-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета graphql.
%endif


%if_enabled    devel
%package       -n gem-graphql-devel
Version:       1.13.23
Release:       alt1
Summary:       A plain-Ruby implementation of GraphQL development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета graphql
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(graphql) = 1.13.23
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(concurrent-ruby) >= 1.0
Requires:      gem(jekyll) >= 0
Requires:      gem(jekyll-algolia) >= 0
Requires:      gem(m) >= 1.5.0
Requires:      gem(memory_profiler) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(minitest-focus) >= 0
Requires:      gem(minitest-reporters) >= 0
Requires:      gem(parser) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(rubocop) >= 1.12
Requires:      gem(webrick) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(bootsnap) >= 0
Requires:      gem(evt) >= 0
Requires:      gem(graphql-batch) >= 0
Requires:      gem(libev_scheduler) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(pry-stack_explorer) >= 0
Requires:      gem(stackprof) >= 0
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(m) >= 1.6
Conflicts:     gem(rubocop) >= 2

%description   -n gem-graphql-devel
A plain-Ruby implementation of GraphQL development package.

%description   -n gem-graphql-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета graphql.
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
%doc MIT-LICENSE readme.md CHANGELOG-enterprise.md CHANGELOG-pro.md CHANGELOG-relay.md CHANGELOG.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-graphql-doc
%doc MIT-LICENSE readme.md CHANGELOG-enterprise.md CHANGELOG-pro.md CHANGELOG-relay.md CHANGELOG.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-graphql-devel
%doc MIT-LICENSE readme.md CHANGELOG-enterprise.md CHANGELOG-pro.md CHANGELOG-relay.md CHANGELOG.md
%endif


%changelog
* Mon Jan 20 2025 Pavel Skrylev <majioa@altlinux.org> 1.13.23-alt1
- ^ 1.13.15 -> 1.13.23

* Sat Oct 08 2022 Pavel Skrylev <majioa@altlinux.org> 1.13.15-alt1
- ^ 1.13.12 -> 1.13.15

* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 1.13.12-alt1
- ^ 1.12.16 -> 1.13.12

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.12.16-alt1
- ^ 1.9.6 -> 1.12.16

* Wed Jun 05 2019 Pavel Skrylev <majioa@altlinux.org> 1.9.6-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
