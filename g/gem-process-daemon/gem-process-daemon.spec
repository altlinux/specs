%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname process-daemon

Name:          gem-process-daemon
Version:       1.0.1
Release:       alt1
Summary:       `Process::Daemon` is a stable and helpful base class for long running tasks and daemons
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ioquatix/process-daemon
Vcs:           https://github.com/ioquatix/process-daemon.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.3
BuildRequires: gem(rspec) >= 3.4.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(rainbow) >= 2.0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rainbow) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rainbow >= 3.1.0,rainbow < 4
Requires:      gem(rainbow) >= 2.0
Conflicts:     gem(rainbow) >= 4
Provides:      gem(process-daemon) = 1.0.1


%description
`Process::Daemon` is a stable and helpful base class for long running tasks and
daemons. Provides standard `start`, `stop`, `restart`, `status` operations.


%if_enabled    doc
%package       -n gem-process-daemon-doc
Version:       1.0.1
Release:       alt1
Summary:       `Process::Daemon` is a stable and helpful base class for long running tasks and daemons documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета process-daemon
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(process-daemon) = 1.0.1

%description   -n gem-process-daemon-doc
`Process::Daemon` is a stable and helpful base class for long running tasks and
daemons. Provides standard `start`, `stop`, `restart`, `status` operations
documentation files.

%description   -n gem-process-daemon-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета process-daemon.
%endif


%if_enabled    devel
%package       -n gem-process-daemon-devel
Version:       1.0.1
Release:       alt1
Summary:       `Process::Daemon` is a stable and helpful base class for long running tasks and daemons development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета process-daemon
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(process-daemon) = 1.0.1
Requires:      gem(bundler) >= 1.3
Requires:      gem(rspec) >= 3.4.0
Requires:      gem(rake) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(coveralls) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rspec) >= 4

%description   -n gem-process-daemon-devel
`Process::Daemon` is a stable and helpful base class for long running tasks and
daemons. Provides standard `start`, `stop`, `restart`, `status` operations
development package.

%description   -n gem-process-daemon-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета process-daemon.
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
%files         -n gem-process-daemon-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-process-daemon-devel
%doc README.md
%endif


%changelog
* Tue Jul 30 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- + packaged gem with Ruby Policy 2.0
