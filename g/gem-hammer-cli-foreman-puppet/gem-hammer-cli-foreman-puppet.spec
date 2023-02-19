%define        gemname hammer_cli_foreman_puppet

Name:          gem-hammer-cli-foreman-puppet
Version:       0.0.6
Release:       alt1
Summary:       Foreman Puppet plugin for Hammer CLI
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/hammer-cli-foreman-puppet
Vcs:           https://github.com/theforeman/hammer-cli-foreman-puppet.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(ci_reporter) >= 1.6.3
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(minitest-spec-context) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(rake) >= 10.1.0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(hammer_cli_foreman) > 2.6.0
BuildConflicts: gem(ci_reporter) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(hammer_cli_foreman) >= 4.0.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency ci_reporter >= 2.0.0,ci_reporter < 3
%ruby_alias_names hammer_cli_foreman_puppet,hammer-cli-foreman-puppet
Requires:      gem(hammer_cli_foreman) > 2.6.0
Conflicts:     gem(hammer_cli_foreman) >= 4.0.0
Provides:      gem(hammer_cli_foreman_puppet) = 0.0.6


%description
This Hammer CLI plugin contains a set of commands for foreman_puppet, a plugin
that adds Puppet functionality to Foreman.


%package       -n gem-hammer-cli-foreman-puppet-doc
Version:       0.0.6
Release:       alt1
Summary:       Foreman Puppet plugin for Hammer CLI documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hammer_cli_foreman_puppet
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_puppet) = 0.0.6

%description   -n gem-hammer-cli-foreman-puppet-doc
Foreman Puppet plugin for Hammer CLI documentation files.

This Hammer CLI plugin contains a set of commands for foreman_puppet, a plugin
that adds Puppet functionality to Foreman.

%description   -n gem-hammer-cli-foreman-puppet-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hammer_cli_foreman_puppet.


%package       -n gem-hammer-cli-foreman-puppet-devel
Version:       0.0.6
Release:       alt1
Summary:       Foreman Puppet plugin for Hammer CLI development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hammer_cli_foreman_puppet
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_puppet) = 0.0.6
Requires:      gem(ci_reporter) >= 1.6.3
Requires:      gem(minitest) >= 0
Requires:      gem(minitest-spec-context) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(rake) >= 10.1.0
Requires:      gem(simplecov) >= 0
Conflicts:     gem(ci_reporter) >= 3
Conflicts:     gem(rake) >= 14

%description   -n gem-hammer-cli-foreman-puppet-devel
Foreman Puppet plugin for Hammer CLI development package.

This Hammer CLI plugin contains a set of commands for foreman_puppet, a plugin
that adds Puppet functionality to Foreman.

%description   -n gem-hammer-cli-foreman-puppet-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hammer_cli_foreman_puppet.


%prep
%setup

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

%files         -n gem-hammer-cli-foreman-puppet-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-hammer-cli-foreman-puppet-devel
%doc README.md


%changelog
* Mon Feb 06 2023 Pavel Skrylev <majioa@altlinux.org> 0.0.6-alt1
- ^ 0.0.3 -> 0.0.6

* Fri Dec 03 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.3-alt1
- + packaged gem with Ruby Policy 2.0
