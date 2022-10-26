%define        gemname blankslate

Name:          gem-blankslate
Version:       2.1.2.5
Release:       alt1
Summary:       BlankSlate extracted from Builder
License:       Unlicense
Group:         Development/Ruby
Url:           https://github.com/masover/blankslate
Vcs:           https://github.com/masover/blankslate.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(blankslate) = 2.1.2.5

%ruby_use_gem_version blankslate:2.1.2.5

%description
BlankSlate extracted from Builder.


%package       -n gem-blankslate-doc
Version:       2.1.2.5
Release:       alt1
Summary:       BlankSlate extracted from Builder documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета blankslate
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(blankslate) = 2.1.2.5

%description   -n gem-blankslate-doc
BlankSlate extracted from Builder documentation files.

%description   -n gem-blankslate-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета blankslate.


%package       -n gem-blankslate-devel
Version:       2.1.2.5
Release:       alt1
Summary:       BlankSlate extracted from Builder development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета blankslate
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(blankslate) = 2.1.2.5

%description   -n gem-blankslate-devel
BlankSlate extracted from Builder development package.

%description   -n gem-blankslate-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета blankslate.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-blankslate-doc
%doc README
%ruby_gemdocdir

%files         -n gem-blankslate-devel
%doc README


%changelog
* Tue Oct 18 2022 Pavel Skrylev <majioa@altlinux.org> 2.1.2.5-alt1
- + packaged gem with Ruby Policy 2.0
