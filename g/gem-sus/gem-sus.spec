%define        gemname sus

Name:          gem-sus
Version:       0.14.0
Release:       alt1
Summary:       A fast and scalable test runner
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ioquatix/sus
Vcs:           https://github.com/ioquatix/sus.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bake-test) >= 0.1 gem(bake-test) < 1
BuildRequires: gem(bake-test-external) >= 0.1 gem(bake-test-external) < 1
BuildRequires: gem(covered) >= 0.16.6 gem(covered) < 1
%endif
%ruby_use_gem_dependency covered >= 0.18.2,covered < 1
%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(sus) = 0.14.0


%description
An opinionated test framework designed with several goals:

* As fast as possible, aiming for ~10,000 assertions per second per core.
* Isolated tests which parallelise easily (including class definitions).
* Native support for balanced (work-stealing) multi-core execution.
* Incredible test output with detailed failure logging (including nested
assertions and predicates).

Non-features:

* Flexibility at the expense of performance.
* Backwards compatibility.


%package       -n sus
Version:       0.14.0
Release:       alt1
Summary:       A fast and scalable test runner executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета sus
Group:         Other
BuildArch:     noarch

Requires:      gem(sus) = 0.14.0

%description   -n sus
A fast and scalable test runner executable(s).

An opinionated test framework designed with several goals:

* As fast as possible, aiming for ~10,000 assertions per second per core.
* Isolated tests which parallelise easily (including class definitions).
* Native support for balanced (work-stealing) multi-core execution.
* Incredible test output with detailed failure logging (including nested
assertions and predicates).

Non-features:

* Flexibility at the expense of performance.
* Backwards compatibility.

%description   -n sus -l ru_RU.UTF-8
Исполнямка для самоцвета sus.


%package       -n gem-sus-doc
Version:       0.14.0
Release:       alt1
Summary:       A fast and scalable test runner documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sus
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sus) = 0.14.0

%description   -n gem-sus-doc
A fast and scalable test runner documentation files.

An opinionated test framework designed with several goals:

* As fast as possible, aiming for ~10,000 assertions per second per core.
* Isolated tests which parallelise easily (including class definitions).
* Native support for balanced (work-stealing) multi-core execution.
* Incredible test output with detailed failure logging (including nested
assertions and predicates).

Non-features:

* Flexibility at the expense of performance.
* Backwards compatibility.

%description   -n gem-sus-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sus.


%package       -n gem-sus-devel
Version:       0.14.0
Release:       alt1
Summary:       A fast and scalable test runner development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sus
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sus) = 0.14.0
Requires:      gem(bake-test) >= 0.1 gem(bake-test) < 1
Requires:      gem(bake-test-external) >= 0.1 gem(bake-test-external) < 1
Requires:      gem(covered) >= 0.16.6 gem(covered) < 1

%description   -n gem-sus-devel
A fast and scalable test runner development package.

An opinionated test framework designed with several goals:

* As fast as possible, aiming for ~10,000 assertions per second per core.
* Isolated tests which parallelise easily (including class definitions).
* Native support for balanced (work-stealing) multi-core execution.
* Incredible test output with detailed failure logging (including nested
assertions and predicates).

Non-features:

* Flexibility at the expense of performance.
* Backwards compatibility.

%description   -n gem-sus-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sus.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc readme.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n sus
%doc readme.md
%_bindir/sus
%_bindir/sus-parallel

%files         -n gem-sus-doc
%doc readme.md
%ruby_gemdocdir

%files         -n gem-sus-devel
%doc readme.md


%changelog
* Sun Oct 16 2022 Pavel Skrylev <majioa@altlinux.org> 0.14.0-alt1
- ^ 0.6.2 -> 0.14.0

* Wed Mar 16 2022 Pavel Skrylev <majioa@altlinux.org> 0.6.2-alt1
- + packaged gem with Ruby Policy 2.0
