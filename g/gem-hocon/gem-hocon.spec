%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname hocon

Name:          gem-hocon
Version:       1.4.0
Release:       alt1
Summary:       This is a port of the Typesafe Config library to Ruby
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/puppetlabs/ruby-hocon
Vcs:           https://github.com/puppetlabs/ruby-hocon.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rspec) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Obsoletes:     ruby-hocon < %EVR
Provides:      ruby-hocon = %EVR
Provides:      gem(hocon) = 1.4.0


%description
The library provides Ruby support for the HOCON configuration file format.


%package       -n hocon
Version:       1.4.0
Release:       alt1
Summary:       This is a port of the Typesafe Config library to Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета hocon
Group:         Other
BuildArch:     noarch

Requires:      gem(hocon) = 1.4.0

%description   -n hocon
This is a port of the Typesafe Config library to Ruby executable(s).

The library provides Ruby support for the HOCON configuration file format.
%description   -n hocon -l ru_RU.UTF-8
Исполнямка для самоцвета hocon.


%if_enabled    doc
%package       -n gem-hocon-doc
Version:       1.4.0
Release:       alt1
Summary:       This is a port of the Typesafe Config library to Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hocon
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hocon) = 1.4.0
Obsoletes:     ruby-hocon-doc < %EVR
Provides:      ruby-hocon-doc = %EVR

%description   -n gem-hocon-doc
This is a port of the Typesafe Config library to Ruby documentation files.

The library provides Ruby support for the HOCON configuration file format.
%description   -n gem-hocon-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hocon.
%endif


%if_enabled    devel
%package       -n gem-hocon-devel
Version:       1.4.0
Release:       alt1
Summary:       This is a port of the Typesafe Config library to Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hocon
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hocon) = 1.4.0
Requires:      gem(rspec) >= 3

%description   -n gem-hocon-devel
This is a port of the Typesafe Config library to Ruby development package.

The library provides Ruby support for the HOCON configuration file format.
%description   -n gem-hocon-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hocon.
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

%files         -n hocon
%doc README.md
%_bindir/hocon

%if_enabled    doc
%files         -n gem-hocon-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-hocon-devel
%doc README.md
%endif


%changelog
* Tue Feb 20 2024 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- ^ 1.3.1 -> 1.4.0

* Thu Jun 17 2021 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- New version.
- Rename to gem-hocon and build as gem.
- Fix License tag.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.5-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Apr 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.5-alt1
- New version

* Tue Feb 28 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.4-alt1
- Initial build in Sisyphus
