%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%def_disable   java
%define        gemname puma

Name:          gem-puma
Version:       5.6.8
Release:       alt1
Summary:       A Ruby/Rack web server built for concurrency
License:       BSD-3-Clause
Group:         Networking/WWW
Url:           https://github.com/puma/puma
Vcs:           https://github.com/puma/puma.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libssl-devel
%if_enabled check
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(rake-compiler) >= 1.1.1
BuildRequires: gem(json) >= 2.3
%if_enabled java
BuildRequires: gem(jruby-openssl) >= 0
%endif
BuildRequires: gem(nio4r) >= 2.0
BuildRequires: gem(rack) >= 2.1
BuildRequires: gem(minitest) >= 5.11
BuildRequires: gem(minitest-retry) >= 0
BuildRequires: gem(minitest-proveit) >= 0
BuildRequires: gem(minitest-stub-const) >= 0
BuildRequires: gem(sd_notify) >= 0
BuildRequires: gem(rubocop) >= 0.64.0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(m) >= 0
BuildRequires: gem(localhost) >= 0
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(json) >= 3
BuildConflicts: gem(nio4r) >= 3
BuildConflicts: gem(rack) >= 4
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rack >= 3.0.0,rack < 4
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
Requires:      gem(nio4r) >= 2.0
Conflicts:     gem(nio4r) >= 3
Provides:      gem(puma) = 5.6.8


%description
Puma is a simple, fast, threaded, and highly concurrent HTTP 1.1 server for
Ruby/Rack applications in development and production.


%package       -n puma
Version:       5.6.8
Release:       alt1
Summary:       A Ruby/Rack web server built for concurrency executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета puma
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(puma) = 5.6.8

%description   -n puma
A Ruby/Rack web server built for concurrency executable(s).

Puma is a simple, fast, threaded, and highly concurrent HTTP 1.1 server for
Ruby/Rack applications in development and production.

%description   -n puma -l ru_RU.UTF-8
Исполнямка для самоцвета puma.


%if_enabled    doc
%package       -n gem-puma-doc
Version:       5.6.8
Release:       alt1
Summary:       A Ruby/Rack web server built for concurrency documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета puma
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(puma) = 5.6.8
Obsoletes:     puma-doc
Provides:      puma-doc

%description   -n gem-puma-doc
A Ruby/Rack web server built for concurrency documentation files.

Puma is a simple, fast, threaded, and highly concurrent HTTP 1.1 server for
Ruby/Rack applications in development and production.

%description   -n gem-puma-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета puma.
%endif


%if_enabled    devel
%package       -n gem-puma-devel
Version:       5.6.8
Release:       alt1
Summary:       A Ruby/Rack web server built for concurrency development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета puma
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(puma) = 5.6.8
Requires:      gem(rdoc) >= 0
Requires:      gem(rake-compiler) >= 1.1.1
Requires:      gem(json) >= 2.3
Requires:      gem(rack) >= 2.1
Requires:      gem(minitest) >= 5.11
Requires:      gem(minitest-retry) >= 0
Requires:      gem(minitest-proveit) >= 0
Requires:      gem(minitest-stub-const) >= 0
Requires:      gem(sd_notify) >= 0
%if_enabled java
Requires:      gem(jruby-openssl) >= 0
%endif
Requires:      gem(rubocop) >= 0.64.0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(m) >= 0
Requires:      gem(localhost) >= 0
Requires:      libssl-devel
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(json) >= 3
Conflicts:     gem(rack) >= 4
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rubocop) >= 2
Obsoletes:     puma-devel
Provides:      puma-devel

%description   -n gem-puma-devel
A Ruby/Rack web server built for concurrency development package.

Puma is a simple, fast, threaded, and highly concurrent HTTP 1.1 server for
Ruby/Rack applications in development and production.

%description   -n gem-puma-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета puma.
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

%files         -n puma
%doc README.md
%_bindir/puma
%_bindir/pumactl

%if_enabled    doc
%files         -n gem-puma-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-puma-devel
%doc README.md
%ruby_includedir/*
%endif


%changelog
* Fri Jul 26 2024 Pavel Skrylev <majioa@altlinux.org> 5.6.8-alt1
- ^ 5.6.5 -> 5.6.8

* Wed Jan 18 2023 Pavel Skrylev <majioa@altlinux.org> 5.6.5-alt1
- ^ 5.6.2 -> 5.6.5

* Thu Mar 17 2022 Pavel Skrylev <majioa@altlinux.org> 5.6.2-alt1
- ^ 5.3.2 -> 5.6.2

* Fri Jun 25 2021 Pavel Skrylev <majioa@altlinux.org> 5.3.2-alt1
- ^ 4.3.3 -> 5.3.2

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 4.3.3-alt1.1
- ! spec tags

* Tue Mar 24 2020 Andrey Cherepanov <cas@altlinux.org> 4.3.3-alt1
- New version.

* Mon Dec 09 2019 Pavel Skrylev <majioa@altlinux.org> 4.3.1-alt1
- updated (^) 4.2.1 -> 4.3.1
- added (+) SSL build dependency

* Mon Oct 21 2019 Pavel Skrylev <majioa@altlinux.org> 4.2.1-alt1
- updated (^) 4.2.0 -> 4.2.1
- added (+) build deps
- enabled (+) SSL for puma

* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 4.2.0-alt1
- updated (^) 3.12.1 -> 4.2.0
- updated (^) -> Ruby Policy 2.0

* Mon Apr 01 2019 Andrey Cherepanov <cas@altlinux.org> 3.12.1-alt1
- New version.

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 3.12.0-alt1
- New version.
- Package according to Ruby Policy 2.0

* Sun Jul 08 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.4-alt2
- Package as gem.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.4-alt1
- Initial build for Sisyphus
