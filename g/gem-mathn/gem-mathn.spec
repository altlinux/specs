%define        gemname mathn

Name:          gem-mathn
Version:       0.1.0.1
Release:       alt0.1
Summary:       Deprecated library that extends math operations
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/mathn
Vcs:           https://github.com/ruby/mathn.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         remove-deprecated.patch
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(matrix) >= 0
BuildRequires: gem(cmath) >= 0
BuildRequires: gem(prime) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(matrix) >= 0
Requires:      gem(cmath) >= 0
Requires:      gem(prime) >= 0
Provides:      gem(mathn) = 0.1.0.1

%ruby_use_gem_version mathn:0.1.0.1

%description
Deprecated library that extends math operations.


%package       -n gem-mathn-doc
Version:       0.1.0.1
Release:       alt0.1
Summary:       Deprecated library that extends math operations documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mathn
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mathn) = 0.1.0.1

%description   -n gem-mathn-doc
Deprecated library that extends math operations documentation files.

%description   -n gem-mathn-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mathn.


%package       -n gem-mathn-devel
Version:       0.1.0.1
Release:       alt0.1
Summary:       Deprecated library that extends math operations development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mathn
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mathn) = 0.1.0.1
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0

%description   -n gem-mathn-devel
Deprecated library that extends math operations development package.

%description   -n gem-mathn-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mathn.


%prep
%setup
%autopatch

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

%files         -n gem-mathn-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-mathn-devel
%doc README.md


%changelog
* Mon Feb 06 2023 Pavel Skrylev <majioa@altlinux.org> 0.1.0.1-alt0.1
- + packaged gem with Ruby Policy 2.0 with ver 0.1.0a1
