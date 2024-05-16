%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname resque-scheduler

Name:          gem-resque-scheduler
Version:       4.10.1
Release:       alt1
Summary:       Light weight job scheduling on top of Resque
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/resque/resque-scheduler
Vcs:           https://github.com/resque/resque-scheduler.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rufus-scheduler) >= 3.6
BuildRequires: gem(redis) >= 3.3
BuildRequires: gem(sinatra) >= 2.0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(json) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(timecop) >= 0
BuildRequires: gem(rubocop) >= 0.40.0
BuildRequires: gem(mono_logger) >= 1.0
BuildRequires: gem(resque) >= 1.27
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(mono_logger) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rufus-scheduler >= 3.6
Requires:      gem(rufus-scheduler) >= 3.6
Requires:      gem(redis) >= 3.3
Requires:      gem(mono_logger) >= 1.0
Requires:      gem(resque) >= 1.27
Conflicts:     gem(mono_logger) >= 2
Provides:      gem(resque-scheduler) = 4.10.1


%description
Light weight job scheduling on top of Resque. Adds methods enqueue_at/enqueue_in
to schedule jobs in the future. Also supports queueing jobs on a fixed,
cron-like schedule.


%package       -n resque-scheduler
Version:       4.10.1
Release:       alt1
Summary:       Light weight job scheduling on top of Resque executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета resque-scheduler
Group:         Other
BuildArch:     noarch

Requires:      gem(resque-scheduler) = 4.10.1

%description   -n resque-scheduler
Light weight job scheduling on top of Resque executable(s).

Light weight job scheduling on top of Resque. Adds methods enqueue_at/enqueue_in
to schedule jobs in the future. Also supports queueing jobs on a fixed,
cron-like schedule.

%description   -n resque-scheduler -l ru_RU.UTF-8
Исполнямка для самоцвета resque-scheduler.


%if_enabled    doc
%package       -n gem-resque-scheduler-doc
Version:       4.10.1
Release:       alt1
Summary:       Light weight job scheduling on top of Resque documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета resque-scheduler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(resque-scheduler) = 4.10.1

%description   -n gem-resque-scheduler-doc
Light weight job scheduling on top of Resque documentation files.

Light weight job scheduling on top of Resque. Adds methods enqueue_at/enqueue_in
to schedule jobs in the future. Also supports queueing jobs on a fixed,
cron-like schedule.

%description   -n gem-resque-scheduler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета resque-scheduler.
%endif


%if_enabled    devel
%package       -n gem-resque-scheduler-devel
Version:       4.10.1
Release:       alt1
Summary:       Light weight job scheduling on top of Resque development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета resque-scheduler
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(resque-scheduler) = 4.10.1
Requires:      gem(sinatra) >= 2.0
Requires:      gem(bundler) >= 0
Requires:      gem(json) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rack-test) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(timecop) >= 0
Requires:      gem(rubocop) >= 0.40.0
Conflicts:     gem(rubocop) >= 2

%description   -n gem-resque-scheduler-devel
Light weight job scheduling on top of Resque development package.

Light weight job scheduling on top of Resque. Adds methods enqueue_at/enqueue_in
to schedule jobs in the future. Also supports queueing jobs on a fixed,
cron-like schedule.

%description   -n gem-resque-scheduler-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета resque-scheduler.
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

%files         -n resque-scheduler
%doc README.md
%_bindir/resque-scheduler

%if_enabled    doc
%files         -n gem-resque-scheduler-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-resque-scheduler-devel
%doc README.md
%endif


%changelog
* Wed Apr 17 2024 Pavel Skrylev <majioa@altlinux.org> 4.10.1-alt1
- + packaged gem with Ruby Policy 2.0
