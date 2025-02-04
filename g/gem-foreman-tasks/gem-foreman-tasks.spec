%define        _unpackaged_files_terminate_build 1
%def_disable    check
%def_enable    doc
%def_enable    devel
%define        gemname foreman-tasks

Name:          gem-foreman-tasks
Epoch:         1
Version:       10.0.0
Release:       alt1
Summary:       Foreman plugin for showing tasks information for resources and users
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman-tasks
Vcs:           https://github.com/theforeman/foreman-tasks.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source1:       public.tar
Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(factory_bot_rails) >= 4.8.0
BuildRequires: gem(sqlite3) >= 0
BuildRequires: gem(theforeman-rubocop) >= 0.1.0
BuildRequires: gem(dynflow) >= 1.9.0
BuildRequires: gem(fugit) >= 1.8
BuildRequires: gem(get_process_mem) >= 0
BuildRequires: gem(sinatra) >= 0
BuildConflicts: gem(factory_bot_rails) >= 7
BuildConflicts: gem(theforeman-rubocop) >= 0.2
BuildConflicts: gem(fugit) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency factory_bot_rails >= 6.2.0,factory_bot_rails < 7
Requires:      gem(dynflow) >= 1.9.0
Requires:      gem(fugit) >= 1.8
Requires:      gem(get_process_mem) >= 0
Requires:      gem(sinatra) >= 0
Conflicts:     gem(fugit) >= 2
Provides:      gem(foreman-tasks) = 10.0.0


%description
The goal of this plugin is to unify the way of showing task statuses across the
Foreman instance. It defines Task model for keeping the information about the
tasks and Lock for assigning the tasks to resources. The locking allows dealing
with preventing multiple colliding tasks to be run on the same resource. It also
optionally provides Dynflow infrastructure for using it for managing the tasks.


%if_enabled    doc
%package       -n gem-foreman-tasks-doc
Version:       10.0.0
Release:       alt1
Summary:       Foreman plugin for showing tasks information for resources and users documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman-tasks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman-tasks) = 10.0.0

%description   -n gem-foreman-tasks-doc
Foreman plugin for showing tasks information for resources and users
documentation files.

The goal of this plugin is to unify the way of showing task statuses across the
Foreman instance. It defines Task model for keeping the information about the
tasks and Lock for assigning the tasks to resources. The locking allows dealing
with preventing multiple colliding tasks to be run on the same resource. It also
optionally provides Dynflow infrastructure for using it for managing the tasks.

%description   -n gem-foreman-tasks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman-tasks.
%endif


%if_enabled    devel
%package       -n gem-foreman-tasks-devel
Version:       10.0.0
Release:       alt1
Summary:       Foreman plugin for showing tasks information for resources and users development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman-tasks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman-tasks) = 10.0.0
Requires:      gem(factory_bot_rails) >= 4.8.0
Requires:      gem(sqlite3) >= 0
Requires:      gem(theforeman-rubocop) >= 0.1.0
Conflicts:     gem(factory_bot_rails) >= 7
Conflicts:     gem(theforeman-rubocop) >= 0.2

%description   -n gem-foreman-tasks-devel
Foreman plugin for showing tasks information for resources and users development
package.

The goal of this plugin is to unify the way of showing task statuses across the
Foreman instance. It defines Task model for keeping the information about the
tasks and Lock for assigning the tasks to resources. The locking allows dealing
with preventing multiple colliding tasks to be run on the same resource. It also
optionally provides Dynflow infrastructure for using it for managing the tasks.

%description   -n gem-foreman-tasks-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета foreman-tasks.
%endif


%prep
%setup
%autopatch

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
%files         -n gem-foreman-tasks-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-foreman-tasks-devel
%doc README.md
%endif


%changelog
* Thu Oct 03 2024 Pavel Skrylev <majioa@altlinux.org> 1:10.0.0-alt1
- ^ 7.0.0 -> 10.0.0

* Thu Apr 06 2023 Pavel Skrylev <majioa@altlinux.org> 1:7.0.0-alt2.1
- ! public webpack and assets

* Thu Mar 30 2023 Pavel Skrylev <majioa@altlinux.org> 1:7.0.0-alt2
- ! patch to properly save a host record

* Tue Jan 31 2023 Pavel Skrylev <majioa@altlinux.org> 1:7.0.0-alt1.1
- ! with closing build deps under check condition

* Fri Sep 23 2022 Pavel Skrylev <majioa@altlinux.org> 1:7.0.0-alt1
- ^ 5.1.1 -> 7.0.0

* Fri Oct 22 2021 Pavel Skrylev <majioa@altlinux.org> 1:5.1.1-alt1.1
- ^ 5.0.0 -> 5.1.1
- ! file path argument to render with template

* Wed Sep 01 2021 Pavel Skrylev <majioa@altlinux.org> 1:5.0.0-alt1
- ^ 3.0.2 -> 5.0.0
- ! epoch for gem-foreman-tasks-doc package

* Mon Dec 07 2020 Pavel Skrylev <majioa@altlinux.org> 3.0.2-alt1
- + packaged gem with usage Ruby Policy 2.0
