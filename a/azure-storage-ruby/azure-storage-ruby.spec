%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc

Name:          azure-storage-ruby
Version:       0.20240423
Release:       alt1
Summary:       Microsoft Azure Storage Library for Ruby
License:       MIT
Group:         Development/Ruby
Url:           http://azure.github.io/azure-storage-ruby/
Vcs:           https://github.com/Azure/azure-storage-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(faraday) >= 1.0
BuildRequires: gem(faraday_middleware) >= 1.0.0
BuildRequires: gem(net-http-persistent) >= 4.0
BuildRequires: gem(nokogiri) >= 1.12.5
BuildRequires: gem(adal) >= 1.0
BuildRequires: gem(dotenv) >= 2.0
BuildRequires: gem(minitest) >= 5
BuildRequires: gem(minitest-reporters) >= 1
BuildRequires: gem(mocha) >= 1.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(timecop) >= 0.7
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(bundler) >= 1.11
BuildConflicts: gem(faraday) >= 3
BuildConflicts: gem(faraday_middleware) >= 2
BuildConflicts: gem(net-http-persistent) >= 5
BuildConflicts: gem(nokogiri) >= 2
BuildConflicts: gem(adal) >= 2
BuildConflicts: gem(dotenv) >= 3
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(minitest-reporters) >= 2
BuildConflicts: gem(mocha) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(timecop) >= 1
BuildConflicts: gem(bundler) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency faraday >= 2.6.0,faraday < 3
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
%ruby_use_gem_dependency faraday_middleware >= 1.2.0,faraday_middleware < 2
Requires:      gem(faraday) >= 1.0
Requires:      gem(faraday_middleware) >= 1.0.0
Requires:      gem(net-http-persistent) >= 4.0
Requires:      gem(nokogiri) >= 1.12.5
Requires:      gem(adal) >= 1.0
Requires:      gem(dotenv) >= 2.0
Requires:      gem(minitest) >= 5
Requires:      gem(minitest-reporters) >= 1
Requires:      gem(mocha) >= 1.0
Requires:      gem(rake) >= 13.0
Requires:      gem(timecop) >= 0.7
Requires:      gem(yard) >= 0.9
Requires:      gem(coveralls) >= 0
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(faraday_middleware) >= 2
Conflicts:     gem(net-http-persistent) >= 5
Conflicts:     gem(nokogiri) >= 2
Conflicts:     gem(adal) >= 2
Conflicts:     gem(dotenv) >= 3
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-reporters) >= 2
Conflicts:     gem(mocha) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(timecop) >= 1
Provides:      ruby-azure-storage-ruby

%ruby_ignore_names azure-storage-ruby

%description
This project provides Ruby packages that makes it easy to access and manage
Microsoft Azure Storage Services.


%package       -n gem-azure-storage-blob
Version:       2.0.2
Release:       alt1
Summary:       Official Ruby client library to consume Azure Storage Blob service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(azure-storage-common) >= 2.0
Requires:      gem(nokogiri) >= 1.12.5
Conflicts:     gem(azure-storage-common) >= 3
Conflicts:     gem(nokogiri) >= 2
Provides:      gem(azure-storage-blob) = 2.0.2

%description   -n gem-azure-storage-blob
Microsoft Azure Storage Blob Client Library for Ruby


%if_enabled    doc
%package       -n azure-storage-blob-doc
Version:       2.0.2
Release:       alt1
Summary:       Official Ruby client library to consume Azure Storage Blob service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета azure-storage-blob
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(azure-storage-blob) = 2.0.2

%description   -n azure-storage-blob-doc
Official Ruby client library to consume Azure Storage Blob service documentation
files.

Microsoft Azure Storage Blob Client Library for Ruby

%description   -n azure-storage-blob-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета azure-storage-blob.
%endif


