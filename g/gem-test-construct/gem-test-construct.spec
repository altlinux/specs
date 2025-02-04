%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname test_construct

Name:          gem-test-construct
Version:       2.0.2.9
Release:       alt0.1
Summary:       Creates temporary files and directories for testing
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bhb/test_construct
Vcs:           https://github.com/bhb/test_construct.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 2.1.4
%if_enabled check
BuildRequires: gem(minitest) >= 5.0.8
BuildRequires: gem(mocha) >= 0.14.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(mocha) >= 3
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 2.0,mocha < 3
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_alias_names test_construct,test-construct
Provides:      test_construct = %EVR
Provides:      gem(test_construct) = 2.0.2.9

%ruby_use_gem_version test_construct:2.0.2.9

%description
TestConstruct is a DSL for creating temporary files and directories during
testing.


%if_enabled    doc
%package       -n gem-test-construct-doc
Version:       2.0.2.9
Release:       alt0.1
Summary:       Creates temporary files and directories for testing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета test_construct
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(test_construct) = 2.0.2.9

%description   -n gem-test-construct-doc
Creates temporary files and directories for testing documentation files.

%description   -n gem-test-construct-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета test_construct.
%endif


%if_enabled    devel
%package       -n gem-test-construct-devel
Version:       2.0.2.9
Release:       alt0.1
Summary:       Creates temporary files and directories for testing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета test_construct
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(test_construct) = 2.0.2.9
Requires:      gem(bundler) >= 2.1.4
Requires:      gem(minitest) >= 5.0.8
Requires:      gem(mocha) >= 0.14.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(mocha) >= 3
Conflicts:     gem(rspec) >= 4

%description   -n gem-test-construct-devel
Creates temporary files and directories for testing development package.

%description   -n gem-test-construct-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета test_construct.
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
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-test-construct-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-test-construct-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Sun Jan 26 2025 Pavel Skrylev <majioa@altlinux.org> 2.0.2.9-alt0.1
- ^ 2.0.2 -> 2.0.2p9

* Fri Oct 29 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.2-alt1
- + packaged gem with Ruby Policy 2.0
