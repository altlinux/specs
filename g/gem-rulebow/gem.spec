%define        gemname rulebow

Name:          gem-rulebow
Version:       0.4.0
Release:       alt1
Summary:       An autological build tool
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           http://rubyworks.github.com/rulebow
Vcs:           https://github.com/rubyworks/rulebow.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(notify) >= 0
# BuildRequires: gem(detroit) >= 0
BuildRequires: gem(mast) >= 0
# BuildRequires: gem(qed) >= 0
BuildRequires: gem(ae) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(notify) >= 0
Provides:      gem(rulebow) = 0.4.0


%description
Rulebow is an automated build tool with a set-logic based rule system. Rulebow
is the perfect tool for performing continuous integration during development.


%package       -n bow
Version:       0.4.0
Release:       alt1
Summary:       An autological build tool executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rulebow
Group:         Other
BuildArch:     noarch

Requires:      gem(rulebow) = 0.4.0

%description   -n bow
An autological build tool executable(s).

Rulebow is an automated build tool with a set-logic based rule system. Rulebow
is the perfect tool for performing continuous integration during development.

%description   -n bow -l ru_RU.UTF-8
Исполнямка для самоцвета rulebow.


%package       -n gem-rulebow-doc
Version:       0.4.0
Release:       alt1
Summary:       An autological build tool documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rulebow
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rulebow) = 0.4.0

%description   -n gem-rulebow-doc
An autological build tool documentation files.

Rulebow is an automated build tool with a set-logic based rule system. Rulebow
is the perfect tool for performing continuous integration during development.

%description   -n gem-rulebow-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rulebow.


%package       -n gem-rulebow-devel
Version:       0.4.0
Release:       alt1
Summary:       An autological build tool development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rulebow
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rulebow) = 0.4.0
# Requires:      gem(detroit) >= 0
Requires:      gem(mast) >= 0
# Requires:      gem(qed) >= 0
Requires:      gem(ae) >= 0

%description   -n gem-rulebow-devel
An autological build tool development package.

Rulebow is an automated build tool with a set-logic based rule system. Rulebow
is the perfect tool for performing continuous integration during development.

%description   -n gem-rulebow-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rulebow.


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

%files         -n bow
%doc README.md
%_bindir/bow

%files         -n gem-rulebow-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rulebow-devel
%doc README.md


%changelog
* Sat Sep 11 2021 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- + packaged gem with Ruby Policy 2.0
