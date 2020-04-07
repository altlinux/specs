# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname puma

Name:          gem-%pkgname
Version:       4.3.3
Release:       alt1.1
Summary:       A Ruby/Rack web server built for concurrency
License:       BSD-3-Clause
Group:         Networking/WWW
Url:           https://github.com/puma/puma
Vcs:           https://github.com/puma/puma.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: libssl-devel
BuildRequires: gem(nio4r)
BuildRequires: gem(rack)
BuildRequires: gem-minitest
BuildRequires: gem(minitest-retry)
BuildRequires: gem(minitest-proveit)
BuildRequires: gem(rubocop)
BuildRequires: gem(m)

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
Puma is a simple, fast, threaded, and highly concurrent HTTP 1.1 server
for Ruby/Rack applications in development and production.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch
Obsoletes:     %pkgname-doc
Provides:      %pkgname-doc

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       devel
Summary:       Development headers files for %gemname gem
Summary(ru_RU.UTF-8): Файлы заголовков для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

Obsoletes:     %pkgname-devel
Provides:      %pkgname-devel
Requires:      libssl-devel

%description   devel
Development headers for %gemname gem.

%description   devel -l ru_RU.UTF8
Файлы заголовков для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n %pkgname
%doc README*
%_bindir/%{pkgname}*

%files         doc
%ruby_gemdocdir

%files         devel
%ruby_includedir/*


%changelog
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
