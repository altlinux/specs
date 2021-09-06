%define        gemname graphql

Name:          gem-graphql
Version:       1.12.16
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
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(concurrent-ruby) >= 1.0 gem(concurrent-ruby) < 2
BuildRequires: gem(memory_profiler) >= 0
BuildRequires: gem(minitest) >= 5.9.0 gem(minitest) < 6
BuildRequires: gem(minitest-focus) >= 1.1 gem(minitest-focus) < 2
BuildRequires: gem(minitest-reporters) >= 1.0 gem(minitest-reporters) < 2
BuildRequires: gem(racc) >= 1.4 gem(racc) < 2
BuildRequires: gem(rake) >= 12 gem(rake) < 14
BuildRequires: gem(rubocop) >= 0.68 gem(rubocop) < 2
BuildRequires: gem(parser) >= 0
BuildRequires: gem(jekyll) >= 0
BuildRequires: gem(yard) >= 0
# BuildRequires: gem(jekyll-algolia) >= 0
# BuildRequires: gem(jekyll-redirect-from) >= 0
BuildRequires: gem(m) >= 1.5.0 gem(m) < 1.6
BuildRequires: gem(webrick) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_ignore_names dummy
Provides:      gem(graphql) = 1.12.16


%description
Ruby implementation of GraphQL.


%package       -n gem-graphql-doc
Version:       1.12.16
Release:       alt1
Summary:       A plain-Ruby implementation of GraphQL documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета graphql
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(graphql) = 1.12.16

%description   -n gem-graphql-doc
A plain-Ruby implementation of GraphQL documentation files.

Ruby implementation of GraphQL.

%description   -n gem-graphql-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета graphql.


%package       -n gem-graphql-devel
Version:       1.12.16
Release:       alt1
Summary:       A plain-Ruby implementation of GraphQL development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета graphql
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(graphql) = 1.12.16
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(concurrent-ruby) >= 1.0 gem(concurrent-ruby) < 2
Requires:      gem(memory_profiler) >= 0
Requires:      gem(minitest) >= 5.9.0 gem(minitest) < 6
Requires:      gem(minitest-focus) >= 1.1 gem(minitest-focus) < 2
Requires:      gem(minitest-reporters) >= 1.0 gem(minitest-reporters) < 2
Requires:      gem(racc) >= 1.4 gem(racc) < 2
Requires:      gem(rake) >= 12 gem(rake) < 14
Requires:      gem(rubocop) >= 0.68 gem(rubocop) < 2
Requires:      gem(parser) >= 0
Requires:      gem(jekyll) >= 0
Requires:      gem(yard) >= 0
# Requires:      gem(jekyll-algolia) >= 0
# Requires:      gem(jekyll-redirect-from) >= 0
Requires:      gem(m) >= 1.5.0 gem(m) < 1.6
Requires:      gem(webrick) >= 0

%description   -n gem-graphql-devel
A plain-Ruby implementation of GraphQL development package.

Ruby implementation of GraphQL.

%description   -n gem-graphql-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета graphql.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc readme.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-graphql-doc
%doc readme.md
%ruby_gemdocdir

%files         -n gem-graphql-devel
%doc readme.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.12.16-alt1
- ^ 1.9.6 -> 1.12.16

* Wed Jun 05 2019 Pavel Skrylev <majioa@altlinux.org> 1.9.6-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
