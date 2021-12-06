%define        gemname hammer_cli_foreman_admin

Name:          gem-hammer-cli-foreman-admin
Version:       1.1.0
Release:       alt1
Summary:       Foreman administrative commands plugin
License:       GPL-3
Group:         Development/Ruby
Url:           https://github.com/theforeman/hammer-cli-foreman-admin
Vcs:           https://github.com/theforeman/hammer-cli-foreman-admin.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       foreman_admin.yml
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(hammer_cli) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(hammer_cli) >= 0
Provides:      gem(hammer_cli_foreman_admin) = 1.1.0


%description
Foreman administrative commands plugin for Hammer CLI


%package       -n gem-hammer-cli-foreman-admin-doc
Version:       1.1.0
Release:       alt1
Summary:       Foreman administrative commands plugin documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hammer_cli_foreman_admin
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_admin) = 1.1.0

%description   -n gem-hammer-cli-foreman-admin-doc
Foreman administrative commands plugin documentation files.

Foreman administrative commands plugin for Hammer CLI

%description   -n gem-hammer-cli-foreman-admin-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hammer_cli_foreman_admin.


%package       -n gem-hammer-cli-foreman-admin-devel
Version:       1.1.0
Release:       alt1
Summary:       Foreman administrative commands plugin development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hammer_cli_foreman_admin
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_admin) = 1.1.0

%description   -n gem-hammer-cli-foreman-admin-devel
Foreman administrative commands plugin development package.

Foreman administrative commands plugin for Hammer CLI

%description   -n gem-hammer-cli-foreman-admin-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hammer_cli_foreman_admin.


%prep
%setup

%build
%ruby_build

%install
%ruby_install
install -Dm0644 %SOURCE1 %buildroot%_sysconfdir/hammer/cli.modules.d/foreman_admin.yml

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%attr(770,_foreman,foreman) %config(noreplace) %_sysconfdir/hammer/cli.modules.d/foreman_admin.yml

%files         -n gem-hammer-cli-foreman-admin-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-hammer-cli-foreman-admin-devel
%doc README.md


%changelog
* Fri Dec 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with Ruby Policy 2.0
