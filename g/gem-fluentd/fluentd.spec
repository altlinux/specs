%define        gemname fluentd

Name:          gem-fluentd
Version:       1.14.0
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
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(msgpack) >= 1.3.1 gem(msgpack) < 2.0.0
BuildRequires: gem(yajl-ruby) >= 1.0 gem(yajl-ruby) < 2
BuildRequires: gem(cool.io) >= 1.4.5 gem(cool.io) < 2.0.0
BuildRequires: gem(serverengine) >= 2.2.2 gem(serverengine) < 3.0.0
BuildRequires: gem(http_parser.rb) >= 0.5.1 gem(http_parser.rb) < 0.8.0
BuildRequires: gem(sigdump) >= 0.2.2 gem(sigdump) < 0.3
BuildRequires: gem(tzinfo) >= 1.0 gem(tzinfo) < 3.0
BuildRequires: gem(tzinfo-data) >= 1.0 gem(tzinfo-data) < 2
BuildRequires: gem(strptime) >= 0.2.2 gem(strptime) < 1.0.0
BuildRequires: gem(webrick) >= 1.4.2 gem(webrick) < 1.8.0
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(flexmock) >= 2.0 gem(flexmock) < 3
BuildRequires: gem(parallel_tests) >= 0.15.3 gem(parallel_tests) < 4
BuildRequires: gem(simplecov) >= 0.7 gem(simplecov) < 1
BuildRequires: gem(rr) >= 3.0 gem(rr) < 4
BuildRequires: gem(timecop) >= 0.9 gem(timecop) < 1
BuildRequires: gem(test-unit) >= 3.3 gem(test-unit) < 4
BuildRequires: gem(test-unit-rr) >= 1.0 gem(test-unit-rr) < 2
BuildRequires: gem(oj) >= 2.14 gem(oj) < 4
# BuildRequires: gem(async-http) >= 0.50.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency parallel_tests >= 3.7.0,parallel_tests < 4
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency test-unit >= 3.3.5,test-unit < 4
Requires:      gem(bundler) >= 0
Requires:      gem(msgpack) >= 1.3.1 gem(msgpack) < 2.0.0
Requires:      gem(yajl-ruby) >= 1.0 gem(yajl-ruby) < 2
Requires:      gem(cool.io) >= 1.4.5 gem(cool.io) < 2.0.0
Requires:      gem(serverengine) >= 2.2.2 gem(serverengine) < 3.0.0
Requires:      gem(http_parser.rb) >= 0.5.1 gem(http_parser.rb) < 0.8.0
Requires:      gem(sigdump) >= 0.2.2 gem(sigdump) < 0.3
Requires:      gem(tzinfo) >= 1.0 gem(tzinfo) < 3.0
Requires:      gem(tzinfo-data) >= 1.0 gem(tzinfo-data) < 2
Requires:      gem(strptime) >= 0.2.2 gem(strptime) < 1.0.0
Requires:      gem(webrick) >= 1.4.2 gem(webrick) < 1.8.0
Obsoletes:     ruby-fluentd < %EVR
Provides:      ruby-fluentd = %EVR
Provides:      gem(fluentd) = 1.14.0


%description
Fluentd collects events from various data sources and writes them to files,
RDBMS, NoSQL, IaaS, SaaS, Hadoop and so on. Fluentd helps you unify your
logging infrastructure (Learn more about the Unified Logging Layer).


%package       -n fluentd
Version:       1.14.0
Release:       alt1
Summary:       Fluentd: Unified Logging Layer (project under CNCF) executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета fluentd
Group:         Documentation
BuildArch:     noarch

Requires:      gem(fluentd) = 1.14.0

%description   -n fluentd
Fluentd: Unified Logging Layer (project under CNCF) executable(s).

Fluentd collects events from various data sources and writes them to files,
RDBMS, NoSQL, IaaS, SaaS, Hadoop and so on. Fluentd helps you unify your
logging infrastructure (Learn more about the Unified Logging Layer).

%description   -n fluentd -l ru_RU.UTF-8
Исполнямка для самоцвета fluentd.


%package       -n gem-fluentd-doc
Version:       1.14.0
Release:       alt1
Summary:       Fluentd: Unified Logging Layer (project under CNCF) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fluentd
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fluentd) = 1.14.0

%description   -n gem-fluentd-doc
Fluentd: Unified Logging Layer (project under CNCF) documentation
files.

Fluentd collects events from various data sources and writes them to files,
RDBMS, NoSQL, IaaS, SaaS, Hadoop and so on. Fluentd helps you unify your
logging infrastructure (Learn more about the Unified Logging Layer).

%description   -n gem-fluentd-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fluentd.


%package       -n gem-fluentd-devel
Version:       1.14.0
Release:       alt1
Summary:       Fluentd: Unified Logging Layer (project under CNCF) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fluentd
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fluentd) = 1.14.0
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(flexmock) >= 2.0 gem(flexmock) < 3
Requires:      gem(parallel_tests) >= 0.15.3 gem(parallel_tests) < 4
Requires:      gem(simplecov) >= 0.7 gem(simplecov) < 1
Requires:      gem(rr) >= 3.0 gem(rr) < 4
Requires:      gem(timecop) >= 0.9 gem(timecop) < 1
Requires:      gem(test-unit) >= 3.3 gem(test-unit) < 4
Requires:      gem(test-unit-rr) >= 1.0 gem(test-unit-rr) < 2
Requires:      gem(oj) >= 2.14 gem(oj) < 4
# Requires:      gem(async-http) >= 0.50.0

%description   -n gem-fluentd-devel
Fluentd: Unified Logging Layer (project under CNCF) development
package.

Fluentd collects events from various data sources and writes them to files,
RDBMS, NoSQL, IaaS, SaaS, Hadoop and so on. Fluentd helps you unify your
logging infrastructure (Learn more about the Unified Logging Layer).

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
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.14.0-alt1
- ^ 1.9.3 -> 1.14.0

* Mon Mar 30 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.9.3-alt2
- Change used ruby documentation macro

* Thu Mar 19 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.9.3-alt1
- new version 1.9.3

* Thu Sep 27 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.5-alt1
- Initial build for Sisyphus
