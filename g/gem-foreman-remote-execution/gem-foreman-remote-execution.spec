%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname foreman_remote_execution

Name:          gem-foreman-remote-execution
Version:       16.2.3
Release:       alt1
Summary:       A plugin bringing remote execution to the Foreman
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman_remote_execution
Vcs:           https://github.com/theforeman/foreman_remote_execution.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(deface) >= 0
BuildRequires: gem(dynflow) >= 1.0.2
BuildRequires: gem(factory_bot_rails) >= 4.8.0
BuildRequires: gem(foreman-tasks) >= 8.3.0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(theforeman-rubocop) >= 0.1.2
BuildConflicts: gem(dynflow) >= 2.0.0
BuildConflicts: gem(factory_bot_rails) >= 7
BuildConflicts: gem(theforeman-rubocop) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency factory_bot_rails >= 6.2.0,factory_bot_rails < 7
%ruby_use_gem_dependency theforeman-rubocop >= 0.1.2,theforeman-rubocop < 1
%ruby_alias_names foreman_remote_execution,foreman-remote-execution
Requires:      ruby >= 2.7
Requires:      gem(deface) >= 0
Requires:      gem(dynflow) >= 1.0.2
Requires:      gem(foreman-tasks) >= 8.3.0
Conflicts:     ruby >= 4
Conflicts:     gem(dynflow) >= 2.0.0
Provides:      gem(foreman_remote_execution) = 16.2.3

%description
A plugin bringing remote execution to the Foreman, completing the config
management functionality with remote management functionality.


%if_enabled    doc
%package       -n gem-foreman-remote-execution-doc
Version:       16.2.3
Release:       alt1
Summary:       A plugin bringing remote execution to the Foreman documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_remote_execution
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_remote_execution) = 16.2.3

%description   -n gem-foreman-remote-execution-doc
A plugin bringing remote execution to the Foreman documentation files.

A plugin bringing remote execution to the Foreman, completing the config
management functionality with remote management functionality.

%description   -n gem-foreman-remote-execution-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman_remote_execution.
%endif


%if_enabled    devel
%package       -n gem-foreman-remote-execution-devel
Version:       16.2.3
Release:       alt1
Summary:       A plugin bringing remote execution to the Foreman development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman_remote_execution
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman_remote_execution) = 16.2.3
Requires:      gem(factory_bot_rails) >= 4.8.0
Requires:      gem(rdoc) >= 0
Conflicts:     gem(factory_bot_rails) >= 7

%description   -n gem-foreman-remote-execution-devel
A plugin bringing remote execution to the Foreman development package.

A plugin bringing remote execution to the Foreman, completing the config
management functionality with remote management functionality.

%description   -n gem-foreman-remote-execution-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета foreman_remote_execution.
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
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-foreman-remote-execution-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-foreman-remote-execution-devel
%doc LICENSE README.md
%endif


%changelog
* Wed Oct 22 2025 Pavel Skrylev <majioa@altlinux.org> 16.2.3-alt1
- ^ 14.0.0 -> 16.2.3

* Tue Oct 01 2024 Pavel Skrylev <majioa@altlinux.org> 14.0.0-alt1
- ^ 8.0.0 -> 14.0.0

* Thu Apr 06 2023 Pavel Skrylev <majioa@altlinux.org> 8.0.0-alt1.1
- ! public assets and webpack

* Fri Sep 23 2022 Pavel Skrylev <majioa@altlinux.org> 8.0.0-alt1
- ^ 4.7.0 -> 8.0.0

* Wed Sep 01 2021 Pavel Skrylev <majioa@altlinux.org> 4.7.0-alt1
- ^ 4.2.1 -> 4.7.0

* Mon Dec 07 2020 Pavel Skrylev <majioa@altlinux.org> 4.2.1-alt1
- + packaged gem with usage Ruby Policy 2.0
