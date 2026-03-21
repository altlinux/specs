%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname hammer_cli_foreman_templates

Name:          gem-hammer-cli-foreman-templates
Version:       0.4.1
Release:       alt1
Summary:       Foreman Hammer commands for exporting and importing templates
License:       GPL-3.0-only
Group:         Development/Ruby
Url:           https://github.com/theforeman/hammer-cli-foreman-templates
Vcs:           https://github.com/theforeman/hammer-cli-foreman-templates.git
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       foreman_templates.yml
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(ci_reporter) >= 1.6.3
BuildRequires: gem(gettext) >= 3.1.3
BuildRequires: gem(hammer_cli_foreman) >= 3.0.0
BuildRequires: gem(minitest) >= 5.1
BuildRequires: gem(minitest-spec-context) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(theforeman-rubocop) >= 0.1.0
BuildConflicts: gem(ci_reporter) >= 3
BuildConflicts: gem(gettext) >= 4.0.0
BuildConflicts: gem(hammer_cli_foreman) >= 4.0.0
BuildConflicts: gem(theforeman-rubocop) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency ci_reporter >= 2.0.0,ci_reporter < 3
%ruby_use_gem_dependency theforeman-rubocop >= 0.1.2,theforeman-rubocop < 1
%ruby_alias_names hammer_cli_foreman_templates,hammer-cli-foreman-templates
Requires:      ruby >= 2.7
Requires:      gem(hammer_cli_foreman) >= 3.0.0
Conflicts:     ruby >= 4
Conflicts:     gem(hammer_cli_foreman) >= 4.0.0
Provides:      gem(hammer_cli_foreman_templates) = 0.4.1

%description
CLI plugin with import and export commands for Hammer_CLI_Foreman


%if_enabled    doc
%package       -n gem-hammer-cli-foreman-templates-doc
Version:       0.4.1
Release:       alt1
Summary:       Foreman Hammer commands for exporting and importing templates documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hammer_cli_foreman_templates
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(hammer_cli_foreman_templates) = 0.4.1

%description   -n gem-hammer-cli-foreman-templates-doc
Foreman Hammer commands for exporting and importing templates documentation
files.

CLI plugin with import and export commands for Hammer_CLI_Foreman

%description   -n gem-hammer-cli-foreman-templates-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hammer_cli_foreman_templates.
%endif


%if_enabled    devel
%package       -n gem-hammer-cli-foreman-templates-devel
Version:       0.4.1
Release:       alt1
Summary:       Foreman Hammer commands for exporting and importing templates development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hammer_cli_foreman_templates
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(hammer_cli_foreman_templates) = 0.4.1

%description   -n gem-hammer-cli-foreman-templates-devel
Foreman Hammer commands for exporting and importing templates development
package.

CLI plugin with import and export commands for Hammer_CLI_Foreman

%description   -n gem-hammer-cli-foreman-templates-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hammer_cli_foreman_templates.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-hammer-cli-foreman-templates-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-hammer-cli-foreman-templates-devel
%doc LICENSE README.md
%endif


%changelog
* Sat Mar 21 2026 Pavel Skrylev <majioa@altlinux.org> 0.4.1-alt1
- ^ 0.2.0p1 -> 0.4.1

* Mon Feb 06 2023 Pavel Skrylev <majioa@altlinux.org> 0.2.0.1-alt0.1
- ^ 0.2.0 -> 0.2.0p1

* Sat Dec 04 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1
- + packaged gem with Ruby Policy 2.0
