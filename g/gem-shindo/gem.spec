%define        gemname shindo

Name:          gem-shindo
Version:       0.3.10
Release:       alt1
Summary:       Simple depth first Ruby testing
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/geemus/shindo
Vcs:           https://github.com/geemus/shindo.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(formatador) >= 0.1.1
BuildRequires: gem(rake) >= 0 gem(rake) < 14
BuildRequires: gem(rdoc) >= 0 gem(rdoc) < 7

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(formatador) >= 0.1.1
Provides:      gem(shindo) = 0.3.10


%description
Work with your tests, not against them.


%package       -n shindo
Version:       0.3.10
Release:       alt1
Summary:       Simple depth first Ruby testing executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета shindo
Group:         Other
BuildArch:     noarch

Requires:      gem(shindo) = 0.3.10

%description   -n shindo
Simple depth first Ruby testing executable(s).

Work with your tests, not against them.

%description   -n shindo -l ru_RU.UTF-8
Исполнямка для самоцвета shindo.


%package       -n gem-shindo-doc
Version:       0.3.10
Release:       alt1
Summary:       Simple depth first Ruby testing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета shindo
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(shindo) = 0.3.10

%description   -n gem-shindo-doc
Simple depth first Ruby testing documentation files.

Work with your tests, not against them.

%description   -n gem-shindo-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета shindo.


%package       -n gem-shindo-devel
Version:       0.3.10
Release:       alt1
Summary:       Simple depth first Ruby testing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета shindo
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(shindo) = 0.3.10
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(rdoc) >= 0 gem(rdoc) < 7

%description   -n gem-shindo-devel
Simple depth first Ruby testing development package.

Work with your tests, not against them.

%description   -n gem-shindo-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета shindo.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n shindo
%doc README.rdoc
%_bindir/shindo
%_bindir/shindont

%files         -n gem-shindo-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-shindo-devel
%doc README.rdoc


%changelog
* Tue Jun 08 2021 Pavel Skrylev <majioa@altlinux.org> 0.3.10-alt1
- + packaged gem with Ruby Policy 2.0
