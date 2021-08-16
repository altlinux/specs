%define        gemname shoulda

Name:          gem-shoulda
Version:       4.0.0
Release:       alt1
Summary:       Making tests easy on the fingers and eyes
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/thoughtbot/shoulda
Vcs:           https://github.com/thoughtbot/shoulda.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(shoulda-context) >= 2.0.0 gem(shoulda-context) < 3
BuildRequires: gem(shoulda-matchers) >= 4.0 gem(shoulda-matchers) < 5

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(shoulda-context) >= 2.0.0 gem(shoulda-context) < 3
Requires:      gem(shoulda-matchers) >= 4.0 gem(shoulda-matchers) < 5
Provides:      gem(shoulda) = 4.0.0


%description
Shoulda makes it easy to write elegant, understandable, and maintainable tests.
Shoulda consists of test macros, assertions, and helpers added on to the
Test::Unit framework. It's fully compatible with your existing tests, and
requires no retooling to use.


%package       -n gem-shoulda-doc
Version:       4.0.0
Release:       alt1
Summary:       Making tests easy on the fingers and eyes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета shoulda
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(shoulda) = 4.0.0

%description   -n gem-shoulda-doc
Making tests easy on the fingers and eyes documentation files.

Shoulda makes it easy to write elegant, understandable, and maintainable tests.
Shoulda consists of test macros, assertions, and helpers added on to the
Test::Unit framework. It's fully compatible with your existing tests, and
requires no retooling to use.

%description   -n gem-shoulda-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета shoulda.


%package       -n gem-shoulda-devel
Version:       4.0.0
Release:       alt1
Summary:       Making tests easy on the fingers and eyes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета shoulda
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(shoulda) = 4.0.0

%description   -n gem-shoulda-devel
Making tests easy on the fingers and eyes development package.

Shoulda makes it easy to write elegant, understandable, and maintainable tests.
Shoulda consists of test macros, assertions, and helpers added on to the
Test::Unit framework. It's fully compatible with your existing tests, and
requires no retooling to use.

%description   -n gem-shoulda-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета shoulda.


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

%files         -n gem-shoulda-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-shoulda-devel
%doc README.md


%changelog
* Wed Jun 30 2021 Pavel Skrylev <majioa@altlinux.org> 4.0.0-alt1
- ^ 2.11.1 -> 4.0.0

* Tue Jul 20 2010 Alexey I. Froloff <raorn@altlinux.org> 2.11.1-alt1
- [2.11.1]

* Mon Oct 19 2009 Alexey I. Froloff <raorn@altlinux.org> 2.10.2-alt1
- Built for Sisyphus
