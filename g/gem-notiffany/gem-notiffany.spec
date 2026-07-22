%define        _unpackaged_files_terminate_build 1
%def_disable    check
%def_enable    doc
%def_enable    devel
%define        gemname notiffany

Name:          gem-notiffany
Version:       0.1.3
Release:       alt1
Summary:       Notifier library (extracted from Guard project)
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/guard/notiffany
Vcs:           https://github.com/guard/notiffany.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.7
BuildRequires: gem(guard-rspec) >= 4.6
BuildRequires: gem(guard-rubocop) >= 1.2
BuildRequires: gem(listen) >= 3.1
BuildRequires: gem(nenv) >= 0.3
BuildRequires: gem(rake) >= 11.1
BuildRequires: gem(rspec) >= 3.4
BuildRequires: gem(rubocop) >= 0.40
BuildRequires: gem(shellany) >= 0.0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(guard-rspec) >= 5
BuildConflicts: gem(guard-rubocop) >= 2
BuildConflicts: gem(listen) >= 4
BuildConflicts: gem(nenv) >= 1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(shellany) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.5.9,bundler < 3
%ruby_use_gem_dependency rake >= 13.3.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.81.6,rubocop < 2
Requires:      gem(nenv) >= 0.3
Requires:      gem(shellany) >= 0.0
Conflicts:     gem(nenv) >= 1
Conflicts:     gem(shellany) >= 1
Provides:      gem(notiffany) = 0.1.3

%description
Wrapper libray for most popular notification libraries such as Growl, Libnotify,
Notifu


%if_enabled    doc
%package       -n gem-notiffany-doc
Version:       0.1.3
Release:       alt1
Summary:       Notifier library (extracted from Guard project) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета notiffany
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(notiffany) = 0.1.3

%description   -n gem-notiffany-doc
Notifier library (extracted from Guard project) documentation files.

Wrapper libray for most popular notification libraries such as Growl, Libnotify,
Notifu

%description   -n gem-notiffany-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета notiffany.
%endif


%if_enabled    devel
%package       -n gem-notiffany-devel
Version:       0.1.3
Release:       alt1
Summary:       Notifier library (extracted from Guard project) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета notiffany
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(notiffany) = 0.1.3
Requires:      gem(bundler) >= 1.7
Requires:      gem(guard-rspec) >= 4.6
Requires:      gem(guard-rubocop) >= 1.2
Requires:      gem(listen) >= 3.1
Requires:      gem(rake) >= 11.1
Requires:      gem(rspec) >= 3.4
Requires:      gem(rubocop) >= 0.40
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(guard-rspec) >= 5
Conflicts:     gem(guard-rubocop) >= 2
Conflicts:     gem(listen) >= 4
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2

%description   -n gem-notiffany-devel
Notifier library (extracted from Guard project) development package.

Wrapper libray for most popular notification libraries such as Growl, Libnotify,
Notifu

%description   -n gem-notiffany-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета notiffany.
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
%doc LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-notiffany-doc
%doc LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-notiffany-devel
%doc LICENSE.txt README.md
%endif


%changelog
* Tue Jul 07 2026 Alexander Burmatov <thatman@altlinux.org> 0.1.3-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
