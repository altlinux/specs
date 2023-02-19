%define        gemname cork

Name:          gem-cork
Version:       0.3.0.1
Release:       alt0.1
Summary:       A delightful CLI UI module
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/CocoaPods/Cork
Vcs:           https://github.com/cocoapods/cork.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.3
BuildRequires: gem(bacon) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(mocha-on-bacon) >= 0
BuildRequires: gem(prettybacon) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(codecov) >= 0
BuildRequires: gem(colored2) >= 3.1
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(bacon) > 2
BuildConflicts: gem(colored2) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency bacon >= 1.2.0,bacon < 2
Requires:      gem(colored2) >= 3.1
Conflicts:     gem(colored2) >= 4
Provides:      gem(cork) = 0.3.0.1

%ruby_use_gem_version cork:0.3.0.1

%description
A delightful CLI UI module.


%package       -n gem-cork-doc
Version:       0.3.0.1
Release:       alt0.1
Summary:       A delightful CLI UI module documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cork
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(cork) = 0.3.0.1

%description   -n gem-cork-doc
A delightful CLI UI module documentation files.

%description   -n gem-cork-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cork.


%package       -n gem-cork-devel
Version:       0.3.0.1
Release:       alt0.1
Summary:       A delightful CLI UI module development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cork
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(cork) = 0.3.0.1
Requires:      gem(bundler) >= 1.3
Requires:      gem(bacon) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(mocha-on-bacon) >= 0
Requires:      gem(prettybacon) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(rake) >= 10.0
Requires:      gem(codecov) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(bacon) > 2

%description   -n gem-cork-devel
A delightful CLI UI module development package.

%description   -n gem-cork-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета cork.


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

%files         -n gem-cork-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-cork-devel
%doc README.md


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 0.3.0.1-alt0.1
- ^ 0.3.0 -> 0.3.0.1

* Fri May 06 2022 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt0.1
- + packaged gem with Ruby Policy 2.0
