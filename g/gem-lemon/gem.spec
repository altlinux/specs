%define        gemname lemon

Name:          gem-lemon
Version:       0.8.4
Release:       alt1
Summary:       Pucker-tight Unit Testing
License:       Apache 2.0
Group:         Development/Ruby
Url:           https://github.com/rubyworks/lemon
Vcs:           https://github.com/rubyworks/lemon.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(ae) >= 0
BuildRequires: gem(ansi) >= 1.3
#BuildRequires: gem(detroit) >= 0
#BuildRequires: gem(reap) >= 0
#BuildRequires: gem(qed) >= 0
#BuildRequires: gem(cucumber) >= 0
#BuildRequires: gem(aruba) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_version lemon:0.8.4
Requires:      gem(ae) >= 0
Requires:      gem(ansi) >= 1.3
Provides:      gem(lemon) = 0.8.4


%description
Lemon is a unit testing framework that tightly correlates class to test case and
method to test unit.


%package       -n lemon-tester
Version:       0.8.4
Release:       alt1
Summary:       Pucker-tight Unit Testing executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета lemon
Group:         Other
BuildArch:     noarch

Requires:      gem(lemon) = 0.8.4
Conflicts:     lemon

%description   -n lemon-tester
Pucker-tight Unit Testing executable(s).

Lemon is a unit testing framework that tightly correlates class to test case and
method to test unit.

%description   -n lemon-tester -l ru_RU.UTF-8
Исполнямка для самоцвета lemon.


%package       -n gem-lemon-doc
Version:       0.8.4
Release:       alt1
Summary:       Pucker-tight Unit Testing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета lemon
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(lemon) = 0.8.4

%description   -n gem-lemon-doc
Pucker-tight Unit Testing documentation files.

Lemon is a unit testing framework that tightly correlates class to test case and
method to test unit.

%description   -n gem-lemon-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета lemon.


%package       -n gem-lemon-devel
Version:       0.8.4
Release:       alt1
Summary:       Pucker-tight Unit Testing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета lemon
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(lemon) = 0.8.4
#Requires:      gem(detroit) >= 0
#Requires:      gem(reap) >= 0
Requires:      gem(qed) >= 0
#Requires:      gem(cucumber) >= 0
#Requires:      gem(aruba) >= 0

%description   -n gem-lemon-devel
Pucker-tight Unit Testing development package.

Lemon is a unit testing framework that tightly correlates class to test case and
method to test unit.

%description   -n gem-lemon-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета lemon.


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

%files         -n lemon-tester
%doc README.rdoc
%_bindir/lemon

%files         -n gem-lemon-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-lemon-devel
%doc README.rdoc


%changelog
* Sat Sep 11 2021 Pavel Skrylev <majioa@altlinux.org> 0.8.4-alt1
- + packaged gem with Ruby Policy 2.0
