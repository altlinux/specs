%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname semver2

Name:          gem-semver2
Version:       3.4.2
Release:       alt1
Summary:       Semantic Versioning
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/haf/semver
Vcs:           https://github.com/haf/semver.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 10
BuildRequires: gem(rspec) >= 2.12.0
BuildRequires: gem(rubocop) >= 0.59.2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Provides:      gem(semver2) = 3.4.2


%description
maintain versions as per http://semver.org


%package       -n semver
Version:       3.4.2
Release:       alt1
Summary:       Semantic Versioning executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета semver2
Group:         Other
BuildArch:     noarch

Requires:      gem(semver2) = 3.4.2

%description   -n semver
Semantic Versioning executable(s).

maintain versions as per http://semver.org

%description   -n semver -l ru_RU.UTF-8
Исполнямка для самоцвета semver2.


%if_enabled    doc
%package       -n gem-semver2-doc
Version:       3.4.2
Release:       alt1
Summary:       Semantic Versioning documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета semver2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(semver2) = 3.4.2

%description   -n gem-semver2-doc
Semantic Versioning documentation files.

maintain versions as per http://semver.org

%description   -n gem-semver2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета semver2.
%endif


%if_enabled    devel
%package       -n gem-semver2-devel
Version:       3.4.2
Release:       alt1
Summary:       Semantic Versioning development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета semver2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(semver2) = 3.4.2
Requires:      gem(rake) >= 10
Requires:      gem(rspec) >= 2.12.0
Requires:      gem(rubocop) >= 0.59.2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2

%description   -n gem-semver2-devel
Semantic Versioning development package.

maintain versions as per http://semver.org

%description   -n gem-semver2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета semver2.
%endif


%prep
%setup
%autopatch -p1

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

%files         -n semver
%doc README.md
%_bindir/semver

%if_enabled    doc
%files         -n gem-semver2-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-semver2-devel
%doc README.md
%endif


%changelog
* Fri Oct 18 2024 Pavel Skrylev <majioa@altlinux.org> 3.4.2-alt1
- + packaged gem with Ruby Policy 2.0
