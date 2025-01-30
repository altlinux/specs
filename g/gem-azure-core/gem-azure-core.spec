%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname azure-core

Name:          gem-azure-core
Version:       0.1.15.3
Release:       alt0.1
Summary:       Azure Ruby SDK Service Management Core HTTP
License:       Apache License, Version 2.0
Group:         Development/Ruby
Url:           https://github.com/Azure/azure-ruby-asm-core
Vcs:           https://github.com/azure/azure-ruby-asm-core.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.11
BuildRequires: gem(dotenv) >= 2.0
BuildRequires: gem(faraday) >= 0.9
BuildRequires: gem(faraday_middleware) >= 0.10
BuildRequires: gem(minitest) >= 5
BuildRequires: gem(minitest-reporters) >= 1
BuildRequires: gem(mocha) >= 1.0
BuildRequires: gem(nokogiri) >= 1.6
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(timecop) >= 0.7
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(dotenv) >= 3
BuildConflicts: gem(faraday) >= 3
BuildConflicts: gem(faraday_middleware) >= 2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(minitest-reporters) >= 2
BuildConflicts: gem(mocha) >= 3
BuildConflicts: gem(nokogiri) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(timecop) >= 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency faraday_middleware >= 1.2.0,faraday_middleware < 2
%ruby_use_gem_dependency mocha >= 2.0,mocha < 3
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency faraday >= 2.6.0,faraday < 3
Requires:      ruby >= 1.9.3
Requires:      gem(faraday) >= 0.9
Requires:      gem(faraday_middleware) >= 0.10
Requires:      gem(nokogiri) >= 1.6
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(faraday_middleware) >= 2
Conflicts:     gem(nokogiri) >= 2
Obsoletes:     ruby-azure-core < %EVR
Provides:      ruby-azure-core = %EVR
Provides:      azure-core = %EVR
Provides:      gem(azure-core) = 0.1.15.3

%ruby_use_gem_version azure-core:0.1.15.3

%description
This project provides a Ruby package with core functionality consumed by Azure
SDK gems.


%if_enabled    doc
%package       -n gem-azure-core-doc
Version:       0.1.15.3
Release:       alt0.1
Summary:       Azure Ruby SDK Service Management Core HTTP documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета azure-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(azure-core) = 0.1.15.3

%description   -n gem-azure-core-doc
Azure Ruby SDK Service Management Core HTTP documentation files.

This project provides a Ruby package with core functionality consumed by Azure
SDK gems.

%description   -n gem-azure-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета azure-core.
%endif


%if_enabled    devel
%package       -n gem-azure-core-devel
Version:       0.1.15.3
Release:       alt0.1
Summary:       Azure Ruby SDK Service Management Core HTTP development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета azure-core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(azure-core) = 0.1.15.3
Requires:      gem(bundler) >= 1.11
Requires:      gem(dotenv) >= 2.0
Requires:      gem(minitest) >= 5
Requires:      gem(minitest-reporters) >= 1
Requires:      gem(mocha) >= 1.0
Requires:      gem(rake) >= 10.0
Requires:      gem(timecop) >= 0.7
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(dotenv) >= 3
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-reporters) >= 2
Conflicts:     gem(mocha) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(timecop) >= 1

%description   -n gem-azure-core-devel
Azure Ruby SDK Service Management Core HTTP development package.

This project provides a Ruby package with core functionality consumed by Azure
SDK gems.

%description   -n gem-azure-core-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета azure-core.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc ChangeLog.md README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-azure-core-doc
%doc ChangeLog.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-azure-core-devel
%doc ChangeLog.md README.md
%endif


%changelog
* Mon Jan 27 2025 Pavel Skrylev <majioa@altlinux.org> 0.1.15.3-alt0.1
- ^ 0.1.15 -> 0.1.15p3

* Thu Oct 20 2022 Pavel Skrylev <majioa@altlinux.org> 0.1.15-alt1.1
- !fix build deps to novel gems

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
