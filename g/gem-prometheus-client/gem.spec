%define        gemname prometheus-client

Name:          gem-prometheus-client
Version:       2.1.0
Release:       alt1
Summary:       A suite of instrumentation metric primitivesthat can be exposed through a web services interface
License:       Apache 2.0
Group:         Development/Ruby
Url:           https://github.com/prometheus/client_ruby
Vcs:           https://github.com/prometheus/client_ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(concurrent-ruby) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names rack
Provides:      gem(prometheus-client) = 2.1.0


%description
A suite of instrumentation metric primitives for Ruby that can be exposed
through a HTTP interface. Intended to be used together with a Prometheus server.


%package       -n gem-prometheus-client-doc
Version:       2.1.0
Release:       alt1
Summary:       A suite of instrumentation metric primitivesthat can be exposed through a web services interface documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета prometheus-client
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(prometheus-client) = 2.1.0

%description   -n gem-prometheus-client-doc
A suite of instrumentation metric primitivesthat can be exposed through a web
services interface documentation files.

A suite of instrumentation metric primitives for Ruby that can be exposed
through a HTTP interface. Intended to be used together with a Prometheus server.

%description   -n gem-prometheus-client-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета prometheus-client.


%package       -n gem-prometheus-client-devel
Version:       2.1.0
Release:       alt1
Summary:       A suite of instrumentation metric primitivesthat can be exposed through a web services interface development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета prometheus-client
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(prometheus-client) = 2.1.0
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(concurrent-ruby) >= 0

%description   -n gem-prometheus-client-devel
A suite of instrumentation metric primitivesthat can be exposed through a web
services interface development package.

A suite of instrumentation metric primitives for Ruby that can be exposed
through a HTTP interface. Intended to be used together with a Prometheus server.

%description   -n gem-prometheus-client-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета prometheus-client.


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

%files         -n gem-prometheus-client-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-prometheus-client-devel
%doc README.md


%changelog
* Tue Sep 14 2021 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- ^ 2.0.0 -> 2.1.0

* Mon Mar 02 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- ^ 0.9.0 -> 2.0.0

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.0-alt2
- + findreq filter in spec
- ! spec

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
