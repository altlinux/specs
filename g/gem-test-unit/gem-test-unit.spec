%define        gemname test-unit

Name:          gem-test-unit
Version:       3.5.3
Release:       alt1
Summary:       An xUnit family unit testing framework for Ruby
License:       Ruby or BSDL or PSFL
Group:         Development/Ruby
Url:           http://test-unit.github.io/
Vcs:           https://github.com/test-unit/test-unit.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(power_assert) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(packnga) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(power_assert) >= 0
Obsoletes:     ruby-test-unit < %EVR
Provides:      ruby-test-unit = %EVR
Provides:      gem(test-unit) = 3.5.3


%description
An xUnit family unit testing framework for Ruby.

test-unit (Test::Unit) is unit testing framework for Ruby, based on xUnit
principles. These were originally designed by Kent Beck, creator of extreme
programming software development methodology, for Smalltalk's SUnit. It allows
writing tests, checking results and automated testing in Ruby.


%package       -n gem-test-unit-doc
Version:       3.5.3
Release:       alt1
Summary:       An xUnit family unit testing framework for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета test-unit
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(test-unit) = 3.5.3

%description   -n gem-test-unit-doc
An xUnit family unit testing framework for Ruby documentation files.

%description   -n gem-test-unit-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета test-unit.


%package       -n gem-test-unit-devel
Version:       3.5.3
Release:       alt1
Summary:       An xUnit family unit testing framework for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета test-unit
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(test-unit) = 3.5.3
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(kramdown) >= 0
Requires:      gem(packnga) >= 0

%description   -n gem-test-unit-devel
An xUnit family unit testing framework for Ruby development package.

%description   -n gem-test-unit-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета test-unit.


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

%files         -n gem-test-unit-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-test-unit-devel
%doc README.md


%changelog
* Sun Apr 03 2022 Pavel Skrylev <majioa@altlinux.org> 3.5.3-alt1
- ^ 3.3.5 -> 3.5.3

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 3.3.5-alt1
- ^ 3.3.1 -> 3.3.5
- ! spec tags

* Thu Apr 04 2019 Pavel Skrylev <majioa@altlinux.org> 3.3.1-alt1
- Bump to 3.3.1
- Use Ruby Policy 2.0

* Tue Jan 15 2019 Pavel Skrylev <majioa@altlinux.org> 3.2.9-alt1
- Bump to 3.2.9

* Sat Dec 29 2018 Pavel Skrylev <majioa@altlinux.org> 2.5.3-alt1
- Initial build for Sisyphus, packaged as a gem
