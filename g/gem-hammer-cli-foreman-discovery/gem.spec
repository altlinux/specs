%define        gemname hammer_cli_foreman_discovery

Name:          gem-hammer-cli-foreman-discovery
Version:       1.0.2
Release:       alt1
Summary:       Foreman CLI plugin for managing discovery hosts in foreman
License:       GPL-3.0-or-later
Group:         Development/Ruby
Url:           https://github.com/theforeman/hammer-cli-foreman-discovery
Vcs:           https://github.com/theforeman/hammer-cli-foreman-discovery.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       foreman_discovery.yml
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(hammer_cli_foreman) >= 0.1.2
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(hammer_cli_foreman) >= 0.1.2
Provides:      gem(hammer_cli_foreman_discovery) = 1.0.2


%description
Contains the code for managing host discovery in foreman(results and progress)
in the Hammer CLI.


%package       -n gem-hammer-cli-foreman-discovery-doc
Version:       1.0.2
Release:       alt1
Summary:       Foreman CLI plugin for managing discovery hosts in foreman documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hammer_cli_foreman_discovery
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_discovery) = 1.0.2

%description   -n gem-hammer-cli-foreman-discovery-doc
Foreman CLI plugin for managing discovery hosts in foreman documentation
files.

Contains the code for managing host discovery in foreman(results and progress)
in the Hammer CLI.

%description   -n gem-hammer-cli-foreman-discovery-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hammer_cli_foreman_discovery.


%package       -n gem-hammer-cli-foreman-discovery-devel
Version:       1.0.2
Release:       alt1
Summary:       Foreman CLI plugin for managing discovery hosts in foreman development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hammer_cli_foreman_discovery
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_discovery) = 1.0.2
Requires:      gem(rake) >= 0

%description   -n gem-hammer-cli-foreman-discovery-devel
Foreman CLI plugin for managing discovery hosts in foreman development
package.

Contains the code for managing host discovery in foreman(results and progress)
in the Hammer CLI.

%description   -n gem-hammer-cli-foreman-discovery-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hammer_cli_foreman_discovery.


%prep
%setup

%build
%ruby_build

%install
%ruby_install
install -Dm0644 %SOURCE1 %buildroot%_sysconfdir/hammer/cli.modules.d/foreman_discovery.yml

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%attr(770,_foreman,foreman) %config(noreplace) %_sysconfdir/hammer/cli.modules.d/foreman_discovery.yml

%files         -n gem-hammer-cli-foreman-discovery-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-hammer-cli-foreman-discovery-devel
%doc README.md


%changelog
* Sat Dec 04 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1
- + packaged gem with Ruby Policy 2.0
