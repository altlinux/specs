%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname danger

Name:          gem-danger
Version:       9.4.3
Release:       alt1
Summary:       Like Unit Tests, but for your Team Culture
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/danger/danger
Vcs:           https://github.com/danger/danger.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         patch.patch
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(chandler) >= 0
BuildRequires: gem(danger-gitlab) >= 0
BuildRequires: gem(danger-junit) >= 0.5
BuildRequires: gem(fuubar) >= 2.5
BuildRequires: gem(guard) >= 2.16
BuildRequires: gem(guard-rspec) >= 4.7
BuildRequires: gem(guard-rubocop) >= 1.2
BuildRequires: gem(listen) = 3.0.7
BuildRequires: gem(pry) >= 0.13
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.9
BuildRequires: gem(rspec_junit_formatter) >= 0.4
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(test-queue) >= 0
BuildRequires: gem(webmock) >= 3.13.0
BuildRequires: gem(yard) >= 0.9.11
BuildRequires: gem(claide) >= 1.0
BuildRequires: gem(claide-plugins) >= 0.9.2
BuildRequires: gem(colored2) >= 3.1
BuildRequires: gem(cork) >= 0.1
BuildRequires: gem(faraday) >= 0.9.0
BuildRequires: gem(faraday-http-cache) >= 2.0
BuildRequires: gem(git) >= 1.13
BuildRequires: gem(kramdown) >= 2.3
BuildRequires: gem(kramdown-parser-gfm) >= 1.0
BuildRequires: gem(no_proxy_fix) >= 0
BuildRequires: gem(octokit) >= 4.0
BuildRequires: gem(terminal-table) >= 1
BuildConflicts: gem(danger-junit) >= 1
BuildConflicts: gem(fuubar) >= 3
BuildConflicts: gem(guard) >= 3
BuildConflicts: gem(guard-rspec) >= 5
BuildConflicts: gem(guard-rubocop) >= 2
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec_junit_formatter) >= 1
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(claide) >= 2
BuildConflicts: gem(colored2) >= 4
BuildConflicts: gem(cork) >= 1
BuildConflicts: gem(faraday) >= 3
BuildConflicts: gem(faraday-http-cache) >= 3
BuildConflicts: gem(git) >= 2
BuildConflicts: gem(kramdown) >= 3
BuildConflicts: gem(kramdown-parser-gfm) >= 2
BuildConflicts: gem(terminal-table) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
Requires:      gem(claide) >= 1.0
Requires:      gem(claide-plugins) >= 0.9.2
Requires:      gem(colored2) >= 3.1
Requires:      gem(cork) >= 0.1
Requires:      gem(faraday) >= 0.9.0
Requires:      gem(faraday-http-cache) >= 2.0
Requires:      gem(git) >= 1.13
Requires:      gem(kramdown) >= 2.3
Requires:      gem(kramdown-parser-gfm) >= 1.0
Requires:      gem(no_proxy_fix) >= 0
Requires:      gem(octokit) >= 4.0
Requires:      gem(terminal-table) >= 1
Conflicts:     gem(claide) >= 2
Conflicts:     gem(colored2) >= 4
Conflicts:     gem(cork) >= 1
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(faraday-http-cache) >= 3
Conflicts:     gem(git) >= 2
Conflicts:     gem(kramdown) >= 3
Conflicts:     gem(kramdown-parser-gfm) >= 2
Conflicts:     gem(terminal-table) >= 4
Provides:      gem(danger) = 9.4.3


%description
Stop Saying 'You Forgot To...' in Code Review. Formalize your Pull Request
etiquette.


%package       -n danger
Version:       9.4.3
Release:       alt1
Summary:       Like Unit Tests, but for your Team Culture executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета danger
Group:         Other
BuildArch:     noarch

Requires:      gem(danger) = 9.4.3

%description   -n danger
Like Unit Tests, but for your Team Culture executable(s).

Stop Saying 'You Forgot To...' in Code Review. Formalize your Pull Request
etiquette.

%description   -n danger -l ru_RU.UTF-8
Исполнямка для самоцвета danger.


%if_enabled    doc
%package       -n gem-danger-doc
Version:       9.4.3
Release:       alt1
Summary:       Like Unit Tests, but for your Team Culture documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета danger
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(danger) = 9.4.3

%description   -n gem-danger-doc
Like Unit Tests, but for your Team Culture documentation files.

Stop Saying 'You Forgot To...' in Code Review. Formalize your Pull Request
etiquette.

%description   -n gem-danger-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета danger.
%endif


%if_enabled    devel
%package       -n gem-danger-devel
Version:       9.4.3
Release:       alt1
Summary:       Like Unit Tests, but for your Team Culture development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета danger
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(danger) = 9.4.3
Requires:      gem(bundler) >= 0
Requires:      gem(chandler) >= 0
Requires:      gem(danger-gitlab) >= 0
Requires:      gem(danger-junit) >= 0.5
Requires:      gem(fuubar) >= 2.5
Requires:      gem(guard) >= 2.16
Requires:      gem(guard-rspec) >= 4.7
Requires:      gem(guard-rubocop) >= 1.2
Requires:      gem(listen) = 3.0.7
Requires:      gem(pry) >= 0.13
Requires:      gem(pry-byebug) >= 0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.9
Requires:      gem(rspec_junit_formatter) >= 0.4
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(simplecov) >= 0.17
Requires:      gem(test-queue) >= 0
Requires:      gem(webmock) >= 3.13.0
Requires:      gem(yard) >= 0.9.11
Conflicts:     gem(danger-junit) >= 1
Conflicts:     gem(fuubar) >= 3
Conflicts:     gem(guard) >= 3
Conflicts:     gem(guard-rspec) >= 5
Conflicts:     gem(guard-rubocop) >= 2
Conflicts:     gem(pry) >= 1
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rspec_junit_formatter) >= 1
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(webmock) >= 4
Conflicts:     gem(yard) >= 1

%description   -n gem-danger-devel
Like Unit Tests, but for your Team Culture development package.

Stop Saying 'You Forgot To...' in Code Review. Formalize your Pull Request
etiquette.

%description   -n gem-danger-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета danger.
%endif


%prep
%setup
%autopatch

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

%files         -n danger
%doc README.md
%_bindir/danger

%if_enabled    doc
%files         -n gem-danger-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-danger-devel
%doc README.md
%endif


%changelog
* Fri Mar 15 2024 Pavel Skrylev <majioa@altlinux.org> 9.4.3-alt1
- ^ 9.0.0 -> 9.4.3

* Fri Oct 14 2022 Pavel Skrylev <majioa@altlinux.org> 9.0.0-alt0.1
- ^ 8.6.1 -> 9.0.0

* Fri May 06 2022 Pavel Skrylev <majioa@altlinux.org> 8.6.1-alt1
- + packaged gem with Ruby Policy 2.0
