%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname yell

Name:          gem-yell
Version:       2.2.2
Release:       alt1
Summary:       Yell - Your Extensible Logging Library
License:       MIT
Group:         Development/Ruby
Url:           http://rudionrailspec.github.com/yell
Vcs:           https://github.com/rudionrails/yell.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0
%if_enabled check
BuildRequires: gem(activesupport) >= 5
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(rspec-core) >= 3
BuildRequires: gem(rspec-expectations) >= 0
BuildRequires: gem(rspec-its) >= 0
BuildRequires: gem(rspec-mocks) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(timecop) >= 0
BuildConflicts: gem(activesupport) >= 8
BuildConflicts: gem(rspec-core) >= 4
BuildRequires: gem(rubocop) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency activesupport >= 7.1,activesupport < 8
Provides:      gem(yell) = 2.2.2

%description
Yell - Your Extensible Logging Library. Define multiple adapters, various log
level combinations or message formatting options like you've never done before


%if_enabled    doc
%package       -n gem-yell-doc
Version:       2.2.2
Release:       alt1
Summary:       Yell - Your Extensible Logging Library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета yell
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(yell) = 2.2.2

%description   -n gem-yell-doc
Yell - Your Extensible Logging Library documentation files.

Yell - Your Extensible Logging Library. Define multiple adapters, various log
level combinations or message formatting options like you've never done before

%description   -n gem-yell-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета yell.
%endif


%if_enabled    devel
%package       -n gem-yell-devel
Version:       2.2.2
Release:       alt1
Summary:       Yell - Your Extensible Logging Library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета yell
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(yell) = 2.2.2
Requires:      gem(activesupport) >= 5
Requires:      gem(coveralls) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec-core) >= 3
Requires:      gem(rspec-expectations) >= 0
Requires:      gem(rspec-its) >= 0
Requires:      gem(rspec-mocks) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(timecop) >= 0
Conflicts:     gem(activesupport) >= 8
Conflicts:     gem(rspec-core) >= 4

%description   -n gem-yell-devel
Yell - Your Extensible Logging Library development package.

Yell - Your Extensible Logging Library. Define multiple adapters, various log
level combinations or message formatting options like you've never done before

%description   -n gem-yell-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета yell.
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
%files         -n gem-yell-doc
%doc LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-yell-devel
%doc LICENSE.txt README.md
%endif


%changelog
* Sun Jan 26 2025 Pavel Skrylev <majioa@altlinux.org> 2.2.2-alt1
- ^ 2.2.0 -> 2.2.2

* Mon Oct 31 2022 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- + packaged gem with Ruby Policy 2.0
