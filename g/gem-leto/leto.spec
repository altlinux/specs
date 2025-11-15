%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname leto

Name:          gem-leto
Version:       2.1.0
Release:       alt1
Summary:       Generic object traverser
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jaynetics/leto
Vcs:           https://github.com/jaynetics/leto.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(relaxed-rubocop) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 1.21
BuildRequires: gem(simplecov-cobertura) >= 0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.3.0
Requires:      gem(rake) >= 13.0
Requires:      gem(relaxed-rubocop) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 1.21
Requires:      gem(simplecov-cobertura) >= 0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Provides:      gem(leto) = 2.1.0

%description
Generic object traverser


%if_enabled    doc
%package       -n gem-leto-doc
Version:       2.1.0
Release:       alt1
Summary:       Generic object traverser documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета leto
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(leto) = 2.1.0

%description   -n gem-leto-doc
Generic object traverser documentation files.

%description   -n gem-leto-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета leto.
%endif


%if_enabled    devel
%package       -n gem-leto-devel
Version:       2.1.0
Release:       alt1
Summary:       Generic object traverser development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета leto
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(leto) = 2.1.0
Requires:      gem(rake) >= 13.0
Requires:      gem(relaxed-rubocop) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 1.21
Requires:      gem(simplecov-cobertura) >= 0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2

%description   -n gem-leto-devel
Generic object traverser development package.

%description   -n gem-leto-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета leto.
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
%files         -n gem-leto-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-leto-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Thu Oct 30 2025 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
