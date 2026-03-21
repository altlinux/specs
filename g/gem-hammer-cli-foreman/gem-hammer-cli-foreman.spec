%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname hammer_cli_foreman

Name:          gem-hammer-cli-foreman
Version:       3.18.1
Release:       alt1
Summary:       Foreman commands for Hammer
License:       GPL-3.0-or-later
Group:         Development/Ruby
Url:           https://github.com/theforeman/hammer-cli-foreman
Vcs:           https://github.com/theforeman/hammer-cli-foreman.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(apipie-bindings) >= 0.7.0
BuildRequires: gem(ci_reporter_minitest) >= 1.0.0
BuildRequires: gem(gettext) >= 3.1.3
BuildRequires: gem(hammer_cli) >= 3.15.0
BuildRequires: gem(jwt) >= 2.2.1
BuildRequires: gem(minitest) >= 5.18
BuildRequires: gem(mocha) >= 2.1.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rest-client) >= 1.8.0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(thor) >= 0
BuildConflicts: gem(ci_reporter_minitest) >= 1.1
BuildConflicts: gem(gettext) >= 4.0.0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(mocha) >= 4
BuildConflicts: gem(rest-client) >= 3.0.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names hammer_cli_foreman,hammer-cli-foreman
%ruby_use_gem_dependency mocha >= 2.7.1,mocha < 4
Requires:      gem(apipie-bindings) >= 0.7.0
Requires:      gem(hammer_cli) >= 3.15.0
Requires:      gem(jwt) >= 2.2.1
Requires:      gem(rest-client) >= 1.8.0
Conflicts:     gem(rest-client) >= 3.0.0
Provides:      gem(hammer_cli_foreman) = 3.18.1

%description
This Hammer CLI plugin contains set of commands for Foreman.


%if_enabled    doc
%package       -n gem-hammer-cli-foreman-doc
Version:       3.18.1
Release:       alt1
Summary:       Foreman commands for Hammer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hammer_cli_foreman
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(hammer_cli_foreman) = 3.18.1

%description   -n gem-hammer-cli-foreman-doc
Foreman commands for Hammer documentation files.

This Hammer CLI plugin contains set of commands for Foreman.

%description   -n gem-hammer-cli-foreman-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hammer_cli_foreman.
%endif


%if_enabled    devel
%package       -n gem-hammer-cli-foreman-devel
Version:       3.18.1
Release:       alt1
Summary:       Foreman commands for Hammer development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hammer_cli_foreman
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(hammer_cli_foreman) = 3.18.1
Requires:      gem(ci_reporter_minitest) >= 1.0.0
Requires:      gem(gettext) >= 3.1.3
Requires:      gem(minitest) >= 5.18
Requires:      gem(mocha) >= 2.1.0
Requires:      gem(rake) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(thor) >= 0
Conflicts:     gem(ci_reporter_minitest) >= 1.1
Conflicts:     gem(gettext) >= 4.0.0
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(mocha) >= 4

%description   -n gem-hammer-cli-foreman-devel
Foreman commands for Hammer development package.

This Hammer CLI plugin contains set of commands for Foreman.

%description   -n gem-hammer-cli-foreman-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hammer_cli_foreman.
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
%files         -n gem-hammer-cli-foreman-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-hammer-cli-foreman-devel
%doc LICENSE README.md
%endif


%changelog
* Sat Mar 21 2026 Pavel Skrylev <majioa@altlinux.org> 3.18.1-alt1
- ^ 3.5.0 -> 3.18.1

* Mon Feb 06 2023 Pavel Skrylev <majioa@altlinux.org> 3.5.0-alt1
- ^ 3.1.0 -> 3.5.0

* Fri Dec 03 2021 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- + packaged gem with Ruby Policy 2.0
