%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname resque

Name:          gem-resque
Version:       3.0.0
Release:       alt1
Summary:       Resque is a Redis-backed Ruby library for creating background jobs, placing them on multiple queues, and processing them later
License:       MIT
Group:         Development/Ruby
Url:           http://resque.github.io/
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(base64) >= 0.1
BuildRequires: gem(benchmark) >= 0
BuildRequires: gem(json) >= 0
BuildRequires: gem(logger) >= 0
BuildRequires: gem(minitest) >= 5.11
BuildRequires: gem(mocha) >= 2.0
BuildRequires: gem(mono_logger) >= 1
BuildRequires: gem(multi_json) >= 1.0
BuildRequires: gem(ostruct) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(puma) >= 0
BuildRequires: gem(rack) >= 3.0
BuildRequires: gem(rack-test) >= 1.1.0
BuildRequires: gem(rackup) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(redis) >= 5.0
BuildRequires: gem(redis-namespace) >= 1.6
BuildRequires: gem(rubocop) >= 0.80
BuildRequires: gem(sinatra) >= 2.0
BuildRequires: gem(webrick) >= 0
BuildConflicts: gem(base64) >= 1
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(mocha) >= 3
BuildConflicts: gem(mono_logger) >= 2
BuildConflicts: gem(multi_json) >= 2
BuildConflicts: gem(rack) >= 4
BuildConflicts: gem(rack-test) >= 3
BuildConflicts: gem(redis) >= 7
BuildConflicts: gem(redis-namespace) >= 2
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency redis >= 6.0.0,redis < 7
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rack-test >= 1.1.0,rack-test < 2
Requires:      ruby >= 3.0.0
Requires:      gem(base64) >= 0.1
Requires:      gem(logger) >= 0
Requires:      gem(mono_logger) >= 1
Requires:      gem(multi_json) >= 1.0
Requires:      gem(redis) >= 5.0
Requires:      gem(redis-namespace) >= 1.6
Requires:      gem(sinatra) >= 2.0
Conflicts:     gem(base64) >= 1
Conflicts:     gem(mono_logger) >= 2
Conflicts:     gem(multi_json) >= 2
Conflicts:     gem(redis) >= 7
Conflicts:     gem(redis-namespace) >= 2
Provides:      gem(resque) = 3.0.0

%description
Resque (pronounced like "rescue") is a Redis-backed library for creating
background jobs, placing those jobs on multiple queues, and processing them
later.

Background jobs can be any Ruby class or module that responds to perform. Your
existing classes can easily be converted to background jobs or you can create
new classes specifically to do work. Or, you can do both.

Resque is heavily inspired by DelayedJob (which rocks) and comprises three
parts:

* A Ruby library for creating, querying, and processing jobs
* A Rake task for starting a worker which processes jobs
* A Sinatra app for monitoring queues, jobs, and workers.

Resque workers can be distributed between multiple machines, support priorities,
are resilient to memory bloat / "leaks," are optimized for REE (but work on MRI
and JRuby), tell you what they're doing, and expect failure.

Resque queues are persistent; support constant time, atomic push and pop (thanks
to Redis); provide visibility into their contents; and store jobs as simple JSON
packages.

The Resque frontend tells you what workers are doing, what workers are not
doing, what queues you're using, what's in those queues, provides general usage
stats, and helps you track failures.

Resque now supports Ruby 2.3.0 and above. We will also only be supporting Redis
3.0 and above going forward.


%package       -n resque
Version:       3.0.0
Release:       alt1
Summary:       Resque is a Redis-backed Ruby library for creating background jobs, placing them on multiple queues, and processing them later executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета resque
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(resque) = 3.0.0
Requires:      gem(benchmark) >= 0
Requires:      gem(ostruct) >= 0
Requires:      gem(rack) >= 3.0
Requires:      gem(rackup) >= 0
Requires:      gem(redis) >= 5.0
Conflicts:     gem(rack) >= 4
Conflicts:     gem(redis) >= 7

%description   -n resque
Resque is a Redis-backed Ruby library for creating background jobs, placing them
on multiple queues, and processing them later executable(s).

%description   -n resque -l ru_RU.UTF-8
Исполнямка для самоцвета resque.


%if_enabled    doc
%package       -n gem-resque-doc
Version:       3.0.0
Release:       alt1
Summary:       Resque is a Redis-backed Ruby library for creating background jobs, placing them on multiple queues, and processing them later documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета resque
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(resque) = 3.0.0

%description   -n gem-resque-doc
Resque is a Redis-backed Ruby library for creating background jobs, placing them
on multiple queues, and processing them later documentation files.

%description   -n gem-resque-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета resque.
%endif


%if_enabled    devel
%package       -n gem-resque-devel
Version:       3.0.0
Release:       alt1
Summary:       Resque is a Redis-backed Ruby library for creating background jobs, placing them on multiple queues, and processing them later development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета resque
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(resque) = 3.0.0
Requires:      gem(base64) >= 0.1
Requires:      gem(benchmark) >= 0
Requires:      gem(json) >= 0
Requires:      gem(logger) >= 0
Requires:      gem(minitest) >= 5.11
Requires:      gem(mocha) >= 2.0
Requires:      gem(mono_logger) >= 1
Requires:      gem(multi_json) >= 1.0
Requires:      gem(ostruct) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(puma) >= 0
Requires:      gem(rack) >= 3.0
Requires:      gem(rack-test) >= 1.1.0
Requires:      gem(rackup) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(redis) >= 5.0
Requires:      gem(redis-namespace) >= 1.6
Requires:      gem(rubocop) >= 0.80
Requires:      gem(sinatra) >= 2.0
Requires:      gem(webrick) >= 0
Conflicts:     gem(base64) >= 1
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(mocha) >= 3
Conflicts:     gem(mono_logger) >= 2
Conflicts:     gem(multi_json) >= 2
Conflicts:     gem(rack) >= 4
Conflicts:     gem(rack-test) >= 3
Conflicts:     gem(redis) >= 7
Conflicts:     gem(redis-namespace) >= 2
Conflicts:     gem(rubocop) >= 2

%description   -n gem-resque-devel
Resque is a Redis-backed Ruby library for creating background jobs, placing them
on multiple queues, and processing them later development package.

%description   -n gem-resque-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета resque.
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
%doc HISTORY.md LICENSE README.markdown CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n resque
%doc HISTORY.md LICENSE README.markdown CONTRIBUTING.md
%_bindir/resque
%_bindir/resque-web

%if_enabled    doc
%files         -n gem-resque-doc
%doc HISTORY.md LICENSE README.markdown CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-resque-devel
%doc HISTORY.md LICENSE README.markdown CONTRIBUTING.md
%endif


%changelog
* Mon Mar 30 2026 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- ^ 2.4.0 -> 3.0.0

* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- ^ 2.1.0 -> 2.4.0

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- ^ 2.0.0 -> 2.1.0

* Tue Sep 10 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1.1
- ! spec

* Thu Apr 11 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
