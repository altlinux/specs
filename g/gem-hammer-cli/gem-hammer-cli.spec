%define        gemname hammer_cli

Name:          gem-hammer-cli
Version:       3.5.0
Release:       alt1
Summary:       Next-gen CLI tool for foreman
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/hammer-cli
Vcs:           https://github.com/theforeman/hammer-cli.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source1:       default_config.yml
Source:        %name-%version.tar
Patch:         clamp-1.3.2.patch
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(gettext) >= 3.1.3
BuildRequires: gem(rake) >= 10.1.0
BuildRequires: gem(thor) >= 0
BuildRequires: gem(minitest) >= 4.7.4
BuildRequires: gem(minitest-spec-context) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(ci_reporter) >= 1.6.3
BuildRequires: gem(clamp) >= 1.3.2
BuildRequires: gem(logging) >= 0
BuildRequires: gem(unicode-display_width) >= 0
BuildRequires: gem(unicode) >= 0
BuildRequires: gem(amazing_print) >= 0
BuildRequires: gem(highline) >= 0
BuildRequires: gem(fast_gettext) >= 0
BuildRequires: gem(locale) >= 2.0.6
BuildRequires: gem(apipie-bindings) >= 0.5.0
BuildConflicts: gem(gettext) >= 4.0.0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(ci_reporter) >= 3
BuildConflicts: gem(clamp) >= 1.4.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency ci_reporter >= 2.0.0,minitest < 3
%ruby_alias_names hammer_cli,hammer-cli
Requires:      gem(clamp) >= 1.3.2
Requires:      gem(logging) >= 0
Requires:      gem(unicode-display_width) >= 0
Requires:      gem(unicode) >= 0
Requires:      gem(amazing_print) >= 0
Requires:      gem(highline) >= 0
Requires:      gem(fast_gettext) >= 0
Requires:      gem(locale) >= 2.0.6
Requires:      gem(apipie-bindings) >= 0.5.0
Conflicts:     gem(clamp) >= 1.4.0
Provides:      gem(hammer_cli) = 3.5.0

%description
Hammer is a generic clamp-based CLI framework. Hammer-cli provides just the core
functionality. The core is extensible using plugins that contain
application-specific commands.

This architecture allows for easy customization according to your application.
Nearly any Ruby script can be turned into a Hammer command, so the possibilities
are endless. You also can easily add custom commands for your specific use, such
as bulk actions or admin tasks.

Available plugins are listed on the Foreman's wiki.


%package       -n hammer
Version:       3.5.0
Release:       alt1
Summary:       Next-gen CLI tool for foreman executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета hammer_cli
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hammer_cli) = 3.5.0

%description   -n hammer
Next-gen CLI tool for foreman executable(s).

Hammer is a generic clamp-based CLI framework. Hammer-cli provides just the core
functionality. The core is extensible using plugins that contain
application-specific commands.

This architecture allows for easy customization according to your application.
Nearly any Ruby script can be turned into a Hammer command, so the possibilities
are endless. You also can easily add custom commands for your specific use, such
as bulk actions or admin tasks.

Available plugins are listed on the Foreman's wiki.

%description   -n hammer -l ru_RU.UTF-8
Исполнямка для самоцвета hammer_cli.


%package       -n gem-hammer-cli-doc
Version:       3.5.0
Release:       alt1
Summary:       Next-gen CLI tool for foreman documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hammer_cli
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hammer_cli) = 3.5.0

%description   -n gem-hammer-cli-doc
Next-gen CLI tool for foreman documentation files.

Hammer is a generic clamp-based CLI framework. Hammer-cli provides just the core
functionality. The core is extensible using plugins that contain
application-specific commands.

This architecture allows for easy customization according to your application.
Nearly any Ruby script can be turned into a Hammer command, so the possibilities
are endless. You also can easily add custom commands for your specific use, such
as bulk actions or admin tasks.

Available plugins are listed on the Foreman's wiki.

%description   -n gem-hammer-cli-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hammer_cli.


%package       -n gem-hammer-cli-devel
Version:       3.5.0
Release:       alt1
Summary:       Next-gen CLI tool for foreman development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hammer_cli
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hammer_cli) = 3.5.0
Requires:      gem(gettext) >= 3.1.3
Requires:      gem(rake) >= 10.1.0
Requires:      gem(thor) >= 0
Requires:      gem(minitest) >= 4.7.4
Requires:      gem(minitest-spec-context) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(ci_reporter) >= 1.6.3
Conflicts:     gem(gettext) >= 4.0.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(ci_reporter) >= 3

%description   -n gem-hammer-cli-devel
Next-gen CLI tool for foreman development package.

Hammer is a generic clamp-based CLI framework. Hammer-cli provides just the core
functionality. The core is extensible using plugins that contain
application-specific commands.

This architecture allows for easy customization according to your application.
Nearly any Ruby script can be turned into a Hammer command, so the possibilities
are endless. You also can easily add custom commands for your specific use, such
as bulk actions or admin tasks.

Available plugins are listed on the Foreman's wiki.


%description   -n gem-hammer-cli-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hammer_cli.


%prep
%setup
%autopatch

%build
%ruby_build

%install
%ruby_install
install -Dm0644 %SOURCE1 %buildroot%_sysconfdir/hammer/cli.modules.d/default_config.yml

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n hammer
%doc README.md
%_bindir/hammer
%_bindir/hammer-complete
%config(noreplace) %attr(710,_foreman,foreman) %_sysconfdir/hammer/cli.modules.d/default_config.yml

%files         -n gem-hammer-cli-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-hammer-cli-devel
%doc README.md


%changelog
* Mon Feb 06 2023 Pavel Skrylev <majioa@altlinux.org> 3.5.0-alt1
- ^ 3.1.0 -> 3.5.0

* Tue Nov 23 2021 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- ^ 2.3.0 -> 3.1.0

* Thu Dec 10 2020 Pavel Skrylev <majioa@altlinux.org> 2.3.0-alt1
- + packaged gem with usage Ruby Policy 2.0
