%define        gemname standard

Name:          gem-standard
Version:       1.1.1
Release:       alt1
Summary:       Ruby Style Guide, with linter & automatic code fixer
License:       ALT-XFree86-other and MIT
Group:         Development/Ruby
Url:           https://github.com/testdouble/standard
Vcs:           https://github.com/testdouble/standard.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rubocop) >= 1.13.0 gem(rubocop) < 2
BuildRequires: gem(rubocop-performance) >= 1.11.2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.13.0,rubocop < 2
%ruby_use_gem_dependency rubocop-performance >= 1.11.2
Requires:      gem(rubocop) >= 1.13.0 gem(rubocop) < 2
Requires:      gem(rubocop-performance) >= 1.11.2
Provides:      gem(standard) = 1.1.1

%description
This gem is a spiritual port of StandardJS and aims to save you (and others!)
time in the same three ways:

* No configuration. The easiest way to enforce consistent style in your project.
  Just drop it in.
* Automatically format code. Just run standardrb --fix and say goodbye to messy
  or inconsistent code.
* Catch style issues & programmer errors early. Save precious code review time
  by eliminating back-and-forth between reviewer & contributor.

No decisions to make. It just works. Here's a zap lightning talk zap about it.


%package       -n standardrb
Version:       1.1.1
Release:       alt1
Summary:       Ruby Style Guide, with linter & automatic code fixer executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета standard
Group:         Other
BuildArch:     noarch

Requires:      gem(standard) = 1.1.1

%description   -n standardrb
Ruby Style Guide, with linter & automatic code fixer executable(s).

This gem is a spiritual port of StandardJS and aims to save you (and others!)
time in the same three ways:

* No configuration. The easiest way to enforce consistent style in your project.
  Just drop it in.
* Automatically format code. Just run standardrb --fix and say goodbye to messy
  or inconsistent code.
* Catch style issues & programmer errors early. Save precious code review time
  by eliminating back-and-forth between reviewer & contributor.

No decisions to make. It just works. Here's a zap lightning talk zap about it.

%description   -n standardrb -l ru_RU.UTF-8
Исполнямка для самоцвета standard.


%package       -n gem-standard-doc
Version:       1.1.1
Release:       alt1
Summary:       Ruby Style Guide, with linter & automatic code fixer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета standard
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(standard) = 1.1.1

%description   -n gem-standard-doc
Ruby Style Guide, with linter & automatic code fixer documentation files.

This gem is a spiritual port of StandardJS and aims to save you (and others!)
time in the same three ways:

* No configuration. The easiest way to enforce consistent style in your project.
  Just drop it in.
* Automatically format code. Just run standardrb --fix and say goodbye to messy
  or inconsistent code.
* Catch style issues & programmer errors early. Save precious code review time
  by eliminating back-and-forth between reviewer & contributor.

No decisions to make. It just works. Here's a zap lightning talk zap about it.

%description   -n gem-standard-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета standard.


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

%files         -n standardrb
%doc README.md
%_bindir/standardrb

%files         -n gem-standard-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- + packaged gem with Ruby Policy 2.0
