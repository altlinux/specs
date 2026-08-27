%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname json_schemer

Name:          gem-json-schemer
Version:       2.5.0
Release:       alt1
Summary:       JSON Schema validator. Supports drafts 4, 6, and 7
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/davishmcclurg/json_schemer
Vcs:           https://github.com/davishmcclurg/json_schemer.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(base64) >= 0
BuildRequires: gem(bigdecimal) >= 0
BuildRequires: gem(bundler) >= 2.1.4
BuildRequires: gem(csv) >= 0
BuildRequires: gem(hana) >= 1.3
BuildRequires: gem(i18n) >= 0
BuildRequires: gem(i18n-debug) >= 0
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(openssl) >= 3.0.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(regexp_parser) >= 2.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(simpleidn) >= 0.2
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(hana) >= 2
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(openssl) >= 4
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(regexp_parser) >= 3
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(simpleidn) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency openssl >= 3.0.0,openssl < 4
%ruby_use_gem_dependency minitest >= 6.0
%ruby_alias_names json_schemer,json-schemer
Requires:      ruby >= 2.7
Requires:      gem(bigdecimal) >= 0
Requires:      gem(hana) >= 1.3
Requires:      gem(regexp_parser) >= 2.0
Requires:      gem(simpleidn) >= 0.2
Conflicts:     gem(hana) >= 2
Conflicts:     gem(regexp_parser) >= 3
Conflicts:     gem(simpleidn) >= 1
Provides:      json_schemer = %EVR
Provides:      gem(json_schemer) = 2.5.0

%description
JSON Schema validator. Supports drafts 4, 6, and 7.


%package       -n json-schemer
Version:       2.5.0
Release:       alt1
Summary:       JSON Schema validator. Supports drafts 4, 6, and 7 executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета json_schemer
Group:         Other
BuildArch:     noarch

Requires:      gem(json_schemer) = 2.5.0

%description   -n json-schemer
JSON Schema validator. Supports drafts 4, 6, and 7 executable(s).

%description   -n json-schemer -l ru_RU.UTF-8
Исполнямка для самоцвета json_schemer.


%if_enabled    doc
%package       -n gem-json-schemer-doc
Version:       2.5.0
Release:       alt1
Summary:       JSON Schema validator. Supports drafts 4, 6, and 7 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета json_schemer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(json_schemer) = 2.5.0

%description   -n gem-json-schemer-doc
JSON Schema validator. Supports drafts 4, 6, and 7 documentation files.

%description   -n gem-json-schemer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета json_schemer.
%endif


%if_enabled    devel
%package       -n gem-json-schemer-devel
Version:       2.5.0
Release:       alt1
Summary:       JSON Schema validator. Supports drafts 4, 6, and 7 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета json_schemer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(json_schemer) = 2.5.0
Requires:      gem(base64) >= 0
Requires:      gem(bundler) >= 2.1.4
Requires:      gem(csv) >= 0
Requires:      gem(i18n) >= 0
Requires:      gem(i18n-debug) >= 0
Requires:      gem(minitest) >= 5.0
Requires:      gem(openssl) >= 3.0.0
Requires:      gem(rake) >= 13.0
Requires:      gem(simplecov) >= 0.17
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(minitest) >= 7
Conflicts:     gem(openssl) >= 4
Conflicts:     gem(rake) >= 14
Conflicts:     gem(simplecov) >= 1

%description   -n gem-json-schemer-devel
JSON Schema validator. Supports drafts 4, 6, and 7 development package.

%description   -n gem-json-schemer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета json_schemer.
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

%files         -n json-schemer
%doc CHANGELOG.md LICENSE.txt README.md
%_bindir/json_schemer

%if_enabled    doc
%files         -n gem-json-schemer-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-json-schemer-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Fri Aug 21 2026 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt1
- ^ 0.2.22 -> 2.5.0

* Sat Oct 29 2022 Pavel Skrylev <majioa@altlinux.org> 0.2.22-alt1
- + packaged gem with Ruby Policy 2.0
