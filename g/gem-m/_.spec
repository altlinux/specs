%define        gemname m

Name:          gem-m
Version:       1.5.1.1
Release:       alt0.1
Summary:       A Test::Unit runner that can run tests by line number
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/qrush/m
Vcs:           https://github.com/qrush/m.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(method_source) >= 0.6.7
BuildRequires: gem(rake) >= 0.9.2.2 gem(rake) < 14
BuildRequires: gem(activesupport) >= 0 gem(activesupport) < 7
BuildRequires: gem(rdiscount) >= 0
BuildRequires: gem(rocco) >= 0
BuildRequires: gem(appraisal) >= 0 gem(appraisal) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency appraisal >= 2.4.0,appraisal < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency activesupport >= 6.1.3.2,activesupport < 7
%ruby_use_gem_version m:1.5.1.1
Requires:      gem(method_source) >= 0.6.7
Requires:      gem(rake) >= 0.9.2.2 gem(rake) < 14
Provides:      gem(m) = 1.5.1.1

%description
m stands for metal, a better test/unit and minitest test runner that can run
tests by line number.


%package       -n m
Version:       1.5.1.1
Release:       alt0.1
Summary:       A Test::Unit runner that can run tests by line number executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета m
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(m) = 1.5.1.1

%description   -n m
A Test::Unit runner that can run tests by line number executable(s).

m stands for metal, a better test/unit and minitest test runner that can run
tests by line number.

%description   -n m -l ru_RU.UTF-8
Исполнямка для самоцвета m.


%package       -n gem-m-doc
Version:       1.5.1.1
Release:       alt0.1
Summary:       A Test::Unit runner that can run tests by line number documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета m
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(m) = 1.5.1.1

%description   -n gem-m-doc
A Test::Unit runner that can run tests by line number documentation files.

m stands for metal, a better test/unit and minitest test runner that can run
tests by line number.

%description   -n gem-m-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета m.


%package       -n gem-m-devel
Version:       1.5.1.1
Release:       alt0.1
Summary:       A Test::Unit runner that can run tests by line number development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета m
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(m) = 1.5.1.1
Requires:      gem(activesupport) >= 0 gem(activesupport) < 7
Requires:      gem(rdiscount) >= 0
Requires:      gem(rocco) >= 0
Requires:      gem(appraisal) >= 0 gem(appraisal) < 3

%description   -n gem-m-devel
A Test::Unit runner that can run tests by line number development package.

m stands for metal, a better test/unit and minitest test runner that can run
tests by line number.

%description   -n gem-m-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета m.


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

%files         -n m
%doc README.md
%_bindir/m

%files         -n gem-m-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-m-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.5.1.1-alt0.1
- ^ 1.5.1 -> 1.5.1[.1]

* Tue Oct 22 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.1-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
