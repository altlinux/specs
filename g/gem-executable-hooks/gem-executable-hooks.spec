%define        _unpackaged_files_terminate_build 1
%define        gemname executable-hooks

Name:          gem-executable-hooks
Version:       1.6.1
Release:       alt1
Summary:       Hook into rubygems executables allowing extra actions to be taken before executable is run
License:       Apache 2.0
Group:         Development/Ruby
Url:           https://github.com/rvm/executable-hooks
Vcs:           https://github.com/rvm/executable-hooks.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(tf) >= 0.4
BuildConflicts: gem(tf) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(executable-hooks) = 1.6.1

%ruby_bindir_to %ruby_bindir

%description
Hook into rubygems executables allowing extra actions to be taken before
executable is run.


%package       -n executable-hooks-uninstaller
Version:       1.6.1
Release:       alt1
Summary:       Hook into rubygems executables allowing extra actions to be taken before executable is run executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета executable-hooks
Group:         Other
BuildArch:     noarch

Requires:      gem(executable-hooks) = 1.6.1

%description   -n executable-hooks-uninstaller
Hook into rubygems executables allowing extra actions to be taken before
executable is run executable(s).

%description   -n executable-hooks-uninstaller -l ru_RU.UTF-8
Исполнямка для самоцвета executable-hooks.


%package       -n gem-executable-hooks-doc
Version:       1.6.1
Release:       alt1
Summary:       Hook into rubygems executables allowing extra actions to be taken before executable is run documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета executable-hooks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(executable-hooks) = 1.6.1

%description   -n gem-executable-hooks-doc
Hook into rubygems executables allowing extra actions to be taken before
executable is run documentation files.

%description   -n gem-executable-hooks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета executable-hooks.


%package       -n gem-executable-hooks-devel
Version:       1.6.1
Release:       alt1
Summary:       Hook into rubygems executables allowing extra actions to be taken before executable is run development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета executable-hooks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(executable-hooks) = 1.6.1
Requires:      gem(tf) >= 0.4
Conflicts:     gem(tf) >= 1

%description   -n gem-executable-hooks-devel
Hook into rubygems executables allowing extra actions to be taken before
executable is run development package.

%description   -n gem-executable-hooks-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета executable-hooks.


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
%ruby_gemextdir

%files         -n executable-hooks-uninstaller
%doc README.md
%ruby_bindir/executable-hooks-uninstaller

%files         -n gem-executable-hooks-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-executable-hooks-devel
%doc README.md


%changelog
* Wed Nov 22 2023 Pavel Skrylev <majioa@altlinux.org> 1.6.1-alt1
- + packaged gem with Ruby Policy 2.0
