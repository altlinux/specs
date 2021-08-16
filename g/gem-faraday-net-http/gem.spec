%define        gemname faraday-net_http

Name:          gem-faraday-net-http
Version:       1.0.1
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
BuildRequires: gem(bundler) >= 2.0 gem(bundler) < 3
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(simplecov) >= 0.17 gem(simplecov) < 1
BuildRequires: gem(rubocop) >= 0.91.1 gem(rubocop) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.13.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Provides:      gem(faraday-net_http) = 1.0.1


%description
Faraday adapter for Net::HTTP.


%package       -n gem-faraday-net-http-doc
Version:       1.0.1
Release:       alt1
Summary:       Faraday adapter for Net::HTTP documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faraday-net_http
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(faraday-net_http) = 1.0.1

%description   -n gem-faraday-net-http-doc
Faraday adapter for Net::HTTP documentation files.

Faraday adapter for Net::HTTP.

%description   -n gem-faraday-net-http-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faraday-net_http.


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


%changelog
* Sat Jun 05 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- + packaged gem with Ruby Policy 2.0
