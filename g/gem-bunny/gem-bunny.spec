%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname bunny

Name:          gem-bunny
Version:       2.22.0
Release:       alt1
Summary:       Popular easy to use Ruby client for RabbitMQ
License:       MIT
Group:         Development/Ruby
Url:           http://rubybunny.info
Vcs:           https://github.com/ruby-amqp/bunny.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 12.3.1
BuildRequires: gem(yard) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(ruby-prof) >= 0
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(rabbitmq_http_api_client) >= 2.2.0
BuildRequires: gem(toxiproxy) >= 1.0.3
BuildRequires: gem(amq-protocol) >= 2.3.1
BuildRequires: gem(sorted_set) >= 1.0.2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rabbitmq_http_api_client) >= 2.3
BuildConflicts: gem(toxiproxy) >= 3
BuildConflicts: gem(amq-protocol) >= 3
BuildConflicts: gem(sorted_set) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency toxiproxy >= 2.0.1,toxiproxy < 3
Requires:      gem(amq-protocol) >= 2.3.1
Requires:      gem(sorted_set) >= 1.0.2
Conflicts:     gem(amq-protocol) >= 3
Conflicts:     gem(sorted_set) >= 2
Provides:      gem(bunny) = 2.22.0


%description
Easy to use, feature complete Ruby client for RabbitMQ 3.9 and later versions.


%if_enabled    doc
%package       -n gem-bunny-doc
Version:       2.22.0
Release:       alt1
Summary:       Popular easy to use Ruby client for RabbitMQ documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bunny
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bunny) = 2.22.0

%description   -n gem-bunny-doc
Popular easy to use Ruby client for RabbitMQ documentation files.

Easy to use, feature complete Ruby client for RabbitMQ 3.9 and later versions.

%description   -n gem-bunny-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bunny.
%endif


%if_enabled    devel
%package       -n gem-bunny-devel
Version:       2.22.0
Release:       alt1
Summary:       Popular easy to use Ruby client for RabbitMQ development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bunny
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bunny) = 2.22.0
Requires:      gem(rake) >= 12.3.1
Requires:      gem(yard) >= 0
Requires:      gem(redcarpet) >= 0
Requires:      gem(ruby-prof) >= 0
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(rabbitmq_http_api_client) >= 2.2.0
Requires:      gem(toxiproxy) >= 1.0.3
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rabbitmq_http_api_client) >= 2.3
Conflicts:     gem(toxiproxy) >= 3

%description   -n gem-bunny-devel
Popular easy to use Ruby client for RabbitMQ development package.

Easy to use, feature complete Ruby client for RabbitMQ 3.9 and later versions.

%description   -n gem-bunny-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bunny.
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
%files         -n gem-bunny-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-bunny-devel
%doc README.md
%endif


%changelog
* Wed Apr 24 2024 Pavel Skrylev <majioa@altlinux.org> 2.22.0-alt1
- + packaged gem with Ruby Policy 2.0
