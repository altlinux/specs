%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname fluentd

Name:          gem-fluentd
Version:       1.19.2
Release:       alt1
Summary:       Fluentd: Unified Logging Layer (project under CNCF)
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/fluent/fluentd
Vcs:           https://github.com/fluent/fluentd.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(async-http) >= 0.86
BuildRequires: gem(aws-sdk-core) >= 3.191
BuildRequires: gem(aws-sigv4) >= 1.8
BuildRequires: gem(base64) >= 0.2
BuildRequires: gem(benchmark) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(console) >= 1.30
BuildRequires: gem(cool.io) >= 1.4.5
BuildRequires: gem(csv) >= 3.2
BuildRequires: gem(drb) >= 2.2
BuildRequires: gem(flexmock) >= 2.0
BuildRequires: gem(http_parser.rb) >= 0.5.1
BuildRequires: gem(logger) >= 1.6
BuildRequires: gem(msgpack) >= 1.3.1
BuildRequires: gem(net-http) >= 0.8
BuildRequires: gem(oj) >= 2.14
BuildRequires: gem(ostruct) >= 0.6
BuildRequires: gem(parallel_tests) >= 0.15.3
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rexml) >= 3.2
BuildRequires: gem(rr) >= 3.0
BuildRequires: gem(serverengine) >= 2.3.2
BuildRequires: gem(sigdump) >= 0.2.5
BuildRequires: gem(simplecov) >= 0.7
BuildRequires: gem(strptime) >= 0.2.4
BuildRequires: gem(test-unit) >= 3.3
BuildRequires: gem(test-unit-rr) >= 1.0
BuildRequires: gem(tzinfo) >= 1.0
BuildRequires: gem(tzinfo-data) >= 1.0
BuildRequires: gem(uri) >= 1.0
BuildRequires: gem(webrick) >= 1.4
BuildRequires: gem(yajl-ruby) >= 1.0
BuildRequires: gem(zstd-ruby) >= 1.5
BuildConflicts: gem(async-http) >= 1
BuildConflicts: gem(aws-sdk-core) >= 4
BuildConflicts: gem(aws-sigv4) >= 2
BuildConflicts: gem(base64) >= 1
BuildConflicts: gem(console) >= 2
BuildConflicts: gem(cool.io) >= 2.0.0
BuildConflicts: gem(csv) >= 4
BuildConflicts: gem(drb) >= 3
BuildConflicts: gem(flexmock) >= 3
BuildConflicts: gem(http_parser.rb) >= 0.9.0
BuildConflicts: gem(logger) >= 2
BuildConflicts: gem(msgpack) >= 2.0.0
BuildConflicts: gem(net-http) >= 1
BuildConflicts: gem(oj) >= 4
BuildConflicts: gem(ostruct) >= 1
BuildConflicts: gem(parallel_tests) >= 4
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rexml) >= 4
BuildConflicts: gem(rr) >= 4
BuildConflicts: gem(serverengine) >= 3.0.0
BuildConflicts: gem(sigdump) >= 0.3
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(strptime) >= 1.0.0
BuildConflicts: gem(test-unit) >= 4
BuildConflicts: gem(test-unit-rr) >= 2
BuildConflicts: gem(timecop) >= 0.9.9
BuildConflicts: gem(tzinfo) >= 3.0
BuildConflicts: gem(tzinfo-data) >= 2
BuildConflicts: gem(uri) >= 2
BuildConflicts: gem(webrick) >= 2
BuildConflicts: gem(yajl-ruby) >= 2
BuildConflicts: gem(zstd-ruby) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency zstd-ruby >= 2.0.6,zstd-ruby < 3
%ruby_use_gem_dependency parallel_tests >= 3.7.0,parallel_tests < 4
Requires:      ruby >= 3.2
Requires:      gem(async-http) >= 0.86
Requires:      gem(base64) >= 0.2
Requires:      gem(benchmark) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(cool.io) >= 1.4.5
Requires:      gem(csv) >= 3.2
Requires:      gem(drb) >= 2.2
Requires:      gem(http_parser.rb) >= 0.5.1
Requires:      gem(logger) >= 1.6
Requires:      gem(msgpack) >= 1.3.1
Requires:      gem(net-http) >= 0.8
Requires:      gem(ostruct) >= 0.6
Requires:      gem(serverengine) >= 2.3.2
Requires:      gem(sigdump) >= 0.2.5
Requires:      gem(strptime) >= 0.2.4
Requires:      gem(tzinfo) >= 1.0
Requires:      gem(tzinfo-data) >= 1.0
Requires:      gem(uri) >= 1.0
Requires:      gem(webrick) >= 1.4
Requires:      gem(yajl-ruby) >= 1.0
Requires:      gem(zstd-ruby) >= 1.5
Conflicts:     gem(async-http) >= 1
Conflicts:     gem(base64) >= 1
Conflicts:     gem(cool.io) >= 2.0.0
Conflicts:     gem(csv) >= 4
Conflicts:     gem(drb) >= 3
Conflicts:     gem(http_parser.rb) >= 0.9.0
Conflicts:     gem(logger) >= 2
Conflicts:     gem(msgpack) >= 2.0.0
Conflicts:     gem(net-http) >= 1
Conflicts:     gem(ostruct) >= 1
Conflicts:     gem(serverengine) >= 3.0.0
Conflicts:     gem(sigdump) >= 0.3
Conflicts:     gem(strptime) >= 1.0.0
Conflicts:     gem(tzinfo) >= 3.0
Conflicts:     gem(tzinfo-data) >= 2
Conflicts:     gem(uri) >= 2
Conflicts:     gem(webrick) >= 2
Conflicts:     gem(yajl-ruby) >= 2
Conflicts:     gem(zstd-ruby) >= 3
Obsoletes:     ruby-fluentd < %EVR
Provides:      ruby-fluentd = %EVR
Provides:      gem(fluentd) = 1.19.0

