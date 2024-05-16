%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname backburner

Name:          gem-backburner
Version:       1.6.1
Release:       alt1
Summary:       Reliable beanstalk background job processing made easy for Ruby and Sinatra
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/nesquena/backburner
Vcs:           https://github.com/nesquena/backburner.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 3.2.0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(beaneater) >= 1.0
BuildRequires: gem(dante) > 0.1.5
BuildRequires: gem(concurrent-ruby) >= 1.0.1
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(beaneater) >= 2
BuildConflicts: gem(concurrent-ruby) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Requires:      gem(beaneater) >= 1.0
Requires:      gem(dante) > 0.1.5
Requires:      gem(concurrent-ruby) >= 1.0.1
Conflicts:     gem(beaneater) >= 2
Conflicts:     gem(concurrent-ruby) >= 2
Provides:      gem(backburner) = 1.6.1


%description
Backburner is a beanstalkd-powered job queue that can handle a very high volume
of jobs. You create background jobs and place them on multiple work queues to be
processed later.

Processing background jobs reliably has never been easier than with beanstalkd
and Backburner. This gem works with any ruby-based web framework, but is
especially suited for use with Sinatra, Padrino and Rails.

If you want to use beanstalk for your job processing, consider using Backburner.
Backburner is heavily inspired by Resque and DelayedJob. Backburner stores all
jobs as simple JSON message payloads. Persistent queues are supported when
beanstalkd persistence mode is enabled.

Backburner supports multiple queues, job priorities, delays, and timeouts. In
addition, Backburner has robust support for retrying failed jobs, handling error
cases, custom logging, and extensible plugin hooks.


%package       -n backburner
Version:       1.6.1
Release:       alt1
Summary:       Reliable beanstalk background job processing made easy for Ruby and Sinatra executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета backburner
Group:         Other
BuildArch:     noarch

Requires:      gem(backburner) = 1.6.1

%description   -n backburner
Reliable beanstalk background job processing made easy for Ruby and Sinatra
executable(s).

Backburner is a beanstalkd-powered job queue that can handle a very high volume
of jobs. You create background jobs and place them on multiple work queues to be
processed later.

Processing background jobs reliably has never been easier than with beanstalkd
and Backburner. This gem works with any ruby-based web framework, but is
especially suited for use with Sinatra, Padrino and Rails.

If you want to use beanstalk for your job processing, consider using Backburner.
Backburner is heavily inspired by Resque and DelayedJob. Backburner stores all
jobs as simple JSON message payloads. Persistent queues are supported when
beanstalkd persistence mode is enabled.

Backburner supports multiple queues, job priorities, delays, and timeouts. In
addition, Backburner has robust support for retrying failed jobs, handling error
cases, custom logging, and extensible plugin hooks.


%description   -n backburner -l ru_RU.UTF-8
Исполнямка для самоцвета backburner.


%if_enabled    doc
%package       -n gem-backburner-doc
Version:       1.6.1
Release:       alt1
Summary:       Reliable beanstalk background job processing made easy for Ruby and Sinatra documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета backburner
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(backburner) = 1.6.1

%description   -n gem-backburner-doc
Reliable beanstalk background job processing made easy for Ruby and Sinatra
documentation files.

Backburner is a beanstalkd-powered job queue that can handle a very high volume
of jobs. You create background jobs and place them on multiple work queues to be
processed later.

Processing background jobs reliably has never been easier than with beanstalkd
and Backburner. This gem works with any ruby-based web framework, but is
especially suited for use with Sinatra, Padrino and Rails.

If you want to use beanstalk for your job processing, consider using Backburner.
Backburner is heavily inspired by Resque and DelayedJob. Backburner stores all
jobs as simple JSON message payloads. Persistent queues are supported when
beanstalkd persistence mode is enabled.

Backburner supports multiple queues, job priorities, delays, and timeouts. In
addition, Backburner has robust support for retrying failed jobs, handling error
cases, custom logging, and extensible plugin hooks.


%description   -n gem-backburner-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета backburner.
%endif


%if_enabled    devel
%package       -n gem-backburner-devel
Version:       1.6.1
Release:       alt1
Summary:       Reliable beanstalk background job processing made easy for Ruby and Sinatra development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета backburner
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(backburner) = 1.6.1
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 3.2.0
Requires:      gem(mocha) >= 0
Conflicts:     gem(minitest) >= 6

%description   -n gem-backburner-devel
Reliable beanstalk background job processing made easy for Ruby and Sinatra
development package.

Backburner is a beanstalkd-powered job queue that can handle a very high volume
of jobs. You create background jobs and place them on multiple work queues to be
processed later.

Processing background jobs reliably has never been easier than with beanstalkd
and Backburner. This gem works with any ruby-based web framework, but is
especially suited for use with Sinatra, Padrino and Rails.

If you want to use beanstalk for your job processing, consider using Backburner.
Backburner is heavily inspired by Resque and DelayedJob. Backburner stores all
jobs as simple JSON message payloads. Persistent queues are supported when
beanstalkd persistence mode is enabled.

Backburner supports multiple queues, job priorities, delays, and timeouts. In
addition, Backburner has robust support for retrying failed jobs, handling error
cases, custom logging, and extensible plugin hooks.


%description   -n gem-backburner-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета backburner.
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

%files         -n backburner
%doc README.md
%_bindir/backburner

%if_enabled    doc
%files         -n gem-backburner-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-backburner-devel
%doc README.md
%endif


%changelog
* Wed Apr 24 2024 Pavel Skrylev <majioa@altlinux.org> 1.6.1-alt1
- + packaged gem with Ruby Policy 2.0
