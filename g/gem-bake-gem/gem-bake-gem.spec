%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname bake-gem

Name:          gem-bake-gem
Version:       0.10.0
Release:       alt1
Summary:       Release management for Ruby gems
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ioquatix/bake-gem
Vcs:           https://github.com/ioquatix/bake-gem.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(console) >= 1.25
BuildConflicts: gem(console) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.1
Requires:      gem(console) >= 1.25
Conflicts:     gem(console) >= 2
Provides:      gem(bake-gem) = 0.10.0

%description
Release management for Ruby gems.


%if_enabled    doc
%package       -n gem-bake-gem-doc
Version:       0.10.0
Release:       alt1
Summary:       Release management for Ruby gems documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bake-gem
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bake-gem) = 0.10.0

%description   -n gem-bake-gem-doc
Release management for Ruby gems documentation files.

%description   -n gem-bake-gem-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bake-gem.
%endif


%if_enabled    devel
%package       -n gem-bake-gem-devel
Version:       0.10.0
Release:       alt1
Summary:       Release management for Ruby gems development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bake-gem
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bake-gem) = 0.10.0

%description   -n gem-bake-gem-devel
Release management for Ruby gems development package.

%description   -n gem-bake-gem-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bake-gem.
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
%doc license.md readme.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-bake-gem-doc
%doc license.md readme.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-bake-gem-devel
%doc license.md readme.md
%endif


%changelog
* Fri Jul 11 2025 Pavel Skrylev <majioa@altlinux.org> 0.10.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
