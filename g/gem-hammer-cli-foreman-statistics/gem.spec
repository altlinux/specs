%define        gemname hammer_cli_foreman_statistics

Name:          gem-hammer-cli-foreman-statistics
Version:       0.0.1
Release:       alt1
Summary:       Foreman Statistics plugin for Hammer CLI
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/hammer-cli-foreman-statistics
Vcs:           https://github.com/theforeman/hammer-cli-foreman-statistics.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(hammer_cli_foreman_statistics) = 0.0.1


%description
This Hammer CLI plugin contains set of commands for foreman_statistics.


%package       -n gem-hammer-cli-foreman-statistics-doc
Version:       0.0.1
Release:       alt1
Summary:       Foreman Statistics plugin for Hammer CLI documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hammer_cli_foreman_statistics
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_statistics) = 0.0.1

%description   -n gem-hammer-cli-foreman-statistics-doc
Foreman Statistics plugin for Hammer CLI documentation files.

This Hammer CLI plugin contains set of commands for foreman_statistics.

%description   -n gem-hammer-cli-foreman-statistics-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hammer_cli_foreman_statistics.


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

%files         -n gem-hammer-cli-foreman-statistics-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Fri Dec 03 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.1-alt1
- + packaged gem with Ruby Policy 2.0
