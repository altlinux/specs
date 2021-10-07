%define        gemname midwire_common

Name:          gem-midwire-common
Version:       1.1.0
Release:       alt1
Summary:       Midwire Tech Ruby Library
License:       MIT
Group:         Development/Ruby
Url:           https://bitbucket.org/midwiretech/midwire_common
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec) >= 2.14 gem(rspec) < 4
BuildRequires: gem(simplecov) >= 0.7 gem(simplecov) < 1
# BuildRequires: gem(guard) >= 2.11 gem(guard) < 3
# BuildRequires: gem(guard-bundler) >= 2.1 gem(guard-bundler) < 3
# BuildRequires: gem(guard-rspec) >= 4.5 gem(guard-rspec) < 5
# BuildRequires: gem(guard-rubocop) >= 1.2 gem(guard-rubocop) < 2
# BuildRequires: gem(pry-nav) >= 0.2 gem(pry-nav) < 1
BuildRequires: gem(rake) >= 10.1 gem(rake) < 14
BuildRequires: gem(rubocop) >= 0.36 gem(rubocop) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Provides:      gem(midwire_common) = 1.1.0


%description
A useful Ruby library


%package       -n gem-midwire-common-doc
Version:       1.1.0
Release:       alt1
Summary:       Midwire Tech Ruby Library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета midwire_common
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(midwire_common) = 1.1.0

%description   -n gem-midwire-common-doc
Midwire Tech Ruby Library documentation files.

A useful Ruby library

%description   -n gem-midwire-common-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета midwire_common.


%package       -n gem-midwire-common-devel
Version:       1.1.0
Release:       alt1
Summary:       Midwire Tech Ruby Library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета midwire_common
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(midwire_common) = 1.1.0
Requires:      gem(rspec) >= 2.14 gem(rspec) < 4
Requires:      gem(simplecov) >= 0.7 gem(simplecov) < 1
# Requires:      gem(guard) >= 2.11 gem(guard) < 3
# Requires:      gem(guard-bundler) >= 2.1 gem(guard-bundler) < 3
# Requires:      gem(guard-rspec) >= 4.5 gem(guard-rspec) < 5
# Requires:      gem(guard-rubocop) >= 1.2 gem(guard-rubocop) < 2
# Requires:      gem(pry-nav) >= 0.2 gem(pry-nav) < 1
Requires:      gem(rake) >= 10.1 gem(rake) < 14
Requires:      gem(rubocop) >= 0.36 gem(rubocop) < 2

%description   -n gem-midwire-common-devel
Midwire Tech Ruby Library development package.

A useful Ruby library

%description   -n gem-midwire-common-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета midwire_common.


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

%files         -n gem-midwire-common-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-midwire-common-devel
%doc README.md


%changelog
* Wed Oct 06 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with Ruby Policy 2.0
