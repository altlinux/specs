%define        gemname hammer_cli_foreman_templates

Name:          gem-hammer-cli-foreman-templates
Version:       0.2.0.1
Release:       alt0.1
Summary:       Foreman Hammer commands for exporting and importing templates
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/hammer-cli-foreman-templates
Vcs:           https://github.com/theforeman/hammer-cli-foreman-templates.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source1:       foreman_templates.yml
Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 10.1.0
BuildRequires: gem(minitest) >= 4.7.4
BuildRequires: gem(minitest-spec-context) >= 0
BuildRequires: gem(mocha) >= 1.1.0
BuildRequires: gem(simplecov) >= 0.11.2
BuildRequires: gem(gettext) >= 3.1.3
BuildRequires: gem(hammer_cli_foreman) >= 0.11.0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(mocha) >= 2
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(gettext) >= 4.0.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 1.11.2,mocha < 2
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_alias_names hammer_cli_foreman_templates,hammer-cli-foreman-templates
Requires:      gem(hammer_cli_foreman) >= 0.11.0
Provides:      gem(hammer_cli_foreman_templates) = 0.2.0.1

%ruby_use_gem_version hammer_cli_foreman_templates:0.2.0.1

%description
CLI plugin with import and export commands for Hammer_CLI_Foreman


%package       -n gem-hammer-cli-foreman-templates-doc
Version:       0.2.0.1
Release:       alt0.1
Summary:       Foreman Hammer commands for exporting and importing templates documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hammer_cli_foreman_templates
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_templates) = 0.2.0.1

%description   -n gem-hammer-cli-foreman-templates-doc
Foreman Hammer commands for exporting and importing templates documentation
files.

CLI plugin with import and export commands for Hammer_CLI_Foreman

%description   -n gem-hammer-cli-foreman-templates-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hammer_cli_foreman_templates.


%package       -n gem-hammer-cli-foreman-templates-devel
Version:       0.2.0.1
Release:       alt0.1
Summary:       Foreman Hammer commands for exporting and importing templates development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hammer_cli_foreman_templates
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_templates) = 0.2.0.1
Requires:      gem(rake) >= 10.1.0
Requires:      gem(minitest) >= 4.7.4
Requires:      gem(minitest-spec-context) >= 0
Requires:      gem(mocha) >= 1.1.0
Requires:      gem(simplecov) >= 0.11.2
Requires:      gem(gettext) >= 3.1.3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(mocha) >= 2
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(gettext) >= 4.0.0

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

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-hammer-cli-foreman-templates-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-hammer-cli-foreman-templates-devel
%doc README.md


%changelog
* Mon Feb 06 2023 Pavel Skrylev <majioa@altlinux.org> 0.2.0.1-alt0.1
- ^ 0.2.0 -> 0.2.0p1

* Sat Dec 04 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1
- + packaged gem with Ruby Policy 2.0
