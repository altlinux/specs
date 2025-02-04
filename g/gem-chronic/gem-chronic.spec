%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname chronic

Name:          gem-chronic
Version:       0.10.2.71
Release:       alt0.1
Summary:       Chronic is a pure Ruby natural language date parser
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mojombo/chronic
Vcs:           https://github.com/mojombo/chronic.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 10
%if_enabled check
BuildRequires: gem(activesupport) >= 4.0
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(numerizer) >= 0.2
BuildRequires: gem(simplecov) >= 0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(numerizer) >= 1
BuildConflicts: gem(simplecov) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(numerizer) >= 0.2
Conflicts:     gem(numerizer) >= 1
Obsoletes:     ruby-chronic < %EVR
Provides:      ruby-chronic = %EVR
Provides:      gem(chronic) = 0.10.2.71

%ruby_use_gem_version chronic:0.10.2.71

%description
Chronic is a natural language date/time parser written in pure Ruby. See below
for the wide variety of formats Chronic will parse.


%if_enabled    doc
%package       -n gem-chronic-doc
Version:       0.10.2.71
Release:       alt0.1
Summary:       Chronic is a pure Ruby natural language date parser documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chronic
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chronic) = 0.10.2.71

%description   -n gem-chronic-doc
Chronic is a pure Ruby natural language date parser documentation
files.

Chronic is a natural language date/time parser written in pure Ruby. See below
for the wide variety of formats Chronic will parse.

%description   -n gem-chronic-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chronic.
%endif


%if_enabled    devel
%package       -n gem-chronic-devel
Version:       0.10.2.71
Release:       alt0.1
Summary:       Chronic is a pure Ruby natural language date parser development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chronic
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chronic) = 0.10.2.71
Requires:      gem(activesupport) >= 4.0
Requires:      gem(minitest) >= 5.0
Requires:      gem(rake) >= 10
Requires:      gem(simplecov) >= 0
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(simplecov) >= 1

%description   -n gem-chronic-devel
Chronic is a pure Ruby natural language date parser development
package.

Chronic is a natural language date/time parser written in pure Ruby. See below
for the wide variety of formats Chronic will parse.

%description   -n gem-chronic-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chronic.
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
%doc HISTORY.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-chronic-doc
%doc HISTORY.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-chronic-devel
%doc HISTORY.md LICENSE README.md
%endif


%changelog
* Mon Jan 27 2025 Pavel Skrylev <majioa@altlinux.org> 0.10.2.71-alt0.1
- ^ 0.10.2[1] -> 0.10.2p71

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.10.2.1-alt0.1
- ^ 0.10.2 -> 0.10.2[1]

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.10.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Apr 24 2017 Andrey Cherepanov <cas@altlinux.org> 0.10.2-alt1
- Initial build in Sisyphus
