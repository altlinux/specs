%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname backports

Name:          gem-backports
Version:       3.25.2
Release:       alt1
Summary:       The latest features of Ruby backported to older versions
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/marcandre/backports
Vcs:           https://github.com/marcandre/backports.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(activesupport) >= 3.2.0
BuildRequires: gem(mspec) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
BuildConflicts: gem(activesupport) >= 8
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency activesupport >= 7.1,activesupport < 8
Obsoletes:     ruby-backports < %EVR
Provides:      ruby-backports = %EVR
Provides:      gem(backports) = 3.25.2

%description
The goal of 'backports' is to make it easier to write ruby code that runs across
different versions of Ruby.


%if_enabled    doc
%package       -n gem-backports-doc
Version:       3.25.2
Release:       alt1
Summary:       The latest features of Ruby backported to older versions documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета backports
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(backports) = 3.25.2
Obsoletes:     ruby-backports-doc < %EVR
Provides:      ruby-backports-doc = %EVR

%description   -n gem-backports-doc
The latest features of Ruby backported to older versions documentation
files.

The goal of 'backports' is to make it easier to write ruby code that runs across
different versions of Ruby.

%description   -n gem-backports-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета backports.
%endif


%if_enabled    devel
%package       -n gem-backports-devel
Version:       3.25.2
Release:       alt1
Summary:       The latest features of Ruby backported to older versions development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета backports
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(backports) = 3.25.2
Requires:      gem(activesupport) >= 3.2.0
Requires:      gem(mspec) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0
Conflicts:     gem(activesupport) >= 8
Conflicts:     gem(rubocop) >= 2

%description   -n gem-backports-devel
The latest features of Ruby backported to older versions development
package.

The goal of 'backports' is to make it easier to write ruby code that runs across
different versions of Ruby.

%description   -n gem-backports-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета backports.
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
%files         -n gem-backports-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-backports-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Sat Nov 29 2025 Pavel Skrylev <majioa@altlinux.org> 3.25.2-alt1
- ^ 3.24.0 -> 3.25.2

* Wed Mar 08 2023 Andrey Cherepanov <cas@altlinux.org> 3.24.0-alt1
- New version.

* Sat Jan 01 2022 Andrey Cherepanov <cas@altlinux.org> 3.23.0-alt1
- New version.

* Fri Apr 02 2021 Andrey Cherepanov <cas@altlinux.org> 3.21.0-alt1
- New version.

* Thu Jan 28 2021 Andrey Cherepanov <cas@altlinux.org> 3.20.2-alt1
- New version.

* Mon Jan 04 2021 Andrey Cherepanov <cas@altlinux.org> 3.20.1-alt1
- New version.

* Thu Dec 31 2020 Andrey Cherepanov <cas@altlinux.org> 3.20.0-alt1
- New version.

* Mon Dec 28 2020 Andrey Cherepanov <cas@altlinux.org> 3.19.0-alt1
- New version.

* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 3.18.2-alt1
- New version.
- Rename to gem-backports according to Ruby Policy 2.0.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Mar 29 2017 Denis Medvedev <nbr@altlinux.org> 3.7.0-alt1
- Initial build in sisyphus
