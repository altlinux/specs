%define        gemname nap

Name:          gem-nap
Version:       1.1.0
Release:       alt1
Summary:       Nap is a really simple REST library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/Fingertips/nap
Vcs:           https://github.com/fingertips/nap.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 10 gem(rake) < 14
BuildRequires: gem(peck) >= 0.5 gem(peck) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Provides:      gem(nap) = 1.1.0


%description
Nap is a really simple REST library. It allows you to perform HTTP requests with
minimal amounts of code.


%package       -n gem-nap-doc
Version:       1.1.0
Release:       alt1
Summary:       Nap is a really simple REST library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета nap
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(nap) = 1.1.0

%description   -n gem-nap-doc
Nap is a really simple REST library documentation files.

Nap is a really simple REST library. It allows you to perform HTTP requests with
minimal amounts of code.

%description   -n gem-nap-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета nap.


%package       -n gem-nap-devel
Version:       1.1.0
Release:       alt1
Summary:       Nap is a really simple REST library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета nap
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(nap) = 1.1.0
Requires:      gem(rake) >= 10 gem(rake) < 14
Requires:      gem(peck) >= 0.5 gem(peck) < 1

%description   -n gem-nap-devel
Nap is a really simple REST library development package.

Nap is a really simple REST library. It allows you to perform HTTP requests with
minimal amounts of code.

%description   -n gem-nap-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета nap.


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

%files         -n gem-nap-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-nap-devel
%doc README.md


%changelog
* Fri May 06 2022 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with Ruby Policy 2.0
