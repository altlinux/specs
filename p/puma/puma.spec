# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname puma

Name:          %pkgname
Version:       4.2.0
Release:       alt1
Summary:       A Ruby/Rack web server built for concurrency
License:       BSD 3-Clause
Group:         Networking/WWW
Url:           https://github.com/puma/puma
%vcs           https://github.com/puma/puma.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake-compiler)
BuildRequires: gem(rack)

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
Puma is a simple, fast, threaded, and highly concurrent HTTP 1.1 server
for Ruby/Rack applications in development and production.


%package       -n gem-%pkgname
Summary:       Code for the %gemname gem
Group:         Development/Ruby

Provides:      ruby-%pkgname
Obsoletes:     ruby-%pkgname
Requires:      %pkgname = %version

%description   -n gem-%pkgname
Puma is a simple, fast, threaded, and highly concurrent HTTP 1.1 server
for Ruby/Rack applications in development and production.

%description   -n gem-%pkgname -l ru_RU.UTF8
Код для самоцвета %gemname.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch
Obsoletes:     %pkgname-doc
Provides:      %pkgname-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.

%description   -n gem-%pkgname-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-%pkgname-devel
Summary:       Development headers files for %gemname gem
Summary(ru_RU.UTF-8): Файлы заголовков для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch
Obsoletes:     %pkgname-devel
Provides:      %pkgname-devel

%description   -n gem-%pkgname-devel
Development headers for %gemname gem.

%description   -n gem-%pkgname-devel -l ru_RU.UTF8
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
%_bindir/%{pkgname}*

%files         -n gem-%pkgname
%doc README*
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%files         -n gem-%pkgname-devel
%ruby_includedir/*


%changelog
* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 4.2.0-alt1
- update (^) 3.12.1 -> 4.2.0
- update (^) Ruby Policy 2.0

* Mon Apr 01 2019 Andrey Cherepanov <cas@altlinux.org> 3.12.1-alt1
- New version.

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 3.12.0-alt1
- New version.
- Package according to Ruby Policy 2.0

* Sun Jul 08 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.4-alt2
- Package as gem.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.4-alt1
- Initial build for Sisyphus
