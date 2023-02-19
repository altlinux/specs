%define        gemname test-unit-rr

Name:          gem-test-unit-rr
Version:       1.0.5.1
Release:       alt1
Summary:       test-unit-rr is a RR adapter for test-unit
License:       LGPLv2+
Group:         Development/Ruby
Url:           https://github.com/test-unit/test-unit-rr
Vcs:           https://github.com/test-unit/test-unit-rr.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(packnga) >= 0
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(test-unit) >= 2.5.2
BuildRequires: gem(rr) >= 1.1.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(test-unit) >= 2.5.2
Requires:      gem(rr) >= 1.1.1
Provides:      gem(test-unit-rr) = 1.0.5.1

%ruby_use_gem_version test-unit-rr:1.0.5.1

%description
You don't need RR setup codes with test-unit-rr. You just require
"test/unit/rr".


%package       -n gem-test-unit-rr-doc
Version:       1.0.5.1
Release:       alt1
Summary:       test-unit-rr is a RR adapter for test-unit documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета test-unit-rr
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(test-unit-rr) = 1.0.5.1

%description   -n gem-test-unit-rr-doc
test-unit-rr is a RR adapter for test-unit documentation files.

You don't need RR setup codes with test-unit-rr. You just require
"test/unit/rr".

%description   -n gem-test-unit-rr-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета test-unit-rr.


%package       -n gem-test-unit-rr-devel
Version:       1.0.5.1
Release:       alt1
Summary:       test-unit-rr is a RR adapter for test-unit development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета test-unit-rr
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(test-unit-rr) = 1.0.5.1
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(packnga) >= 0
Requires:      gem(kramdown) >= 0

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
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.5.1-alt1
- ^ 1.0.5 -> 1.0.5.1

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt1
- + packaged gem with Ruby Policy 2.0
