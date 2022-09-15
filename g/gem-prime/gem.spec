%define        gemname prime

Name:          gem-prime
Version:       0.1.2
Release:       alt1
Summary:       Prime numbers and factorization library
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/prime
Vcs:           https://github.com/ruby/prime.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(singleton) >= 0
BuildRequires: gem(forwardable) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(singleton) >= 0
Requires:      gem(forwardable) >= 0
Provides:      gem(prime) = 0.1.2


%description
Prime numbers and factorization library.


%package       -n gem-prime-doc
Version:       0.1.2
Release:       alt1
Summary:       Prime numbers and factorization library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета prime
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(prime) = 0.1.2

%description   -n gem-prime-doc
Prime numbers and factorization library documentation files.

%description   -n gem-prime-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета prime.


%package       -n gem-prime-devel
Version:       0.1.2
Release:       alt1
Summary:       Prime numbers and factorization library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета prime
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(prime) = 0.1.2

%description   -n gem-prime-devel
Prime numbers and factorization library development package.

%description   -n gem-prime-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета prime.


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

%files         -n gem-prime-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-prime-devel
%doc README.md


%changelog
* Sun Apr 03 2022 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt1
- + packaged gem with Ruby Policy 2.0
