%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname pstore

Name:          gem-pstore
Version:       0.2.1
Release:       alt1
Summary:       Transactional File Storage for Ruby Objects
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/pstore
Vcs:           https://github.com/ruby/pstore.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(test-unit-ruby-core) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(pstore) = 0.2.1

%description
Transactional File Storage for Ruby Objects


%if_enabled    doc
%package       -n gem-pstore-doc
Version:       0.2.1
Release:       alt1
Summary:       Transactional File Storage for Ruby Objects documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pstore
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pstore) = 0.2.1

%description   -n gem-pstore-doc
Transactional File Storage for Ruby Objects documentation files.

%description   -n gem-pstore-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pstore.
%endif


%if_enabled    devel
%package       -n gem-pstore-devel
Version:       0.2.1
Release:       alt1
Summary:       Transactional File Storage for Ruby Objects development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pstore
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pstore) = 0.2.1
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(test-unit-ruby-core) >= 0

%description   -n gem-pstore-devel
Transactional File Storage for Ruby Objects development package.

%description   -n gem-pstore-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pstore.
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
%doc COPYING README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-pstore-doc
%doc COPYING README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-pstore-devel
%doc COPYING README.md
%endif


%changelog
* Fri Aug 14 2026 Pavel Skrylev <majioa@altlinux.org> 0.2.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
