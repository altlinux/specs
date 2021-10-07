%define        gemname morecane

Name:          gem-morecane
Version:       0.2.0
Release:       alt1
Summary:       Extra checks for the cane gem
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/yob/morecane
Vcs:           https://github.com/yob/morecane.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(cane) >= 2.1.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.5 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(cane) >= 2.1.0
Provides:      gem(morecane) = 0.2.0


%description
A set of common checks that I use with cane across my projects


%package       -n gem-morecane-doc
Version:       0.2.0
Release:       alt1
Summary:       Extra checks for the cane gem documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета morecane
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(morecane) = 0.2.0

%description   -n gem-morecane-doc
Extra checks for the cane gem documentation files.

A set of common checks that I use with cane across my projects

%description   -n gem-morecane-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета morecane.


%package       -n gem-morecane-devel
Version:       0.2.0
Release:       alt1
Summary:       Extra checks for the cane gem development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета morecane
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(morecane) = 0.2.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.5 gem(rspec) < 4

%description   -n gem-morecane-devel
Extra checks for the cane gem development package.

A set of common checks that I use with cane across my projects

%description   -n gem-morecane-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета morecane.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-morecane-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-morecane-devel
%doc README.rdoc


%changelog
* Sun Sep 12 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1
- + packaged gem with Ruby Policy 2.0