%if_enabled    devel
%package       -n azure-storage-blob-devel
Version:       2.0.2
Release:       alt1
Summary:       Official Ruby client library to consume Azure Storage Blob service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета azure-storage-blob
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(azure-storage-blob) = 2.0.2
Requires:      gem(dotenv) >= 2.0
Requires:      gem(minitest) >= 5
Requires:      gem(minitest-reporters) >= 1
Requires:      gem(mocha) >= 1.0
Requires:      gem(rake) >= 13.0
Requires:      gem(timecop) >= 0.7
Requires:      gem(yard) >= 0.9
Requires:      gem(coveralls) >= 0
Conflicts:     gem(dotenv) >= 3
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-reporters) >= 2
Conflicts:     gem(mocha) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(timecop) >= 1

%description   -n azure-storage-blob-devel
Official Ruby client library to consume Azure Storage Blob service development
package.

Microsoft Azure Storage Blob Client Library for Ruby

%description   -n azure-storage-blob-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета azure-storage-blob.
%endif


%package       -n gem-azure-storage-file
Version:       2.0.3
Release:       alt1
Summary:       Official Ruby client library to consume Azure Storage File service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(azure-storage-common) >= 2.0
Requires:      gem(nokogiri) >= 1.12.5
Conflicts:     gem(azure-storage-common) >= 3
Conflicts:     gem(nokogiri) >= 2
Provides:      gem(azure-storage-file) = 2.0.3

%description   -n gem-azure-storage-file
Microsoft Azure Storage File Client Library for Ruby


%if_enabled    doc
%package       -n azure-storage-file-doc
Version:       2.0.3
Release:       alt1
Summary:       Official Ruby client library to consume Azure Storage File service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета azure-storage-file
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(azure-storage-file) = 2.0.3

%description   -n azure-storage-file-doc
Official Ruby client library to consume Azure Storage File service documentation
files.

Microsoft Azure Storage File Client Library for Ruby

%description   -n azure-storage-file-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета azure-storage-file.
%endif


%if_enabled    devel
%package       -n azure-storage-file-devel
Version:       2.0.3
Release:       alt1
Summary:       Official Ruby client library to consume Azure Storage File service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета azure-storage-file
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(azure-storage-file) = 2.0.3
Requires:      gem(dotenv) >= 2.0
Requires:      gem(minitest) >= 5
Requires:      gem(minitest-reporters) >= 1
Requires:      gem(mocha) >= 1.0
Requires:      gem(rake) >= 13.0
Requires:      gem(timecop) >= 0.7
Requires:      gem(yard) >= 0.9
Requires:      gem(coveralls) >= 0
Conflicts:     gem(dotenv) >= 3
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-reporters) >= 2
Conflicts:     gem(mocha) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(timecop) >= 1

%description   -n azure-storage-file-devel
Official Ruby client library to consume Azure Storage File service development
package.

Microsoft Azure Storage File Client Library for Ruby

%description   -n azure-storage-file-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета azure-storage-file.
%endif


%package       -n gem-azure-storage-queue
Version:       2.0.3
Release:       alt1
Summary:       Official Ruby client library to consume Azure Storage Queue service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(azure-storage-common) >= 2.0
Requires:      gem(nokogiri) >= 1.12.5
Conflicts:     gem(azure-storage-common) >= 3
Conflicts:     gem(nokogiri) >= 2
Provides:      gem(azure-storage-queue) = 2.0.3

%description   -n gem-azure-storage-queue
Microsoft Azure Storage Queue Client Library for Ruby


%if_enabled    doc
%package       -n azure-storage-queue-doc
Version:       2.0.3
Release:       alt1
Summary:       Official Ruby client library to consume Azure Storage Queue service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета azure-storage-queue
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(azure-storage-queue) = 2.0.3

%description   -n azure-storage-queue-doc
Official Ruby client library to consume Azure Storage Queue service
documentation files.

Microsoft Azure Storage Queue Client Library for Ruby

%description   -n azure-storage-queue-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета azure-storage-queue.
%endif


