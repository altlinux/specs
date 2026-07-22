%define        _unpackaged_files_terminate_build 1
%def_disable    check
%def_enable    doc
%def_enable    devel
%define        gemname guard-bundler

Name:          gem-guard-bundler
Version:       3.1.0
Release:       alt1
Summary:       Guard gem for Bundler
License:       MIT
Group:         Development/Ruby
Url:           https://rubygems.org/gems/guard-bundler
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 2.1
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(guard) >= 2.2
BuildRequires: gem(guard-compat) >= 1.1
BuildRequires: gem(guard-rspec) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(ruby_gntp) >= 0
BuildConflicts: gem(bundler) >= 5
BuildConflicts: gem(guard) >= 3
BuildConflicts: gem(guard-compat) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.4.9
Requires:      gem(bundler) >= 2.1
Requires:      gem(guard) >= 2.2
Requires:      gem(guard-compat) >= 1.1
Conflicts:     gem(bundler) >= 5
Conflicts:     gem(guard) >= 3
Conflicts:     gem(guard-compat) >= 2
Provides:      gem(guard-bundler) = 3.1.0

%description
Guard::Bundler automatically install/update your gem bundle when needed


%if_enabled    doc
%package       -n gem-guard-bundler-doc
Version:       3.1.0
Release:       alt1
Summary:       Guard gem for Bundler documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета guard-bundler
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(guard-bundler) = 3.1.0

%description   -n gem-guard-bundler-doc
Guard gem for Bundler documentation files.

Guard::Bundler automatically install/update your gem bundle when needed

%description   -n gem-guard-bundler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета guard-bundler.
%endif


%if_enabled    devel
%package       -n gem-guard-bundler-devel
Version:       3.1.0
Release:       alt1
Summary:       Guard gem for Bundler development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета guard-bundler
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(guard-bundler) = 3.1.0
Requires:      gem(coveralls) >= 0
Requires:      gem(guard-rspec) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(ruby_gntp) >= 0

%description   -n gem-guard-bundler-devel
Guard gem for Bundler development package.

Guard::Bundler automatically install/update your gem bundle when needed

%description   -n gem-guard-bundler-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета guard-bundler.
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
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-guard-bundler-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-guard-bundler-devel
%doc LICENSE README.md
%endif


%changelog
* Tue Jul 07 2026 Alexander Burmatov <thatman@altlinux.org> 3.1.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
