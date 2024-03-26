%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname ice_nine

Name:          gem-ice-nine
Version:       0.11.1
Release:       alt1
Summary:       Deep Freeze Ruby Objects
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/dkubb/ice_nine
Vcs:           https://github.com/dkubb/ice_nine.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.6
BuildRequires: gem(rake) >= 10.4.0
BuildRequires: gem(rspec) >= 3.1.0
BuildRequires: gem(rspec-core) >= 3.1.7
BuildRequires: gem(rspec-its) >= 1.1.0
BuildRequires: gem(yard) >= 0.8.7.6
BuildRequires: gem(kramdown) >= 1.5.0
BuildRequires: gem(guard) >= 2.10.1
BuildRequires: gem(guard-bundler) >= 2.0.0
BuildRequires: gem(guard-rspec) >= 4.3.1
BuildRequires: gem(guard-rubocop) >= 1.2.0
BuildRequires: gem(listen) >= 2.8.1
BuildRequires: gem(rb-fchange) >= 0.0.6
BuildRequires: gem(rb-fsevent) >= 0.9.4
BuildRequires: gem(rb-inotify) >= 0.9.5
BuildRequires: gem(libnotify) >= 0.8.4
BuildRequires: gem(rb-notifu) >= 0.0.4
BuildRequires: gem(terminal-notifier-guard) >= 1.6.4
BuildRequires: gem(coveralls) >= 0.7.2
BuildRequires: gem(flay) >= 2.5.0
BuildRequires: gem(flog) >= 4.3.0
BuildRequires: gem(reek) >= 1.5.0
BuildRequires: gem(rubocop) >= 0.27.1
BuildRequires: gem(simplecov) >= 0.9.1
BuildRequires: gem(yardstick) >= 0.9.9
BuildRequires: gem(json) >= 1.8.1
BuildRequires: gem(racc) >= 1.4.12
BuildRequires: gem(rbench) >= 0.2.3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-core) >= 4
BuildConflicts: gem(rspec-its) >= 1.2
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(kramdown) >= 3
BuildConflicts: gem(guard) >= 2.11
BuildConflicts: gem(guard-bundler) >= 2.1
BuildConflicts: gem(guard-rspec) >= 4.4
BuildConflicts: gem(guard-rubocop) >= 1.3
BuildConflicts: gem(listen) >= 2.9
BuildConflicts: gem(rb-fchange) >= 0.1
BuildConflicts: gem(rb-fsevent) >= 0.10
BuildConflicts: gem(rb-inotify) >= 0.10
BuildConflicts: gem(libnotify) >= 0.9
BuildConflicts: gem(rb-notifu) >= 0.1
BuildConflicts: gem(terminal-notifier-guard) >= 1.7
BuildConflicts: gem(coveralls) >= 0.8
BuildConflicts: gem(flay) >= 2.6
BuildConflicts: gem(flog) >= 4.4
BuildConflicts: gem(reek) >= 1.6
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(yardstick) >= 0.10
BuildConflicts: gem(json) >= 3
BuildConflicts: gem(racc) >= 1.5
BuildConflicts: gem(rbench) >= 0.3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency kramdown >= 2.3.1,kramdown < 3
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rspec-core >= 3.10.1,rspec-core < 4
%ruby_use_gem_dependency json >= 2.3.0,json < 3
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
Provides:      gem(ice_nine) = 0.11.1


%description
Deep Freeze Ruby Objects


%if_enabled    doc
%package       -n gem-ice-nine-doc
Version:       0.11.1
Release:       alt1
Summary:       Deep Freeze Ruby Objects documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ice_nine
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ice_nine) = 0.11.1

%description   -n gem-ice-nine-doc
Deep Freeze Ruby Objects documentation files.
%description   -n gem-ice-nine-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ice_nine.
%endif


%if_enabled    devel
%package       -n gem-ice-nine-devel
Version:       0.11.1
Release:       alt1
Summary:       Deep Freeze Ruby Objects development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ice_nine
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ice_nine) = 0.11.1
Requires:      gem(bundler) >= 1.6
Requires:      gem(rake) >= 10.4.0
Requires:      gem(rspec) >= 3.1.0
Requires:      gem(rspec-core) >= 3.1.7
Requires:      gem(rspec-its) >= 1.1.0
Requires:      gem(yard) >= 0.8.7.6
Requires:      gem(kramdown) >= 1.5.0
Requires:      gem(guard) >= 2.10.1
Requires:      gem(guard-bundler) >= 2.0.0
Requires:      gem(guard-rspec) >= 4.3.1
Requires:      gem(guard-rubocop) >= 1.2.0
Requires:      gem(listen) >= 2.8.1
Requires:      gem(rb-fchange) >= 0.0.6
Requires:      gem(rb-fsevent) >= 0.9.4
Requires:      gem(rb-inotify) >= 0.9.5
Requires:      gem(libnotify) >= 0.8.4
Requires:      gem(rb-notifu) >= 0.0.4
Requires:      gem(terminal-notifier-guard) >= 1.6.4
Requires:      gem(coveralls) >= 0.7.2
Requires:      gem(flay) >= 2.5.0
Requires:      gem(flog) >= 4.3.0
Requires:      gem(reek) >= 1.5.0
Requires:      gem(rubocop) >= 0.27.1
Requires:      gem(simplecov) >= 0.9.1
Requires:      gem(yardstick) >= 0.9.9
Requires:      gem(json) >= 1.8.1
Requires:      gem(racc) >= 1.4.12
Requires:      gem(rbench) >= 0.2.3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rspec-core) >= 4
Conflicts:     gem(rspec-its) >= 1.2
Conflicts:     gem(yard) >= 1
Conflicts:     gem(kramdown) >= 3
Conflicts:     gem(guard) >= 2.11
Conflicts:     gem(guard-bundler) >= 2.1
Conflicts:     gem(guard-rspec) >= 4.4
Conflicts:     gem(guard-rubocop) >= 1.3
Conflicts:     gem(listen) >= 2.9
Conflicts:     gem(rb-fchange) >= 0.1
Conflicts:     gem(rb-fsevent) >= 0.10
Conflicts:     gem(rb-inotify) >= 0.10
Conflicts:     gem(libnotify) >= 0.9
Conflicts:     gem(rb-notifu) >= 0.1
Conflicts:     gem(terminal-notifier-guard) >= 1.7
Conflicts:     gem(coveralls) >= 0.8
Conflicts:     gem(flay) >= 2.6
Conflicts:     gem(flog) >= 4.4
Conflicts:     gem(reek) >= 1.6
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(yardstick) >= 0.10
Conflicts:     gem(json) >= 3
Conflicts:     gem(racc) >= 1.5
Conflicts:     gem(rbench) >= 0.3

%description   -n gem-ice-nine-devel
Deep Freeze Ruby Objects development package.
%description   -n gem-ice-nine-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ice_nine.
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
%files         -n gem-ice-nine-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ice-nine-devel
%doc README.md
%endif


%changelog
* Tue Mar 26 2024 Pavel Skrylev <majioa@altlinux.org> 0.11.1-alt1
- + packaged gem with Ruby Policy 2.0
