%define        gemname yardstick

Name:          gem-yardstick
Version:       0.9.9
Release:       alt1
Summary:       A tool for verifying YARD documentation coverage
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/dkubb/yardstick
Vcs:           https://github.com/dkubb/yardstick.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.3
BuildRequires: gem(rake) >= 10.1.0
BuildRequires: gem(rspec) >= 2.14.1
BuildRequires: gem(yard) >= 0.8.7.2
BuildRequires: gem(rubysl-singleton) >= 2.0.0
BuildRequires: gem(kramdown) >= 1.3.0
BuildRequires: gem(guard) >= 2.2.4
BuildRequires: gem(guard-bundler) >= 2.0.0
BuildRequires: gem(guard-rspec) >= 4.2.0
BuildRequires: gem(guard-rubocop) >= 1.0.0
BuildRequires: gem(listen) >= 2.4.0
BuildRequires: gem(rb-fchange) >= 0.0.6
BuildRequires: gem(rb-fsevent) >= 0.9.3
BuildRequires: gem(rb-inotify) >= 0.9.0
BuildRequires: gem(libnotify) >= 0.8.0
BuildRequires: gem(rb-notifu) >= 0.0.4
BuildRequires: gem(terminal-notifier-guard) >= 1.5.3
BuildRequires: gem(coveralls) >= 0.7.0
BuildRequires: gem(flay) >= 2.4.0
BuildRequires: gem(flog) >= 4.2.0
BuildRequires: gem(reek) >= 1.3.2
BuildRequires: gem(rubocop) >= 0.16.0
BuildRequires: gem(simplecov) >= 0.8.2
BuildRequires: gem(mutant) >= 0.3.4
BuildRequires: gem(yard-spellcheck) >= 0.1.5
BuildRequires: gem(json) >= 1.8.1
BuildRequires: gem(racc) >= 1.4.10
BuildRequires: gem(rubysl-logger) >= 2.0.0
BuildRequires: gem(rubysl-open-uri) >= 2.0.0
BuildRequires: gem(rubysl-prettyprint) >= 2.0.2
BuildRequires: gem(rbench) >= 0.2.3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(rubysl-singleton) >= 2.1
BuildConflicts: gem(kramdown) >= 3
BuildConflicts: gem(guard) >= 2.3
BuildConflicts: gem(guard-bundler) >= 2.1
BuildConflicts: gem(guard-rspec) >= 4.3
BuildConflicts: gem(guard-rubocop) >= 1.1
BuildConflicts: gem(listen) >= 2.5
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
BuildConflicts: gem(mutant) >= 0.4
BuildConflicts: gem(yard-spellcheck) >= 0.2
BuildConflicts: gem(json) >= 3
BuildConflicts: gem(racc) >= 1.5
BuildConflicts: gem(rubysl-logger) >= 2.1
BuildConflicts: gem(rubysl-open-uri) >= 2.1
BuildConflicts: gem(rubysl-prettyprint) >= 2.1
BuildConflicts: gem(rbench) >= 0.3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency kramdown >= 2.3.1,kramdown < 3
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency json >= 2.3.0,json < 3
%ruby_use_gem_dependency yard >= 0.9.27,yard < 1
Requires:      gem(yard) >= 0.8.7.2
Conflicts:     gem(yard) >= 1
Provides:      gem(yardstick) = 0.9.9


%description
Measure YARD documentation coverage


%package       -n yardstick
Version:       0.9.9
Release:       alt1
Summary:       A tool for verifying YARD documentation coverage executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета yardstick
Group:         Other
BuildArch:     noarch

Requires:      gem(yardstick) = 0.9.9

%description   -n yardstick
A tool for verifying YARD documentation coverage executable(s).

Measure YARD documentation coverage

%description   -n yardstick -l ru_RU.UTF-8
Исполнямка для самоцвета yardstick.


%package       -n gem-yardstick-doc
Version:       0.9.9
Release:       alt1
Summary:       A tool for verifying YARD documentation coverage documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета yardstick
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(yardstick) = 0.9.9

%description   -n gem-yardstick-doc
A tool for verifying YARD documentation coverage documentation files.

Measure YARD documentation coverage

%description   -n gem-yardstick-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета yardstick.


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

%files         -n yardstick
%doc README.md
%_bindir/yardstick

%files         -n gem-yardstick-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Tue Feb 07 2023 Pavel Skrylev <majioa@altlinux.org> 0.9.9-alt1
- + packaged gem with Ruby Policy 2.0
