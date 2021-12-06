%define        gemname hammer_cli

Name:          gem-hammer-cli
Version:       3.1.0
Release:       alt1
Summary:       Next-gen CLI tool for foreman
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/hammer-cli
Vcs:           https://github.com/theforeman/hammer-cli.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       default_config.yml
Patch:         clamp-1.3.2.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(clamp) >= 1.3.2 gem(clamp) < 2
BuildRequires: gem(logging) >= 0
BuildRequires: gem(unicode-display_width) >= 0
BuildRequires: gem(unicode) >= 0
BuildRequires: gem(amazing_print) >= 0
BuildRequires: gem(highline) >= 0
BuildRequires: gem(fast_gettext) >= 0
BuildRequires: gem(locale) >= 2.0.6
BuildRequires: gem(apipie-bindings) >= 0.2.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency clamp >= 1.3.2,clamp < 2
%ruby_alias_names hammer_cli,hammer-cli
Requires:      gem(clamp) >= 1.1 gem(clamp) < 2
Requires:      gem(logging) >= 0
Requires:      gem(unicode-display_width) >= 0
Requires:      gem(unicode) >= 0
Requires:      gem(amazing_print) >= 0
Requires:      gem(highline) >= 0
Requires:      gem(fast_gettext) >= 0
Requires:      gem(locale) >= 2.0.6
Requires:      gem(apipie-bindings) >= 0.2.0
Provides:      gem(hammer_cli) = 3.1.0


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
Version:       3.1.0
Release:       alt1
Summary:       Next-gen CLI tool for foreman executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета hammer_cli
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hammer_cli) = 3.1.0

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
Version:       3.1.0
Release:       alt1
Summary:       Next-gen CLI tool for foreman documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hammer_cli
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hammer_cli) = 3.1.0

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
Version:       3.1.0
Release:       alt1
Summary:       Next-gen CLI tool for foreman development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hammer_cli
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hammer_cli) = 3.1.0
Requires:      gem(clamp) >= 1.2 gem(clamp) < 2

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
%patch

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
* Tue Nov 23 2021 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- ^ 2.3.0 -> 3.1.0

* Thu Dec 10 2020 Pavel Skrylev <majioa@altlinux.org> 2.3.0-alt1
- + packaged gem with usage Ruby Policy 2.0
