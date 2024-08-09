%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rubydns

Name:          gem-rubydns
Version:       2.0.2
Release:       alt1
Summary:       An easy to use DNS server and resolver for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/rubydns
Vcs:           https://github.com/socketry/rubydns.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(async-rspec) >= 1.0
BuildRequires: gem(covered) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rspec) >= 3.4
BuildRequires: gem(rake) >= 0
BuildRequires: gem(process-daemon) >= 0
BuildRequires: gem(nio4r) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(async-dns) >= 1.0
BuildConflicts: gem(async-rspec) >= 2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(async-dns) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(async-dns) >= 1.0
Conflicts:     gem(async-dns) >= 2
Provides:      gem(rubydns) = 2.0.2


%description
RubyDNS provides a rule-based DSL for implementing DNS servers, built on top of
`Async::DNS`.


%package       -n rubydns-check
Version:       2.0.2
Release:       alt1
Summary:       An easy to use DNS server and resolver for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rubydns
Group:         Other
BuildArch:     noarch

Requires:      gem(rubydns) = 2.0.2

%description   -n rubydns-check
An easy to use DNS server and resolver for Ruby executable(s).

RubyDNS provides a rule-based DSL for implementing DNS servers, built on top of
`Async::DNS`.

%description   -n rubydns-check -l ru_RU.UTF-8
Исполнямка для самоцвета rubydns.


%if_enabled    doc
%package       -n gem-rubydns-doc
Version:       2.0.2
Release:       alt1
Summary:       An easy to use DNS server and resolver for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubydns
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubydns) = 2.0.2

%description   -n gem-rubydns-doc
An easy to use DNS server and resolver for Ruby documentation files.

RubyDNS provides a rule-based DSL for implementing DNS servers, built on top of
`Async::DNS`.

%description   -n gem-rubydns-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubydns.
%endif


%if_enabled    devel
%package       -n gem-rubydns-devel
Version:       2.0.2
Release:       alt1
Summary:       An easy to use DNS server and resolver for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubydns
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubydns) = 2.0.2
Requires:      gem(async-rspec) >= 1.0
Requires:      gem(covered) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(rspec) >= 3.4
Requires:      gem(rake) >= 0
Requires:      gem(process-daemon) >= 0
Requires:      gem(nio4r) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(coveralls) >= 0
Conflicts:     gem(async-rspec) >= 2
Conflicts:     gem(rspec) >= 4

%description   -n gem-rubydns-devel
An easy to use DNS server and resolver for Ruby development package.

RubyDNS provides a rule-based DSL for implementing DNS servers, built on top of
`Async::DNS`.

%description   -n gem-rubydns-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubydns.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n rubydns-check
%doc README.md
%_bindir/rubydns-check

%if_enabled    doc
%files         -n gem-rubydns-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rubydns-devel
%doc README.md
%endif


%changelog
* Tue Jul 30 2024 Pavel Skrylev <majioa@altlinux.org> 2.0.2-alt1
- + packaged gem with Ruby Policy 2.0
