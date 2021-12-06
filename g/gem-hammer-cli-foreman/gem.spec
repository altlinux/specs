%define        gemname hammer_cli_foreman

Name:          gem-hammer-cli-foreman
Version:       3.1.0
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
BuildRequires: gem(hammer_cli) >= 3.1.0
BuildRequires: gem(apipie-bindings) >= 0.4.0
BuildRequires: gem(rest-client) >= 1.8.0 gem(rest-client) < 3.0.0
BuildRequires: gem(jwt) >= 2.2.1 gem(jwt) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(hammer_cli) >= 3.1.0
Requires:      gem(apipie-bindings) >= 0.4.0
Requires:      gem(rest-client) >= 1.8.0 gem(rest-client) < 3.0.0
Requires:      gem(jwt) >= 2.2.1 gem(jwt) < 3
Provides:      gem(hammer_cli_foreman) = 3.1.0


%description
This Hammer CLI plugin contains set of commands for Foreman.


%package       -n gem-hammer-cli-foreman-doc
Version:       3.1.0
Release:       alt1
Summary:       Foreman commands for Hammer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hammer_cli_foreman
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman) = 3.1.0

%description   -n gem-hammer-cli-foreman-doc
Foreman commands for Hammer documentation files.

This Hammer CLI plugin contains set of commands for Foreman.

%description   -n gem-hammer-cli-foreman-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hammer_cli_foreman.


%package       -n gem-hammer-cli-foreman-devel
Version:       3.1.0
Release:       alt1
Summary:       Foreman commands for Hammer development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hammer_cli_foreman
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman) = 3.1.0

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
* Fri Dec 03 2021 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- + packaged gem with Ruby Policy 2.0
