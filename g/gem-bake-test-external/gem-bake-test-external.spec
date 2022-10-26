%define        gemname bake-test-external

Name:          gem-bake-test-external
Version:       0.3.2
Release:       alt1
Summary:       Run external test suites to check for breakage
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ioquatix/bake-test-external
Vcs:           https://github.com/ioquatix/bake-test-external.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bake) >= 0
BuildRequires: gem(rspec) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(bake) >= 0
Provides:      gem(bake-test-external) = 0.3.2

%description
A gem for executing external (downstream) tests.


%package       -n gem-bake-test-external-doc
Version:       0.3.2
Release:       alt1
Summary:       Run external test suites to check for breakage documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bake-test-external
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bake-test-external) = 0.3.2

%description   -n gem-bake-test-external-doc
Run external test suites to check for breakage documentation files.

A gem for executing external (downstream) tests.

%description   -n gem-bake-test-external-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bake-test-external.


%package       -n gem-bake-test-external-devel
Version:       0.3.2
Release:       alt1
Summary:       Run external test suites to check for breakage development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bake-test-external
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bake-test-external) = 0.3.2
Requires:      gem(rspec) >= 0

%description   -n gem-bake-test-external-devel
Run external test suites to check for breakage development package.

A gem for executing external (downstream) tests.

%description   -n gem-bake-test-external-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bake-test-external.


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

%files         -n gem-bake-test-external-doc
%doc readme.md
%ruby_gemdocdir

%files         -n gem-bake-test-external-devel
%doc readme.md


%changelog
* Sun Oct 16 2022 Pavel Skrylev <majioa@altlinux.org> 0.3.2-alt1
- + packaged gem with Ruby Policy 2.0
