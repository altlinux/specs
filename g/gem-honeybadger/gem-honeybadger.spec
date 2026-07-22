%define        _unpackaged_files_terminate_build 1
%def_disable    check
%def_enable    doc
%def_enable    devel
%define        gemname honeybadger

Name:          gem-honeybadger
Version:       6.9.0
Release:       alt1
Summary:       Full-stack error tracking, performance monitoring, logging, and more
License:       MIT
Group:         Development/Ruby
Url:           https://www.honeybadger.io/for/ruby/
Vcs:           https://github.com/honeybadger-io/honeybadger-ruby.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(appraisal) >= 2.1
BuildRequires: gem(aruba) >= 2.0
BuildRequires: gem(base64) >= 0
BuildRequires: gem(bigdecimal) >= 0
BuildRequires: gem(bump) >= 0.10.0
BuildRequires: gem(capistrano) >= 0
BuildRequires: gem(guard) >= 0
BuildRequires: gem(guard-rspec) >= 0
BuildRequires: gem(logger) >= 0
BuildRequires: gem(mutex_m) >= 0
BuildRequires: gem(ostruct) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rspec-its) >= 1.3.1
BuildRequires: gem(standard) >= 0
BuildRequires: gem(timecop) >= 0
BuildRequires: gem(webmock) >= 0
BuildConflicts: gem(appraisal) >= 3
BuildConflicts: gem(aruba) >= 3
BuildConflicts: gem(bump) >= 1
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-its) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bump >= 0.10.0,bump < 1
Requires:      ruby >= 3.0.0
Requires:      gem(logger) >= 0
Requires:      gem(ostruct) >= 0
Provides:      gem(honeybadger) = 6.9.0

%description
Honeybadger.io unifies error tracking, performance and uptime monitoring, and
logging in one powerfully simple platform. Detect, diagnose, and resolve
production issues faster-so you can focus on building, not debugging.


%package       -n honeybadger
Version:       6.9.0
Release:       alt1
Summary:       Full-stack error tracking, performance monitoring, logging, and more executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета honeybadger
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(honeybadger) = 6.9.0

%description   -n honeybadger
Full-stack error tracking, performance monitoring, logging, and more
executable(s).

Honeybadger.io unifies error tracking, performance and uptime monitoring, and
logging in one powerfully simple platform. Detect, diagnose, and resolve
production issues faster-so you can focus on building, not debugging.

%description   -n honeybadger -l ru_RU.UTF-8
Исполнямка для самоцвета honeybadger.


%if_enabled    doc
%package       -n gem-honeybadger-doc
Version:       6.9.0
Release:       alt1
Summary:       Full-stack error tracking, performance monitoring, logging, and more documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета honeybadger
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(honeybadger) = 6.9.0

%description   -n gem-honeybadger-doc
Full-stack error tracking, performance monitoring, logging, and more
documentation files.

Honeybadger.io unifies error tracking, performance and uptime monitoring, and
logging in one powerfully simple platform. Detect, diagnose, and resolve
production issues faster-so you can focus on building, not debugging.

%description   -n gem-honeybadger-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета honeybadger.
%endif


%if_enabled    devel
%package       -n gem-honeybadger-devel
Version:       6.9.0
Release:       alt1
Summary:       Full-stack error tracking, performance monitoring, logging, and more development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета honeybadger
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(honeybadger) = 6.9.0
Requires:      gem(appraisal) >= 2.1
Requires:      gem(aruba) >= 2.0
Requires:      gem(base64) >= 0
Requires:      gem(bigdecimal) >= 0
Requires:      gem(bump) >= 0.10.0
Requires:      gem(capistrano) >= 0
Requires:      gem(guard) >= 0
Requires:      gem(guard-rspec) >= 0
Requires:      gem(mutex_m) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rspec-its) >= 1.3.1
Requires:      gem(standard) >= 0
Requires:      gem(timecop) >= 0
Requires:      gem(webmock) >= 0
Conflicts:     gem(appraisal) >= 3
Conflicts:     gem(aruba) >= 3
Conflicts:     gem(bump) >= 1
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rspec-its) >= 3

%description   -n gem-honeybadger-devel
Full-stack error tracking, performance monitoring, logging, and more development
package.

Honeybadger.io unifies error tracking, performance and uptime monitoring, and
logging in one powerfully simple platform. Detect, diagnose, and resolve
production issues faster-so you can focus on building, not debugging.

%description   -n gem-honeybadger-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета honeybadger.
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
%doc CHANGELOG.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n honeybadger
%doc CHANGELOG.md LICENSE README.md
%_bindir/honeybadger

%if_enabled    doc
%files         -n gem-honeybadger-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-honeybadger-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Fri Jul 03 2026 Alexander Burmatov <thatman@altlinux.org> 6.9.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
