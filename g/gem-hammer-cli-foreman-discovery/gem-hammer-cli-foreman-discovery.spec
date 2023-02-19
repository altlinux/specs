%define        gemname hammer_cli_foreman_discovery

Name:          gem-hammer-cli-foreman-discovery
Version:       1.1.0
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
%if_with check
BuildRequires: gem(gettext) >= 3.1.3
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(thor) >= 0
BuildRequires: gem(minitest) >= 4.7.4
BuildRequires: gem(minitest-spec-context) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(ci_reporter) >= 1.6.3
BuildRequires: gem(hammer_cli_foreman) >= 0.1.2
BuildConflicts: gem(gettext) >= 4.0.0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(ci_reporter) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency ci_reporter >= 2.0.0,ci_reporter < 3
%ruby_alias_names hammer_cli_foreman_discovery,hammer-cli-foreman-discovery
Requires:      gem(hammer_cli_foreman) >= 0.1.2
Provides:      gem(hammer_cli_foreman_discovery) = 1.1.0


%description
Contains the code for managing host discovery in foreman(results and progress)
in the Hammer CLI.


%package       -n gem-hammer-cli-foreman-discovery-doc
Version:       1.1.0
Release:       alt1
Summary:       Foreman CLI plugin for managing discovery hosts in foreman documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hammer_cli_foreman_discovery
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_discovery) = 1.1.0

%description   -n gem-hammer-cli-foreman-discovery-doc
Foreman CLI plugin for managing discovery hosts in foreman documentation
files.

Contains the code for managing host discovery in foreman(results and progress)
in the Hammer CLI.

%description   -n gem-hammer-cli-foreman-discovery-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hammer_cli_foreman_discovery.


%package       -n gem-hammer-cli-foreman-discovery-devel
Version:       1.1.0
Release:       alt1
Summary:       Foreman CLI plugin for managing discovery hosts in foreman development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hammer_cli_foreman_discovery
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_discovery) = 1.1.0
Requires:      gem(gettext) >= 3.1.3
Requires:      gem(rake) >= 12.3.3
Requires:      gem(thor) >= 0
Requires:      gem(minitest) >= 4.7.4
Requires:      gem(minitest-spec-context) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(ci_reporter) >= 1.6.3
Conflicts:     gem(gettext) >= 4.0.0
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(ci_reporter) >= 3

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
* Mon Feb 06 2023 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- ^ 1.0.2 -> 1.1.0

* Sat Dec 04 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1
- + packaged gem with Ruby Policy 2.0
