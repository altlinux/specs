%define        gemname azure-storage

Name:          gem-azure-storage
Version:       0.15.0
Release:       alt1.2
Summary:       Microsoft Azure Storage Library for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/azure/azure-storage-ruby
Vcs:           https://github.com/azure/azure-storage-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(azure-core) >= 0.1 gem(azure-core) < 1
BuildRequires: gem(faraday) >= 0.9 gem(faraday) < 2
BuildRequires: gem(faraday_middleware) >= 0.10 gem(faraday_middleware) < 2
BuildRequires: gem(nokogiri) >= 1.6.8 gem(nokogiri) < 2
BuildRequires: gem(dotenv) >= 2.0 gem(dotenv) < 3
BuildRequires: gem(minitest) >= 5 gem(minitest) < 6
BuildRequires: gem(minitest-reporters) >= 1 gem(minitest-reporters) < 2
BuildRequires: gem(mocha) >= 1.0 gem(mocha) < 2
BuildRequires: gem(rake) >= 10.0 gem(rake) < 14
BuildRequires: gem(timecop) >= 0.7 gem(timecop) < 1
BuildRequires: gem(yard) >= 0.8 gem(yard) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency faraday >= 0.9,faraday < 2
%ruby_use_gem_dependency faraday_middleware >= 0.10,faraday_middleware < 2
%ruby_use_gem_version %gemname:%version
Requires:      gem(azure-core) >= 0.1 gem(azure-core) < 1
Requires:      gem(faraday) >= 0.9 gem(faraday) < 2
Requires:      gem(faraday_middleware) >= 0.10 gem(faraday_middleware) < 2
Requires:      gem(nokogiri) >= 1.6.8 gem(nokogiri) < 2
Obsoletes:     ruby-azure-storage < %EVR
Provides:      ruby-azure-storage = %EVR
Provides:      azure-storage-ruby = %EVR
Provides:      gem(azure-storage) = 0.15.0


%description
This project provides Ruby packages that makes it easy to access and manage
Microsoft Azure Storage Services.


%package       -n gem-azure-storage-doc
Version:       0.15.0
Release:       alt1.2
Summary:       Microsoft Azure Storage Library for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета azure-storage
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(azure-storage) = 0.15.0

%description   -n gem-azure-storage-doc
Microsoft Azure Storage Library for Ruby documentation files.

This project provides Ruby packages that makes it easy to access and manage
Microsoft Azure Storage Services.

%description   -n gem-azure-storage-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета azure-storage.


%package       -n gem-azure-storage-devel
Version:       0.15.0
Release:       alt1.2
Summary:       Microsoft Azure Storage Library for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета azure-storage
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(azure-storage) = 0.15.0
Requires:      gem(dotenv) >= 2.0 gem(dotenv) < 3
Requires:      gem(minitest) >= 5 gem(minitest) < 6
Requires:      gem(minitest-reporters) >= 1 gem(minitest-reporters) < 2
Requires:      gem(mocha) >= 1.0 gem(mocha) < 2
Requires:      gem(rake) >= 10.0 gem(rake) < 14
Requires:      gem(timecop) >= 0.7 gem(timecop) < 1
Requires:      gem(yard) >= 0.8 gem(yard) < 1

%description   -n gem-azure-storage-devel
Microsoft Azure Storage Library for Ruby development package.

This project provides Ruby packages that makes it easy to access and manage
Microsoft Azure Storage Services.

%description   -n gem-azure-storage-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета azure-storage.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-azure-storage-doc
%ruby_gemdocdir

%files         -n gem-azure-storage-devel


%changelog
* Sun Aug 01 2021 Pavel Skrylev <majioa@altlinux.org> 0.15.0-alt1.2
- ! spec

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.15.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 0.15.0-alt1
- Initial build for Sisyphus
