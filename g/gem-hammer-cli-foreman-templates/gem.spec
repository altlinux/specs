%define        gemname hammer_cli_foreman_templates

Name:          gem-hammer-cli-foreman-templates
Version:       0.2.0
Release:       alt1
Summary:       Foreman Hammer commands for exporting and importing templates
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/hammer-cli-foreman-templates
Vcs:           https://github.com/theforeman/hammer-cli-foreman-templates.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       foreman_templates.yml
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(hammer_cli_foreman) >= 0.11.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(hammer_cli_foreman) >= 0.11.0
Provides:      gem(hammer_cli_foreman_templates) = 0.2.0


%description
CLI plugin with import and export commands for Hammer_CLI_Foreman


%package       -n gem-hammer-cli-foreman-templates-doc
Version:       0.2.0
Release:       alt1
Summary:       Foreman Hammer commands for exporting and importing templates documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hammer_cli_foreman_templates
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_templates) = 0.2.0

%description   -n gem-hammer-cli-foreman-templates-doc
Foreman Hammer commands for exporting and importing templates documentation
files.

CLI plugin with import and export commands for Hammer_CLI_Foreman

%description   -n gem-hammer-cli-foreman-templates-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hammer_cli_foreman_templates.


%package       -n gem-hammer-cli-foreman-templates-devel
Version:       0.2.0
Release:       alt1
Summary:       Foreman Hammer commands for exporting and importing templates development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hammer_cli_foreman_templates
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_templates) = 0.2.0

%description   -n gem-hammer-cli-foreman-templates-devel
Foreman Hammer commands for exporting and importing templates development
package.

CLI plugin with import and export commands for Hammer_CLI_Foreman

%description   -n gem-hammer-cli-foreman-templates-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hammer_cli_foreman_templates.


%prep
%setup

%build
%ruby_build

%install
%ruby_install
install -Dm0644 %SOURCE1 %buildroot%_sysconfdir/hammer/cli.modules.d/foreman_templates.yml

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%attr(770,_foreman,foreman) %config(noreplace) %_sysconfdir/hammer/cli.modules.d/foreman_templates.yml

%files         -n gem-hammer-cli-foreman-templates-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-hammer-cli-foreman-templates-devel
%doc README.md


%changelog
* Sat Dec 04 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1
- + packaged gem with Ruby Policy 2.0
