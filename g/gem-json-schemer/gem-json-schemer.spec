%define        gemname json_schemer

Name:          gem-json-schemer
Version:       0.2.22
Release:       alt1
Summary:       JSON Schema validator. Supports drafts 4, 6, and 7
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/davishmcclurg/json_schemer
Vcs:           https://github.com/davishmcclurg/json_schemer.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 2.0 gem(bundler) < 3
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(minitest) >= 5.0 gem(minitest) < 6
BuildRequires: gem(ecma-re-validator) >= 0.3 gem(ecma-re-validator) < 1
BuildRequires: gem(hana) >= 1.3 gem(hana) < 2
BuildRequires: gem(uri_template) >= 0.7 gem(uri_template) < 1
BuildRequires: gem(regexp_parser) >= 2.0 gem(regexp_parser) < 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(ecma-re-validator) >= 0.3 gem(ecma-re-validator) < 1
Requires:      gem(hana) >= 1.3 gem(hana) < 2
Requires:      gem(uri_template) >= 0.7 gem(uri_template) < 1
Requires:      gem(regexp_parser) >= 2.0 gem(regexp_parser) < 3
Provides:      gem(json_schemer) = 0.2.22


%description
JSON Schema validator. Supports drafts 4, 6, and 7.


%package       -n json-schemer
Version:       0.2.22
Release:       alt1
Summary:       JSON Schema validator. Supports drafts 4, 6, and 7 executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета json_schemer
Group:         Other
BuildArch:     noarch

Requires:      gem(json_schemer) = 0.2.22

%description   -n json-schemer
JSON Schema validator. Supports drafts 4, 6, and 7 executable(s).

%description   -n json-schemer -l ru_RU.UTF-8
Исполнямка для самоцвета json_schemer.


%package       -n gem-json-schemer-doc
Version:       0.2.22
Release:       alt1
Summary:       JSON Schema validator. Supports drafts 4, 6, and 7 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета json_schemer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(json_schemer) = 0.2.22

%description   -n gem-json-schemer-doc
JSON Schema validator. Supports drafts 4, 6, and 7 documentation files.

%description   -n gem-json-schemer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета json_schemer.


%package       -n gem-json-schemer-devel
Version:       0.2.22
Release:       alt1
Summary:       JSON Schema validator. Supports drafts 4, 6, and 7 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета json_schemer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(json_schemer) = 0.2.22
Requires:      gem(bundler) >= 2.0 gem(bundler) < 3
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6

%description   -n gem-json-schemer-devel
JSON Schema validator. Supports drafts 4, 6, and 7 development package.

%description   -n gem-json-schemer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета json_schemer.


%prep
%setup

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

%files         -n json-schemer
%doc README.md
%_bindir/json_schemer

%files         -n gem-json-schemer-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-json-schemer-devel
%doc README.md


%changelog
* Sat Oct 29 2022 Pavel Skrylev <majioa@altlinux.org> 0.2.22-alt1
- + packaged gem with Ruby Policy 2.0
