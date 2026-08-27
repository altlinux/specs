%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname optimist

Name:          gem-optimist
Version:       3.2.1
Release:       alt1
Summary:       Optimist is a commandline option parser for Ruby that just gets out of your way
License:       MIT
Group:         Development/Ruby
Url:           http://manageiq.github.io/optimist/
Vcs:           https://github.com/manageiq/optimist.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(chronic) >= 0
BuildRequires: gem(manageiq-style) >= 0
BuildRequires: gem(minitest) >= 5.25
BuildRequires: gem(rake) >= 10.0
BuildConflicts: gem(minitest) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 6.0,minitest < 7
Provides:      gem(optimist) = 3.2.1

%description
Optimist is a commandline option parser for Ruby that just gets out of your way.
One line of code per option is all you need to write. For that, you get a nice
automatically-generated help page, robust option parsing, and sensible defaults
for everything you don't specify.


%if_enabled    doc
%package       -n gem-optimist-doc
Version:       3.2.1
Release:       alt1
Summary:       Optimist is a commandline option parser for Ruby that just gets out of your way documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета optimist
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(optimist) = 3.2.1

%description   -n gem-optimist-doc
Optimist is a commandline option parser for Ruby that just gets out of your way
documentation files.

%description   -n gem-optimist-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета optimist.
%endif


%if_enabled    devel
%package       -n gem-optimist-devel
Version:       3.2.1
Release:       alt1
Summary:       Optimist is a commandline option parser for Ruby that just gets out of your way development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета optimist
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(optimist) = 3.2.1
Requires:      gem(chronic) >= 0
Requires:      gem(manageiq-style) >= 0
Requires:      gem(minitest) >= 5.25
Requires:      gem(rake) >= 10.0
Conflicts:     gem(minitest) >= 7

%description   -n gem-optimist-devel
Optimist is a commandline option parser for Ruby that just gets out of your way
development package.

%description   -n gem-optimist-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета optimist.
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
%files         -n gem-optimist-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-optimist-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Sat Aug 22 2026 Pavel Skrylev <majioa@altlinux.org> 3.2.1-alt1
- ^ 3.0.1 -> 3.2.1

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- ^ 3.0.0 -> 3.0.1

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