%description
Fluentd collects events from various data sources and writes them to files,
RDBMS, NoSQL, IaaS, SaaS, Hadoop and so on. Fluentd helps you unify your logging
infrastructure (Learn more about the Unified Logging Layer).


%package       -n fluent
Version:       1.19.2
Release:       alt1
Summary:       Fluentd: Unified Logging Layer (project under CNCF) executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета fluentd
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(fluentd) = 1.19.0
Requires:      gem(benchmark) >= 0

%description   -n fluent
Fluentd: Unified Logging Layer (project under CNCF) executable(s).

Fluentd collects events from various data sources and writes them to files,
RDBMS, NoSQL, IaaS, SaaS, Hadoop and so on. Fluentd helps you unify your logging
infrastructure (Learn more about the Unified Logging Layer).

%description   -n fluent -l ru_RU.UTF-8
Исполнямка для самоцвета fluentd.


%if_enabled    doc
%package       -n gem-fluentd-doc
Version:       1.19.2
Release:       alt1
Summary:       Fluentd: Unified Logging Layer (project under CNCF) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fluentd
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(fluentd) = 1.19.0

%description   -n gem-fluentd-doc
Fluentd: Unified Logging Layer (project under CNCF) documentation
files.

Fluentd collects events from various data sources and writes them to files,
RDBMS, NoSQL, IaaS, SaaS, Hadoop and so on. Fluentd helps you unify your logging
infrastructure (Learn more about the Unified Logging Layer).

%description   -n gem-fluentd-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fluentd.
%endif


%if_enabled    devel
%package       -n gem-fluentd-devel
Version:       1.19.2
Release:       alt1
Summary:       Fluentd: Unified Logging Layer (project under CNCF) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fluentd
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(fluentd) = 1.19.0
Requires:      gem(aws-sdk-core) >= 3.191
Requires:      gem(aws-sigv4) >= 1.8
Requires:      gem(console) >= 1.30
Requires:      gem(flexmock) >= 2.0
Requires:      gem(oj) >= 2.14
Requires:      gem(parallel_tests) >= 0.15.3
Requires:      gem(rake) >= 13.0
Requires:      gem(rexml) >= 3.2
Requires:      gem(rr) >= 3.0
Requires:      gem(simplecov) >= 0.7
Requires:      gem(test-unit) >= 3.3
Requires:      gem(test-unit-rr) >= 1.0
Conflicts:     gem(aws-sdk-core) >= 4
Conflicts:     gem(aws-sigv4) >= 2
Conflicts:     gem(console) >= 2
Conflicts:     gem(flexmock) >= 3
Conflicts:     gem(oj) >= 4
Conflicts:     gem(parallel_tests) >= 4
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rexml) >= 4
Conflicts:     gem(rr) >= 4
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(test-unit) >= 4
Conflicts:     gem(test-unit-rr) >= 2
Conflicts:     gem(timecop) >= 0.9.9

%description   -n gem-fluentd-devel
Fluentd: Unified Logging Layer (project under CNCF) development
package.

Fluentd collects events from various data sources and writes them to files,
RDBMS, NoSQL, IaaS, SaaS, Hadoop and so on. Fluentd helps you unify your logging
infrastructure (Learn more about the Unified Logging Layer).

%description   -n gem-fluentd-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fluentd.
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
%doc CHANGELOG.md CONTRIBUTING.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n fluent
%doc CHANGELOG.md CONTRIBUTING.md LICENSE README.md
%_bindir/fluent-binlog-reader
%_bindir/fluent-ca-generate
%_bindir/fluent-cap-ctl
%_bindir/fluent-cat
%_bindir/fluent-ctl
%_bindir/fluent-debug
%_bindir/fluent-gem
%_bindir/fluent-plugin-config-format
%_bindir/fluent-plugin-generate
%_bindir/fluentd

%if_enabled    doc
%files         -n gem-fluentd-doc
%doc CHANGELOG.md CONTRIBUTING.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-fluentd-devel
%doc CHANGELOG.md CONTRIBUTING.md LICENSE README.md
%endif


%changelog
* Fri Mar 20 2026 Pavel Skrylev <majioa@altlinux.org> 1.19.2-alt1
- ^ 1.18.0 -> 1.19.2

* Fri Feb 07 2025 Pavel Skrylev <majioa@altlinux.org> 1.18.0-alt1
- ^ 1.14.6 -> 1.18.0

* Wed Oct 19 2022 Pavel Skrylev <majioa@altlinux.org> 1.14.6-alt1.1
- !build gem build requires due to novel gems

* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 1.14.6-alt1
- ^ 1.14.0 -> 1.14.6

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.14.0-alt1
- ^ 1.9.3 -> 1.14.0

* Mon Mar 30 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.9.3-alt2
- Change used ruby documentation macro

* Thu Mar 19 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.9.3-alt1
- new version 1.9.3

* Thu Sep 27 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.5-alt1
- Initial build for Sisyphus
