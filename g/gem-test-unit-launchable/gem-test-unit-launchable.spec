%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname test-unit-launchable

Name:          gem-test-unit-launchable
Version:       0.1.5
Release:       alt1
Summary:       test-unit plugin that generates a Launchable test report file
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ono-max/test-unit-launchable
Vcs:           https://github.com/ono-max/test-unit-launchable.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(test-unit) >= 0
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(test-unit) >= 0
Provides:      gem(test-unit-launchable) = 0.1.5


%description
test-unit-launchable is a convinient plugin for test-unit that generates a
Launchable test report file based on the test results.


%if_enabled    doc
%package       -n gem-test-unit-launchable-doc
Version:       0.1.5
Release:       alt1
Summary:       test-unit plugin that generates a Launchable test report file documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета test-unit-launchable
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(test-unit-launchable) = 0.1.5

%description   -n gem-test-unit-launchable-doc
test-unit plugin that generates a Launchable test report file documentation
files.

test-unit-launchable is a convinient plugin for test-unit that generates a
Launchable test report file based on the test results.

%description   -n gem-test-unit-launchable-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета test-unit-launchable.
%endif


%if_enabled    devel
%package       -n gem-test-unit-launchable-devel
Version:       0.1.5
Release:       alt1
Summary:       test-unit plugin that generates a Launchable test report file development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета test-unit-launchable
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(test-unit-launchable) = 0.1.5
Requires:      gem(rake) >= 13.0
Conflicts:     gem(rake) >= 14

%description   -n gem-test-unit-launchable-devel
test-unit plugin that generates a Launchable test report file development
package.

test-unit-launchable is a convinient plugin for test-unit that generates a
Launchable test report file based on the test results.

%description   -n gem-test-unit-launchable-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета test-unit-launchable.
%endif


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

%if_enabled    doc
%files         -n gem-test-unit-launchable-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-test-unit-launchable-devel
%doc README.md
%endif


%changelog
* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 0.1.5-alt1
- + packaged gem with Ruby Policy 2.0
