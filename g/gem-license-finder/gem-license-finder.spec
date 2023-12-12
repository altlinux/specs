%define        _unpackaged_files_terminate_build 1
%define        gemname license_finder

Name:          gem-license-finder
Version:       7.1.0
Release:       alt1
Summary:       Audit the OSS licenses of your application's dependencies
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/pivotal/LicenseFinder
Vcs:           https://github.com/pivotal/licensefinder.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(addressable) >= 2.8.0
BuildRequires: gem(capybara) >= 3.32.2
BuildRequires: gem(e2mmap) >= 0.1.0
BuildRequires: gem(fakefs) >= 1.8.0
BuildRequires: gem(matrix) >= 0.1.0
BuildRequires: gem(mime-types) = 3.4.1
BuildRequires: gem(pry) >= 0.13.1
BuildRequires: gem(rake) >= 13.0.6
BuildRequires: gem(rspec) >= 3
BuildRequires: gem(rspec-its) >= 1.3.0
BuildRequires: gem(rubocop) >= 1.12.1
BuildRequires: gem(rubocop-performance) >= 1.10.2
BuildRequires: gem(webmock) >= 3.13.0
BuildRequires: gem(nokogiri) >= 1.10
BuildRequires: gem(rack) >= 2.2.2
BuildRequires: gem(rack-test) > 0.7
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rubyzip) >= 1
BuildRequires: gem(thor) >= 1.2
BuildRequires: gem(tomlrb) >= 1.3
BuildRequires: gem(with_env) = 1.1.0
BuildRequires: gem(xml-simple) >= 1.1.9
BuildConflicts: gem(addressable) >= 3
BuildConflicts: gem(capybara) >= 4
BuildConflicts: gem(e2mmap) >= 0.2
BuildConflicts: gem(fakefs) >= 2
BuildConflicts: gem(matrix) >= 1
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-its) >= 1.4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(nokogiri) >= 2
BuildConflicts: gem(rack) >= 3.1
BuildConflicts: gem(rubyzip) >= 3
BuildConflicts: gem(thor) >= 2
BuildConflicts: gem(tomlrb) >= 3
BuildConflicts: gem(xml-simple) >= 1.2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rack >= 2.2.2,rack < 3
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency tomlrb >= 2.0.1,tomlrb < 3
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
%ruby_use_gem_dependency rack-test >= 1.1.0,rack-test < 2
%ruby_use_gem_dependency addressable >= 2.8.0,addressable < 3
%ruby_use_gem_dependency capybara >= 3.37.0,capybara < 4
%ruby_use_gem_dependency matrix >= 0.4.2,matrix < 1
%ruby_use_gem_dependency fakefs >= 1.9.0,fakefs < 2
Requires:      gem(bundler) >= 0
Requires:      gem(rubyzip) >= 1
Requires:      gem(thor) >= 1.2
Requires:      gem(tomlrb) >= 1.3
Requires:      gem(with_env) = 1.1.0
Requires:      gem(xml-simple) >= 1.1.9
Conflicts:     gem(rubyzip) >= 3
Conflicts:     gem(thor) >= 2
Conflicts:     gem(tomlrb) >= 3
Conflicts:     gem(xml-simple) >= 1.2
Provides:      gem(license_finder) = 7.1.0

%ruby_bindir_to %ruby_bindir

%description
LicenseFinder works with your package managers to find dependencies, detect the
licenses of the packages in them, compare those licenses against a user-defined
list of permitted licenses, and give you an actionable exception report.


%package       -n license-finder
Version:       7.1.0
Release:       alt1
Summary:       Audit the OSS licenses of your application's dependencies executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета license_finder
Group:         Other
BuildArch:     noarch

Requires:      gem(license_finder) = 7.1.0

%description   -n license-finder
Audit the OSS licenses of your application's dependencies
executable(s).

LicenseFinder works with your package managers to find dependencies, detect the
licenses of the packages in them, compare those licenses against a user-defined
list of permitted licenses, and give you an actionable exception report.

%description   -n license-finder -l ru_RU.UTF-8
Исполнямка для самоцвета license_finder.


%package       -n gem-license-finder-doc
Version:       7.1.0
Release:       alt1
Summary:       Audit the OSS licenses of your application's dependencies documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета license_finder
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(license_finder) = 7.1.0

%description   -n gem-license-finder-doc
Audit the OSS licenses of your application's dependencies documentation
files.

LicenseFinder works with your package managers to find dependencies, detect the
licenses of the packages in them, compare those licenses against a user-defined
list of permitted licenses, and give you an actionable exception report.

%description   -n gem-license-finder-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета license_finder.


%package       -n gem-license-finder-devel
Version:       7.1.0
Release:       alt1
Summary:       Audit the OSS licenses of your application's dependencies development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета license_finder
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(license_finder) = 7.1.0
Requires:      gem(addressable) >= 2.8.0
Requires:      gem(capybara) >= 3.32.2
Requires:      gem(e2mmap) >= 0.1.0
Requires:      gem(fakefs) >= 1.8.0
Requires:      gem(matrix) >= 0.1.0
Requires:      gem(mime-types) = 3.4.1
Requires:      gem(pry) >= 0.13.1
Requires:      gem(rake) >= 13.0.6
Requires:      gem(rspec) >= 3
Requires:      gem(rspec-its) >= 1.3.0
Requires:      gem(rubocop) >= 1.12.1
Requires:      gem(rubocop-performance) >= 1.10.2
Requires:      gem(webmock) >= 3.13.0
Requires:      gem(nokogiri) >= 1.10
Requires:      gem(rack) >= 2.2.2
Requires:      gem(rack-test) > 0.7
Conflicts:     gem(addressable) >= 3
Conflicts:     gem(capybara) >= 4
Conflicts:     gem(e2mmap) >= 0.2
Conflicts:     gem(fakefs) >= 2
Conflicts:     gem(matrix) >= 1
Conflicts:     gem(pry) >= 1
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rspec-its) >= 1.4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(webmock) >= 4
Conflicts:     gem(nokogiri) >= 2
Conflicts:     gem(rack) >= 3.1

%description   -n gem-license-finder-devel
Audit the OSS licenses of your application's dependencies development
package.

LicenseFinder works with your package managers to find dependencies, detect the
licenses of the packages in them, compare those licenses against a user-defined
list of permitted licenses, and give you an actionable exception report.

%description   -n gem-license-finder-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета license_finder.


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

%files         -n license-finder
%doc README.md
%ruby_bindir/license_finder
%ruby_bindir/license_finder_pip.py

%files         -n gem-license-finder-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-license-finder-devel
%doc README.md


%changelog
* Tue Dec 05 2023 Pavel Skrylev <majioa@altlinux.org> 7.1.0-alt1
- + packaged gem with Ruby Policy 2.0
