%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_enable    devel
%define        gemname rabbitmq_http_api_client

Name:          gem-rabbitmq-http-api-client
Version:       2.2.0
Release:       alt1
Summary:       RabbitMQ HTTP API client for Ruby
License:       MIT or MPL-2.0
Group:         Development/Ruby
Url:           http://github.com/ruby-amqp/rabbitmq_http_api_client
Vcs:           https://github.com/ruby-amqp/rabbitmq_http_api_client.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rspec) >= 3.10
BuildRequires: gem(bunny) >= 2.17.0
BuildRequires: gem(rantly) >= 0
BuildRequires: gem(addressable) >= 2.7
BuildRequires: gem(hashie) >= 4.1
BuildRequires: gem(multi_json) >= 1.15
BuildRequires: gem(faraday) >= 1.3
BuildRequires: gem(faraday_middleware) >= 1.2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(bunny) >= 3
BuildConflicts: gem(addressable) >= 3
BuildConflicts: gem(hashie) >= 5
BuildConflicts: gem(multi_json) >= 2
BuildConflicts: gem(faraday) >= 3
BuildConflicts: gem(faraday_middleware) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency faraday >= 2.6.0,faraday < 3
%ruby_use_gem_dependency bunny >= 2.22,bunny < 3
Requires:      gem(addressable) >= 2.7
Requires:      gem(hashie) >= 4.1
Requires:      gem(multi_json) >= 1.15
Requires:      gem(faraday) >= 1.3
Requires:      gem(faraday_middleware) >= 1.2
Conflicts:     gem(addressable) >= 3
Conflicts:     gem(hashie) >= 5
Conflicts:     gem(multi_json) >= 2
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(faraday_middleware) >= 2
Provides:      gem(rabbitmq_http_api_client) = 2.2.0


%description
RabbitMQ HTTP API client for Ruby


%if_enabled    doc
%package       -n gem-rabbitmq-http-api-client-doc
Version:       2.2.0
Release:       alt1
Summary:       RabbitMQ HTTP API client for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rabbitmq_http_api_client
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rabbitmq_http_api_client) = 2.2.0

%description   -n gem-rabbitmq-http-api-client-doc
RabbitMQ HTTP API client for Ruby documentation files.

%description   -n gem-rabbitmq-http-api-client-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rabbitmq_http_api_client.
%endif


%if_enabled    devel
%package       -n gem-rabbitmq-http-api-client-devel
Version:       2.2.0
Release:       alt1
Summary:       RabbitMQ HTTP API client for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rabbitmq_http_api_client
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rabbitmq_http_api_client) = 2.2.0
Requires:      gem(rspec) >= 3.10
Requires:      gem(bunny) >= 2.17.0
Requires:      gem(rantly) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(bunny) >= 3

%description   -n gem-rabbitmq-http-api-client-devel
RabbitMQ HTTP API client for Ruby development package.

%description   -n gem-rabbitmq-http-api-client-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rabbitmq_http_api_client.
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
%files         -n gem-rabbitmq-http-api-client-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rabbitmq-http-api-client-devel
%doc README.md
%endif


%changelog
* Wed Apr 24 2024 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- + packaged gem with Ruby Policy 2.0
