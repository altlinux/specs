%define        gemname rubocop-standard

Name:          gem-rubocop-standard
Version:       7.1.0
Release:       alt1
Summary:       Enhanced RuboCop configurations
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/gjtorikian/rubocop-standard
Vcs:           https://github.com/gjtorikian/rubocop-standard.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-minitest) >= 0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rails) >= 0
BuildRequires: gem(rubocop-rake) >= 0
BuildRequires: gem(rubocop-sorbet) >= 0
BuildRequires: gem(rubocop-shopify) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-minitest) >= 0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rails) >= 0
Requires:      gem(rubocop-rake) >= 0
Requires:      gem(rubocop-sorbet) >= 0
Requires:      gem(rubocop-shopify) >= 0
Provides:      gem(rubocop-standard) = 7.1.0


%description
Enables Shopify's Ruby Style Guide recommendations (and bundles them with other
niceties, like `rubocop-{minitest,performance,rails,rake}`).


%package       -n gem-rubocop-standard-doc
Version:       7.1.0
Release:       alt1
Summary:       Enhanced RuboCop configurations documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-standard
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-standard) = 7.1.0

%description   -n gem-rubocop-standard-doc
Enhanced RuboCop configurations documentation files.

Enables Shopify's Ruby Style Guide recommendations (and bundles them with other
niceties, like `rubocop-{minitest,performance,rails,rake}`).

%description   -n gem-rubocop-standard-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-standard.


%package       -n gem-rubocop-standard-devel
Version:       7.1.0
Release:       alt1
Summary:       Enhanced RuboCop configurations development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-standard
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-standard) = 7.1.0
Requires:      gem(rake) >= 0

%description   -n gem-rubocop-standard-devel
Enhanced RuboCop configurations development package.

Enables Shopify's Ruby Style Guide recommendations (and bundles them with other
niceties, like `rubocop-{minitest,performance,rails,rake}`).

%description   -n gem-rubocop-standard-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-standard.


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

%files         -n gem-rubocop-standard-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rubocop-standard-devel
%doc README.md


%changelog
* Mon Oct 31 2022 Pavel Skrylev <majioa@altlinux.org> 7.1.0-alt1
- + packaged gem with Ruby Policy 2.0
