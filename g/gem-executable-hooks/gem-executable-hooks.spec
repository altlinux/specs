%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname executable-hooks

Name:          gem-executable-hooks
Version:       1.7.1.2
Release:       alt0.1
Summary:       Hook into rubygems executables allowing extra actions to be taken before executable is run
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/rvm/executable-hooks
Vcs:           https://github.com/rvm/executable-hooks.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(tf) >= 0.4
BuildConflicts: gem(tf) >= 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      executable-hooks = %EVR
Provides:      gem(executable-hooks) = 1.7.1.2

%description
Hook into rubygems executables allowing extra actions to be taken before
executable is run.

%ruby_use_gem_version executable-hooks:1.7.1.2

%package       -n executable-hooks-uninstaller
Version:       1.7.1.2
Release:       alt0.1
Summary:       Hook into rubygems executables allowing extra actions to be taken before executable is run executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета executable-hooks
Group:         Other
BuildArch:     noarch

Requires:      gem(executable-hooks) = 1.7.1.2

%description   -n executable-hooks-uninstaller
Hook into rubygems executables allowing extra actions to be taken before
executable is run executable(s).

%description   -n executable-hooks-uninstaller -l ru_RU.UTF-8
Исполнямка для самоцвета executable-hooks.


%if_enabled    doc
%package       -n gem-executable-hooks-doc
Version:       1.7.1.2
Release:       alt0.1
Summary:       Hook into rubygems executables allowing extra actions to be taken before executable is run documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета executable-hooks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(executable-hooks) = 1.7.1.2

%description   -n gem-executable-hooks-doc
Hook into rubygems executables allowing extra actions to be taken before
executable is run documentation files.

%description   -n gem-executable-hooks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета executable-hooks.
%endif


%if_enabled    devel
%package       -n gem-executable-hooks-devel
Version:       1.7.1.2
Release:       alt0.1
Summary:       Hook into rubygems executables allowing extra actions to be taken before executable is run development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета executable-hooks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(executable-hooks) = 1.7.1.2
Requires:      gem(tf) >= 0.4
Conflicts:     gem(tf) >= 1

%description   -n gem-executable-hooks-devel
Hook into rubygems executables allowing extra actions to be taken before
executable is run development package.

%description   -n gem-executable-hooks-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета executable-hooks.
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
%doc CHANGELOG.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir
%ruby_gemplugin

%files         -n executable-hooks-uninstaller
%doc CHANGELOG.md LICENSE README.md
%_bindir/executable-hooks-uninstaller
%_bindir/ruby_executable_hooks

%if_enabled    doc
%files         -n gem-executable-hooks-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-executable-hooks-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Wed Mar 26 2025 Pavel Skrylev <majioa@altlinux.org> 1.7.1.2-alt0.1
- ^ 1.7.1p1 -> 1.7.1p2
- ! added ruby_executable_hooks to gems executables with proper rights

* Fri Dec 13 2024 Pavel Skrylev <majioa@altlinux.org> 1.7.1.1-alt0.1
- ^ 1.7.1 -> 1.7.1p1
- ! fixed build for spec
- ! closes wrapper installation in rescue clause

* Fri Mar 15 2024 Pavel Skrylev <majioa@altlinux.org> 1.7.1-alt1
- ^ 1.6.1 -> 1.7.1

* Wed Nov 22 2023 Pavel Skrylev <majioa@altlinux.org> 1.6.1-alt1
- + packaged gem with Ruby Policy 2.0
