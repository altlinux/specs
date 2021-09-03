%define        gemname necromancer

Name:          gem-necromancer
Version:       0.7.0
Release:       alt1
Summary:       Conversion from one object type to another
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/piotrmurach/necromancer
Vcs:           https://github.com/piotrmurach/necromancer.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Provides:      gem(necromancer) = 0.7.0


%description
Necromancer provides independent type conversion component for TTY toolkit.


%package       -n gem-necromancer-doc
Version:       0.7.0
Release:       alt1
Summary:       Conversion from one object type to another documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета necromancer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(necromancer) = 0.7.0

%description   -n gem-necromancer-doc
Conversion from one object type to another documentation
files.

Necromancer provides independent type conversion component for TTY toolkit.

%description   -n gem-necromancer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета necromancer.


%package       -n gem-necromancer-devel
Version:       0.7.0
Release:       alt1
Summary:       Conversion from one object type to another development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета necromancer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(necromancer) = 0.7.0
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4

%description   -n gem-necromancer-devel
Conversion from one object type to another development
package.

Necromancer provides independent type conversion component for TTY toolkit.

%description   -n gem-necromancer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета necromancer.


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

%files         -n gem-necromancer-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-necromancer-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt1
- ^ 0.5.0 -> 0.7.0

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1.1
- ! spec according to changelog rules

* Thu Aug 08 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- + packaged gem with usage Ruby Policy 2.0
