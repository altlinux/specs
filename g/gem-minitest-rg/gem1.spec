%define        gemname minitest-rg

Name:          gem-minitest-rg
Version:       5.2.0
Release:       alt1
Summary:       Red/Green for MiniTest
License:       MIT
Group:         Development/Ruby
Url:           http://blowmage.com/minitest-rg
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) >= 5.0 gem(minitest) < 6
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7
BuildRequires: gem(hoe) >= 3.13 gem(hoe) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_version minitest-rg:5.2.0
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6
Provides:      gem(minitest-rg) = 5.2.0


%description
Colored red/green output for Minitest


%package       -n gem-minitest-rg-doc
Version:       5.2.0
Release:       alt1
Summary:       Red/Green for MiniTest documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-rg
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-rg) = 5.2.0

%description   -n gem-minitest-rg-doc
Red/Green for MiniTest documentation files.

Colored red/green output for Minitest

%description   -n gem-minitest-rg-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-rg.


%package       -n gem-minitest-rg-devel
Version:       5.2.0
Release:       alt1
Summary:       Red/Green for MiniTest development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-rg
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-rg) = 5.2.0
Requires:      gem(rdoc) >= 4.0 gem(rdoc) < 7
Requires:      gem(hoe) >= 3.13 gem(hoe) < 4

%description   -n gem-minitest-rg-devel
Red/Green for MiniTest development package.

Colored red/green output for Minitest

%description   -n gem-minitest-rg-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-rg.


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

%files         -n gem-minitest-rg-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-minitest-rg-devel
%doc README.rdoc


%changelog
* Thu Jul 15 2021 Pavel Skrylev <majioa@altlinux.org> 5.2.0-alt1
- + packaged gem with Ruby Policy 2.0
