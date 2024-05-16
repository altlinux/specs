%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname sneakers

Name:          gem-sneakers
Version:       2.12.0
Release:       alt1
Summary:       Fast background processing framework for Ruby and RabbitMQ
License:       MIT
Group:         Development/Ruby
Url:           http://sneakers.io
Vcs:           https://github.com/jondot/sneakers.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(ruby-prof) >= 0
BuildRequires: gem(rabbitmq_http_api_client) >= 0
BuildRequires: gem(redis) >= 0
BuildRequires: gem(rake) >= 13.1.0
BuildRequires: gem(minitest) >= 5.11
BuildRequires: gem(rr) >= 1.2.1
BuildRequires: gem(unparser) = 0.2.2
BuildRequires: gem(metric_fu) >= 4.12
BuildRequires: gem(simplecov) >= 0.16
BuildRequires: gem(simplecov-rcov-text) >= 0
BuildRequires: gem(guard) >= 2.15
BuildRequires: gem(guard-minitest) >= 2.4
BuildRequires: gem(pry-byebug) >= 3.7
BuildRequires: gem(serverengine) >= 2.1.0
BuildRequires: gem(bunny) >= 2.14
BuildRequires: gem(concurrent-ruby) >= 1.0
BuildRequires: gem(thor) >= 0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rr) >= 4
BuildConflicts: gem(metric_fu) >= 5
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(guard) >= 3
BuildConflicts: gem(guard-minitest) >= 3
BuildConflicts: gem(pry-byebug) >= 4
BuildConflicts: gem(serverengine) >= 3
BuildConflicts: gem(bunny) >= 3
BuildConflicts: gem(concurrent-ruby) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rr >= 3.0.4,rr < 4
%ruby_use_gem_dependency serverengine >= 2.3.1,serverengine < 3
Requires:      gem(rake) >= 13.1.0
Requires:      gem(serverengine) >= 2.1.0
Requires:      gem(bunny) >= 2.14
Requires:      gem(concurrent-ruby) >= 1.0
Requires:      gem(thor) >= 0
Conflicts:     gem(serverengine) >= 3
Conflicts:     gem(bunny) >= 3
Conflicts:     gem(concurrent-ruby) >= 2
Provides:      gem(sneakers) = 2.12.0


%description
Fast background processing framework for Ruby and RabbitMQ


%package       -n sneakers
Version:       2.12.0
Release:       alt1
Summary:       Fast background processing framework for Ruby and RabbitMQ executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета sneakers
Group:         Other
BuildArch:     noarch

Requires:      gem(sneakers) = 2.12.0

%description   -n sneakers
Fast background processing framework for Ruby and RabbitMQ executable(s).

%description   -n sneakers -l ru_RU.UTF-8
Исполнямка для самоцвета sneakers.


%if_enabled    doc
%package       -n gem-sneakers-doc
Version:       2.12.0
Release:       alt1
Summary:       Fast background processing framework for Ruby and RabbitMQ documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sneakers
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sneakers) = 2.12.0

%description   -n gem-sneakers-doc
Fast background processing framework for Ruby and RabbitMQ documentation files.

%description   -n gem-sneakers-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sneakers.
%endif


%if_enabled    devel
%package       -n gem-sneakers-devel
Version:       2.12.0
Release:       alt1
Summary:       Fast background processing framework for Ruby and RabbitMQ development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sneakers
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sneakers) = 2.12.0
Requires:      gem(ruby-prof) >= 0
Requires:      gem(rabbitmq_http_api_client) >= 0
Requires:      gem(redis) >= 0
Requires:      gem(minitest) >= 5.11
Requires:      gem(rr) >= 1.2.1
Requires:      gem(unparser) = 0.2.2
Requires:      gem(metric_fu) >= 4.12
Requires:      gem(simplecov) >= 0.16
Requires:      gem(simplecov-rcov-text) >= 0
Requires:      gem(guard) >= 2.15
Requires:      gem(guard-minitest) >= 2.4
Requires:      gem(pry-byebug) >= 3.7
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rr) >= 4
Conflicts:     gem(metric_fu) >= 5
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(guard) >= 3
Conflicts:     gem(guard-minitest) >= 3
Conflicts:     gem(pry-byebug) >= 4

%description   -n gem-sneakers-devel
Fast background processing framework for Ruby and RabbitMQ development package.

%description   -n gem-sneakers-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sneakers.
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

%files         -n sneakers
%doc README.md
%_bindir/sneakers

%if_enabled    doc
%files         -n gem-sneakers-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-sneakers-devel
%doc README.md
%endif


%changelog
* Tue Apr 23 2024 Pavel Skrylev <majioa@altlinux.org> 2.12.0-alt1
- + packaged gem with Ruby Policy 2.0
