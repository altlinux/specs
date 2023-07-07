%define        gemname foreman_monitoring

Name:          gem-foreman-monitoring
Version:       2.1.0
Release:       alt2
Summary:       Foreman plugin for monitoring system integration
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman_monitoring
Vcs:           https://github.com/theforeman/foreman_monitoring.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         foreman-3.5.0.patch
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(rubocop) >= 0.80.0 gem(rubocop) < 2
BuildRequires: gem(rubocop-minitest) >= 0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rails) >= 0
BuildRequires: gem(deface) < 2.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(deface) < 2.0
Provides:      gem(foreman_monitoring) = 2.1.0

%ruby_alias_names foreman_monitoring,foreman-monitoring

%description
Foreman plugin for monitoring system integration.


%package       -n gem-foreman-monitoring-doc
Version:       2.1.0
Release:       alt2
Summary:       Foreman plugin for monitoring system integration documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_monitoring
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_monitoring) = 2.1.0

%description   -n gem-foreman-monitoring-doc
Foreman plugin for monitoring system integration documentation files.

%description   -n gem-foreman-monitoring-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman_monitoring.


%package       -n gem-foreman-monitoring-devel
Version:       2.1.0
Release:       alt2
Summary:       Foreman plugin for monitoring system integration development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman_monitoring
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman_monitoring) = 2.1.0
Requires:      gem(rdoc) >= 0
Requires:      gem(rubocop) >= 0.80.0 gem(rubocop) < 2
Requires:      gem(rubocop-minitest) >= 0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rails) >= 0

%description   -n gem-foreman-monitoring-devel
Foreman plugin for monitoring system integration development package.

%description   -n gem-foreman-monitoring-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета foreman_monitoring.


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

%files         -n gem-foreman-monitoring-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-foreman-monitoring-devel
%doc README.md


%changelog
* Wed Jul 05 2023 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt2
- ! fixed patch for proper defaults

* Tue Apr 04 2023 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1.1
- ! patch to allow proper migrating

* Fri Sep 23 2022 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- + packaged gem with Ruby Policy 2.0
