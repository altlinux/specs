%define        gemname coveralls

Name:          gem-coveralls
Version:       0.8.23.2
Release:       alt0.1
Summary:       Coveralls for Ruby
Summary(ru_RU.UTF-8): Покрытия для рубина
License:       MIT
Group:         Development/Ruby
Url:           https://coveralls.io
Vcs:           https://github.com/lemurheavy/coveralls-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(rake) >= 10.3
BuildRequires: gem(rspec) >= 3.2
BuildRequires: gem(truthy) >= 1
BuildRequires: gem(vcr) >= 2.9
BuildRequires: gem(webmock) >= 1.20
BuildRequires: gem(addressable) >= 2.3.8
BuildRequires: gem(mime-types) >= 1.25
BuildRequires: gem(json) >= 1.8
BuildRequires: gem(term-ansicolor) >= 1.4
BuildRequires: gem(tins) >= 1.7
BuildRequires: gem(pry) >= 0
BuildRequires: gem(thor) >= 0.19.4
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(addressable) >= 3
BuildConflicts: gem(mime-types) >= 4
BuildConflicts: gem(json) >= 3
BuildConflicts: gem(term-ansicolor) >= 2
BuildConflicts: gem(tins) >= 2
BuildConflicts: gem(thor) >= 2.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency tins >= 1.32.0,tins < 2
%ruby_use_gem_dependency term-ansicolor >= 1.7.1,term-ansicolor < 2
%ruby_use_gem_dependency addressable >= 2.8.0,addressable < 3
%ruby_use_gem_dependency mime-types >= 3.3.1,mime-types < 4
Requires:      gem(json) >= 1.8
Requires:      gem(term-ansicolor) >= 1.4
Requires:      gem(tins) >= 1.7
Requires:      gem(thor) >= 0.19.4
Conflicts:     gem(json) >= 3
Conflicts:     gem(term-ansicolor) >= 2
Conflicts:     gem(tins) >= 2
Conflicts:     gem(thor) >= 2.0
Provides:      gem(coveralls) = 0.8.23.2

%ruby_use_gem_version coveralls:0.8.23.2

%description
Coveralls was designed with Ruby projects in mind, and we've made it as easy as
we possibly can to get started.

%description         -l ru_RU.UTF-8
Покрытия были разработаны для проектов рубина с умом, мы сделали его настолько
простым на сколько могли, чтобы сразу начать разработку.


%package       -n coveralls
Version:       0.8.23.2
Release:       alt0.1
Summary:       Coveralls for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета coveralls
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(coveralls) = 0.8.23.2
Conflicts:     python-module-z4r-coveralls

%description   -n coveralls
Coveralls for Ruby executable(s).

Coveralls was designed with Ruby projects in mind, and we've made it as easy as
we possibly can to get started.

%description   -n coveralls -l ru_RU.UTF-8
Исполнямка для самоцвета coveralls.

Покрытия были разработаны для проектов рубина с умом, мы сделали его настолько
простым на сколько могли, чтобы сразу начать разработку.


%package       -n gem-coveralls-doc
Version:       0.8.23.2
Release:       alt0.1
Summary:       Coveralls for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета coveralls
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(coveralls) = 0.8.23.2

%description   -n gem-coveralls-doc
Coveralls for Ruby documentation files.

Coveralls was designed with Ruby projects in mind, and we've made it as easy as
we possibly can to get started.

%description   -n gem-coveralls-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета coveralls.

Покрытия были разработаны для проектов рубина с умом, мы сделали его настолько
простым на сколько могли, чтобы сразу начать разработку.


%package       -n gem-coveralls-devel
Version:       0.8.23.2
Release:       alt0.1
Summary:       Coveralls for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета coveralls
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(coveralls) = 0.8.23.2
Requires:      gem(bundler) >= 2.0
Requires:      gem(rake) >= 10.3
Requires:      gem(rspec) >= 3.2
Requires:      gem(truthy) >= 1
Requires:      gem(vcr) >= 2.9
Requires:      gem(webmock) >= 1.20
Requires:      gem(addressable) >= 2.3.8
Requires:      gem(mime-types) >= 1.25
Requires:      gem(pry) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(addressable) >= 3
Conflicts:     gem(mime-types) >= 4

%description   -n gem-coveralls-devel
Coveralls for Ruby development package.

Coveralls was designed with Ruby projects in mind, and we've made it as easy as
we possibly can to get started.

%description   -n gem-coveralls-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета coveralls.

Покрытия были разработаны для проектов рубина с умом, мы сделали его настолько
простым на сколько могли, чтобы сразу начать разработку.


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

%files         -n coveralls
%doc README.md
%_bindir/coveralls

%files         -n gem-coveralls-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-coveralls-devel
%doc README.md


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 0.8.23.2-alt0.1
- ^ 0.8.23[1] -> 0.8.23[2]

* Mon May 31 2021 Pavel Skrylev <majioa@altlinux.org> 0.8.23.1-alt0.1
- ^ 0.8.23 -> 0.8.23[1]

* Mon May 31 2021 Pavel Skrylev <majioa@altlinux.org> 0.8.23-alt2
- ! spec
 + + explicit conflict for bump to python-module-z4r-coveralls
 + * minor

* Fri Jun 05 2020 Pavel Skrylev <majioa@altlinux.org> 0.8.23-alt1.1
- - spec dep to pry

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.8.23-alt1
- Bump to 0.8.23
- Fixed spec

* Fri Mar 1 2019 Pavel Skrylev <majioa@altlinux.org> 0.8.22-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
