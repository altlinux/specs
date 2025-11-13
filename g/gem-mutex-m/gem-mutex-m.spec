%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname mutex_m

Name:          gem-mutex-m
Version:       0.3.0
Release:       alt1
Summary:       Mixin to extend objects to be handled like a Mutex
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/mutex_m
Vcs:           https://github.com/ruby/mutex_m.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rbs) >= 3.4
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(test-unit) >= 0
BuildConflicts: gem(rbs) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names mutex_m,mutex-m
Requires:      ruby >= 2.5
Requires:      gem(rbs) >= 3.4
Requires:      gem(rdoc) >= 0
Conflicts:     gem(rbs) >= 4
Provides:      gem(mutex_m) = 0.3.0

%description
Mixin to extend objects to be handled like a Mutex.


%if_enabled    doc
%package       -n gem-mutex-m-doc
Version:       0.3.0
Release:       alt1
Summary:       Mixin to extend objects to be handled like a Mutex documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mutex_m
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mutex_m) = 0.3.0

%description   -n gem-mutex-m-doc
Mixin to extend objects to be handled like a Mutex documentation files.

%description   -n gem-mutex-m-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mutex_m.
%endif


%if_enabled    devel
%package       -n gem-mutex-m-devel
Version:       0.3.0
Release:       alt1
Summary:       Mixin to extend objects to be handled like a Mutex development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mutex_m
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mutex_m) = 0.3.0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0

%description   -n gem-mutex-m-devel
Mixin to extend objects to be handled like a Mutex development package.

%description   -n gem-mutex-m-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mutex_m.
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
%files         -n gem-mutex-m-doc
%doc COPYING README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-mutex-m-devel
%doc COPYING README.md
%endif


%changelog
* Thu Oct 23 2025 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
