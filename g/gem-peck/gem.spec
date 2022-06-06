%define        gemname peck

Name:          gem-peck
Version:       0.5.4
Release:       alt1
Summary:       Peck is a concurrent spec framework
License:       Unlicensed
Group:         Development/Ruby
Url:           https://github.com/Fingertips/Peck
Vcs:           https://github.com/Fingertips/Peck.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(peck) = 0.5.4


%description
Peck is a concurrent spec framework which inherits a lot from the fabulous
Bacon and MacBacon. We call it a framework because it was designed to be used
in parts and is easily extended executable(s)


%package       -n peck
Version:       0.5.4
Release:       alt1
Summary:       Peck is a concurrent spec framework executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета peck
Group:         Other
BuildArch:     noarch

Requires:      gem(peck) = 0.5.4

%description   -n peck
Peck is a concurrent spec framework executable(s).

Peck is a concurrent spec framework which inherits a lot from the fabulous
Bacon and MacBacon. We call it a framework because it was designed to be used
in parts and is easily extended executable(s)

%description   -n peck -l ru_RU.UTF-8
Исполнямка для самоцвета peck.


%package       -n gem-peck-doc
Version:       0.5.4
Release:       alt1
Summary:       Peck is a concurrent spec framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета peck
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(peck) = 0.5.4

%description   -n gem-peck-doc
Peck is a concurrent spec framework  documentation files.

Peck is a concurrent spec framework which inherits a lot from the fabulous
Bacon and MacBacon. We call it a framework because it was designed to be used
in parts and is easily extended executable(s)

%description   -n gem-peck-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета peck.


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

%files         -n peck
%doc README.md
%_bindir/peck

%files         -n gem-peck-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Fri May 06 2022 Pavel Skrylev <majioa@altlinux.org> 0.5.4-alt1
- + packaged gem with Ruby Policy 2.0
