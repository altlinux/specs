%define        gemname hammer_cli_foreman_puppet

Name:          gem-hammer-cli-foreman-puppet
Version:       0.0.3
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
BuildRequires: gem(hammer_cli_foreman) > 2.6.0 gem(hammer_cli_foreman) < 4.0.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(hammer_cli_foreman) > 2.6.0 gem(hammer_cli_foreman) < 4.0.0
Provides:      gem(hammer_cli_foreman_puppet) = 0.0.3


%description
This Hammer CLI plugin contains a set of commands for foreman_puppet, a plugin
that adds Puppet functionality to Foreman.


%package       -n gem-hammer-cli-foreman-puppet-doc
Version:       0.0.3
Release:       alt1
Summary:       Foreman Puppet plugin for Hammer CLI documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hammer_cli_foreman_puppet
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_puppet) = 0.0.3

%description   -n gem-hammer-cli-foreman-puppet-doc
Foreman Puppet plugin for Hammer CLI documentation files.

This Hammer CLI plugin contains a set of commands for foreman_puppet, a plugin
that adds Puppet functionality to Foreman.

%description   -n gem-hammer-cli-foreman-puppet-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hammer_cli_foreman_puppet.


%package       -n gem-hammer-cli-foreman-puppet-devel
Version:       0.0.3
Release:       alt1
Summary:       Foreman Puppet plugin for Hammer CLI development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hammer_cli_foreman_puppet
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_puppet) = 0.0.3

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
* Fri Dec 03 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.3-alt1
- + packaged gem with Ruby Policy 2.0
