%define        gemname faraday-retry

Name:          gem-faraday-retry
Version:       2.0.0
Release:       alt1
Summary:       Catches exceptions and retries each request a limited number of times
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lostisland/faraday-retry
Vcs:           https://github.com/lostisland/faraday-retry.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-packaging) >= 0.5.0
BuildRequires: gem(rubocop-performance) >= 1.0
BuildRequires: gem(rubocop-rspec) >= 2.0
BuildRequires: gem(faraday-multipart) >= 1.0
BuildRequires: gem(faraday) >= 2.0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-packaging) >= 0.6
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rspec) >= 3
BuildConflicts: gem(faraday-multipart) >= 2
BuildConflicts: gem(faraday) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Requires:      gem(faraday) >= 2.0
Conflicts:     gem(faraday) >= 3
Provides:      gem(faraday-retry) = 2.0.0


%description
Catches exceptions and retries each request a limited number of times.


%package       -n gem-faraday-retry-doc
Version:       2.0.0
Release:       alt1
Summary:       Catches exceptions and retries each request a limited number of times documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faraday-retry
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(faraday-retry) = 2.0.0

%description   -n gem-faraday-retry-doc
Catches exceptions and retries each request a limited number of times
documentation files.

%description   -n gem-faraday-retry-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faraday-retry.


%package       -n gem-faraday-retry-devel
Version:       2.0.0
Release:       alt1
Summary:       Catches exceptions and retries each request a limited number of times development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета faraday-retry
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(faraday-retry) = 2.0.0
Requires:      gem(bundler) >= 2.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(simplecov) >= 0.17
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-packaging) >= 0.5.0
Requires:      gem(rubocop-performance) >= 1.0
Requires:      gem(rubocop-rspec) >= 2.0
Requires:      gem(faraday-multipart) >= 1.0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-packaging) >= 0.6
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rspec) >= 3
Conflicts:     gem(faraday-multipart) >= 2

%description   -n gem-faraday-retry-devel
Catches exceptions and retries each request a limited number of times
development package.

%description   -n gem-faraday-retry-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета faraday-retry.


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

%files         -n gem-faraday-retry-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-faraday-retry-devel
%doc README.md


%changelog
* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged gem with Ruby Policy 2.0
