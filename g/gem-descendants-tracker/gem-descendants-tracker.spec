%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname descendants_tracker

Name:          gem-descendants-tracker
Version:       0.0.4
Release:       alt1
Summary:       Module that adds descendant tracking to a class
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/dkubb/descendants_tracker
Vcs:           https://github.com/dkubb/descendants_tracker.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.5
BuildRequires: gem(rake) >= 10.2.1
BuildRequires: gem(rspec) >= 2.14.1
BuildRequires: gem(rspec-core) >= 2.14.8
BuildRequires: gem(yard) >= 0.8.7.4
BuildRequires: gem(rubysl-singleton) >= 2.0.0
BuildRequires: gem(kramdown) >= 1.3.3
BuildRequires: gem(guard) >= 2.6.0
BuildRequires: gem(guard-bundler) >= 2.0.0
BuildRequires: gem(guard-rspec) >= 4.2.8
BuildRequires: gem(guard-rubocop) >= 1.0.2
BuildRequires: gem(listen) >= 2.7.1
BuildRequires: gem(rb-fchange) >= 0.0.6
BuildRequires: gem(rb-fsevent) >= 0.9.4
BuildRequires: gem(rb-inotify) >= 0.9.3
BuildRequires: gem(libnotify) >= 0.8.2
BuildRequires: gem(rb-notifu) >= 0.0.4
BuildRequires: gem(terminal-notifier-guard) >= 1.5.3
BuildRequires: gem(coveralls) >= 0.7.0
BuildRequires: gem(flay) >= 2.4.0
BuildRequires: gem(flog) >= 4.2.0
BuildRequires: gem(reek) >= 1.3.7
BuildRequires: gem(rubocop) >= 0.19.1
BuildRequires: gem(simplecov) >= 0.8.2
BuildRequires: gem(yardstick) >= 0.9.9
BuildRequires: gem(mutant) >= 0.5.8
BuildRequires: gem(mutant-rspec) >= 0.5.3
BuildRequires: gem(yard-spellcheck) >= 0.1.5
BuildRequires: gem(json) >= 1.8.1
BuildRequires: gem(racc) >= 1.4.11
BuildRequires: gem(rubysl-logger) >= 2.0.0
BuildRequires: gem(rubysl-open-uri) >= 2.0.0
BuildRequires: gem(rubysl-prettyprint) >= 2.0.3
BuildRequires: gem(rbench) >= 0.2.3
BuildRequires: gem(thread_safe) >= 0.3.1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-core) >= 4
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(rubysl-singleton) >= 2.1
BuildConflicts: gem(kramdown) >= 3
BuildConflicts: gem(guard) >= 2.7
BuildConflicts: gem(guard-bundler) >= 2.1
BuildConflicts: gem(guard-rspec) >= 4.3
BuildConflicts: gem(guard-rubocop) >= 1.1
BuildConflicts: gem(listen) >= 2.8
BuildConflicts: gem(rb-fchange) >= 0.1
BuildConflicts: gem(rb-fsevent) >= 0.10
BuildConflicts: gem(rb-inotify) >= 0.10
BuildConflicts: gem(libnotify) >= 0.9
BuildConflicts: gem(rb-notifu) >= 0.1
BuildConflicts: gem(terminal-notifier-guard) >= 1.6
BuildConflicts: gem(coveralls) >= 0.8
BuildConflicts: gem(flay) >= 2.5
BuildConflicts: gem(flog) >= 4.3
BuildConflicts: gem(reek) >= 1.4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(yardstick) >= 0.10
BuildConflicts: gem(mutant) >= 0.6
BuildConflicts: gem(mutant-rspec) >= 0.6
BuildConflicts: gem(yard-spellcheck) >= 0.2
BuildConflicts: gem(json) >= 3
BuildConflicts: gem(racc) >= 1.5
BuildConflicts: gem(rubysl-logger) >= 2.1
BuildConflicts: gem(rubysl-open-uri) >= 2.1
BuildConflicts: gem(rubysl-prettyprint) >= 2.1
BuildConflicts: gem(rbench) >= 0.3
BuildConflicts: gem(thread_safe) >= 1
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
Requires:      gem(thread_safe) >= 0.3.1
Conflicts:     gem(thread_safe) >= 1
Provides:      gem(descendants_tracker) = 0.0.4


%description
Module that adds descendant tracking to a class


%if_enabled    doc
%package       -n gem-descendants-tracker-doc
Version:       0.0.4
Release:       alt1
Summary:       Module that adds descendant tracking to a class documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета descendants_tracker
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(descendants_tracker) = 0.0.4

