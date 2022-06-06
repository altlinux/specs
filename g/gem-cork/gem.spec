%define        gemname cork

Name:          gem-cork
Version:       0.3.0
Release:       alt1
Summary:       A delightful CLI UI module
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/CocoaPods/Cork
Vcs:           https://github.com/cocoapods/cork.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(colored2) >= 3.1 gem(colored2) < 4
BuildRequires: gem(bundler) >= 1.3 gem(bundler) < 3
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(bacon) >= 1.1 gem(bacon) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Requires:      gem(colored2) >= 3.1 gem(colored2) < 4
Provides:      gem(cork) = 0.3.0

%description
A delightful CLI UI module.


%package       -n gem-cork-doc
Version:       0.3.0
Release:       alt1
Summary:       A delightful CLI UI module documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cork
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(cork) = 0.3.0

%description   -n gem-cork-doc
A delightful CLI UI module documentation files.

%description   -n gem-cork-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cork.


%package       -n gem-cork-devel
Version:       0.3.0
Release:       alt1
Summary:       A delightful CLI UI module development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cork
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(cork) = 0.3.0
Requires:      gem(bundler) >= 1.3 gem(bundler) < 3
Requires:      gem(rake) >= 10.0
Requires:      gem(bacon) >= 1.1 gem(bacon) < 2

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
* Fri May 06 2022 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- + packaged gem with Ruby Policy 2.0
