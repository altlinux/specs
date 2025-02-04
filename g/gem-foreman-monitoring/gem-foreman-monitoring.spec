%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname foreman_monitoring

Name:          gem-foreman-monitoring
Version:       3.2.0
Release:       alt1
Summary:       Foreman plugin for monitoring system integration
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman_monitoring
Vcs:           https://github.com/theforeman/foreman_monitoring.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(theforeman-rubocop) >= 0.1.0
BuildConflicts: gem(theforeman-rubocop) >= 0.2
BuildConflicts: gem(deface) >= 2.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names foreman_monitoring,foreman-monitoring
Conflicts:     gem(deface) >= 2.0
Provides:      gem(foreman_monitoring) = 3.2.0


%description
Foreman plugin for monitoring system integration.


%if_enabled    doc
%package       -n gem-foreman-monitoring-doc
Version:       3.2.0
Release:       alt1
Summary:       Foreman plugin for monitoring system integration documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_monitoring
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_monitoring) = 3.2.0

%description   -n gem-foreman-monitoring-doc
Foreman plugin for monitoring system integration documentation files.

%description   -n gem-foreman-monitoring-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman_monitoring.
%endif


%if_enabled    devel
%package       -n gem-foreman-monitoring-devel
Version:       3.2.0
Release:       alt1
Summary:       Foreman plugin for monitoring system integration development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman_monitoring
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman_monitoring) = 3.2.0
Requires:      gem(rdoc) >= 0
Requires:      gem(theforeman-rubocop) >= 0.1.0
Conflicts:     gem(theforeman-rubocop) >= 0.2

%description   -n gem-foreman-monitoring-devel
Foreman plugin for monitoring system integration development package.

%description   -n gem-foreman-monitoring-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета foreman_monitoring.
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
%files         -n gem-foreman-monitoring-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-foreman-monitoring-devel
%doc README.md
%endif


%changelog
* Fri Oct 04 2024 Pavel Skrylev <majioa@altlinux.org> 3.2.0-alt1
- ^ 2.1.0 -> 3.2.0

* Wed Jul 05 2023 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt2
- ! fixed patch for proper defaults

* Tue Apr 04 2023 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1.1
- ! patch to allow proper migrating

* Fri Sep 23 2022 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- + packaged gem with Ruby Policy 2.0
