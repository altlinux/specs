%define        gemname faraday-em_http

Name:          gem-faraday-em-http
Version:       1.0.0.1
Release:       alt0.1
Summary:       Faraday adapter for Em::Http
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lostisland/faraday-em_http
Vcs:           https://github.com/lostisland/faraday-em_http.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(em-http-request) >= 1.1
BuildRequires: gem(faraday) >= 1.0
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(multipart-parser) >= 0.1.1
BuildRequires: gem(webmock) >= 3.4
BuildRequires: gem(rubocop) >= 0.91.1
BuildRequires: gem(rubocop-packaging) >= 0.5
BuildRequires: gem(rubocop-performance) >= 1.0
BuildConflicts: gem(faraday) >= 3
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(multipart-parser) >= 0.2
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-packaging) >= 1
BuildConflicts: gem(rubocop-performance) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency faraday >= 2.6.0,faraday < 3
%ruby_alias_names faraday-em_http,faraday-em-http
Provides:      gem(faraday-em_http) = 1.0.0.1

%ruby_use_gem_version faraday-em_http:1.0.0.1

%description
Faraday adapter for Em::Http.


%package       -n gem-faraday-em-http-doc
Version:       1.0.0.1
Release:       alt0.1
Summary:       Faraday adapter for Em::Http documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faraday-em_http
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(faraday-em_http) = 1.0.0.1

%description   -n gem-faraday-em-http-doc
Faraday adapter for Em::Http documentation files.

%description   -n gem-faraday-em-http-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faraday-em_http.


%package       -n gem-faraday-em-http-devel
Version:       1.0.0.1
Release:       alt0.1
Summary:       Faraday adapter for Em::Http development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета faraday-em_http
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(faraday-em_http) = 1.0.0.1
Requires:      gem(em-http-request) >= 1.1
Requires:      gem(faraday) >= 1.0
Requires:      gem(bundler) >= 2.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(simplecov) >= 0.17
Requires:      gem(multipart-parser) >= 0.1.1
Requires:      gem(webmock) >= 3.4
Requires:      gem(rubocop) >= 0.91.1
Requires:      gem(rubocop-packaging) >= 0.5
Requires:      gem(rubocop-performance) >= 1.0
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(multipart-parser) >= 0.2
Conflicts:     gem(webmock) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-packaging) >= 1
Conflicts:     gem(rubocop-performance) >= 2

%description   -n gem-faraday-em-http-devel
Faraday adapter for Em::Http development package.

%description   -n gem-faraday-em-http-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета faraday-em_http.


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

%files         -n gem-faraday-em-http-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-faraday-em-http-devel
%doc README.md


%changelog
* Wed Jan 25 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.0.1-alt0.1
- ^ 1.0.0 -> 1.0.0[1]

* Sat Jun 05 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
