%define        gemname test-unit-rr

Name:          gem-test-unit-rr
Version:       1.0.5
Release:       alt1
Summary:       test-unit-rr is a RR adapter for test-unit
License:       LGPLv2 or later
Group:         Development/Ruby
Url:           https://github.com/test-unit/test-unit-rr
Vcs:           https://github.com/test-unit/test-unit-rr.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(test-unit) >= 2.5.2 gem(test-unit) < 4
BuildRequires: gem(rr) >= 1.1.1
BuildRequires: gem(bundler) >= 0 gem(bundler) < 3
BuildRequires: gem(rake) >= 0 gem(rake) < 14
BuildRequires: gem(packnga) >= 0
BuildRequires: gem(kramdown) >= 0 gem(kramdown) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency test-unit >= 3.3.5,test-unit < 4
%ruby_use_gem_dependency kramdown >= 2.3.1,kramdown < 3
Requires:      gem(test-unit) >= 2.5.2 gem(test-unit) < 4
Requires:      gem(rr) >= 1.1.1
Provides:      gem(test-unit-rr) = 1.0.5


%description
You don't need RR setup codes with test-unit-rr. You just require
"test/unit/rr".


%package       -n gem-test-unit-rr-doc
Version:       1.0.5
Release:       alt1
Summary:       test-unit-rr is a RR adapter for test-unit documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета test-unit-rr
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(test-unit-rr) = 1.0.5

%description   -n gem-test-unit-rr-doc
test-unit-rr is a RR adapter for test-unit documentation files.

You don't need RR setup codes with test-unit-rr. You just require
"test/unit/rr".

%description   -n gem-test-unit-rr-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета test-unit-rr.


%package       -n gem-test-unit-rr-devel
Version:       1.0.5
Release:       alt1
Summary:       test-unit-rr is a RR adapter for test-unit development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета test-unit-rr
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(test-unit-rr) = 1.0.5
Requires:      gem(bundler) >= 0 gem(bundler) < 3
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(packnga) >= 0
Requires:      gem(kramdown) >= 0 gem(kramdown) < 3

%description   -n gem-test-unit-rr-devel
test-unit-rr is a RR adapter for test-unit development package.

You don't need RR setup codes with test-unit-rr. You just require
"test/unit/rr".

%description   -n gem-test-unit-rr-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета test-unit-rr.


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

%files         -n gem-test-unit-rr-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-test-unit-rr-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt1
- + packaged gem with Ruby Policy 2.0
