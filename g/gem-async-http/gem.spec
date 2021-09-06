%define        gemname async-http

Name:          gem-async-http
Version:       0.56.5
Release:       alt1
Summary:       A HTTP client and server library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/async-http
Vcs:           https://github.com/socketry/async-http.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(async) >= 1.25
BuildRequires: gem(async-io) >= 1.28
BuildRequires: gem(async-pool) >= 0.2
BuildRequires: gem(protocol-http) >= 0.22.0 gem(protocol-http) < 0.23
BuildRequires: gem(protocol-http1) >= 0.14.0 gem(protocol-http1) < 0.15
BuildRequires: gem(protocol-http2) >= 0.14.0 gem(protocol-http2) < 0.15
BuildRequires: gem(async-container) >= 0.14 gem(async-container) < 1
BuildRequires: gem(async-rspec) >= 1.10 gem(async-rspec) < 2
# BuildRequires: gem(covered) >= 0
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(rspec) >= 3.6 gem(rspec) < 4
BuildRequires: gem(localhost) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names trenni,fetch
Requires:      gem(async) >= 1.25
Requires:      gem(async-io) >= 1.28
Requires:      gem(async-pool) >= 0.2
Requires:      gem(protocol-http) >= 0.22.0 gem(protocol-http) < 0.23
Requires:      gem(protocol-http1) >= 0.14.0 gem(protocol-http1) < 0.15
Requires:      gem(protocol-http2) >= 0.14.0 gem(protocol-http2) < 0.15
Provides:      gem(async-http) = 0.56.5

%description
An asynchronous client and server implementation of HTTP/1.0, HTTP/1.1 and
HTTP/2 including TLS. Support for streaming requests and responses. Built on
top of async and async-io. falcon provides a rack-compatible server.


%package       -n gem-async-http-doc
Version:       0.56.5
Release:       alt1
Summary:       A HTTP client and server library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета async-http
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(async-http) = 0.56.5

%description   -n gem-async-http-doc
A HTTP client and server library documentation files.

An asynchronous client and server implementation of HTTP/1.0, HTTP/1.1 and
HTTP/2 including TLS. Support for streaming requests and responses. Built on
top of async and async-io. falcon provides a rack-compatible server.

%description   -n gem-async-http-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета async-http.


%package       -n gem-async-http-devel
Version:       0.56.5
Release:       alt1
Summary:       A HTTP client and server library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета async-http
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(async-http) = 0.56.5
Requires:      gem(async-container) >= 0.14 gem(async-container) < 1
Requires:      gem(async-rspec) >= 1.10 gem(async-rspec) < 2
Requires:      gem(covered) >= 0
Requires:      gem(rack-test) >= 0
Requires:      gem(rspec) >= 3.6 gem(rspec) < 4
Requires:      gem(localhost) >= 0

%description   -n gem-async-http-devel
A HTTP client and server library development package.

An asynchronous client and server implementation of HTTP/1.0, HTTP/1.1 and
HTTP/2 including TLS. Support for streaming requests and responses. Built on
top of async and async-io. falcon provides a rack-compatible server.

%description   -n gem-async-http-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета async-http.


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

%files         -n gem-async-http-doc
%ruby_gemdocdir

%files         -n gem-async-http-devel


%changelog
* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 0.56.5-alt1
- + packaged gem with Ruby Policy 2.0
