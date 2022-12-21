%define        gemname foreman_api_client

Name:          gem-foreman-api-client
Version:       1.0.2
Release:       alt1.1
Summary:       Foreman apipie-bindings wrapper
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/ManageIQ/foreman_api_client
Vcs:           https://github.com/manageiq/foreman_api_client.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(apipie-bindings) >= 0.4.0,gem(apipie-bindings) < 1
BuildRequires: gem(rest-client) >= 2.0 gem(rest-client) < 3
BuildRequires: gem(manageiq-style) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(vcr) >= 3.0.2 gem(vcr) < 7
BuildRequires: gem(webmock) >= 2.3.1 gem(webmock) < 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency vcr >= 6.0.0,vcr < 7
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency apipie-bindings >= 0.5.0,apipie-bindings < 1
Requires:      gem(apipie-bindings) >= 0.4.0,gem(apipie-bindings) < 1
Requires:      gem(rest-client) >= 2.0 gem(rest-client) < 3
Provides:      gem(foreman_api_client) = 1.0.2

%ruby_alias_names foreman_api_client,foreman-api-client

%description
Foreman apipie-bindings wrapper


%package       -n gem-foreman-api-client-doc
Version:       1.0.2
Release:       alt1.1
Summary:       Foreman apipie-bindings wrapper documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_api_client
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_api_client) = 1.0.2

%description   -n gem-foreman-api-client-doc
Foreman apipie-bindings wrapper documentation files.

%description   -n gem-foreman-api-client-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman_api_client.


%package       -n gem-foreman-api-client-devel
Version:       1.0.2
Release:       alt1.1
Summary:       Foreman apipie-bindings wrapper development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman_api_client
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman_api_client) = 1.0.2
Requires:      gem(manageiq-style) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(simplecov) >= 0.17
Requires:      gem(vcr) >= 3.0.2 gem(vcr) < 7
Requires:      gem(webmock) >= 2.3.1 gem(webmock) < 4

%description   -n gem-foreman-api-client-devel
Foreman apipie-bindings wrapper development package.

%description   -n gem-foreman-api-client-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета foreman_api_client.


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

%files         -n gem-foreman-api-client-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-foreman-api-client-devel
%doc README.md


%changelog
* Fri Dec 16 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1.1
- ! closes build requires under the check condition

* Fri Sep 23 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1
- + packaged gem with Ruby Policy 2.0
