%define        gemname rbench

Name:          gem-rbench
Version:       0.2.4
Release:       alt1
Summary:       Library for generating nice ruby-benchmarks
License:       MIT
Group:         Development/Ruby
Url:           http://www.github.com/somebee/rbench
Vcs:           https://github.com/somebee/rbench.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(rbench) = 0.2.4


%description
Library for generating nice ruby-benchmarks


%package       -n gem-rbench-doc
Version:       0.2.4
Release:       alt1
Summary:       Library for generating nice ruby-benchmarks documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rbench
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rbench) = 0.2.4

%description   -n gem-rbench-doc
Library for generating nice ruby-benchmarks documentation files.

Library for generating nice ruby-benchmarks

%description   -n gem-rbench-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rbench.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-rbench-doc
%doc README
%ruby_gemdocdir


%changelog
* Wed Aug 25 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.4-alt1
- + packaged gem with Ruby Policy 2.0
