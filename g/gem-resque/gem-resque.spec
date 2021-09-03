%define        gemname resque

Name:          gem-resque
Version:       2.1.0
Release:       alt1
Summary:       Resque is a Redis-backed Ruby library for creating background jobs, placing them on multiple queues, and processing them later
License:       MIT
Group:         Development/Ruby
Url:           http://resque.github.io/
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(redis-namespace) >= 1.6 gem(redis-namespace) < 2
BuildRequires: gem(vegas) >= 0.1.2 gem(vegas) < 0.2
BuildRequires: gem(sinatra) >= 0.9.2
BuildRequires: gem(multi_json) >= 1.0 gem(multi_json) < 2
BuildRequires: gem(mono_logger) >= 1.0 gem(mono_logger) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(redis-namespace) >= 1.6 gem(redis-namespace) < 2
Requires:      gem(vegas) >= 0.1.2 gem(vegas) < 0.2
Requires:      gem(sinatra) >= 0.9.2
Requires:      gem(multi_json) >= 1.0 gem(multi_json) < 2
Requires:      gem(mono_logger) >= 1.0 gem(mono_logger) < 2
Provides:      gem(resque) = 2.1.0


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
Version:       2.1.0
Release:       alt1
Summary:       Resque is a Redis-backed Ruby library for creating background jobs, placing them on multiple queues, and processing them later executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета resque
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(resque) = 2.1.0

%description   -n resque
Resque is a Redis-backed Ruby library for creating background jobs, placing them
on multiple queues, and processing them later executable(s).

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

%description   -n resque -l ru_RU.UTF-8
Исполнямка для самоцвета resque.


%package       -n gem-resque-doc
Version:       2.1.0
Release:       alt1
Summary:       Resque is a Redis-backed Ruby library for creating background jobs, placing them on multiple queues, and processing them later documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета resque
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(resque) = 2.1.0

%description   -n gem-resque-doc
Resque is a Redis-backed Ruby library for creating background jobs, placing them
on multiple queues, and processing them later documentation files.

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

%description   -n gem-resque-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета resque.


%package       -n gem-resque-devel
Version:       2.1.0
Release:       alt1
Summary:       Resque is a Redis-backed Ruby library for creating background jobs, placing them on multiple queues, and processing them later development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета resque
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(resque) = 2.1.0

%description   -n gem-resque-devel
Resque is a Redis-backed Ruby library for creating background jobs, placing them
on multiple queues, and processing them later development package.

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

%description   -n gem-resque-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета resque.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.markdown
%ruby_gemspec
%ruby_gemlibdir

%files         -n resque
%doc README.markdown
%_bindir/resque
%_bindir/resque-web

%files         -n gem-resque-doc
%doc README.markdown
%ruby_gemdocdir

%files         -n gem-resque-devel
%doc README.markdown


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- ^ 2.0.0 -> 2.1.0

* Tue Sep 10 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1.1
- ! spec

* Thu Apr 11 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
