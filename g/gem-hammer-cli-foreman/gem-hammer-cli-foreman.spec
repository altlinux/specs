%define        gemname hammer_cli_foreman

Name:          gem-hammer-cli-foreman
Version:       3.5.0
Release:       alt1
Summary:       Foreman commands for Hammer
License:       GPL-3.0+
Group:         Development/Ruby
Url:           https://github.com/theforeman/hammer-cli-foreman
Vcs:           https://github.com/theforeman/hammer-cli-foreman.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(gettext) >= 3.1.3
BuildRequires: gem(rake) >= 10.1.0
BuildRequires: gem(thor) >= 0
BuildRequires: gem(minitest) >= 5.14.1
BuildRequires: gem(minitest-spec-context) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(ci_reporter_minitest) >= 1.0.0
BuildRequires: gem(hammer_cli) >= 3.3.0
BuildRequires: gem(apipie-bindings) >= 0.5.0
BuildRequires: gem(rest-client) >= 1.8.0
BuildRequires: gem(jwt) >= 2.2.1
BuildConflicts: gem(gettext) >= 4.0.0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(mocha) >= 2
BuildConflicts: gem(ci_reporter_minitest) >= 1.1
BuildConflicts: gem(rest-client) >= 3.0.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 1.11.2,mocha < 2
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_alias_names hammer_cli_foreman,hammer-cli-foreman
Requires:      gem(hammer_cli) >= 3.3.0
Requires:      gem(apipie-bindings) >= 0.5.0
Requires:      gem(rest-client) >= 1.8.0
Requires:      gem(jwt) >= 2.2.1
Conflicts:     gem(rest-client) >= 3.0.0
Provides:      gem(hammer_cli_foreman) = 3.5.0


%description
This Hammer CLI plugin contains set of commands for Foreman.


%package       -n gem-hammer-cli-foreman-doc
Version:       3.5.0
Release:       alt1
Summary:       Foreman commands for Hammer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hammer_cli_foreman
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman) = 3.5.0

%description   -n gem-hammer-cli-foreman-doc
Foreman commands for Hammer documentation files.

This Hammer CLI plugin contains set of commands for Foreman.

%description   -n gem-hammer-cli-foreman-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hammer_cli_foreman.


%package       -n gem-hammer-cli-foreman-devel
Version:       3.5.0
Release:       alt1
Summary:       Foreman commands for Hammer development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hammer_cli_foreman
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman) = 3.5.0
Requires:      gem(gettext) >= 3.1.3
Requires:      gem(rake) >= 10.1.0
Requires:      gem(thor) >= 0
Requires:      gem(minitest) >= 5.14.1
Requires:      gem(minitest-spec-context) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(ci_reporter_minitest) >= 1.0.0
Conflicts:     gem(gettext) >= 4.0.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(mocha) >= 2
Conflicts:     gem(ci_reporter_minitest) >= 1.1

%description   -n gem-hammer-cli-foreman-devel
Foreman commands for Hammer development package.

This Hammer CLI plugin contains set of commands for Foreman.

%description   -n gem-hammer-cli-foreman-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hammer_cli_foreman.


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

%files         -n gem-hammer-cli-foreman-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-hammer-cli-foreman-devel
%doc README.md


%changelog
* Mon Feb 06 2023 Pavel Skrylev <majioa@altlinux.org> 3.5.0-alt1
- ^ 3.1.0 -> 3.5.0

* Fri Dec 03 2021 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- + packaged gem with Ruby Policy 2.0
