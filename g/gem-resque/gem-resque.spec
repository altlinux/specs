%define        pkgname resque

Name:          gem-%pkgname
Version:       2.0.0
Release:       alt1.1
Summary:       Resque is a Redis-backed Ruby library for creating background jobs, placing them on multiple queues, and processing them later
License:       MIT
Group:         Development/Ruby
Url:           http://resque.github.io/
%vcs           https://github.com/resque/resque.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

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


%package       -n %pkgname
Summary:       %summary
Group:         Development/Documentation
BuildArch:     noarch

%description   -n %pkgname
%summary.

That is executable-containing package.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         -n %pkgname
%_bindir/*

%files         doc
%ruby_gemdocdir

%changelog
* Tue Sep 10 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1.1
- ! spec

* Thu Apr 11 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
