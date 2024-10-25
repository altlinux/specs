%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname jeweler

Name:          gem-jeweler
Version:       2.3.9
Release:       alt1
Summary:       Opinionated tool for creating and managing RubyGem projects
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/technicalpickles/jeweler
Vcs:           https://github.com/technicalpickles/jeweler.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(git) >= 1.2.5
BuildRequires: gem(nokogiri) >= 1.5.10
BuildRequires: gem(github_api) >= 0.16.1
BuildRequires: gem(highline) >= 1.6.15
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(builder) >= 0
BuildRequires: gem(semver2) >= 0
BuildRequires: gem(psych) >= 0
BuildRequires: gem(yard) >= 0.8.5
BuildRequires: gem(bluecloth) >= 0
BuildRequires: gem(cucumber) >= 1.1.4
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(timecop) >= 0
BuildRequires: gem(activesupport) >= 3.2.16
BuildRequires: gem(shoulda) >= 0
BuildRequires: gem(mhennemeyer-output_catcher) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(redgreen) >= 0
BuildRequires: gem(test_construct) >= 0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(test-unit-rr) >= 0
BuildRequires: gem(test-unit) >= 0
BuildConflicts: gem(github_api) >= 1
BuildConflicts: gem(activesupport) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency activesupport >= 6.1.3.2,activesupport < 7
%ruby_use_gem_dependency github_api >= 0.19.0,github_api < 1
Requires:      gem(rake) >= 0
Requires:      gem(git) >= 1.2.5
Requires:      gem(nokogiri) >= 1.5.10
Requires:      gem(github_api) >= 0.16.0
Requires:      gem(highline) >= 1.6.15
Requires:      gem(bundler) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(builder) >= 0
Requires:      gem(semver2) >= 0
Requires:      gem(psych) >= 0
Conflicts:     gem(github_api) >= 1
Provides:      gem(jeweler) = 2.3.9


%description
Simple and opinionated helper for creating Rubygem projects on GitHub


%package       -n jeweler
Version:       2.3.9
Release:       alt1
Summary:       Opinionated tool for creating and managing RubyGem projects executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета jeweler
Group:         Other
BuildArch:     noarch

Requires:      gem(jeweler) = 2.3.9

%description   -n jeweler
Opinionated tool for creating and managing RubyGem projects
executable(s).

Simple and opinionated helper for creating Rubygem projects on GitHub

%description   -n jeweler -l ru_RU.UTF-8
Исполнямка для самоцвета jeweler.


%if_enabled    doc
%package       -n gem-jeweler-doc
Version:       2.3.9
Release:       alt1
Summary:       Opinionated tool for creating and managing RubyGem projects documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета jeweler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(jeweler) = 2.3.9

%description   -n gem-jeweler-doc
Opinionated tool for creating and managing RubyGem projects documentation
files.

Simple and opinionated helper for creating Rubygem projects on GitHub

%description   -n gem-jeweler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета jeweler.
%endif


%if_enabled    devel
%package       -n gem-jeweler-devel
Version:       2.3.9
Release:       alt1
Summary:       Opinionated tool for creating and managing RubyGem projects development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета jeweler
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(jeweler) = 2.3.9
Requires:      gem(yard) >= 0.8.5
Requires:      gem(bluecloth) >= 0
Requires:      gem(cucumber) >= 1.1.4
Requires:      gem(simplecov) >= 0
Requires:      gem(timecop) >= 0
Requires:      gem(activesupport) >= 3.2.16
Requires:      gem(shoulda) >= 0
Requires:      gem(mhennemeyer-output_catcher) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(redgreen) >= 0
Requires:      gem(test_construct) >= 0
Requires:      gem(coveralls) >= 0
Requires:      gem(test-unit-rr) >= 0
Requires:      gem(test-unit) >= 0
Conflicts:     gem(activesupport) >= 7

%description   -n gem-jeweler-devel
Opinionated tool for creating and managing RubyGem projects development
package.

Simple and opinionated helper for creating Rubygem projects on GitHub

%description   -n gem-jeweler-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета jeweler.
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
%doc README.markdown README.org features/generator/readme.feature lib/jeweler/templates/README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n jeweler
%doc README.markdown README.org features/generator/readme.feature lib/jeweler/templates/README.rdoc
%_bindir/jeweler

%if_enabled    doc
%files         -n gem-jeweler-doc
%doc README.markdown README.org features/generator/readme.feature lib/jeweler/templates/README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-jeweler-devel
%doc README.markdown README.org features/generator/readme.feature lib/jeweler/templates/README.rdoc
%endif


%changelog
* Fri Oct 18 2024 Pavel Skrylev <majioa@altlinux.org> 2.3.9-alt1
- + packaged gem with Ruby Policy 2.0
