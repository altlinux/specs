%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname sass-embedded

Name:          gem-sass-embedded
Version:       1.99.0
Release:       alt1
Summary:       Use dart-sass with Ruby!
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sass-contrib/sass-embedded-host-ruby
Vcs:           https://github.com/sass-contrib/sass-embedded-host-ruby.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake libruby-devel
%if_enabled check
BuildRequires: gem(google-protobuf) >= 4.31
BuildRequires: gem(rake) >= 13
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(rubocop-rake) >= 0.6.0
BuildRequires: gem(rubocop-rspec) >= 3.7.0
BuildConflicts: gem(google-protobuf) >= 5
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rubocop-rspec >= 3.7.0,rubocop-rspec < 4
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
%ruby_use_gem_dependency rubocop-rake >= 0.6.0,rubocop-rake < 1
Requires:      ruby >= 3.1
Requires:      gem(google-protobuf) >= 4.31
Requires:      gem(rake) >= 13
Conflicts:     gem(google-protobuf) >= 5
Provides:      sass-embedded = %EVR
Provides:      gem(sass-embedded) = 1.99.0

%description
A Ruby library that will communicate with Embedded Dart Sass using the Embedded
Sass protocol. This is a Ruby library that implements the host side of the
Embedded Sass protocol.

It exposes a Ruby API for Sass that's backed by a native Dart Sass executable.


%package       -n sass-embedded
Version:       1.99.0
Release:       alt1
Summary:       Use dart-sass with Ruby! executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета sass-embedded
Group:         Other
BuildArch:     noarch

Requires:      gem(sass-embedded) = 1.99.0
Conflicts:     sass

%description   -n sass-embedded
Use dart-sass with Ruby! executable(s).

A Ruby library that will communicate with Embedded Dart Sass using the Embedded
Sass protocol. This is a Ruby library that implements the host side of the
Embedded Sass protocol.

It exposes a Ruby API for Sass that's backed by a native Dart Sass executable.

%description   -n sass-embedded -l ru_RU.UTF-8
Исполнямка для самоцвета sass-embedded.


%if_enabled    doc
%package       -n gem-sass-embedded-doc
Version:       1.99.0
Release:       alt1
Summary:       Use dart-sass with Ruby! documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sass-embedded
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sass-embedded) = 1.99.0

%description   -n gem-sass-embedded-doc
Use dart-sass with Ruby! documentation files.

A Ruby library that will communicate with Embedded Dart Sass using the Embedded
Sass protocol. This is a Ruby library that implements the host side of the
Embedded Sass protocol.

It exposes a Ruby API for Sass that's backed by a native Dart Sass executable.

%description   -n gem-sass-embedded-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sass-embedded.
%endif


%if_enabled    devel
%package       -n gem-sass-embedded-devel
Version:       1.99.0
Release:       alt1
Summary:       Use dart-sass with Ruby! development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sass-embedded
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sass-embedded) = 1.99.0

%description   -n gem-sass-embedded-devel
Use dart-sass with Ruby! development package.

A Ruby library that will communicate with Embedded Dart Sass using the Embedded
Sass protocol. This is a Ruby library that implements the host side of the
Embedded Sass protocol.

It exposes a Ruby API for Sass that's backed by a native Dart Sass executable.

%description   -n gem-sass-embedded-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sass-embedded.
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
%doc LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n sass-embedded
%doc LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%_bindir/sass

%if_enabled    doc
%files         -n gem-sass-embedded-doc
%doc LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-sass-embedded-devel
%doc LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%endif


%changelog
* Wed May 13 2026 Pavel Skrylev <majioa@altlinux.org> 1.99.0-alt1
- ^ 1.77.5 -> 1.99.0

* Wed Nov 19 2025 Pavel Skrylev <majioa@altlinux.org> 1.77.5-alt1
- ^ 1.62.1 -> 1.77.5

* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 1.62.1-alt1
- + packaged gem with Ruby Policy 2.0
