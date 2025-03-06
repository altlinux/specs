%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname puma

Name:          gem-puma
Version:       6.6.0
Release:       alt1
Summary:       A Ruby/Rack web server built for parallelism
License:       BSD-3-Clause
Group:         Networking/WWW
Url:           https://puma.io
Vcs:           https://github.com/puma/puma.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(concurrent-ruby) >= 1.3
BuildRequires: gem(localhost) >= 0
BuildRequires: gem(m) >= 0
BuildRequires: gem(minitest) >= 5.11
BuildRequires: gem(minitest-proveit) >= 0
BuildRequires: gem(minitest-retry) >= 0
BuildRequires: gem(minitest-stub-const) >= 0
BuildRequires: gem(puma_worker_killer) >= 0
BuildRequires: gem(rack) >= 2.2
BuildRequires: gem(rackup) >= 2.0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(sinatra) >= 0
BuildRequires: gem(nio4r) >= 2
BuildConflicts: gem(concurrent-ruby) >= 2
BuildConflicts: gem(json) >= 3
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(nio4r) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.4
Requires:      gem(nio4r) >= 2.0
Conflicts:     gem(nio4r) >= 3
Provides:      gem(puma) = 6.6.0

%description
Puma is a simple, fast, multi-threaded, and highly parallel HTTP 1.1 server for
Ruby/Rack applications. Puma is intended for use in both development and
production environments. It's great for highly parallel Ruby implementations
such as JRuby and TruffleRuby as well as as providing process worker support to
support CRuby well.


%package       -n puma
Version:       6.6.0
Release:       alt1
Summary:       A Ruby/Rack web server built for parallelism executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета puma
Group:         Networking/WWW
BuildArch:     noarch

Requires:      gem(puma) = 6.6.0

%description   -n puma
A Ruby/Rack web server built for parallelism executable(s).

Puma is a simple, fast, multi-threaded, and highly parallel HTTP 1.1 server for
Ruby/Rack applications. Puma is intended for use in both development and
production environments. It's great for highly parallel Ruby implementations
such as JRuby and TruffleRuby as well as as providing process worker support to
support CRuby well.

%description   -n puma -l ru_RU.UTF-8
Исполнямка для самоцвета puma.


%if_enabled    doc
%package       -n gem-puma-doc
Version:       6.6.0
Release:       alt1
Summary:       A Ruby/Rack web server built for parallelism documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета puma
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(puma) = 6.6.0

%description   -n gem-puma-doc
A Ruby/Rack web server built for parallelism documentation files.

Puma is a simple, fast, multi-threaded, and highly parallel HTTP 1.1 server for
Ruby/Rack applications. Puma is intended for use in both development and
production environments. It's great for highly parallel Ruby implementations
such as JRuby and TruffleRuby as well as as providing process worker support to
support CRuby well.

%description   -n gem-puma-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета puma.
%endif


%if_enabled    devel
%package       -n gem-puma-devel
Version:       6.6.0
Release:       alt1
Summary:       A Ruby/Rack web server built for parallelism development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета puma
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(puma) = 6.6.0
Requires:      gem(concurrent-ruby) >= 1.3
Requires:      gem(json) >= 2.3
Requires:      gem(localhost) >= 0
Requires:      gem(m) >= 0
Requires:      gem(minitest) >= 5.11
Requires:      gem(minitest-proveit) >= 0
Requires:      gem(minitest-retry) >= 0
Requires:      gem(minitest-stub-const) >= 0
Requires:      gem(rack) >= 2.2
Requires:      gem(rackup) >= 2.0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-performance) >= 0
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(json) >= 3
Conflicts:     gem(minitest) >= 6

%description   -n gem-puma-devel
A Ruby/Rack web server built for parallelism development package.

Puma is a simple, fast, multi-threaded, and highly parallel HTTP 1.1 server for
Ruby/Rack applications. Puma is intended for use in both development and
production environments. It's great for highly parallel Ruby implementations
such as JRuby and TruffleRuby as well as as providing process worker support to
support CRuby well.

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
%doc History.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n puma
%doc History.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
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
* Thu Mar 06 2025 Pavel Skrylev <majioa@altlinux.org> 6.6.0-alt1
- ^ 6.4.3 -> 6.6.0
- * define explicit dependencies

* Tue Oct 08 2024 Pavel Skrylev <majioa@altlinux.org> 6.4.3-alt1
- ^ 5.6.8 -> 6.4.3

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
