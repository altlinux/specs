%define        gemname bake-test

Name:          gem-bake-test
Version:       0.2.0
Release:       alt1
Summary:       Run local test suites without knowing exactly hwo to run them
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ioquatix/bake-test
Vcs:           https://github.com/ioquatix/bake-test.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bake) >= 0
BuildRequires: gem(sus) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(bake) >= 0
Provides:      gem(bake-test) = 0.2.0

%description
A gem for executing internal tests.


%package       -n gem-bake-test-doc
Version:       0.2.0
Release:       alt1
Summary:       Run local test suites without knowing exactly hwo to run them documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bake-test
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bake-test) = 0.2.0

%description   -n gem-bake-test-doc
Run local test suites without knowing exactly hwo to run them documentation
files.

A gem for executing internal tests.

%description   -n gem-bake-test-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bake-test.


%package       -n gem-bake-test-devel
Version:       0.2.0
Release:       alt1
Summary:       Run local test suites without knowing exactly hwo to run them development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bake-test
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bake-test) = 0.2.0
Requires:      gem(sus) >= 0

%description   -n gem-bake-test-devel
Run local test suites without knowing exactly hwo to run them development
package.

A gem for executing internal tests.

%description   -n gem-bake-test-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bake-test.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-bake-test-doc
%ruby_gemdocdir

%files         -n gem-bake-test-devel


%changelog
* Sun Oct 16 2022 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1
- + packaged gem with Ruby Policy 2.0
