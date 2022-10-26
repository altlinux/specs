%define        gemname faraday-net_http

Name:          gem-faraday-net-http
Version:       3.0.1
Release:       alt1
Summary:       Faraday adapter for Net::HTTP
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lostisland/faraday-net_http
Vcs:           https://github.com/lostisland/faraday-net_http.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(faraday) >= 2.5
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(simplecov) >= 0.17 gem(simplecov) < 1
BuildRequires: gem(webmock) >= 3.4 gem(webmock) < 4
BuildRequires: gem(rubocop) >= 0.91.1 gem(rubocop) < 2
BuildRequires: gem(rubocop-packaging) >= 0.5 gem(rubocop-packaging) < 1
BuildRequires: gem(rubocop-performance) >= 1.0 gem(rubocop-performance) < 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_alias_names faraday-net_http,faraday-net-http
Provides:      gem(faraday-net_http) = 3.0.1


%description
Faraday adapter for Net::HTTP.


%package       -n gem-faraday-net-http-doc
Version:       3.0.1
Release:       alt1
Summary:       Faraday adapter for Net::HTTP documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faraday-net_http
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(faraday-net_http) = 3.0.1

%description   -n gem-faraday-net-http-doc
Faraday adapter for Net::HTTP documentation files.

%description   -n gem-faraday-net-http-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faraday-net_http.


%package       -n gem-faraday-net-http-devel
Version:       3.0.1
Release:       alt1
Summary:       Faraday adapter for Net::HTTP development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета faraday-net_http
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(faraday-net_http) = 3.0.1
Requires:      gem(faraday) >= 2.5
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Requires:      gem(simplecov) >= 0.17 gem(simplecov) < 1
Requires:      gem(webmock) >= 3.4 gem(webmock) < 4
Requires:      gem(rubocop) >= 0.91.1 gem(rubocop) < 2
Requires:      gem(rubocop-packaging) >= 0.5 gem(rubocop-packaging) < 1
Requires:      gem(rubocop-performance) >= 1.0 gem(rubocop-performance) < 2

%description   -n gem-faraday-net-http-devel
Faraday adapter for Net::HTTP development package.

%description   -n gem-faraday-net-http-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета faraday-net_http.


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

%files         -n gem-faraday-net-http-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-faraday-net-http-devel
%doc README.md


%changelog
* Thu Oct 13 2022 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- ^ 1.0.1 -> 3.0.1

* Sat Jun 05 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- + packaged gem with Ruby Policy 2.0
