%define        gemname fluentd

Name:          gem-fluentd
Version:       1.15.3
Release:       alt1
Summary:       Fluentd: Unified Logging Layer (project under CNCF)
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/fluent/fluentd
Vcs:           https://github.com/fluent/fluentd.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(flexmock) >= 2.0
BuildRequires: gem(parallel_tests) >= 0.15.3
BuildRequires: gem(simplecov) >= 0.7
BuildRequires: gem(rr) >= 3.0
BuildRequires: gem(timecop) >= 0.9
BuildRequires: gem(test-unit) >= 3.3
BuildRequires: gem(test-unit-rr) >= 1.0
BuildRequires: gem(oj) >= 2.14
BuildRequires: gem(async) >= 1.23
BuildRequires: gem(async-http) >= 0.50.0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(msgpack) >= 1.3.1
BuildRequires: gem(yajl-ruby) >= 1.0
BuildRequires: gem(cool.io) >= 1.4.5
BuildRequires: gem(serverengine) >= 2.3.0
BuildRequires: gem(http_parser.rb) >= 0.5.1
BuildRequires: gem(sigdump) >= 0.2.2
BuildRequires: gem(tzinfo) >= 1.0
BuildRequires: gem(tzinfo-data) >= 1.0
BuildRequires: gem(strptime) >= 0.2.4
BuildRequires: gem(webrick) >= 1.4.2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(flexmock) >= 3
BuildConflicts: gem(parallel_tests) >= 4
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(rr) >= 4
BuildConflicts: gem(timecop) >= 1
BuildConflicts: gem(test-unit) >= 4
BuildConflicts: gem(test-unit-rr) >= 2
BuildConflicts: gem(oj) >= 4
BuildConflicts: gem(async) >= 3
BuildConflicts: gem(msgpack) >= 2.0.0
BuildConflicts: gem(yajl-ruby) >= 2
BuildConflicts: gem(cool.io) >= 2.0.0
BuildConflicts: gem(serverengine) >= 3.0.0
BuildConflicts: gem(http_parser.rb) >= 0.9.0
BuildConflicts: gem(sigdump) >= 0.3
BuildConflicts: gem(tzinfo) >= 3.0
BuildConflicts: gem(tzinfo-data) >= 2
BuildConflicts: gem(strptime) >= 1.0.0
BuildConflicts: gem(webrick) >= 1.8.0
%endif
 

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency parallel_tests >= 3.7.0,parallel_tests < 4
%ruby_use_gem_dependency async >= 2.1.0,async < 3
Requires:      gem(msgpack) >= 1.3.1
Requires:      gem(yajl-ruby) >= 1.0
Requires:      gem(cool.io) >= 1.4.5
Requires:      gem(serverengine) >= 2.3.0
Requires:      gem(http_parser.rb) >= 0.5.1
Requires:      gem(sigdump) >= 0.2.2
Requires:      gem(tzinfo) >= 1.0
Requires:      gem(tzinfo-data) >= 1.0
Requires:      gem(strptime) >= 0.2.4
Requires:      gem(webrick) >= 1.4.2
Conflicts:     gem(msgpack) >= 2.0.0
Conflicts:     gem(yajl-ruby) >= 2
Conflicts:     gem(cool.io) >= 2.0.0
Conflicts:     gem(serverengine) >= 3.0.0
Conflicts:     gem(http_parser.rb) >= 0.9.0
Conflicts:     gem(sigdump) >= 0.3
Conflicts:     gem(tzinfo) >= 3.0
Conflicts:     gem(tzinfo-data) >= 2
Conflicts:     gem(strptime) >= 1.0.0
Conflicts:     gem(webrick) >= 1.8.0
Obsoletes:     ruby-fluentd < %EVR
Provides:      ruby-fluentd = %EVR
Provides:      gem(fluentd) = 1.15.3


%description
Fluentd collects events from various data sources and writes them to files,
RDBMS, NoSQL, IaaS, SaaS, Hadoop and so on. Fluentd helps you unify your logging
infrastructure (Learn more about the Unified Logging Layer).


%package       -n fluentd
Version:       1.15.3
Release:       alt1
Summary:       Fluentd: Unified Logging Layer (project under CNCF) executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета fluentd
Group:         Documentation
BuildArch:     noarch

Requires:      gem(fluentd) = 1.15.3

%description   -n fluentd
Fluentd: Unified Logging Layer (project under CNCF) executable(s).

Fluentd collects events from various data sources and writes them to files,
RDBMS, NoSQL, IaaS, SaaS, Hadoop and so on. Fluentd helps you unify your logging
infrastructure (Learn more about the Unified Logging Layer).

%description   -n fluentd -l ru_RU.UTF-8
Исполнямка для самоцвета fluentd.


%package       -n gem-fluentd-doc
Version:       1.15.3
Release:       alt1
Summary:       Fluentd: Unified Logging Layer (project under CNCF) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fluentd
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fluentd) = 1.15.3

%description   -n gem-fluentd-doc
Fluentd: Unified Logging Layer (project under CNCF) documentation
files.

Fluentd collects events from various data sources and writes them to files,
RDBMS, NoSQL, IaaS, SaaS, Hadoop and so on. Fluentd helps you unify your logging
infrastructure (Learn more about the Unified Logging Layer).

%description   -n gem-fluentd-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fluentd.


%package       -n gem-fluentd-devel
Version:       1.15.3
Release:       alt1
Summary:       Fluentd: Unified Logging Layer (project under CNCF) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fluentd
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fluentd) = 1.15.3
Requires:      gem(rake) >= 13.0
Requires:      gem(flexmock) >= 2.0
Requires:      gem(parallel_tests) >= 0.15.3
Requires:      gem(simplecov) >= 0.7
Requires:      gem(rr) >= 3.0
Requires:      gem(timecop) >= 0.9
Requires:      gem(test-unit) >= 3.3
Requires:      gem(test-unit-rr) >= 1.0
Requires:      gem(oj) >= 2.14
Requires:      gem(async) >= 1.23
Requires:      gem(async-http) >= 0.50.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(flexmock) >= 3
Conflicts:     gem(parallel_tests) >= 4
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(rr) >= 4
Conflicts:     gem(timecop) >= 1
Conflicts:     gem(test-unit) >= 4
Conflicts:     gem(test-unit-rr) >= 2
Conflicts:     gem(oj) >= 4
Conflicts:     gem(async) >= 3

%description   -n gem-fluentd-devel
Fluentd: Unified Logging Layer (project under CNCF) development
package.

Fluentd collects events from various data sources and writes them to files,
RDBMS, NoSQL, IaaS, SaaS, Hadoop and so on. Fluentd helps you unify your logging
infrastructure (Learn more about the Unified Logging Layer).

%description   -n gem-fluentd-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fluentd.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md templates/new_gem/README.md.erb
%ruby_gemspec
%ruby_gemlibdir

%files         -n fluentd
%doc README.md templates/new_gem/README.md.erb
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

%files         -n gem-fluentd-doc
%doc README.md templates/new_gem/README.md.erb
%ruby_gemdocdir

%files         -n gem-fluentd-devel
%doc README.md templates/new_gem/README.md.erb


%changelog
* Sun Feb 19 2023 Pavel Skrylev <majioa@altlinux.org> 1.15.3-alt1
- ^ 1.14.6 -> 1.15.3

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
