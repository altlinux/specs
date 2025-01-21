%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname zeitwerk

Name:          gem-zeitwerk
Version:       2.7.1
Release:       alt1
Summary:       Efficient and thread-safe constant autoloader
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fxn/zeitwerk
Vcs:           https://github.com/fxn/zeitwerk.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0
%if_enabled check
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(minitest-focus) >= 0
BuildRequires: gem(minitest-proveit) >= 0
BuildRequires: gem(minitest-reporters) >= 0
BuildRequires: gem(warning) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.2
Provides:      zeitwerk = %EVR
Provides:      gem(zeitwerk) = 2.7.1

%description
Zeitwerk implements constant autoloading with Ruby semantics. Each gem and
application may have their own independent autoloader, with its own
configuration, inflector, and logger. Supports autoloading, reloading, and eager
loading.


%if_enabled    doc
%package       -n gem-zeitwerk-doc
Version:       2.7.1
Release:       alt1
Summary:       Efficient and thread-safe constant autoloader documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета zeitwerk
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(zeitwerk) = 2.7.1

%description   -n gem-zeitwerk-doc
Efficient and thread-safe constant autoloader documentation files.

Zeitwerk implements constant autoloading with Ruby semantics. Each gem and
application may have their own independent autoloader, with its own
configuration, inflector, and logger. Supports autoloading, reloading, and eager
loading.

%description   -n gem-zeitwerk-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета zeitwerk.
%endif


%if_enabled    devel
%package       -n gem-zeitwerk-devel
Version:       2.7.1
Release:       alt1
Summary:       Efficient and thread-safe constant autoloader development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета zeitwerk
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(zeitwerk) = 2.7.1
Requires:      gem(minitest) >= 0
Requires:      gem(minitest-focus) >= 0
Requires:      gem(minitest-proveit) >= 0
Requires:      gem(minitest-reporters) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(warning) >= 0

%description   -n gem-zeitwerk-devel
Efficient and thread-safe constant autoloader development package.

Zeitwerk implements constant autoloading with Ruby semantics. Each gem and
application may have their own independent autoloader, with its own
configuration, inflector, and logger. Supports autoloading, reloading, and eager
loading.

%description   -n gem-zeitwerk-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета zeitwerk.
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
%doc MIT-LICENSE README.md CHANGELOG.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-zeitwerk-doc
%doc MIT-LICENSE README.md CHANGELOG.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-zeitwerk-devel
%doc MIT-LICENSE README.md CHANGELOG.md
%endif


%changelog
* Mon Jan 20 2025 Pavel Skrylev <majioa@altlinux.org> 2.7.1-alt1
- ^ 2.6.1 -> 2.7.1

* Sat Oct 08 2022 Pavel Skrylev <majioa@altlinux.org> 2.6.1-alt1
- ^ 2.4.2 -> 2.6.1

* Tue Jun 15 2021 Pavel Skrylev <majioa@altlinux.org> 2.4.2-alt1
- + packaged gem with Ruby Policy 2.0
