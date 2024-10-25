%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname faraday

Name:          gem-faraday
Version:       2.12.0
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
%if_enabled check
BuildRequires: gem(bake-test-external) >= 0
BuildRequires: gem(coveralls_reborn) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rack) >= 3.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.7
BuildRequires: gem(rspec_junit_formatter) >= 0.4
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(webmock) >= 3.4
BuildRequires: gem(racc) >= 1.7
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-packaging) >= 0.5
BuildRequires: gem(rubocop-performance) >= 1.0
BuildRequires: gem(yard-junk) >= 0
BuildRequires: gem(faraday-net_http) >= 2.0
BuildRequires: gem(json) >= 0
BuildRequires: gem(logger) >= 0
BuildConflicts: gem(rack) >= 4
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec_junit_formatter) >= 1
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(racc) >= 2
BuildConflicts: gem(rubocop-packaging) >= 1
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(faraday-net_http) >= 3.4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(faraday-net_http) >= 2.0
Requires:      gem(json) >= 0
Requires:      gem(logger) >= 0
Conflicts:     gem(faraday-net_http) >= 3.4
Provides:      gem(faraday) = 2.12.0


%description
Faraday is an HTTP client library that provides a common interface over many
adapters (such as Net::HTTP) and embraces the concept of Rack middleware when
processing the request/response cycle.


%if_enabled    doc
%package       -n gem-faraday-doc
Version:       2.12.0
Release:       alt1
Summary:       HTTP/REST API client library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faraday
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(faraday) = 2.12.0

%description   -n gem-faraday-doc
HTTP/REST API client library documentation files.

Faraday is an HTTP client library that provides a common interface over many
adapters (such as Net::HTTP) and embraces the concept of Rack middleware when
processing the request/response cycle.

%description   -n gem-faraday-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faraday.
%endif


%if_enabled    devel
%package       -n gem-faraday-devel
Version:       2.12.0
Release:       alt1
Summary:       HTTP/REST API client library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета faraday
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(faraday) = 2.12.0
Requires:      gem(bake-test-external) >= 0
Requires:      gem(coveralls_reborn) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rack) >= 3.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.7
Requires:      gem(rspec_junit_formatter) >= 0.4
Requires:      gem(simplecov) >= 0
Requires:      gem(webmock) >= 3.4
Requires:      gem(racc) >= 1.7
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-packaging) >= 0.5
Requires:      gem(rubocop-performance) >= 1.0
Requires:      gem(yard-junk) >= 0
Conflicts:     gem(rack) >= 4
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rspec_junit_formatter) >= 1
Conflicts:     gem(webmock) >= 4
Conflicts:     gem(racc) >= 2
Conflicts:     gem(rubocop-packaging) >= 1
Conflicts:     gem(rubocop-performance) >= 2

%description   -n gem-faraday-devel
HTTP/REST API client library development package.

Faraday is an HTTP client library that provides a common interface over many
adapters (such as Net::HTTP) and embraces the concept of Rack middleware when
processing the request/response cycle.

%description   -n gem-faraday-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета faraday.
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

%if_enabled    doc
%files         -n gem-faraday-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-faraday-devel
%doc README.md
%endif


%changelog
* Fri Oct 18 2024 Pavel Skrylev <majioa@altlinux.org> 2.12.0-alt1
- ^ 2.6.0 -> 2.12.0

* Tue Oct 11 2022 Pavel Skrylev <majioa@altlinux.org> 2.6.0-alt1
- ^ 1.4.2 -> 2.6.0

* Sat Jun 05 2021 Pavel Skrylev <majioa@altlinux.org> 1.4.2-alt1
- + packaged gem with Ruby Policy 2.0
