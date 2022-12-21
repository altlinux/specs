%define        gemname foreman_remote_execution

Name:          gem-foreman-remote-execution
Version:       8.0.0
Release:       alt1
Summary:       A plugin bringing remote execution to the Foreman
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman_remote_execution
Vcs:           https://github.com/theforeman/foreman_remote_execution.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       public.tar
Patch:         foreman-3.5.0.patch
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(deface) >= 0
BuildRequires: gem(dynflow) >= 1.0.2 gem(dynflow) < 2.0.0
BuildRequires: gem(foreman-tasks) >= 5.1.0
BuildRequires: gem(factory_bot_rails) >= 4.8.0 gem(factory_bot_rails) < 7
BuildRequires: gem(rdoc) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency factory_bot_rails >= 6.2.0,factory_bot_rails < 7
%ruby_alias_names foreman_remote_execution,foreman-remote-execution
Requires:      gem(deface) >= 0
Requires:      gem(dynflow) >= 1.0.2 gem(dynflow) < 2.0.0
Requires:      gem(foreman-tasks) >= 5.1.0
Provides:      gem(foreman_remote_execution) = 8.0.0


%description
A plugin bringing remote execution to the Foreman, completing the config
management functionality with remote management functionality.


%package       -n gem-foreman-remote-execution-doc
Version:       8.0.0
Release:       alt1
Summary:       A plugin bringing remote execution to the Foreman documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_remote_execution
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_remote_execution) = 8.0.0

%description   -n gem-foreman-remote-execution-doc
A plugin bringing remote execution to the Foreman documentation files.

A plugin bringing remote execution to the Foreman, completing the config
management functionality with remote management functionality.

%description   -n gem-foreman-remote-execution-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman_remote_execution.


%package       -n gem-foreman-remote-execution-devel
Version:       8.0.0
Release:       alt1
Summary:       A plugin bringing remote execution to the Foreman development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman_remote_execution
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman_remote_execution) = 8.0.0
Requires:      gem(factory_bot_rails) >= 4.8.0 gem(factory_bot_rails) < 7
Requires:      gem(rdoc) >= 0

%description   -n gem-foreman-remote-execution-devel
A plugin bringing remote execution to the Foreman development package.

A plugin bringing remote execution to the Foreman, completing the config
management functionality with remote management functionality.

%description   -n gem-foreman-remote-execution-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета foreman_remote_execution.


%prep
%setup
%setup -a 1
%autopatch

%build
%ruby_build

%install
%ruby_install
install -d %buildroot%_datadir/foreman/
cp -rp public %buildroot%_datadir/foreman/

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%_datadir/foreman/public

%files         -n gem-foreman-remote-execution-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-foreman-remote-execution-devel
%doc README.md


%changelog
* Fri Sep 23 2022 Pavel Skrylev <majioa@altlinux.org> 8.0.0-alt1
- ^ 4.7.0 -> 8.0.0

* Wed Sep 01 2021 Pavel Skrylev <majioa@altlinux.org> 4.7.0-alt1
- ^ 4.2.1 -> 4.7.0

* Mon Dec 07 2020 Pavel Skrylev <majioa@altlinux.org> 4.2.1-alt1
- + packaged gem with usage Ruby Policy 2.0
