%define        gemname graphiql-rails

Name:          gem-graphiql-rails
Version:       1.7.0
Release:       alt1
Summary:       A mountable GraphiQL endpoint for Rails
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/rmosolgo/graphiql-rails
Vcs:           https://github.com/rmosolgo/graphiql-rails.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(railties) >= 0
BuildRequires: gem(sprockets-rails) >= 0
BuildRequires: gem(rails) >= 0
BuildRequires: gem(sqlite3) >= 0
BuildRequires: gem(codeclimate-test-reporter) >= 0.4 gem(codeclimate-test-reporter) < 2
BuildRequires: gem(minitest) >= 5 gem(minitest) < 6
BuildRequires: gem(minitest-focus) >= 1.1 gem(minitest-focus) < 2
BuildRequires: gem(minitest-reporters) >= 1.0 gem(minitest-reporters) < 2
BuildRequires: gem(rake) >= 11.0 gem(rake) < 14

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency codeclimate-test-reporter >= 1.0.9,codeclimate-test-reporter < 2
Requires:      gem(railties) >= 0
Requires:      gem(sprockets-rails) >= 0
Provides:      gem(graphiql-rails) = 1.7.0


%description
Use the GraphiQL IDE for GraphQL with Ruby on Rails. This gem includes an
engine, a controller and a view for integrating GraphiQL with your app.


%package       -n gem-graphiql-rails-doc
Version:       1.7.0
Release:       alt1
Summary:       A mountable GraphiQL endpoint for Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета graphiql-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(graphiql-rails) = 1.7.0

%description   -n gem-graphiql-rails-doc
A mountable GraphiQL endpoint for Rails documentation files.

Use the GraphiQL IDE for GraphQL with Ruby on Rails. This gem includes an
engine, a controller and a view for integrating GraphiQL with your app.

%description   -n gem-graphiql-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета graphiql-rails.


%package       -n gem-graphiql-rails-devel
Version:       1.7.0
Release:       alt1
Summary:       A mountable GraphiQL endpoint for Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета graphiql-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(graphiql-rails) = 1.7.0
Requires:      gem(rails) >= 0
Requires:      gem(sqlite3) >= 0
Requires:      gem(codeclimate-test-reporter) >= 0.4 gem(codeclimate-test-reporter) < 2
Requires:      gem(minitest) >= 5 gem(minitest) < 6
Requires:      gem(minitest-focus) >= 1.1 gem(minitest-focus) < 2
Requires:      gem(minitest-reporters) >= 1.0 gem(minitest-reporters) < 2
Requires:      gem(rake) >= 11.0 gem(rake) < 14

%description   -n gem-graphiql-rails-devel
A mountable GraphiQL endpoint for Rails development package.

Use the GraphiQL IDE for GraphQL with Ruby on Rails. This gem includes an
engine, a controller and a view for integrating GraphiQL with your app.

%description   -n gem-graphiql-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета graphiql-rails.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-graphiql-rails-doc
%ruby_gemdocdir

%files         -n gem-graphiql-rails-devel


%changelog
* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- + packaged gem with Ruby Policy 2.0