%description   -n gem-descendants-tracker-doc
Module that adds descendant tracking to a class documentation files.

%description   -n gem-descendants-tracker-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета descendants_tracker.
%endif


%if_enabled    devel
%package       -n gem-descendants-tracker-devel
Version:       0.0.4
Release:       alt1
Summary:       Module that adds descendant tracking to a class development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета descendants_tracker
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(descendants_tracker) = 0.0.4
Requires:      gem(bundler) >= 1.5
Requires:      gem(rake) >= 10.2.1
Requires:      gem(rspec) >= 2.14.1
Requires:      gem(rspec-core) >= 2.14.8
Requires:      gem(yard) >= 0.8.7.4
Requires:      gem(rubysl-singleton) >= 2.0.0
Requires:      gem(kramdown) >= 1.3.3
Requires:      gem(guard) >= 2.6.0
Requires:      gem(guard-bundler) >= 2.0.0
Requires:      gem(guard-rspec) >= 4.2.8
Requires:      gem(guard-rubocop) >= 1.0.2
Requires:      gem(listen) >= 2.7.1
Requires:      gem(rb-fchange) >= 0.0.6
Requires:      gem(rb-fsevent) >= 0.9.4
Requires:      gem(rb-inotify) >= 0.9.3
Requires:      gem(libnotify) >= 0.8.2
Requires:      gem(rb-notifu) >= 0.0.4
Requires:      gem(terminal-notifier-guard) >= 1.5.3
Requires:      gem(coveralls) >= 0.7.0
Requires:      gem(flay) >= 2.4.0
Requires:      gem(flog) >= 4.2.0
Requires:      gem(reek) >= 1.3.7
Requires:      gem(rubocop) >= 0.19.1
Requires:      gem(simplecov) >= 0.8.2
Requires:      gem(yardstick) >= 0.9.9
Requires:      gem(mutant) >= 0.5.8
Requires:      gem(mutant-rspec) >= 0.5.3
Requires:      gem(yard-spellcheck) >= 0.1.5
Requires:      gem(json) >= 1.8.1
Requires:      gem(racc) >= 1.4.11
Requires:      gem(rubysl-logger) >= 2.0.0
Requires:      gem(rubysl-open-uri) >= 2.0.0
Requires:      gem(rubysl-prettyprint) >= 2.0.3
Requires:      gem(rbench) >= 0.2.3
Requires:      gem(jruby-openssl) >= 0.8.5
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rspec-core) >= 4
Conflicts:     gem(yard) >= 1
Conflicts:     gem(rubysl-singleton) >= 2.1
Conflicts:     gem(kramdown) >= 3
Conflicts:     gem(guard) >= 2.7
Conflicts:     gem(guard-bundler) >= 2.1
Conflicts:     gem(guard-rspec) >= 4.3
Conflicts:     gem(guard-rubocop) >= 1.1
Conflicts:     gem(listen) >= 2.8
Conflicts:     gem(rb-fchange) >= 0.1
Conflicts:     gem(rb-fsevent) >= 0.10
Conflicts:     gem(rb-inotify) >= 0.10
Conflicts:     gem(libnotify) >= 0.9
Conflicts:     gem(rb-notifu) >= 0.1
Conflicts:     gem(terminal-notifier-guard) >= 1.6
Conflicts:     gem(coveralls) >= 0.8
Conflicts:     gem(flay) >= 2.5
Conflicts:     gem(flog) >= 4.3
Conflicts:     gem(reek) >= 1.4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(yardstick) >= 0.10
Conflicts:     gem(mutant) >= 0.6
Conflicts:     gem(mutant-rspec) >= 0.6
Conflicts:     gem(yard-spellcheck) >= 0.2
Conflicts:     gem(json) >= 3
Conflicts:     gem(racc) >= 1.5
Conflicts:     gem(rubysl-logger) >= 2.1
Conflicts:     gem(rubysl-open-uri) >= 2.1
Conflicts:     gem(rubysl-prettyprint) >= 2.1
Conflicts:     gem(rbench) >= 0.3
Conflicts:     gem(jruby-openssl) >= 0.9

%description   -n gem-descendants-tracker-devel
Module that adds descendant tracking to a class development package.

%description   -n gem-descendants-tracker-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета descendants_tracker.
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
%files         -n gem-descendants-tracker-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-descendants-tracker-devel
%doc README.md
%endif


%changelog
* Tue Oct 22 2024 Pavel Skrylev <majioa@altlinux.org> 0.0.4-alt1
- + packaged gem with Ruby Policy 2.0
