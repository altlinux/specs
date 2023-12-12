%define        _unpackaged_files_terminate_build 1
%define        gemname yajl-ruby

Name:          gem-yajl-ruby
Version:       1.4.3
Release:       alt1
Summary:       YAJL C Bindings for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/brianmario/yajl-ruby
Vcs:           https://github.com/brianmario/yajl-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(activesupport) >= 0
BuildRequires: gem(json) >= 0
BuildRequires: gem(benchmark-memory) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     yajl-ruby < %EVR
Provides:      yajl-ruby = %EVR
Provides:      gem(yajl-ruby) = 1.4.3


%description
This package is a C binding to the excellent YAJL JSON parsing and generation
library.


%package       -n gem-yajl-ruby-doc
Version:       1.4.3
Release:       alt1
Summary:       YAJL C Bindings for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета yajl-ruby
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(yajl-ruby) = 1.4.3

%description   -n gem-yajl-ruby-doc
YAJL C Bindings for Ruby documentation files.

This package is a C binding to the excellent YAJL JSON parsing and generation
library.

%description   -n gem-yajl-ruby-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета yajl-ruby.


%package       -n gem-yajl-ruby-devel
Version:       1.4.3
Release:       alt1
Summary:       YAJL C Bindings for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета yajl-ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(yajl-ruby) = 1.4.3
Requires:      gem(rake-compiler) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(activesupport) >= 0
Requires:      gem(json) >= 0
Requires:      gem(benchmark-memory) >= 0

%description   -n gem-yajl-ruby-devel
YAJL C Bindings for Ruby development package.

This package is a C binding to the excellent YAJL JSON parsing and generation
library.

%description   -n gem-yajl-ruby-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета yajl-ruby.


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

%files         -n gem-yajl-ruby-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-yajl-ruby-devel
%doc README.md
%ruby_includedir/*


%changelog
* Tue Dec 05 2023 Pavel Skrylev <majioa@altlinux.org> 1.4.3-alt1
- ^ 1.4.1 -> 1.4.3

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt3
- ! spec tags and syntax

* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt2
- > setup gem's dependency detection

* Tue Feb 05 2019 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1
- > Ruby Policy 2.0
- ^ 1.4.0 -> 1.4.1

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Sat Apr 28 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- New version.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1.1
- Rebuild with Ruby 2.5.0

* Tue Nov 07 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- New version

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1
- New version

* Mon Sep 12 2016 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt2
- Rebuild with Ruby 2.3.1

* Thu Oct 01 2015 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1
- New version

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.7.5-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Tue Dec 04 2012 Led <led@altlinux.ru> 0.7.5-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Sun Apr 11 2010 Alexey I. Froloff <raorn@altlinux.org> 0.7.5-alt1
- Built for Sisyphus
