%define        gemname ecma-re-validator

Name:          gem-ecma-re-validator
Version:       0.4.0
Release:       alt1
Summary:       Validate a regular expression string against what ECMA-262 can actually do
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/gjtorikian/ecma-re-validator
Vcs:           https://github.com/gjtorikian/ecma-re-validator.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(awesome_print) >= 0
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.1 gem(rspec) < 4
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(rubocop-standard) >= 0
BuildRequires: gem(regexp_parser) >= 2.2 gem(regexp_parser) < 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(regexp_parser) >= 2.2 gem(regexp_parser) < 3
Provides:      gem(ecma-re-validator) = 0.4.0


%description
Validate a regular expression string against what ECMA-262 can actually do.


%package       -n gem-ecma-re-validator-doc
Version:       0.4.0
Release:       alt1
Summary:       Validate a regular expression string against what ECMA-262 can actually do documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ecma-re-validator
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ecma-re-validator) = 0.4.0

%description   -n gem-ecma-re-validator-doc
Validate a regular expression string against what ECMA-262 can actually do
documentation files.

%description   -n gem-ecma-re-validator-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ecma-re-validator.


%package       -n gem-ecma-re-validator-devel
Version:       0.4.0
Release:       alt1
Summary:       Validate a regular expression string against what ECMA-262 can actually do development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ecma-re-validator
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ecma-re-validator) = 0.4.0
Requires:      gem(awesome_print) >= 0
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.1 gem(rspec) < 4
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-rspec) >= 0
Requires:      gem(rubocop-standard) >= 0

%description   -n gem-ecma-re-validator-devel
Validate a regular expression string against what ECMA-262 can actually do
development package.

%description   -n gem-ecma-re-validator-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ecma-re-validator.


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

%files         -n gem-ecma-re-validator-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-ecma-re-validator-devel
%doc README.md


%changelog
* Sat Oct 29 2022 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- + packaged gem with Ruby Policy 2.0
