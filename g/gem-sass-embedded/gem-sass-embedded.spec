%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname sass-embedded

Name:          gem-sass-embedded
Version:       1.62.1
Release:       alt1
Summary:       Use dart-sass with Ruby!
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sass-contrib/sass-embedded-host-ruby
Vcs:           https://github.com/sass-contrib/sass-embedded-host-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 10.0.0
BuildRequires: gem(rspec) >= 3.12.0
BuildRequires: gem(rubocop) >= 1.50.0
BuildRequires: gem(rubocop-performance) >= 1.17.1
BuildRequires: gem(rubocop-rake) >= 0.6.0
BuildRequires: gem(rubocop-rspec) >= 2.20.0
BuildRequires: gem(google-protobuf) >= 3.21
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-rspec) >= 3
BuildConflicts: gem(google-protobuf) >= 5.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rake) >= 13.0.0
Requires:      gem(google-protobuf) >= 3.21
Conflicts:     gem(google-protobuf) >= 5.0
Provides:      gem(sass-embedded) = 1.75.0


%description
A Ruby library that will communicate with Embedded Dart Sass using the Embedded
Sass protocol. This is a Ruby library that implements the host side of the
Embedded Sass protocol.

It exposes a Ruby API for Sass that's backed by a native Dart Sass executable.


%if_enabled    doc
%package       -n gem-sass-embedded-doc
Version:       1.62.1
Release:       alt1
Summary:       Use dart-sass with Ruby! documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sass-embedded
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sass-embedded) = 1.75.0

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
Version:       1.62.1
Release:       alt1
Summary:       Use dart-sass with Ruby! development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sass-embedded
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sass-embedded) = 1.75.0
Requires:      gem(rspec) >= 3.12.0
Requires:      gem(rubocop) >= 1.50.0
Requires:      gem(rubocop-performance) >= 1.17.1
Requires:      gem(rubocop-rake) >= 0.6.0
Requires:      gem(rubocop-rspec) >= 2.20.0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-rspec) >= 3

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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-sass-embedded-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-sass-embedded-devel
%doc README.md
%endif


%changelog
* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 1.62.1-alt1
- + packaged gem with Ruby Policy 2.0
