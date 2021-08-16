%define        gemname azure-core

Name:          gem-azure-core
Version:       0.1.15
Release:       alt1
Summary:       Azure Ruby SDK Service Management Core HTTP
License:       Apache License, Version 2.0
Group:         Development/Ruby
Url:           https://github.com/Azure/azure-ruby-asm-core
Vcs:           https://github.com/azure/azure-ruby-asm-core.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(faraday) >= 0.9 gem(faraday) < 2
BuildRequires: gem(faraday_middleware) >= 0.10 gem(faraday_middleware) < 2
BuildRequires: gem(nokogiri) >= 1.6 gem(nokogiri) < 2
BuildRequires: gem(dotenv) >= 2.0 gem(dotenv) < 3
BuildRequires: gem(minitest) >= 5 gem(minitest) < 6
BuildRequires: gem(minitest-reporters) >= 1 gem(minitest-reporters) < 2
BuildRequires: gem(mocha) >= 1.0 gem(mocha) < 2
BuildRequires: gem(rake) >= 10.0 gem(rake) < 14
BuildRequires: gem(timecop) >= 0.7 gem(timecop) < 1
BuildRequires: gem(bundler) >= 1.11 gem(bundler) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency faraday >= 0.9,faraday < 2
%ruby_use_gem_dependency faraday_middleware >= 0.10,faraday_middleware < 2
Requires:      gem(faraday) >= 0.9 gem(faraday) < 2
Requires:      gem(faraday_middleware) >= 0.10 gem(faraday_middleware) < 2
Requires:      gem(nokogiri) >= 1.6 gem(nokogiri) < 2
Obsoletes:     ruby-azure-core < %EVR
Provides:      ruby-azure-core = %EVR
Provides:      gem(azure-core) = 0.1.15


%description
This project provides a Ruby package with core functionality consumed by Azure
SDK gems.


%package       -n gem-azure-core-doc
Version:       0.1.15
Release:       alt1
Summary:       Azure Ruby SDK Service Management Core HTTP documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета azure-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(azure-core) = 0.1.15

%description   -n gem-azure-core-doc
Azure Ruby SDK Service Management Core HTTP documentation files.

This project provides a Ruby package with core functionality consumed by Azure
SDK gems.

%description   -n gem-azure-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета azure-core.


%package       -n gem-azure-core-devel
Version:       0.1.15
Release:       alt1
Summary:       Azure Ruby SDK Service Management Core HTTP development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета azure-core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(azure-core) = 0.1.15
Requires:      gem(dotenv) >= 2.0 gem(dotenv) < 3
Requires:      gem(minitest) >= 5 gem(minitest) < 6
Requires:      gem(minitest-reporters) >= 1 gem(minitest-reporters) < 2
Requires:      gem(mocha) >= 1.0 gem(mocha) < 2
Requires:      gem(rake) >= 10.0 gem(rake) < 14
Requires:      gem(timecop) >= 0.7 gem(timecop) < 1
Requires:      gem(bundler) >= 1.11 gem(bundler) < 3

%description   -n gem-azure-core-devel
Azure Ruby SDK Service Management Core HTTP development package.

This project provides a Ruby package with core functionality consumed by Azure
SDK gems.

%description   -n gem-azure-core-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета azure-core.


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

%files         -n gem-azure-core-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-azure-core-devel
%doc README.md


%changelog
* Thu Aug 05 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.15-alt1
- ^ 0.1.14 -> 0.1.15

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.14-alt2.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 08 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.14-alt2
- Disable tests.

* Mon Jan 01 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.14-alt1
- New version.

* Wed Sep 13 2017 Andrey Cherepanov <cas@altlinux.org> 0.1.12-alt1
- New version

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 0.1.11-alt1
- Initial build for Sisyphus
