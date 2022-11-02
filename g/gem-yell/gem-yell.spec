%define        gemname yell

Name:          gem-yell
Version:       2.2.0
Release:       alt1
Summary:       Yell - Your Extensible Logging Library
License:       MIT
Group:         Development/Ruby
Url:           http://rudionrailspec.github.com/yell
Vcs:           https://github.com/rudionrails/yell.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec-core) >= 3 gem(rspec-core) < 4
BuildRequires: gem(rspec-expectations) >= 0
BuildRequires: gem(rspec-mocks) >= 0
BuildRequires: gem(rspec-its) >= 0
BuildRequires: gem(timecop) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(activesupport) >= 5 gem(activesupport) < 7
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(coveralls) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency activesupport >= 6.1.3.2,activesupport < 7
Provides:      gem(yell) = 2.2.0


%description
Yell - Your Extensible Logging Library. Define multiple adapters, various log
level combinations or message formatting options like you've never done before


%package       -n gem-yell-doc
Version:       2.2.0
Release:       alt1
Summary:       Yell - Your Extensible Logging Library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета yell
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(yell) = 2.2.0

%description   -n gem-yell-doc
Yell - Your Extensible Logging Library documentation files.

Yell - Your Extensible Logging Library. Define multiple adapters, various log
level combinations or message formatting options like you've never done before

%description   -n gem-yell-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета yell.


%package       -n gem-yell-devel
Version:       2.2.0
Release:       alt1
Summary:       Yell - Your Extensible Logging Library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета yell
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(yell) = 2.2.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec-core) >= 3 gem(rspec-core) < 4
Requires:      gem(rspec-expectations) >= 0
Requires:      gem(rspec-mocks) >= 0
Requires:      gem(rspec-its) >= 0
Requires:      gem(timecop) >= 0
Requires:      gem(byebug) >= 0
Requires:      gem(activesupport) >= 5 gem(activesupport) < 7
Requires:      gem(simplecov) >= 0
Requires:      gem(coveralls) >= 0

%description   -n gem-yell-devel
Yell - Your Extensible Logging Library development package.

Yell - Your Extensible Logging Library. Define multiple adapters, various log
level combinations or message formatting options like you've never done before

%description   -n gem-yell-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета yell.


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

%files         -n gem-yell-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-yell-devel
%doc README.md


%changelog
* Mon Oct 31 2022 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- + packaged gem with Ruby Policy 2.0
