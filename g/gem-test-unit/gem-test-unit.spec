%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname test-unit

Name:          gem-test-unit
Version:       3.6.2
Release:       alt1
Summary:       An xUnit family unit testing framework for Ruby
License:       Ruby or BSD-2-Clause and PSF-2.0
Group:         Development/Ruby
Url:           http://test-unit.github.io/
Vcs:           https://github.com/test-unit/test-unit.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         licenses.patch
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(packnga) >= 0
BuildRequires: gem(bigdecimal) >= 0
BuildRequires: gem(power_assert) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(power_assert) >= 0
Obsoletes:     ruby-test-unit < %EVR
Provides:      ruby-test-unit = %EVR
Provides:      gem(test-unit) = 3.6.2


%description
An xUnit family unit testing framework for Ruby.

test-unit (Test::Unit) is unit testing framework for Ruby, based on xUnit
principles. These were originally designed by Kent Beck, creator of extreme
programming software development methodology, for Smalltalk's SUnit. It allows
writing tests, checking results and automated testing in Ruby.


%if_enabled    doc
%package       -n gem-test-unit-doc
Version:       3.6.2
Release:       alt1
Summary:       An xUnit family unit testing framework for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета test-unit
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(test-unit) = 3.6.2

%description   -n gem-test-unit-doc
An xUnit family unit testing framework for Ruby documentation files.

%description   -n gem-test-unit-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета test-unit.
%endif


%if_enabled    devel
%package       -n gem-test-unit-devel
Version:       3.6.2
Release:       alt1
Summary:       An xUnit family unit testing framework for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета test-unit
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(test-unit) = 3.6.2
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(kramdown) >= 0
Requires:      gem(packnga) >= 0
Requires:      gem(bigdecimal) >= 0

%description   -n gem-test-unit-devel
An xUnit family unit testing framework for Ruby development package.

%description   -n gem-test-unit-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета test-unit.
%endif


%prep
%setup
%autopatch

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

%if_enabled    doc
%files         -n gem-test-unit-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-test-unit-devel
%doc README.md
%endif


%changelog
* Wed May 08 2024 Pavel Skrylev <majioa@altlinux.org> 3.6.2-alt1
- ^ 3.5.3 -> 3.6.2
- * relicensed

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
