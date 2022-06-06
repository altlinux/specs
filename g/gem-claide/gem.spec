%define        gemname claide

Name:          gem-claide
Version:       1.1.0
Release:       alt1
Summary:       A small command-line interface framework
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/CocoaPods/CLAide
Vcs:           https://github.com/cocoapods/claide.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(claide) = 1.1.0

%description
I was born out of a need for a simple option and command parser, while still
providing an API that allows you to quickly create a full featured command-line
interface.


%package       -n gem-claide-doc
Version:       1.1.0
Release:       alt1
Summary:       A small command-line interface framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета claide
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(claide) = 1.1.0

%description   -n gem-claide-doc
A small command-line interface framework documentation files.

I was born out of a need for a simple option and command parser, while still
providing an API that allows you to quickly create a full featured command-line
interface.

%description   -n gem-claide-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета claide.


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

%files         -n gem-claide-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Fri May 06 2022 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with Ruby Policy 2.0