%if_enabled    devel
%package       -n azure-storage-queue-devel
Version:       2.0.3
Release:       alt1
Summary:       Official Ruby client library to consume Azure Storage Queue service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета azure-storage-queue
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(azure-storage-queue) = 2.0.3
Requires:      gem(dotenv) >= 2.0
Requires:      gem(minitest) >= 5
Requires:      gem(minitest-reporters) >= 1
Requires:      gem(mocha) >= 1.0
Requires:      gem(rake) >= 13.0
Requires:      gem(timecop) >= 0.7
Requires:      gem(yard) >= 0.9
Conflicts:     gem(dotenv) >= 3
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-reporters) >= 2
Conflicts:     gem(mocha) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(timecop) >= 1

%description   -n azure-storage-queue-devel
Official Ruby client library to consume Azure Storage Queue service development
package.

Microsoft Azure Storage Queue Client Library for Ruby

%description   -n azure-storage-queue-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета azure-storage-queue.
%endif


%package       -n gem-azure-storage-table
Version:       2.0.3
Release:       alt1
Summary:       Official Ruby client library to consume Azure Storage Table service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(azure-storage-common) >= 2.0
Requires:      gem(nokogiri) >= 1.12.5
Conflicts:     gem(azure-storage-common) >= 3
Conflicts:     gem(nokogiri) >= 2
Provides:      gem(azure-storage-table) = 2.0.3

%description   -n gem-azure-storage-table
Microsoft Azure Storage Table Client Library for Ruby


%if_enabled    doc
%package       -n azure-storage-table-doc
Version:       2.0.3
Release:       alt1
Summary:       Official Ruby client library to consume Azure Storage Table service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета azure-storage-table
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(azure-storage-table) = 2.0.3

%description   -n azure-storage-table-doc
Official Ruby client library to consume Azure Storage Table service
documentation files.

Microsoft Azure Storage Table Client Library for Ruby

%description   -n azure-storage-table-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета azure-storage-table.
%endif


%if_enabled    devel
%package       -n azure-storage-table-devel
Version:       2.0.3
Release:       alt1
Summary:       Official Ruby client library to consume Azure Storage Table service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета azure-storage-table
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(azure-storage-table) = 2.0.3
Requires:      gem(dotenv) >= 2.0
Requires:      gem(minitest) >= 5
Requires:      gem(minitest-reporters) >= 1
Requires:      gem(mocha) >= 1.0
Requires:      gem(rake) >= 13.0
Requires:      gem(timecop) >= 0.7
Requires:      gem(yard) >= 0.9
Requires:      gem(coveralls) >= 0
Conflicts:     gem(dotenv) >= 3
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-reporters) >= 2
Conflicts:     gem(mocha) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(timecop) >= 1

%description   -n azure-storage-table-devel
Official Ruby client library to consume Azure Storage Table service development
package.

Microsoft Azure Storage Table Client Library for Ruby

%description   -n azure-storage-table-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета azure-storage-table.
%endif


%package       -n gem-azure-storage-common
Version:       2.0.3
Release:       alt1
Summary:       Official Ruby client library to consume Azure Storage Common service
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(faraday) >= 1.0
Requires:      gem(faraday_middleware) >= 1.0.0
Requires:      gem(net-http-persistent) >= 4.0
Requires:      gem(nokogiri) >= 1.12.5
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(faraday_middleware) >= 2
Conflicts:     gem(net-http-persistent) >= 5
Conflicts:     gem(nokogiri) >= 2
Provides:      gem(azure-storage-common) = 2.0.3

%description   -n gem-azure-storage-common
Microsoft Azure Storage Common Client Library for Ruby


%if_enabled    doc
%package       -n azure-storage-common-doc
Version:       2.0.3
Release:       alt1
Summary:       Official Ruby client library to consume Azure Storage Common service documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета azure-storage-common
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(azure-storage-common) = 2.0.3

%description   -n azure-storage-common-doc
Official Ruby client library to consume Azure Storage Common service
documentation files.

Microsoft Azure Storage Common Client Library for Ruby

%description   -n azure-storage-common-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета azure-storage-common.
%endif


