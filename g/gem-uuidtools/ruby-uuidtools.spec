%define        gemname uuidtools

Name:          gem-uuidtools
Version:       2.2.0
Release:       alt1
Summary:       A simple universally unique ID generation library
License:       Apache-2.0
Group:         Development/Ruby
Url:           http://github.com/sporkmonger/uuidtools
Vcs:           https://github.com/sporkmonger/uuidtools.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0.7.3 gem(rake) < 14
BuildRequires: gem(rspec) >= 2.9.0 gem(rspec) < 4
BuildRequires: gem(yard) >= 0.8.2
BuildRequires: gem(launchy) >= 2.0.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Obsoletes:     ruby-uuidtools < %EVR
Provides:      ruby-uuidtools = %EVR
Provides:      gem(uuidtools) = 2.2.0


%description
UUIDTools was designed to be a simple library for generating any of the various
types of UUIDs. It conforms to RFC 4122 whenever possible.


%package       -n gem-uuidtools-doc
Version:       2.2.0
Release:       alt1
Summary:       A simple universally unique ID generation library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета uuidtools
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(uuidtools) = 2.2.0

%description   -n gem-uuidtools-doc
A simple universally unique ID generation library documentation
files.

UUIDTools was designed to be a simple library for generating any of the various
types of UUIDs. It conforms to RFC 4122 whenever possible.

%description   -n gem-uuidtools-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета uuidtools.


%package       -n gem-uuidtools-devel
Version:       2.2.0
Release:       alt1
Summary:       A simple universally unique ID generation library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета uuidtools
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(uuidtools) = 2.2.0
Requires:      gem(rake) >= 0.7.3 gem(rake) < 14
Requires:      gem(rspec) >= 2.9.0 gem(rspec) < 4
Requires:      gem(yard) >= 0.8.2
Requires:      gem(launchy) >= 2.0.0

%description   -n gem-uuidtools-devel
A simple universally unique ID generation library development
package.

UUIDTools was designed to be a simple library for generating any of the various
types of UUIDs. It conforms to RFC 4122 whenever possible.

%description   -n gem-uuidtools-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета uuidtools.


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

%files         -n gem-uuidtools-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-uuidtools-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- ^ 2.1.5 -> 2.2.0

* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.5-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.5-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Sep 08 2017 Andrey Cherepanov <cas@altlinux.org> 2.1.5-alt1
- New version
- Disable use deprecated thread module

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1.2
- Rebuild with Ruby 2.4.1

* Tue Dec 04 2012 Led <led@altlinux.ru> 2.1.0-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Mon Apr 26 2010 Alexey I. Froloff <raorn@altlinux.org> 2.1.0-alt1
- Built for Sisyphus
