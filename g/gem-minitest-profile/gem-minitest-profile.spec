%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname minitest-profile

Name:          gem-minitest-profile
Version:       0.0.2
Release:       alt2
Summary:       Outputter to display the slowest tests in a minitest suite
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/nmeans/minitest-profile
Vcs:           https://github.com/nmeans/minitest-profile.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) >= 5.0
BuildConflicts: gem(minitest) >= 6
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(bundler) >= 1.3
BuildConflicts: gem(bundler) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Provides:      gem(minitest-profile) = 0.0.2


%description
Outputter to display the slowest tests in a minitest suite


%if_enabled    doc
%package       -n gem-minitest-profile-doc
Version:       0.0.2
Release:       alt1
Summary:       Outputter to display the slowest tests in a minitest suite documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-profile
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-profile) = 0.0.2

%description   -n gem-minitest-profile-doc
Outputter to display the slowest tests in a minitest suite documentation files.

%description   -n gem-minitest-profile-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-profile.
%endif


%if_enabled    devel
%package       -n gem-minitest-profile-devel
Version:       0.0.2
Release:       alt1
Summary:       Outputter to display the slowest tests in a minitest suite development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-profile
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-profile) = 0.0.2
Requires:      gem(bundler) >= 1.3
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 5.0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(minitest) >= 6

%description   -n gem-minitest-profile-devel
Outputter to display the slowest tests in a minitest suite development package.

%description   -n gem-minitest-profile-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-profile.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-minitest-profile-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-minitest-profile-devel
%doc README.md
%endif


%changelog
* Sat May 18 2024 Michael Shigorin <mike@altlinux.org> 0.0.2-alt2
- spec: fix BR: --without check

* Tue Apr 23 2024 Pavel Skrylev <majioa@altlinux.org> 0.0.2-alt1
- + packaged gem with Ruby Policy 2.0
