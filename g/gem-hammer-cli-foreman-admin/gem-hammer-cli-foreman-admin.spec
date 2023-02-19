%define        gemname hammer_cli_foreman_admin

Name:          gem-hammer-cli-foreman-admin
Version:       1.1.0.1
Release:       alt0.1
Summary:       Foreman administrative commands plugin
License:       GPL-3
Group:         Development/Ruby
Url:           https://github.com/theforeman/hammer-cli-foreman-admin
Vcs:           https://github.com/theforeman/hammer-cli-foreman-admin.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source1:       foreman_admin.yml
Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(gettext) >= 3.1.3
BuildRequires: gem(rake) >= 10.1.0
BuildRequires: gem(hammer_cli) >= 0
BuildConflicts: gem(gettext) >= 4.0.0
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_alias_names hammer_cli_foreman_admin,hammer-cli-foreman-admin
Requires:      gem(hammer_cli) >= 0
Provides:      gem(hammer_cli_foreman_admin) = 1.1.0.1

%ruby_use_gem_version hammer_cli_foreman_admin:1.1.0.1

%description
Foreman administrative commands plugin for Hammer CLI


%package       -n gem-hammer-cli-foreman-admin-doc
Version:       1.1.0.1
Release:       alt0.1
Summary:       Foreman administrative commands plugin documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hammer_cli_foreman_admin
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_admin) = 1.1.0.1

%description   -n gem-hammer-cli-foreman-admin-doc
Foreman administrative commands plugin documentation files.

Foreman administrative commands plugin for Hammer CLI

%description   -n gem-hammer-cli-foreman-admin-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hammer_cli_foreman_admin.


%package       -n gem-hammer-cli-foreman-admin-devel
Version:       1.1.0.1
Release:       alt0.1
Summary:       Foreman administrative commands plugin development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hammer_cli_foreman_admin
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hammer_cli_foreman_admin) = 1.1.0.1
Requires:      gem(gettext) >= 3.1.3
Requires:      gem(rake) >= 10.1.0
Conflicts:     gem(gettext) >= 4.0.0
Conflicts:     gem(rake) >= 14

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
* Mon Feb 06 2023 Pavel Skrylev <majioa@altlinux.org> 1.1.0.1-alt0.1
- ^ 1.1.0 -> 1.1.0p1

* Fri Dec 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with Ruby Policy 2.0
