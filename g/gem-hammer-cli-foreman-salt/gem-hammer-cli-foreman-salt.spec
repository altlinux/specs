%define        gemname hammer_cli_foreman_salt

Name:          gem-hammer-cli-foreman-salt
Version:       0.1.0
Release:       alt1
Summary:       Foreman Salt-related commands for Hammer
License:       GPL-3.0
Group:         Development/Ruby
Url:           http://github.com/theforeman/hammer_cli_foreman_salt
Vcs:           https://github.com/theforeman/hammer_cli_foreman_salt.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       foreman_salt.yml
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(hammer_cli_foreman) >= 2.0.0
BuildConflicts: gem(hammer_cli_foreman) >= 4.0.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names hammer_cli_foreman_salt,hammer-cli-foreman-salt
Requires:      gem(hammer_cli_foreman) >= 2.0.0
Conflicts:     gem(hammer_cli_foreman) >= 4.0.0
Provides:      gem(hammer_cli_foreman_salt) = 0.1.0


%description
This Hammer CLI plugin contains set of commands for foreman_salt, a plugin to
Foreman for SaltStack.


%package       -n gem-hammer-cli-foreman-salt-doc
Version:       0.1.0
Release:       alt1
Summary:       Foreman Salt-related commands for Hammer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hammer_cli_foreman_salt
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_salt) = 0.1.0

%description   -n gem-hammer-cli-foreman-salt-doc
Foreman Salt-related commands for Hammer documentation files.

This Hammer CLI plugin contains set of commands for foreman_salt, a plugin to
Foreman for SaltStack.

%description   -n gem-hammer-cli-foreman-salt-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hammer_cli_foreman_salt.


%package       -n gem-hammer-cli-foreman-salt-devel
Version:       0.1.0
Release:       alt1
Summary:       Foreman Salt-related commands for Hammer development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hammer_cli_foreman_salt
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_salt) = 0.1.0

%description   -n gem-hammer-cli-foreman-salt-devel
Foreman Salt-related commands for Hammer development package.

This Hammer CLI plugin contains set of commands for foreman_salt, a plugin to
Foreman for SaltStack.

%description   -n gem-hammer-cli-foreman-salt-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hammer_cli_foreman_salt.


%prep
%setup

%build
%ruby_build

%install
%ruby_install
install -Dm0644 %SOURCE1 %buildroot%_sysconfdir/hammer/cli.modules.d/foreman_salt.yml

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%attr(770,_foreman,foreman) %config(noreplace) %_sysconfdir/hammer/cli.modules.d/foreman_salt.yml

%files         -n gem-hammer-cli-foreman-salt-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-hammer-cli-foreman-salt-devel
%doc README.md


%changelog
* Mon Feb 06 2023 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt1
- ^ 0.0.5 -> 0.1.0

* Fri Dec 03 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.5-alt1
- + packaged gem with Ruby Policy 2.0
