%define        gemname faraday

Name:          gem-faraday
Version:       2.6.0
Release:       alt1
Summary:       HTTP/REST API client library
License:       MIT
Group:         Development/Ruby
Url:           https://lostisland.github.io/faraday
Vcs:           https://github.com/lostisland/faraday.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(jruby-openssl) >= 0.11.0 gem(jruby-openssl) < 0.12
BuildRequires: gem(bake-test-external) >= 0
BuildRequires: gem(coveralls_reborn) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rack) >= 2.2 gem(rack) < 3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.7 gem(rspec) < 4
BuildRequires: gem(rspec_junit_formatter) >= 0.4 gem(rspec_junit_formatter) < 1
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(webmock) >= 3.4 gem(webmock) < 4
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-performance) >= 1.0 gem(rubocop-performance) < 2
BuildRequires: gem(yard-junk) >= 0
BuildRequires: gem(faraday-net_http) >= 2.0 gem(faraday-net_http) < 3.1
BuildRequires: gem(ruby2_keywords) >= 0.0.4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(faraday-net_http) >= 2.0 gem(faraday-net_http) < 3.1
Requires:      gem(ruby2_keywords) >= 0.0.4
Provides:      gem(faraday) = 2.6.0


%description
Faraday is an HTTP client library that provides a common interface over many
adapters (such as Net::HTTP) and embraces the concept of Rack middleware when
processing the request/response cycle.


%package       -n gem-faraday-doc
Version:       2.6.0
Release:       alt1
Summary:       HTTP/REST API client library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faraday
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(faraday) = 2.6.0

%description   -n gem-faraday-doc
HTTP/REST API client library documentation files.

Faraday is an HTTP client library that provides a common interface over many
adapters (such as Net::HTTP) and embraces the concept of Rack middleware when
processing the request/response cycle.

%description   -n gem-faraday-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faraday.


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

%files         -n gem-faraday-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Tue Oct 11 2022 Pavel Skrylev <majioa@altlinux.org> 2.6.0-alt1
- ^ 1.4.2 -> 2.6.0

* Sat Jun 05 2021 Pavel Skrylev <majioa@altlinux.org> 1.4.2-alt1
- + packaged gem with Ruby Policy 2.0
