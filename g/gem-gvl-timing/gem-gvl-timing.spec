%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname gvl_timing

Name:          gem-gvl-timing
Version:       0.3.3
Release:       alt1
Summary:       Measure time spent in different GVL states
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jhawthorn/gvl_timing
Vcs:           https://github.com/jhawthorn/gvl_timing.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
BuildRequires: pkgconfig(ruby)
%if_enabled check
BuildRequires: gem(minitest) >= 5.16
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rake-compiler) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 6.0
%ruby_use_gem_dependency rake >= 13.0
%ruby_alias_names gvl_timing,gvl-timing
Requires:      ruby >= 3.2.0
Provides:      gem(gvl_timing) = 0.3.3

%description
Measure time spent in different GVL states


%package       -n gvl-timing
Version:       0.3.3
Release:       alt1
Summary:       Measure time spent in different GVL states executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета gvl_timing
Group:         Other
BuildArch:     noarch

Requires:      gem(gvl_timing) = 0.3.3
Requires:      gem(minitest) >= 5.16
Requires:      gem(rake) >= 13.0
Requires:      gem(rake-compiler) >= 0

%description   -n gvl-timing
Measure time spent in different GVL states executable(s).

%description   -n gvl-timing -l ru_RU.UTF-8
Исполнямка для самоцвета gvl_timing.


%if_enabled    doc
%package       -n gem-gvl-timing-doc
Version:       0.3.3
Release:       alt1
Summary:       Measure time spent in different GVL states documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gvl_timing
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gvl_timing) = 0.3.3

%description   -n gem-gvl-timing-doc
Measure time spent in different GVL states documentation files.

%description   -n gem-gvl-timing-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gvl_timing.
%endif


%if_enabled    devel
%package       -n gem-gvl-timing-devel
Version:       0.3.3
Release:       alt1
Summary:       Measure time spent in different GVL states development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gvl_timing
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gvl_timing) = 0.3.3
Requires:      gem(minitest) >= 5.16
Requires:      gem(rake) >= 13.0
Requires:      gem(rake-compiler) >= 0

%description   -n gem-gvl-timing-devel
Measure time spent in different GVL states development package.

%description   -n gem-gvl-timing-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gvl_timing.
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
%doc CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gvl-timing
%doc CODE_OF_CONDUCT.md LICENSE.txt README.md
%_bindir/gvl_timing

%if_enabled    doc
%files         -n gem-gvl-timing-doc
%doc CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-gvl-timing-devel
%doc CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_includedir/*
%endif


%changelog
* Tue Sep 29 2026 Pavel Skrylev <majioa@altlinux.org> 0.3.3-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
