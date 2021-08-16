%define        gemname puma

Name:          gem-puma
Version:       5.3.2
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
BuildRequires: gem-minitest
BuildRequires: gem(nio4r) >= 2.0 gem(nio4r) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names new_json_with_puma_stats_after_fork,old_json_with_puma_stats_after_fork,new_json,old_json,new_nio4r,old_nio4r,version2,version1
Requires:      gem(nio4r) >= 2.0 gem(nio4r) < 3
Provides:      gem(puma) = 5.3.2


%description
Puma is a simple, fast, threaded, and highly concurrent HTTP 1.1 server for
Ruby/Rack applications in development and production.


%package       -n puma
Version:       5.3.2
Release:       alt1
Summary:       A Ruby/Rack web server built for concurrency executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета puma
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(puma) = 5.3.2

%description   -n puma
A Ruby/Rack web server built for concurrency executable(s).

Puma is a simple, fast, threaded, and highly concurrent HTTP 1.1 server for
Ruby/Rack applications in development and production.

%description   -n puma -l ru_RU.UTF-8
Исполнямка для самоцвета puma.


%package       -n gem-puma-doc
Version:       5.3.2
Release:       alt1
Summary:       A Ruby/Rack web server built for concurrency documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета puma
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(puma) = 5.3.2
Obsoletes:     puma-doc
Provides:      puma-doc

%description   -n gem-puma-doc
A Ruby/Rack web server built for concurrency documentation files.

Puma is a simple, fast, threaded, and highly concurrent HTTP 1.1 server for
Ruby/Rack applications in development and production.

%description   -n gem-puma-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета puma.


%package       -n gem-puma-devel
Version:       5.3.2
Release:       alt1
Summary:       A Ruby/Rack web server built for concurrency development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета puma
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(puma) = 5.3.2
Requires:      libssl-devel
Obsoletes:     puma-devel
Provides:      puma-devel

%description   -n gem-puma-devel
A Ruby/Rack web server built for concurrency development package.

Puma is a simple, fast, threaded, and highly concurrent HTTP 1.1 server for
Ruby/Rack applications in development and production.

%description   -n gem-puma-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета puma.


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

%files         -n gem-puma-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-puma-devel
%doc README.md
%ruby_includedir/*


%changelog
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
