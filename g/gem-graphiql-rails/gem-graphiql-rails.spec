%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname graphiql-rails

Name:          gem-graphiql-rails
Version:       1.10.1
Release:       alt1
Summary:       A mountable GraphiQL endpoint for Rails
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/rmosolgo/graphiql-rails
Vcs:           https://github.com/rmosolgo/graphiql-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(codeclimate-test-reporter) >= 0.4
BuildRequires: gem(minitest) >= 5
BuildRequires: gem(minitest-focus) >= 1.1
BuildRequires: gem(minitest-reporters) >= 1.0
BuildRequires: gem(rails) >= 0
BuildRequires: gem(railties) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(sqlite3) >= 0
BuildConflicts: gem(codeclimate-test-reporter) >= 2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(minitest-focus) >= 2
BuildConflicts: gem(minitest-reporters) >= 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency codeclimate-test-reporter >= 1.0.9,codeclimate-test-reporter < 2
Requires:      ruby >= 2.1.0
Requires:      gem(railties) >= 0
Provides:      graphiql-rails = %EVR
Provides:      gem(graphiql-rails) = 1.10.1

%description
Use the GraphiQL IDE for GraphQL with Ruby on Rails. This gem includes an
engine, a controller and a view for integrating GraphiQL with your app.


%if_enabled    doc
%package       -n gem-graphiql-rails-doc
Version:       1.10.1
Release:       alt1
Summary:       A mountable GraphiQL endpoint for Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета graphiql-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(graphiql-rails) = 1.10.1

%description   -n gem-graphiql-rails-doc
A mountable GraphiQL endpoint for Rails documentation files.

Use the GraphiQL IDE for GraphQL with Ruby on Rails. This gem includes an
engine, a controller and a view for integrating GraphiQL with your app.

%description   -n gem-graphiql-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета graphiql-rails.
%endif


%if_enabled    devel
%package       -n gem-graphiql-rails-devel
Version:       1.10.1
Release:       alt1
Summary:       A mountable GraphiQL endpoint for Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета graphiql-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(graphiql-rails) = 1.10.1
Requires:      gem(codeclimate-test-reporter) >= 0.4
Requires:      gem(minitest) >= 5
Requires:      gem(minitest-focus) >= 1.1
Requires:      gem(minitest-reporters) >= 1.0
Requires:      gem(rails) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(sqlite3) >= 0
Conflicts:     gem(codeclimate-test-reporter) >= 2
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-focus) >= 2
Conflicts:     gem(minitest-reporters) >= 2

%description   -n gem-graphiql-rails-devel
A mountable GraphiQL endpoint for Rails development package.

Use the GraphiQL IDE for GraphQL with Ruby on Rails. This gem includes an
engine, a controller and a view for integrating GraphiQL with your app.

%description   -n gem-graphiql-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета graphiql-rails.
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
%doc LICENSE changelog.md readme.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-graphiql-rails-doc
%doc LICENSE changelog.md readme.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-graphiql-rails-devel
%doc LICENSE changelog.md readme.md
%endif


%changelog
* Tue Jan 21 2025 Pavel Skrylev <majioa@altlinux.org> 1.10.1-alt1
- ^ 1.8.0 -> 1.10.1

* Fri Oct 07 2022 Pavel Skrylev <majioa@altlinux.org> 1.8.0-alt1
- ^ 1.7.0 -> 1.8.0

* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- + packaged gem with Ruby Policy 2.0
