%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname sprite-factory

Name:          gem-sprite-factory
Version:       1.7.1
Release:       alt1
Summary:       Automatic CSS sprite generator
License:       Unlicense
Group:         Development/Ruby
Url:           https://github.com/jakesgordon/sprite-factory
Vcs:           https://github.com/jakesgordon/sprite-factory.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(chunky_png) >= 1.3.0
BuildRequires: gem(minitest) >= 5.8
BuildRequires: gem(rmagick) >= 2.13.4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.8
%ruby_use_gem_dependency chunky_png >= 1.3.0
%ruby_use_gem_dependency rmagick >= 2.13.4
Provides:      gem(sprite-factory) = 1.7.1

%description
Combines individual images from a directory into a single sprite image file and
creates an appropriate CSS stylesheet


%package       -n sprite-factory
Version:       1.7.1
Release:       alt1
Summary:       Automatic CSS sprite generator executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета sprite-factory
Group:         Other
BuildArch:     noarch

Requires:      gem(sprite-factory) = 1.7.1

%description   -n sprite-factory
Automatic CSS sprite generator executable(s).

Combines individual images from a directory into a single sprite image file and
creates an appropriate CSS stylesheet

%description   -n sprite-factory -l ru_RU.UTF-8
Исполнямка для самоцвета sprite-factory.


%if_enabled    doc
%package       -n gem-sprite-factory-doc
Version:       1.7.1
Release:       alt1
Summary:       Automatic CSS sprite generator documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sprite-factory
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sprite-factory) = 1.7.1

%description   -n gem-sprite-factory-doc
Automatic CSS sprite generator documentation files.

Combines individual images from a directory into a single sprite image file and
creates an appropriate CSS stylesheet

%description   -n gem-sprite-factory-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sprite-factory.
%endif


%if_enabled    devel
%package       -n gem-sprite-factory-devel
Version:       1.7.1
Release:       alt1
Summary:       Automatic CSS sprite generator development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sprite-factory
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sprite-factory) = 1.7.1
Requires:      gem(chunky_png) >= 1.3.0
Requires:      gem(minitest) >= 5.8
Requires:      gem(rmagick) >= 2.13.4

%description   -n gem-sprite-factory-devel
Automatic CSS sprite generator development package.

Combines individual images from a directory into a single sprite image file and
creates an appropriate CSS stylesheet

%description   -n gem-sprite-factory-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sprite-factory.
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
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n sprite-factory
%doc LICENSE README.md
%_bindir/sf

%if_enabled    doc
%files         -n gem-sprite-factory-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-sprite-factory-devel
%doc LICENSE README.md
%endif


%changelog
* Tue Sep 22 2026 Pavel Skrylev <majioa@altlinux.org> 1.7.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
