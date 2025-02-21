%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname goodcheck

Name:          gem-goodcheck
Version:       3.1.0.30
Release:       alt1
Summary:       Regexp based customizable linter
License:       MIT
Group:         Development/Ruby
Url:           https://sider.github.io/goodcheck/
Vcs:           https://github.com/sider/goodcheck.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Autoreq:       yes,noruby
Autoprov:      yes,noruby
Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.16
BuildRequires: gem(marcel) >= 1.0
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(psych) >= 3.1
BuildRequires: gem(rainbow) >= 3.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(strong_json) >= 1.1
BuildConflicts: gem(marcel) >= 2.0
BuildConflicts: gem(psych) >= 6
BuildConflicts: gem(rainbow) >= 4
BuildConflicts: gem(strong_json) >= 2.2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency psych >= 5.2.3,psych < 6
Requires:      ruby >= 2.5.0
Requires:      gem(marcel) >= 1.0
Requires:      gem(psych) >= 3.1
Requires:      gem(rainbow) >= 3.0
Requires:      gem(strong_json) >= 1.1
Conflicts:     gem(marcel) >= 2.0
Conflicts:     gem(psych) >= 6
Conflicts:     gem(rainbow) >= 4
Conflicts:     gem(strong_json) >= 2.2
Provides:      gem(goodcheck) = 3.1.0.30

%ruby_use_gem_version goodcheck:3.1.0.30

%description
Goodcheck is a regexp based linter that allows you to define custom rules in a
YAML file.


%package       -n goodcheck
Version:       3.1.0.30
Release:       alt1
Summary:       Regexp based customizable linter executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета goodcheck
Group:         Other
BuildArch:     noarch

Requires:      gem(goodcheck) = 3.1.0.30

%description   -n goodcheck
Regexp based customizable linter executable(s).

Goodcheck is a regexp based linter that allows you to define custom rules in a
YAML file.

%description   -n goodcheck -l ru_RU.UTF-8
Исполнямка для самоцвета goodcheck.


%if_enabled    doc
%package       -n gem-goodcheck-doc
Version:       3.1.0.30
Release:       alt1
Summary:       Regexp based customizable linter documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета goodcheck
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(goodcheck) = 3.1.0.30

%description   -n gem-goodcheck-doc
Regexp based customizable linter documentation files.

Goodcheck is a regexp based linter that allows you to define custom rules in a
YAML file.

%description   -n gem-goodcheck-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета goodcheck.
%endif


%if_enabled    devel
%package       -n gem-goodcheck-devel
Version:       3.1.0.30
Release:       alt1
Summary:       Regexp based customizable linter development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета goodcheck
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(goodcheck) = 3.1.0.30
Requires:      gem(bundler) >= 1.16
Requires:      gem(minitest) >= 5.0
Requires:      gem(rake) >= 13.0
Requires:      gem(simplecov) >= 0.17

%description   -n gem-goodcheck-devel
Regexp based customizable linter development package.

Goodcheck is a regexp based linter that allows you to define custom rules in a
YAML file.

%description   -n gem-goodcheck-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета goodcheck.
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
%doc CHANGELOG.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n goodcheck
%doc CHANGELOG.md LICENSE README.md
%_bindir/goodcheck

%if_enabled    doc
%files         -n gem-goodcheck-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-goodcheck-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Sun Feb 16 2025 Pavel Skrylev <majioa@altlinux.org> 3.1.0.30-alt1
- ^ 3.1.0 -> 3.1.0p30

* Mon May 16 2022 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- + packaged gem with Ruby Policy 2.0
