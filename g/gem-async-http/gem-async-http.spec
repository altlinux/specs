%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname async-http

Name:          gem-async-http
Version:       0.94.2
Release:       alt1
Summary:       A HTTP client and server library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/async-http
Vcs:           https://github.com/socketry/async-http.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(async) >= 2.10.2
BuildRequires: gem(async-pool) >= 0.11
BuildRequires: gem(io-endpoint) >= 0.14
BuildRequires: gem(io-stream) >= 0.6
BuildRequires: gem(metrics) >= 0.12
BuildRequires: gem(protocol-http) >= 0.58
BuildRequires: gem(protocol-http1) >= 0.36
BuildRequires: gem(protocol-http2) >= 0.22
BuildRequires: gem(protocol-url) >= 0.2
BuildRequires: gem(traces) >= 0.10
BuildConflicts: gem(async-pool) >= 1
BuildConflicts: gem(io-endpoint) >= 1
BuildConflicts: gem(io-stream) >= 1
BuildConflicts: gem(metrics) >= 1
BuildConflicts: gem(protocol-http) >= 1
BuildConflicts: gem(protocol-http1) >= 1
BuildConflicts: gem(protocol-http2) >= 1
BuildConflicts: gem(protocol-url) >= 1
BuildConflicts: gem(traces) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.2
Requires:      gem(async) >= 2.10.2
Requires:      gem(async-pool) >= 0.11
Requires:      gem(io-endpoint) >= 0.14
Requires:      gem(io-stream) >= 0.6
Requires:      gem(metrics) >= 0.12
Requires:      gem(protocol-http) >= 0.58
Requires:      gem(protocol-http1) >= 0.36
Requires:      gem(protocol-http2) >= 0.22
Requires:      gem(protocol-url) >= 0.2
Requires:      gem(traces) >= 0.10
Conflicts:     gem(async-pool) >= 1
Conflicts:     gem(io-endpoint) >= 1
Conflicts:     gem(io-stream) >= 1
Conflicts:     gem(metrics) >= 1
Conflicts:     gem(protocol-http) >= 1
Conflicts:     gem(protocol-http1) >= 1
Conflicts:     gem(protocol-http2) >= 1
Conflicts:     gem(protocol-url) >= 1
Conflicts:     gem(traces) >= 1
Provides:      async-http = %EVR
Provides:      gem(async-http) = 0.94.2

%description
An asynchronous client and server implementation of HTTP/1.0, HTTP/1.1 and
HTTP/2 including TLS. Support for streaming requests and responses. Built on top
of async and async-io. falcon provides a rack-compatible server.


%if_enabled    doc
%package       -n gem-async-http-doc
Version:       0.94.2
Release:       alt1
Summary:       A HTTP client and server library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета async-http
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(async-http) = 0.94.2

%description   -n gem-async-http-doc
A HTTP client and server library documentation files.

An asynchronous client and server implementation of HTTP/1.0, HTTP/1.1 and
HTTP/2 including TLS. Support for streaming requests and responses. Built on top
of async and async-io. falcon provides a rack-compatible server.

%description   -n gem-async-http-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета async-http.
%endif


%if_enabled    devel
%package       -n gem-async-http-devel
Version:       0.94.2
Release:       alt1
Summary:       A HTTP client and server library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета async-http
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(async-http) = 0.94.2

%description   -n gem-async-http-devel
A HTTP client and server library development package.

An asynchronous client and server implementation of HTTP/1.0, HTTP/1.1 and
HTTP/2 including TLS. Support for streaming requests and responses. Built on top
of async and async-io. falcon provides a rack-compatible server.

%description   -n gem-async-http-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета async-http.
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
%doc license.md readme.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-async-http-doc
%doc license.md readme.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-async-http-devel
%doc license.md readme.md
%endif


%changelog
* Fri Mar 20 2026 Pavel Skrylev <majioa@altlinux.org> 0.94.2-alt1
- ^ 0.59.2 -> 0.94.2

* Mon Oct 17 2022 Pavel Skrylev <majioa@altlinux.org> 0.59.2-alt1
- ^ 0.56.5 -> 0.59.2

* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 0.56.5-alt1
- + packaged gem with Ruby Policy 2.0
