%define        gemname qed

Name:          gem-qed
Version:       2.9.2
Release:       alt1
Summary:       Quod Erat Demonstrandum
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           http://rubyworks.github.com/qed
Vcs:           https://github.com/rubyworks/qed.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(ansi) >= 0
BuildRequires: gem(brass) >= 0
BuildRequires: gem(ae) >= 0
BuildRequires: gem(rulebow) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(ansi) >= 0
Requires:      gem(brass) >= 0
Provides:      gem(qed) = 2.9.2


%description
QED (Quality Ensured Demonstrations) is a TDD/BDD framework utilizing Literate
Programming techniques.


%package       -n qed
Version:       2.9.2
Release:       alt1
Summary:       Quod Erat Demonstrandum executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета qed
Group:         Other
BuildArch:     noarch

Requires:      gem(qed) = 2.9.2

%description   -n qed
Quod Erat Demonstrandum executable(s).

QED (Quality Ensured Demonstrations) is a TDD/BDD framework utilizing Literate
Programming techniques.

%description   -n qed -l ru_RU.UTF-8
Исполнямка для самоцвета qed.


%package       -n gem-qed-doc
Version:       2.9.2
Release:       alt1
Summary:       Quod Erat Demonstrandum documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета qed
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(qed) = 2.9.2

%description   -n gem-qed-doc
Quod Erat Demonstrandum documentation files.

QED (Quality Ensured Demonstrations) is a TDD/BDD framework utilizing Literate
Programming techniques.

%description   -n gem-qed-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета qed.


%package       -n gem-qed-devel
Version:       2.9.2
Release:       alt1
Summary:       Quod Erat Demonstrandum development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета qed
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(qed) = 2.9.2
Requires:      gem(ae) >= 0
Requires:      gem(rulebow) >= 0

%description   -n gem-qed-devel
Quod Erat Demonstrandum development package.

QED (Quality Ensured Demonstrations) is a TDD/BDD framework utilizing Literate
Programming techniques.

%description   -n gem-qed-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета qed.


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

%files         -n qed
%doc README.md
%_bindir/qed
%_bindir/qedoc

%files         -n gem-qed-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-qed-devel
%doc README.md


%changelog
* Sat Sep 11 2021 Pavel Skrylev <majioa@altlinux.org> 2.9.2-alt1
- + packaged gem with Ruby Policy 2.0
