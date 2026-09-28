%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname gvltest

Name:          gem-gvltest
Version:       0.3.1
Release:       alt1
Summary:       Some test methods for experimenting with CRuby's GVL
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jhawthorn/gvltest
Vcs:           https://github.com/jhawthorn/gvltest.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
BuildRequires: pkgconfig(ruby)
%if_enabled check
BuildRequires: gem(gvl_timing) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rake-compiler) >= 0
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.6.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rake-compiler) >= 0
Conflicts:     gem(rake) >= 14
Provides:      gem(gvltest) = 0.3.1

%description
Some test methods for experimenting with CRuby's GVL


%if_enabled    doc
%package       -n gem-gvltest-doc
Version:       0.3.1
Release:       alt1
Summary:       Some test methods for experimenting with CRuby's GVL documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gvltest
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gvltest) = 0.3.1

%description   -n gem-gvltest-doc
Some test methods for experimenting with CRuby's GVL documentation files.

%description   -n gem-gvltest-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gvltest.
%endif


%if_enabled    devel
%package       -n gem-gvltest-devel
Version:       0.3.1
Release:       alt1
Summary:       Some test methods for experimenting with CRuby's GVL development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gvltest
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gvltest) = 0.3.1
Requires:      gem(gvl_timing) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 13.0
Requires:      gem(rake-compiler) >= 0

%description   -n gem-gvltest-devel
Some test methods for experimenting with CRuby's GVL development package.

%description   -n gem-gvltest-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gvltest.
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

%if_enabled    doc
%files         -n gem-gvltest-doc
%doc CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-gvltest-devel
%doc CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_includedir/*
%endif


%changelog
* Tue Sep 29 2026 Pavel Skrylev <majioa@altlinux.org> 0.3.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
