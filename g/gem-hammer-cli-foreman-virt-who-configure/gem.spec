%define        gemname hammer_cli_foreman_virt_who_configure

Name:          gem-hammer-cli-foreman-virt-who-configure
Version:       0.0.9
Release:       alt1
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
BuildRequires: gem(hammer_cli) >= 0.5.0
BuildRequires: gem(hammer_cli_foreman) >= 0.5.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(hammer_cli) >= 0.5.0
Requires:      gem(hammer_cli_foreman) >= 0.5.0
Provides:      gem(hammer_cli_foreman_virt_who_configure) = 0.0.9


%description
Hammer CLI commands for configuring Virt Who for Katello.


%package       -n gem-hammer-cli-foreman-virt-who-configure-doc
Version:       0.0.9
Release:       alt1
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
Release:       alt1
Summary:       Plugin for configuring Virt Who development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hammer_cli_foreman_virt_who_configure
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_virt_who_configure) = 0.0.9

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
* Sat Dec 04 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.9-alt1
- + packaged gem with Ruby Policy 2.0
