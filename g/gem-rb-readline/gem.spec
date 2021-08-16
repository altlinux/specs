%define        gemname rb-readline

Name:          gem-rb-readline
Version:       0.5.5
Release:       alt1
Summary:       Pure-Ruby Readline Implementation
License:       BSD
Group:         Development/Ruby
Url:           http://github.com/ConnorAtherton/rb-readline
Vcs:           https://github.com/connoratherton/rb-readline.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0 gem(rake) < 14
BuildRequires: gem(minitest) >= 5.2 gem(minitest) < 6

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Provides:      gem(rb-readline) = 0.5.5


%description
The readline library provides a pure Ruby implementation of the GNU readline C
library, as well as the Readline extension that ships as part of the standard
library.


%package       -n gem-rb-readline-doc
Version:       0.5.5
Release:       alt1
Summary:       Pure-Ruby Readline Implementation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rb-readline
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rb-readline) = 0.5.5

%description   -n gem-rb-readline-doc
Pure-Ruby Readline Implementation documentation files.

The readline library provides a pure Ruby implementation of the GNU readline C
library, as well as the Readline extension that ships as part of the standard
library.

%description   -n gem-rb-readline-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rb-readline.


%package       -n gem-rb-readline-devel
Version:       0.5.5
Release:       alt1
Summary:       Pure-Ruby Readline Implementation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rb-readline
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rb-readline) = 0.5.5
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(minitest) >= 5.2 gem(minitest) < 6

%description   -n gem-rb-readline-devel
Pure-Ruby Readline Implementation development package.

The readline library provides a pure Ruby implementation of the GNU readline C
library, as well as the Readline extension that ships as part of the standard
library.

%description   -n gem-rb-readline-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rb-readline.


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

%files         -n gem-rb-readline-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rb-readline-devel
%doc README.md


%changelog
* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.5-alt1
- + packaged gem with Ruby Policy 2.0
