%define        gemname falcon

Name:          gem-falcon
Version:       0.42.3
Release:       alt1
Summary:       A fast, asynchronous, rack-compatible web server
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/falcon
Vcs:           https://github.com/socketry/falcon.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(async) >= 0
BuildRequires: gem(async-container) >= 0.16.0 gem(async-container) < 0.17
BuildRequires: gem(async-http) >= 0.57 gem(async-http) < 1
BuildRequires: gem(async-http-cache) >= 0.4.0 gem(async-http-cache) < 0.5
BuildRequires: gem(async-io) >= 1.22 gem(async-io) < 2
BuildRequires: gem(build-environment) >= 1.13 gem(build-environment) < 2
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(localhost) >= 1.1 gem(localhost) < 2
BuildRequires: gem(openssl) >= 3.0 gem(openssl) < 4
BuildRequires: gem(process-metrics) >= 0.2.0 gem(process-metrics) < 0.3
BuildRequires: gem(protocol-rack) >= 0.1 gem(protocol-rack) < 1
BuildRequires: gem(samovar) >= 2.1 gem(samovar) < 3
BuildRequires: gem(async-process) >= 1.1 gem(async-process) < 2
BuildRequires: gem(async-rspec) >= 1.7 gem(async-rspec) < 2
BuildRequires: gem(async-websocket) >= 0.19.2 gem(async-websocket) < 1
BuildRequires: gem(bake) >= 0
BuildRequires: gem(covered) >= 0
BuildRequires: gem(rspec) >= 3.6 gem(rspec) < 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency async-websocket >= 0.22.1,async-websocket < 1
Requires:      gem(async) >= 0
Requires:      gem(async-container) >= 0.16.0 gem(async-container) < 0.17
Requires:      gem(async-http) >= 0.57 gem(async-http) < 1
Requires:      gem(async-http-cache) >= 0.4.0 gem(async-http-cache) < 0.5
Requires:      gem(async-io) >= 1.22 gem(async-io) < 2
Requires:      gem(build-environment) >= 1.13 gem(build-environment) < 2
Requires:      gem(bundler) >= 0
Requires:      gem(localhost) >= 1.1 gem(localhost) < 2
Requires:      gem(openssl) >= 3.0 gem(openssl) < 4
Requires:      gem(process-metrics) >= 0.2.0 gem(process-metrics) < 0.3
Requires:      gem(protocol-rack) >= 0.1 gem(protocol-rack) < 1
Requires:      gem(samovar) >= 2.1 gem(samovar) < 3
Provides:      gem(falcon) = 0.42.3

%description
Falcon is a multi-process, multi-fiber rack-compatible HTTP server built on top
of async, async-io, async-container and async-http. Each request is executed
within a lightweight fiber and can block on up-stream requests without stalling
the entire server process. Falcon supports HTTP/1 and HTTP/2 natively.


%package       -n falcon-utils
Version:       0.42.3
Release:       alt1
Summary:       A fast, asynchronous, rack-compatible web server executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета falcon
Group:         Other
BuildArch:     noarch

Requires:      gem(falcon) = 0.42.3
Conflicts:     falcon

%description   -n falcon-utils
A fast, asynchronous, rack-compatible web server executable(s).

Falcon is a multi-process, multi-fiber rack-compatible HTTP server built on top
of async, async-io, async-container and async-http. Each request is executed
within a lightweight fiber and can block on up-stream requests without stalling
the entire server process. Falcon supports HTTP/1 and HTTP/2 natively.

%description   -n falcon-utils -l ru_RU.UTF-8
Исполнямка для самоцвета falcon.


%package       -n gem-falcon-doc
Version:       0.42.3
Release:       alt1
Summary:       A fast, asynchronous, rack-compatible web server documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета falcon
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(falcon) = 0.42.3

%description   -n gem-falcon-doc
A fast, asynchronous, rack-compatible web server documentation files.

Falcon is a multi-process, multi-fiber rack-compatible HTTP server built on top
of async, async-io, async-container and async-http. Each request is executed
within a lightweight fiber and can block on up-stream requests without stalling
the entire server process. Falcon supports HTTP/1 and HTTP/2 natively.

%description   -n gem-falcon-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета falcon.


%package       -n gem-falcon-devel
Version:       0.42.3
Release:       alt1
Summary:       A fast, asynchronous, rack-compatible web server development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета falcon
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(falcon) = 0.42.3
Requires:      gem(async-process) >= 1.1 gem(async-process) < 2
Requires:      gem(async-rspec) >= 1.7 gem(async-rspec) < 2
Requires:      gem(async-websocket) >= 0.19.2 gem(async-websocket) < 1
Requires:      gem(bake) >= 0
Requires:      gem(covered) >= 0
Requires:      gem(rspec) >= 3.6 gem(rspec) < 4

%description   -n gem-falcon-devel
A fast, asynchronous, rack-compatible web server development package.

Falcon is a multi-process, multi-fiber rack-compatible HTTP server built on top
of async, async-io, async-container and async-http. Each request is executed
within a lightweight fiber and can block on up-stream requests without stalling
the entire server process. Falcon supports HTTP/1 and HTTP/2 natively.

%description   -n gem-falcon-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета falcon.


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

%files         -n falcon-utils
%_bindir/falcon
%_bindir/falcon-host

%files         -n gem-falcon-doc
%ruby_gemdocdir

%files         -n gem-falcon-devel


%changelog
* Wed Oct 12 2022 Pavel Skrylev <majioa@altlinux.org> 0.42.3-alt1
- + packaged gem with Ruby Policy 2.0
