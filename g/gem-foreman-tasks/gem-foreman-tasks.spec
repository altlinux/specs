%define        gemname foreman-tasks

Name:          gem-foreman-tasks
Epoch:         1
Version:       7.0.0
Release:       alt1
Summary:       Foreman plugin for showing tasks information for resources and users
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman-tasks
Vcs:           https://github.com/theforeman/foreman-tasks.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       public.tar
Patch:         template-fix.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(dynflow) >= 1.6.0
BuildRequires: gem(get_process_mem) >= 0
BuildRequires: gem(parse-cron) >= 0.1.4 gem(parse-cron) < 0.2
BuildRequires: gem(sinatra) >= 0
BuildRequires: gem(factory_bot_rails) >= 4.8.0 gem(factory_bot_rails) < 7
BuildRequires: gem(sqlite3) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency factory_bot_rails >= 6.2.0,factory_bot_rails < 7
Requires:      gem(dynflow) >= 1.6.0
Requires:      gem(get_process_mem) >= 0
Requires:      gem(parse-cron) >= 0.1.4 gem(parse-cron) < 0.2
Requires:      gem(sinatra) >= 0
Provides:      gem(foreman-tasks) = 7.0.0


%description
The goal of this plugin is to unify the way of showing task statuses across the
Foreman instance. It defines Task model for keeping the information about the
tasks and Lock for assigning the tasks to resources. The locking allows dealing
with preventing multiple colliding tasks to be run on the same resource. It also
optionally provides Dynflow infrastructure for using it for managing the tasks.


%package       -n gem-foreman-tasks-doc
Version:       7.0.0
Release:       alt1
Summary:       Foreman plugin for showing tasks information for resources and users documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman-tasks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman-tasks) = 7.0.0

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
Version:       7.0.0
Release:       alt1
Summary:       Foreman plugin for showing tasks information for resources and users development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman-tasks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman-tasks) = 7.0.0
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
%setup -a 1

%build
%ruby_build

%install
%ruby_install
install -d %buildroot%_datadir/foreman
cp -rp public %buildroot%_datadir/foreman

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%_datadir/foreman/public

%files         -n gem-foreman-tasks-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-foreman-tasks-devel
%doc README.md


%changelog
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
