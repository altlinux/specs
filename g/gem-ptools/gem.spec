%define        gemname ptools

Name:          gem-ptools
Version:       1.4.2
Release:       alt1
Summary:       Extra methods for the File class
License:       Artistic-2.0
Group:         Development/Ruby
Url:           https://github.com/djberg96/ptools
Vcs:           https://github.com/djberg96/ptools.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.9 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(ptools) = 1.4.2


%description
The ptools (power tools) library provides several handy methods to Ruby's core
File class, such as File.which for finding executables, File.null to return the
null device on your platform, and so on.


%package       -n gem-ptools-doc
Version:       1.4.2
Release:       alt1
Summary:       Extra methods for the File class documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ptools
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ptools) = 1.4.2

%description   -n gem-ptools-doc
Extra methods for the File class documentation files.

The ptools (power tools) library provides several handy methods to Ruby's core
File class, such as File.which for finding executables, File.null to return the
null device on your platform, and so on.

%description   -n gem-ptools-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ptools.


%package       -n gem-ptools-devel
Version:       1.4.2
Release:       alt1
Summary:       Extra methods for the File class development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ptools
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ptools) = 1.4.2
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4

%description   -n gem-ptools-devel
Extra methods for the File class development package.

The ptools (power tools) library provides several handy methods to Ruby's core
File class, such as File.which for finding executables, File.null to return the
null device on your platform, and so on.

%description   -n gem-ptools-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ptools.


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

%files         -n gem-ptools-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-ptools-devel
%doc README.md


%changelog
* Sun Apr 17 2022 Pavel Skrylev <majioa@altlinux.org> 1.4.2-alt1
- + packaged gem with Ruby Policy 2.0
