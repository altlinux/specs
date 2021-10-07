%define        gemname brass

Name:          gem-brass
Version:       1.2.1
Release:       alt1
Summary:       Bare-Metal Ruby Assertion System Standard
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           http://rubyworks.github.com/brass
Vcs:           https://github.com/detroit/detroit.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
#BuildRequires: gem(detroit) >= 0
#BuildRequires: gem(lemon) >= 0
#BuildRequires: gem(rubytest) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(brass) = 1.2.1


%description
BRASS stands for Bare-Metal Ruby Assertion System Standard. It is a very basic
foundational assertions framework for other assertion and test frameworks to
make use so they can all work together harmoniously.


%package       -n gem-brass-doc
Version:       1.2.1
Release:       alt1
Summary:       Bare-Metal Ruby Assertion System Standard documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета brass
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(brass) = 1.2.1

%description   -n gem-brass-doc
Bare-Metal Ruby Assertion System Standard documentation files.

BRASS stands for Bare-Metal Ruby Assertion System Standard. It is a very basic
foundational assertions framework for other assertion and test frameworks to
make use so they can all work together harmoniously.

%description   -n gem-brass-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета brass.


%package       -n gem-brass-devel
Version:       1.2.1
Release:       alt1
Summary:       Bare-Metal Ruby Assertion System Standard development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета brass
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(brass) = 1.2.1
#Requires:      gem(detroit) >= 0
#Requires:      gem(lemon) >= 0
#Requires:      gem(rubytest) >= 0

%description   -n gem-brass-devel
Bare-Metal Ruby Assertion System Standard development package.

BRASS stands for Bare-Metal Ruby Assertion System Standard. It is a very basic
foundational assertions framework for other assertion and test frameworks to
make use so they can all work together harmoniously.

%description   -n gem-brass-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета brass.


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

%files         -n gem-brass-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-brass-devel
%doc README.md


%changelog
* Sat Sep 11 2021 Pavel Skrylev <majioa@altlinux.org> 1.2.1-alt1
- + packaged gem with Ruby Policy 2.0