%if_enabled    devel
%package       -n azure-storage-common-devel
Version:       2.0.3
Release:       alt1
Summary:       Official Ruby client library to consume Azure Storage Common service development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета azure-storage-common
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(azure-storage-common) = 2.0.3
Requires:      gem(dotenv) >= 2.0
Requires:      gem(minitest) >= 5
Requires:      gem(minitest-reporters) >= 1
Requires:      gem(mocha) >= 1.0
Requires:      gem(rake) >= 13.0
Requires:      gem(timecop) >= 0.7
Requires:      gem(yard) >= 0.9
Requires:      gem(bundler) >= 1.11
Requires:      gem(coveralls) >= 0
Conflicts:     gem(dotenv) >= 3
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-reporters) >= 2
Conflicts:     gem(mocha) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(timecop) >= 1
Conflicts:     gem(bundler) >= 3

%description   -n azure-storage-common-devel
Official Ruby client library to consume Azure Storage Common service development
package.

Microsoft Azure Storage Common Client Library for Ruby

%description   -n azure-storage-common-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета azure-storage-common.
%endif


%if_enabled    devel
%package       -n azure-storage-ruby-devel
Version:       0.20240423
Release:       alt1
Summary:       Microsoft Azure Storage Library for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета azure-storage-ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      azure-storage-blob-devel
Requires:      azure-storage-table-devel
Requires:      azure-storage-queue-devel
Requires:      azure-storage-file-devel
Requires:      azure-storage-common-devel

%description   -n azure-storage-ruby-devel
Microsoft Azure Storage Library for Ruby development package.

%description   -n azure-storage-ruby-devel -l ru_RU.UTF-8
Файлы для разработки azure-storage-ruby.
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

%files         -n gem-azure-storage-blob
%ruby_gemspecdir/azure-storage-blob-2.0.2.gemspec
%ruby_gemslibdir/azure-storage-blob-2.0.2

%if_enabled    doc
%files         -n azure-storage-blob-doc
%ruby_gemsdocdir/azure-storage-blob-2.0.2
%endif

%if_enabled    devel
%files         -n azure-storage-blob-devel
%endif

%files         -n gem-azure-storage-file
%ruby_gemspecdir/azure-storage-file-2.0.3.gemspec
%ruby_gemslibdir/azure-storage-file-2.0.3

%if_enabled    doc
%files         -n azure-storage-file-doc
%ruby_gemsdocdir/azure-storage-file-2.0.3
%endif

%if_enabled    devel
%files         -n azure-storage-file-devel
%endif

%files         -n gem-azure-storage-queue
%ruby_gemspecdir/azure-storage-queue-2.0.3.gemspec
%ruby_gemslibdir/azure-storage-queue-2.0.3

%if_enabled    doc
%files         -n azure-storage-queue-doc
%ruby_gemsdocdir/azure-storage-queue-2.0.3
%endif

%if_enabled    devel
%files         -n azure-storage-queue-devel
%endif

%files         -n gem-azure-storage-table
%ruby_gemspecdir/azure-storage-table-2.0.3.gemspec
%ruby_gemslibdir/azure-storage-table-2.0.3

%if_enabled    doc
%files         -n azure-storage-table-doc
%ruby_gemsdocdir/azure-storage-table-2.0.3
%endif

%if_enabled    devel
%files         -n azure-storage-table-devel
%endif

%files         -n gem-azure-storage-common
%ruby_gemspecdir/azure-storage-common-2.0.3.gemspec
%ruby_gemslibdir/azure-storage-common-2.0.3

%if_enabled    doc
%files         -n azure-storage-common-doc
%ruby_gemsdocdir/azure-storage-common-2.0.3
%endif

%if_enabled    devel
%files         -n azure-storage-common-devel
%endif

%if_enabled    devel
%files         -n azure-storage-ruby-devel
%endif


%changelog
* Tue Apr 23 2024 Pavel Skrylev <majioa@altlinux.org> 0.20240423-alt1
- + packaged gem with Ruby Policy 2.0
