%define        gemname foreman-tasks

Name:          gem-foreman-tasks
Epoch:         1
Version:       5.1.1
Release:       alt1.1
Summary:       Foreman plugin for showing tasks information for resources and users
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman-tasks
Vcs:           https://github.com/theforeman/foreman-tasks.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         template-fix.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(dynflow) >= 1.2.3
BuildRequires: gem(get_process_mem) >= 0
BuildRequires: gem(parse-cron) >= 0.1.4 gem(parse-cron) < 0.2
BuildRequires: gem(sinatra) >= 0
BuildRequires: gem(factory_bot_rails) >= 4.8.0 gem(factory_bot_rails) < 7
BuildRequires: gem(sqlite3) >= 0
BuildRequires: gem(dynflow) >= 1.2.0
BuildRequires: gem(smart_proxy_dynflow) >= 0.5.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency factory_bot_rails >= 6.2.0,factory_bot_rails < 7
Requires:      gem(dynflow) >= 1.2.3
Requires:      gem(get_process_mem) >= 0
Requires:      gem(parse-cron) >= 0.1.4 gem(parse-cron) < 0.2
Requires:      gem(sinatra) >= 0
Provides:      gem(foreman-tasks) = 5.1.1


%description
The goal of this plugin is to unify the way of showing task statuses across the
Foreman instance. It defines Task model for keeping the information about the
tasks and Lock for assigning the tasks to resources. The locking allows dealing
with preventing multiple colliding tasks to be run on the same resource. It also
optionally provides Dynflow infrastructure for using it for managing the tasks.


%package       -n gem-foreman-tasks-core
Version:       0.4.0
Release:       alt1.1
Summary:       Common code used both at Forman and Foreman proxy regarding tasks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dynflow) >= 1.2.0
Requires:      gem(smart_proxy_dynflow) >= 0.5.0
Provides:      gem(foreman-tasks-core) = 0.4.0

%description   -n gem-foreman-tasks-core
Common code used both at Forman and Foreman proxy regarding tasks


%package       -n gem-foreman-tasks-core-doc
Version:       0.4.0
Release:       alt1.1
Summary:       Common code used both at Forman and Foreman proxy regarding tasks documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman-tasks-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman-tasks-core) = 0.4.0

%description   -n gem-foreman-tasks-core-doc
Common code used both at Forman and Foreman proxy regarding tasks documentation
files.

Common code used both at Forman and Foreman proxy regarding tasks

%description   -n gem-foreman-tasks-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman-tasks-core.


%package       -n gem-foreman-tasks-core-devel
Version:       0.4.0
Release:       alt1.1
Summary:       Common code used both at Forman and Foreman proxy regarding tasks development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman-tasks-core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman-tasks-core) = 0.4.0

%description   -n gem-foreman-tasks-core-devel
Common code used both at Forman and Foreman proxy regarding tasks development
package.

Common code used both at Forman and Foreman proxy regarding tasks

%description   -n gem-foreman-tasks-core-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета foreman-tasks-core.


%package       -n gem-foreman-tasks-doc
Version:       5.1.1
Release:       alt1.1
Summary:       Foreman plugin for showing tasks information for resources and users documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman-tasks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman-tasks) = 5.1.1

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


%package       -n gem-foreman-tasks-devel
Version:       5.1.1
Release:       alt1.1
Summary:       Foreman plugin for showing tasks information for resources and users development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman-tasks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman-tasks) = 5.1.1
Requires:      gem(factory_bot_rails) >= 4.8.0 gem(factory_bot_rails) < 7
Requires:      gem(sqlite3) >= 0

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


%prep
%setup
%patch

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

%files         -n gem-foreman-tasks-core
%ruby_gemspecdir/foreman-tasks-core-0.4.0.gemspec
%ruby_gemslibdir/foreman-tasks-core-0.4.0

%files         -n gem-foreman-tasks-core-doc
%ruby_gemsdocdir/foreman-tasks-core-0.4.0

%files         -n gem-foreman-tasks-core-devel

%files         -n gem-foreman-tasks-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-foreman-tasks-devel
%doc README.md


%changelog
* Fri Oct 22 2021 Pavel Skrylev <majioa@altlinux.org> 1:5.1.1-alt1.1
- ^ 5.0.0 -> 5.1.1
- ! file path argument to render with template

* Wed Sep 01 2021 Pavel Skrylev <majioa@altlinux.org> 1:5.0.0-alt1
- ^ 3.0.2 -> 5.0.0
- ! epoch for gem-foreman-tasks-doc package

* Mon Dec 07 2020 Pavel Skrylev <majioa@altlinux.org> 3.0.2-alt1
- + packaged gem with usage Ruby Policy 2.0
