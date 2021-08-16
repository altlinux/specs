%define        gemname faraday

Name:          gem-faraday
Version:       1.4.2
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
BuildRequires: gem(faraday-em_http) >= 1.0 gem(faraday-em_http) < 2
BuildRequires: gem(faraday-em_synchrony) >= 1.0 gem(faraday-em_synchrony) < 2
BuildRequires: gem(faraday-excon) >= 1.1 gem(faraday-excon) < 2
BuildRequires: gem(faraday-net_http) >= 1.0 gem(faraday-net_http) < 2
BuildRequires: gem(faraday-net_http_persistent) >= 1.1 gem(faraday-net_http_persistent) < 2
BuildRequires: gem(multipart-post) >= 1.2 gem(multipart-post) < 3
BuildRequires: gem(ruby2_keywords) >= 0.0.4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names docs
Requires:      gem(faraday-em_http) >= 1.0 gem(faraday-em_http) < 2
Requires:      gem(faraday-em_synchrony) >= 1.0 gem(faraday-em_synchrony) < 2
Requires:      gem(faraday-excon) >= 1.1 gem(faraday-excon) < 2
Requires:      gem(faraday-net_http) >= 1.0 gem(faraday-net_http) < 2
Requires:      gem(faraday-net_http_persistent) >= 1.1 gem(faraday-net_http_persistent) < 2
Requires:      gem(multipart-post) >= 1.2 gem(multipart-post) < 3
Requires:      gem(ruby2_keywords) >= 0.0.4
Provides:      gem(faraday) = 1.4.2

%description
Faraday is an HTTP client library that provides a common interface over many
adapters (such as Net::HTTP) and embraces the concept of Rack middleware when
processing the request/response cycle.


%package       -n gem-faraday-doc
Version:       1.4.2
Release:       alt1
Summary:       HTTP/REST API client library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faraday
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(faraday) = 1.4.2

%description   -n gem-faraday-doc
HTTP/REST API client library documentation files.

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
* Sat Jun 05 2021 Pavel Skrylev <majioa@altlinux.org> 1.4.2-alt1
- + packaged gem with Ruby Policy 2.0
