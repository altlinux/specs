%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname hammer_cli

Name:          gem-hammer-cli
Version:       3.18.0
Release:       alt1
Summary:       Next-gen CLI tool for foreman
License:       GPL-3.0-only
Group:         Development/Ruby
Url:           https://github.com/theforeman/hammer-cli
Vcs:           https://github.com/theforeman/hammer-cli.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       default_config.yml
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(amazing_print) >= 0
BuildRequires: gem(apipie-bindings) >= 0.7.0
BuildRequires: gem(base64) >= 0
BuildRequires: gem(ci_reporter_minitest) >= 1.0
BuildRequires: gem(clamp) >= 1.3.1
BuildRequires: gem(csv) >= 0
BuildRequires: gem(fast_gettext) >= 0
BuildRequires: gem(gettext) >= 3.1.3
BuildRequires: gem(highline) >= 0
BuildRequires: gem(locale) >= 2.0.6
BuildRequires: gem(logging) >= 0
BuildRequires: gem(minitest) >= 5.18
BuildRequires: gem(minitest-spec-context) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(thor) >= 0
BuildRequires: gem(unicode-display_width) >= 0
BuildConflicts: gem(ci_reporter_minitest) >= 2
BuildConflicts: gem(clamp) >= 2.0.0
BuildConflicts: gem(gettext) >= 4.0.0
BuildConflicts: gem(minitest) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names hammer_cli,hammer-cli
Requires:      ruby >= 2.7
Requires:      gem(amazing_print) >= 0
Requires:      gem(apipie-bindings) >= 0.7.0
Requires:      gem(base64) >= 0
Requires:      gem(clamp) >= 1.3.1
Requires:      gem(csv) >= 0
Requires:      gem(fast_gettext) >= 0
Requires:      gem(highline) >= 0
Requires:      gem(locale) >= 2.0.6
Requires:      gem(logging) >= 0
Requires:      gem(unicode-display_width) >= 0
Conflicts:     gem(clamp) >= 2.0.0
Provides:      gem(hammer_cli) = 3.18.0

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
Version:       3.18.0
Release:       alt1
Summary:       Next-gen CLI tool for foreman executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета hammer_cli
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(hammer_cli) = 3.18.0

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


%if_enabled    doc
%package       -n gem-hammer-cli-doc
Version:       3.18.0
Release:       alt1
Summary:       Next-gen CLI tool for foreman documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hammer_cli
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(hammer_cli) = 3.18.0

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
%endif


%if_enabled    devel
%package       -n gem-hammer-cli-devel
Version:       3.18.0
Release:       alt1
Summary:       Next-gen CLI tool for foreman development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hammer_cli
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(hammer_cli) = 3.18.0
Requires:      gem(ci_reporter_minitest) >= 1.0
Requires:      gem(gettext) >= 3.1.3
Requires:      gem(minitest) >= 5.18
Requires:      gem(minitest-spec-context) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(thor) >= 0
Requires:      gem(unicode-display_width) >= 0
Conflicts:     gem(ci_reporter_minitest) >= 2
Conflicts:     gem(gettext) >= 4.0.0
Conflicts:     gem(minitest) >= 6

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
%endif


%prep
%setup
%autopatch

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

%files         -n hammer
%doc LICENSE README.md
%_bindir/hammer
%_bindir/hammer-complete

%if_enabled    doc
%files         -n gem-hammer-cli-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-hammer-cli-devel
%doc LICENSE README.md
%endif


%changelog
* Sat Mar 21 2026 Pavel Skrylev <majioa@altlinux.org> 3.18.0-alt1
- ^ 3.5.0 -> 3.18.0

* Mon Feb 06 2023 Pavel Skrylev <majioa@altlinux.org> 3.5.0-alt1
- ^ 3.1.0 -> 3.5.0

* Tue Nov 23 2021 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- ^ 2.3.0 -> 3.1.0

* Thu Dec 10 2020 Pavel Skrylev <majioa@altlinux.org> 2.3.0-alt1
- + packaged gem with usage Ruby Policy 2.0
