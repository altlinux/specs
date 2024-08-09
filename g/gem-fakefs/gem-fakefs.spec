%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname fakefs

Name:          gem-fakefs
Version:       2.5.0
Release:       alt1
Summary:       A fake filesystem. Use it in your tests
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fakefs/fakefs
Vcs:           https://github.com/fakefs/fakefs.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bump) >= 0.5.3
BuildRequires: gem(maxitest) >= 3.6
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 10.3
BuildRequires: gem(rspec) >= 3.1
BuildRequires: gem(rubocop) >= 0.82.0
BuildConflicts: gem(bump) >= 1
BuildConflicts: gem(maxitest) >= 4
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency bump >= 0.8,bump < 1
Provides:      gem(fakefs) = 2.5.0


%description
A fake filesystem. Use it in your tests.


%if_enabled    doc
%package       -n gem-fakefs-doc
Version:       2.5.0
Release:       alt1
Summary:       A fake filesystem. Use it in your tests documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fakefs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fakefs) = 2.5.0

%description   -n gem-fakefs-doc
A fake filesystem. Use it in your tests documentation files.

%description   -n gem-fakefs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fakefs.
%endif


%if_enabled    devel
%package       -n gem-fakefs-devel
Version:       2.5.0
Release:       alt1
Summary:       A fake filesystem. Use it in your tests development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fakefs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fakefs) = 2.5.0
Requires:      gem(bump) >= 0.5.3
Requires:      gem(maxitest) >= 3.6
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 10.3
Requires:      gem(rspec) >= 3.1
Requires:      gem(rubocop) >= 0.82.0
Conflicts:     gem(bump) >= 1
Conflicts:     gem(maxitest) >= 4
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2

%description   -n gem-fakefs-devel
A fake filesystem. Use it in your tests development package.

%description   -n gem-fakefs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fakefs.
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
%files         -n gem-fakefs-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-fakefs-devel
%doc README.md
%endif


%changelog
* Sat Aug 03 2024 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt1
- ^ 1.9.0 -> 2.5.0

* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 1.9.0-alt1
- ^ 1.3.2 -> 1.9.0

* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.2-alt1
- + packaged gem with Ruby Policy 2.0
