%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname faraday-retry

Name:          gem-faraday-retry
Version:       2.3.2
Release:       alt1
Summary:       Catches exceptions and retries each request a limited number of times
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lostisland/faraday-retry
Vcs:           https://github.com/lostisland/faraday-retry.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(base64) >= 0.2
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(faraday) >= 2.0
BuildRequires: gem(faraday-multipart) >= 1.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-packaging) >= 0.5.0
BuildRequires: gem(rubocop-performance) >= 1.0
BuildRequires: gem(rubocop-rspec) >= 2.0
BuildRequires: gem(simplecov) >= 0.17
BuildConflicts: gem(base64) >= 1
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(faraday) >= 3
BuildConflicts: gem(faraday-multipart) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-packaging) >= 1
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rspec) >= 4
BuildConflicts: gem(simplecov) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rubocop-rspec >= 3.7.0,rubocop-rspec < 4
%ruby_use_gem_dependency rubocop-packaging >= 0.5.2,rubocop-packaging < 1
Requires:      ruby >= 2.6
Requires:      gem(base64) >= 0.2
Requires:      gem(faraday) >= 2.0
Conflicts:     ruby >= 4
Conflicts:     gem(base64) >= 1
Conflicts:     gem(faraday) >= 3
Provides:      gem(faraday-retry) = 2.3.2

%description
Catches exceptions and retries each request a limited number of times.


%if_enabled    doc
%package       -n gem-faraday-retry-doc
Version:       2.3.2
Release:       alt1
Summary:       Catches exceptions and retries each request a limited number of times documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faraday-retry
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(faraday-retry) = 2.3.2

%description   -n gem-faraday-retry-doc
Catches exceptions and retries each request a limited number of times
documentation files.

%description   -n gem-faraday-retry-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faraday-retry.
%endif


%if_enabled    devel
%package       -n gem-faraday-retry-devel
Version:       2.3.2
Release:       alt1
Summary:       Catches exceptions and retries each request a limited number of times development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета faraday-retry
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(faraday-retry) = 2.3.2
Requires:      gem(bundler) >= 2.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-packaging) >= 0.5.0
Requires:      gem(rubocop-performance) >= 1.0
Requires:      gem(rubocop-rspec) >= 2.0
Requires:      gem(simplecov) >= 0.17
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-packaging) >= 1
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rspec) >= 4
Conflicts:     gem(simplecov) >= 1

%description   -n gem-faraday-retry-devel
Catches exceptions and retries each request a limited number of times
development package.

%description   -n gem-faraday-retry-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета faraday-retry.
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
%doc CHANGELOG.md LICENSE.md README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-faraday-retry-doc
%doc CHANGELOG.md LICENSE.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-faraday-retry-devel
%doc CHANGELOG.md LICENSE.md README.md
%endif


%changelog
* Wed Nov 26 2025 Pavel Skrylev <majioa@altlinux.org> 2.3.2-alt1
- ^ 2.0.0 -> 2.3.2

* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged gem with Ruby Policy 2.0
