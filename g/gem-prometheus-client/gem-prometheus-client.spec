%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname prometheus-client

Name:          gem-prometheus-client
Version:       4.2.2
Release:       alt1
Summary:       A suite of instrumentation metric primitivesthat can be exposed through a web services interface
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/prometheus/client_ruby
Vcs:           https://github.com/prometheus/client_ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(concurrent-ruby) >= 0
BuildRequires: gem(timecop) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(simplecov) >= 0
Requires:      gem(json) >= 0
Requires:      gem(rack) >= 0
Requires:      gem(rack-test) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(term-ansicolor) >= 0
Requires:      gem(tins) >= 0
Provides:      gem(prometheus-client) = 4.2.2


%description
A suite of instrumentation metric primitives for Ruby that can be exposed
through a HTTP interface. Intended to be used together with a Prometheus server.


%if_enabled    doc
%package       -n gem-prometheus-client-doc
Version:       4.2.2
Release:       alt1
Summary:       A suite of instrumentation metric primitivesthat can be exposed through a web services interface documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета prometheus-client
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(prometheus-client) = 4.2.2

%description   -n gem-prometheus-client-doc
A suite of instrumentation metric primitivesthat can be exposed through a web
services interface documentation files.

A suite of instrumentation metric primitives for Ruby that can be exposed
through a HTTP interface. Intended to be used together with a Prometheus server.

%description   -n gem-prometheus-client-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета prometheus-client.
%endif


%if_enabled    devel
%package       -n gem-prometheus-client-devel
Version:       4.2.2
Release:       alt1
Summary:       A suite of instrumentation metric primitivesthat can be exposed through a web services interface development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета prometheus-client
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(prometheus-client) = 4.2.2
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(concurrent-ruby) >= 0
Requires:      gem(timecop) >= 0

%description   -n gem-prometheus-client-devel
A suite of instrumentation metric primitivesthat can be exposed through a web
services interface development package.

A suite of instrumentation metric primitives for Ruby that can be exposed
through a HTTP interface. Intended to be used together with a Prometheus server.

%description   -n gem-prometheus-client-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета prometheus-client.
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
%doc LICENSE README.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-prometheus-client-doc
%doc LICENSE README.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-prometheus-client-devel
%doc LICENSE README.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%endif


%changelog
* Thu Mar 28 2024 Pavel Skrylev <majioa@altlinux.org> 4.2.2-alt1
- ^ 4.0.0 -> 4.2.2

* Sat Oct 08 2022 Pavel Skrylev <majioa@altlinux.org> 4.0.0-alt1
- ^ 2.1.0 -> 4.0.0

* Tue Sep 14 2021 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- ^ 2.0.0 -> 2.1.0

* Mon Mar 02 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- ^ 0.9.0 -> 2.0.0

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.0-alt2
- + findreq filter in spec
- ! spec

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
