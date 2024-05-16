%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rufus-scheduler

Name:          gem-rufus-scheduler
Version:       3.9.1
Release:       alt1
Summary:       scheduler for Ruby (at, in, cron and every jobs)
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jmettraux/rufus-scheduler
Vcs:           https://github.com/jmettraux/rufus-scheduler.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rspec) >= 3.7
BuildRequires: gem(chronic) >= 0.10
BuildRequires: gem(fugit) >= 1.1.6
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(chronic) >= 1
BuildConflicts: gem(fugit) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(fugit) >= 1.1.6
Conflicts:     gem(fugit) >= 2
Obsoletes:     ruby-rufus-scheduler < %EVR
Provides:      ruby-rufus-scheduler = %EVR
Provides:      gem(rufus-scheduler) = 3.9.1


%description
Job scheduler for Ruby (at, cron, in and every jobs). It uses threads.


%if_enabled    doc
%package       -n gem-rufus-scheduler-doc
Version:       3.9.1
Release:       alt1
Summary:       scheduler for Ruby (at, in, cron and every jobs) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rufus-scheduler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rufus-scheduler) = 3.9.1

%description   -n gem-rufus-scheduler-doc
scheduler for Ruby (at, in, cron and every jobs) documentation files.

Job scheduler for Ruby (at, cron, in and every jobs). It uses threads.

%description   -n gem-rufus-scheduler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rufus-scheduler.
%endif


%if_enabled    devel
%package       -n gem-rufus-scheduler-devel
Version:       3.9.1
Release:       alt1
Summary:       scheduler for Ruby (at, in, cron and every jobs) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rufus-scheduler
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rufus-scheduler) = 3.9.1
Requires:      gem(rspec) >= 3.7
Requires:      gem(chronic) >= 0.10
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(chronic) >= 1

%description   -n gem-rufus-scheduler-devel
scheduler for Ruby (at, in, cron and every jobs) development package.

Job scheduler for Ruby (at, cron, in and every jobs). It uses threads.

%description   -n gem-rufus-scheduler-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rufus-scheduler.
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
%files         -n gem-rufus-scheduler-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rufus-scheduler-devel
%doc README.md
%endif


%changelog
* Wed Apr 17 2024 Pavel Skrylev <majioa@altlinux.org> 3.9.1-alt1
- > Ruby Policy 2.0
- ^ 3.6.0 -> 3.9.1

* Fri Apr 26 2019 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.5.2-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.5.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus
