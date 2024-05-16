%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname http

Name:          gem-http
Version:       5.2.0
Release:       alt1
Summary:       HTTP should be easy
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/httprb/http
Vcs:           https://github.com/httprb/http.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(webrick) >= 0
BuildRequires: gem(guard-rspec) >= 0
BuildRequires: gem(nokogiri) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(fuubar) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(certificate_authority) >= 1.0
BuildRequires: gem(backports) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rake) >= 0
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(simplecov-lcov) >= 0
BuildRequires: gem(rspec) >= 3.10
BuildRequires: gem(rspec-its) >= 0
BuildRequires: gem(yardstick) >= 0
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(addressable) >= 2.8
BuildRequires: gem(base64) >= 0.1
BuildRequires: gem(http-cookie) >= 1.0
BuildRequires: gem(http-form_data) >= 2.2
BuildRequires: gem(llhttp-ffi) >= 0.5.0
BuildConflicts: gem(certificate_authority) >= 2
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(addressable) >= 3
BuildConflicts: gem(base64) >= 1
BuildConflicts: gem(http-cookie) >= 2
BuildConflicts: gem(http-form_data) >= 3
BuildConflicts: gem(llhttp-ffi) >= 0.6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(addressable) >= 2.8
Requires:      gem(base64) >= 0.1
Requires:      gem(http-cookie) >= 1.0
Requires:      gem(http-form_data) >= 2.2
Requires:      gem(llhttp-ffi) >= 0.5.0
Conflicts:     gem(addressable) >= 3
Conflicts:     gem(base64) >= 1
Conflicts:     gem(http-cookie) >= 2
Conflicts:     gem(http-form_data) >= 3
Conflicts:     gem(llhttp-ffi) >= 0.6
Provides:      gem(http) = 5.2.0


%description
An easy-to-use client library for making requests from Ruby. It uses a simple
method chaining system for building requests, similar to Python's Requests.


%if_enabled    doc
%package       -n gem-http-doc
Version:       5.2.0
Release:       alt1
Summary:       HTTP should be easy documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета http
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(http) = 5.2.0

%description   -n gem-http-doc
HTTP should be easy documentation files.

An easy-to-use client library for making requests from Ruby. It uses a simple
method chaining system for building requests, similar to Python's Requests.

%description   -n gem-http-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета http.
%endif


%if_enabled    devel
%package       -n gem-http-devel
Version:       5.2.0
Release:       alt1
Summary:       HTTP should be easy development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета http
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(http) = 5.2.0
Requires:      gem(rake) >= 0
Requires:      gem(webrick) >= 0
Requires:      gem(guard-rspec) >= 0
Requires:      gem(nokogiri) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(fuubar) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(certificate_authority) >= 1.0
Requires:      gem(backports) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rake) >= 0
Requires:      gem(rubocop-rspec) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov-lcov) >= 0
Requires:      gem(rspec) >= 3.10
Requires:      gem(rspec-its) >= 0
Requires:      gem(yardstick) >= 0
Requires:      gem(kramdown) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(bundler) >= 2.0
Conflicts:     gem(certificate_authority) >= 2
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(bundler) >= 3

%description   -n gem-http-devel
HTTP should be easy development package.

An easy-to-use client library for making requests from Ruby. It uses a simple
method chaining system for building requests, similar to Python's Requests.

%description   -n gem-http-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета http.
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
%files         -n gem-http-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-http-devel
%doc README.md
%endif


%changelog
* Tue Apr 16 2024 Pavel Skrylev <majioa@altlinux.org> 5.2.0-alt1
- + packaged gem with Ruby Policy 2.0
