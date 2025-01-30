%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rubocop-graphql

Name:          gem-rubocop-graphql
Version:       1.5.4
Release:       alt1
Summary:       Automatic performance checking tool for Ruby code
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/DmitryTsepelev/rubocop-graphql
Vcs:           https://github.com/dmitrytsepelev/rubocop-graphql.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Requires:      gem(rubocop) >= 1.15.0
Conflicts:     gem(rubocop) >= 2
Provides:      gem(rubocop-graphql) = 1.5.4


%description
A collection of RuboCop cops to improve GraphQL-related code


%if_enabled    doc
%package       -n gem-rubocop-graphql-doc
Version:       1.5.4
Release:       alt1
Summary:       Automatic performance checking tool for Ruby code documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-graphql
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-graphql) = 1.5.4

%description   -n gem-rubocop-graphql-doc
Automatic performance checking tool for Ruby code documentation files.

A collection of RuboCop cops to improve GraphQL-related code

%description   -n gem-rubocop-graphql-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-graphql.
%endif


%if_enabled    devel
%package       -n gem-rubocop-graphql-devel
Version:       1.5.4
Release:       alt1
Summary:       Automatic performance checking tool for Ruby code development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-graphql
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-graphql) = 1.5.4
Requires:      gem(bundler) >= 2.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake) >= 14

%description   -n gem-rubocop-graphql-devel
Automatic performance checking tool for Ruby code development package.

A collection of RuboCop cops to improve GraphQL-related code

%description   -n gem-rubocop-graphql-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-graphql.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rubocop-graphql-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rubocop-graphql-devel
%doc README.md
%endif


%changelog
* Tue Oct 01 2024 Pavel Skrylev <majioa@altlinux.org> 1.5.4-alt1
- + packaged gem with Ruby Policy 2.0
