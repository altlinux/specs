%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname guard-compat

Name:          gem-guard-compat
Version:       1.2.1
Release:       alt1
Summary:       Tools for developing Guard compatible plugins
License:       MIT
Group:         Development/Ruby
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.7
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubocop) >= 0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.5.9,bundler < 3
%ruby_use_gem_dependency rake >= 13.3.1,rake < 14
Provides:      gem(guard-compat) = 1.2.1

%description
Helps creating valid Guard plugins and testing them


%if_enabled    doc
%package       -n gem-guard-compat-doc
Version:       1.2.1
Release:       alt1
Summary:       Tools for developing Guard compatible plugins documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета guard-compat
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(guard-compat) = 1.2.1

%description   -n gem-guard-compat-doc
Tools for developing Guard compatible plugins documentation files.

Helps creating valid Guard plugins and testing them

%description   -n gem-guard-compat-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета guard-compat.
%endif


%if_enabled    devel
%package       -n gem-guard-compat-devel
Version:       1.2.1
Release:       alt1
Summary:       Tools for developing Guard compatible plugins development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета guard-compat
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(guard-compat) = 1.2.1
Requires:      gem(bundler) >= 1.7
Requires:      gem(rake) >= 10.0
Requires:      gem(rspec) >= 0
Requires:      gem(rubocop) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake) >= 14

%description   -n gem-guard-compat-devel
Tools for developing Guard compatible plugins development package.

Helps creating valid Guard plugins and testing them

%description   -n gem-guard-compat-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета guard-compat.
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
%doc LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-guard-compat-doc
%doc LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-guard-compat-devel
%doc LICENSE.txt README.md
%endif


%changelog
* Tue Jul 07 2026 Alexander Burmatov <thatman@altlinux.org> 1.2.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
