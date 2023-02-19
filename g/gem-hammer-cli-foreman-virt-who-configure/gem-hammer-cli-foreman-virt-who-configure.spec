%define        gemname hammer_cli_foreman_virt_who_configure

Name:          gem-hammer-cli-foreman-virt-who-configure
Version:       0.0.9
Release:       alt1.1
Summary:       Plugin for configuring Virt Who
License:       GPL-3.0+
Group:         Development/Ruby
Url:           https://github.com/theforeman/hammer-cli-foreman-virt-who-configure
Vcs:           https://github.com/theforeman/hammer-cli-foreman-virt-who-configure.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       foreman_virt_who_configure.yml
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(gettext) >= 3.1.3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(thor) >= 0
BuildRequires: gem(minitest) >= 4.7.4
BuildRequires: gem(minitest-spec-context) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(ci_reporter) >= 1.6.3
BuildRequires: gem(hammer_cli) >= 0.5.0
BuildRequires: gem(hammer_cli_foreman) >= 0.5.0
BuildConflicts: gem(gettext) >= 4.0.0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(ci_reporter) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency ci_reporter >= 2.0.0,ci_reporter < 3
%ruby_alias_names hammer_cli_foreman_virt_who_configure,hammer-cli-foreman-virt-who-configure
Requires:      gem(hammer_cli) >= 0.5.0
Requires:      gem(hammer_cli_foreman) >= 0.5.0
Provides:      gem(hammer_cli_foreman_virt_who_configure) = 0.0.9


%description
Hammer CLI commands for configuring Virt Who for Katello.


%package       -n gem-hammer-cli-foreman-virt-who-configure-doc
Version:       0.0.9
Release:       alt1.1
Summary:       Plugin for configuring Virt Who documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hammer_cli_foreman_virt_who_configure
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_virt_who_configure) = 0.0.9

%description   -n gem-hammer-cli-foreman-virt-who-configure-doc
Plugin for configuring Virt Who documentation files.

Hammer CLI commands for configuring Virt Who for Katello.

%description   -n gem-hammer-cli-foreman-virt-who-configure-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hammer_cli_foreman_virt_who_configure.


%package       -n gem-hammer-cli-foreman-virt-who-configure-devel
Version:       0.0.9
Release:       alt1.1
Summary:       Plugin for configuring Virt Who development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hammer_cli_foreman_virt_who_configure
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_virt_who_configure) = 0.0.9
Requires:      gem(gettext) >= 3.1.3
Requires:      gem(rake) >= 0
Requires:      gem(thor) >= 0
Requires:      gem(minitest) >= 4.7.4
Requires:      gem(minitest-spec-context) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(ci_reporter) >= 1.6.3
Conflicts:     gem(gettext) >= 4.0.0
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(ci_reporter) >= 3

%description   -n gem-hammer-cli-foreman-virt-who-configure-devel
Plugin for configuring Virt Who development package.

Hammer CLI commands for configuring Virt Who for Katello.

%description   -n gem-hammer-cli-foreman-virt-who-configure-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hammer_cli_foreman_virt_who_configure.


%prep
%setup

%build
%ruby_build

%install
%ruby_install
install -Dm0644 %SOURCE1 %buildroot%_sysconfdir/hammer/cli.modules.d/foreman_virt_who_configure.yml

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%attr(770,_foreman,foreman) %config(noreplace) %_sysconfdir/hammer/cli.modules.d/foreman_virt_who_configure.yml

%files         -n gem-hammer-cli-foreman-virt-who-configure-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-hammer-cli-foreman-virt-who-configure-devel
%doc README.md


%changelog
* Mon Feb 06 2023 Pavel Skrylev <majioa@altlinux.org> 0.0.9-alt1.1
- ! closes build deps under check condition

* Sat Dec 04 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.9-alt1
- + packaged gem with Ruby Policy 2.0
