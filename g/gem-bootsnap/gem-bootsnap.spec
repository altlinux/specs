%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname bootsnap

Name:          gem-bootsnap
Version:       1.18.3
Release:       alt1
Summary:       Boot large ruby/rails apps faster
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/Shopify/bootsnap
Vcs:           https://github.com/shopify/bootsnap.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(msgpack) >= 1.2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(msgpack) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(msgpack) >= 1.2
Conflicts:     gem(msgpack) >= 2
Provides:      gem(bootsnap) = 1.18.3


%description
Boot large ruby/rails apps faster.


%package       -n bootsnap
Version:       1.18.3
Release:       alt1
Summary:       Boot large ruby/rails apps faster executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета bootsnap
Group:         Other
BuildArch:     noarch

Requires:      gem(bootsnap) = 1.18.3

%description   -n bootsnap
Boot large ruby/rails apps faster executable(s).

%description   -n bootsnap -l ru_RU.UTF-8
Исполнямка для самоцвета bootsnap.


%if_enabled    doc
%package       -n gem-bootsnap-doc
Version:       1.18.3
Release:       alt1
Summary:       Boot large ruby/rails apps faster documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bootsnap
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bootsnap) = 1.18.3

%description   -n gem-bootsnap-doc
Boot large ruby/rails apps faster documentation files.

%description   -n gem-bootsnap-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bootsnap.
%endif


%if_enabled    devel
%package       -n gem-bootsnap-devel
Version:       1.18.3
Release:       alt1
Summary:       Boot large ruby/rails apps faster development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bootsnap
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bootsnap) = 1.18.3
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(minitest) >= 5.0
Requires:      gem(mocha) >= 0
Requires:      gem(rubocop) >= 1.15.0
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rubocop) >= 2

%description   -n gem-bootsnap-devel
Boot large ruby/rails apps faster development package.

%description   -n gem-bootsnap-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bootsnap.
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

%files         -n bootsnap
%doc README.md
%_bindir/bootsnap

%if_enabled    doc
%files         -n gem-bootsnap-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-bootsnap-devel
%doc README.md
%ruby_includedir/*
%endif


%changelog
* Tue Jul 23 2024 Pavel Skrylev <majioa@altlinux.org> 1.18.3-alt1
- ^ 1.13.0 -> 1.18.3

* Wed Sep 21 2022 Pavel Skrylev <majioa@altlinux.org> 1.13.0-alt1
- ^ 1.11.1 -> 1.13.0

* Wed Mar 16 2022 Pavel Skrylev <majioa@altlinux.org> 1.11.1-alt1
- ^ 1.7.5 -> 1.11.1

* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 1.7.5-alt1
- + packaged gem with Ruby Policy 2.0
