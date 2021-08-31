%define        gemname minitest-moar

Name:          gem-minitest-moar
Version:       0.0.4
Release:       alt1
Summary:       Moar Minitest Please!
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/dockyard/minitest-moar
Vcs:           https://github.com/dockyard/minitest-moar.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.6 gem(bundler) < 3
BuildRequires: gem(rake) >= 10.0 gem(rake) < 14
BuildRequires: gem(minitest) >= 5.1 gem(minitest) < 6

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Provides:      gem(minitest-moar) = 0.0.4


%description
Moar Minitest Please!


%package       -n gem-minitest-moar-doc
Version:       0.0.4
Release:       alt1
Summary:       Moar Minitest Please! documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-moar
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-moar) = 0.0.4

%description   -n gem-minitest-moar-doc
Moar Minitest Please! documentation files.

Moar Minitest Please!

%description   -n gem-minitest-moar-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-moar.


%package       -n gem-minitest-moar-devel
Version:       0.0.4
Release:       alt1
Summary:       Moar Minitest Please! development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-moar
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-moar) = 0.0.4
Requires:      gem(bundler) >= 1.6 gem(bundler) < 3
Requires:      gem(rake) >= 10.0 gem(rake) < 14
Requires:      gem(minitest) >= 5.1 gem(minitest) < 6

%description   -n gem-minitest-moar-devel
Moar Minitest Please! development package.

Moar Minitest Please!

%description   -n gem-minitest-moar-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-moar.


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

%files         -n gem-minitest-moar-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-minitest-moar-devel
%doc README.md


%changelog
* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.4-alt1
- + packaged gem with Ruby Policy 2.0
