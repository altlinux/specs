%define        gemname fivemat

Name:          gem-fivemat
Version:       1.3.7
Release:       alt1
Summary:       Why settle for a test output format when you could have a test output fivemat?
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/tpope/fivemat
Vcs:           https://github.com/tpope/fivemat.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(fivemat) = 1.3.7


%description
MiniTest/RSpec/Cucumber formatter that gives each test file its own line of
dots. Why settle for a test output format when you can have a test output
fivemat?

I'm tired of the two de facto standards for test output:

* Bunch of dots - Wait till the end to see what failed, and guess the dot count
  to estimate progress.
* Extreme verbosity - See failures as they happen if you pay very, very close
  attention.

In other words, you can choose between "too little" or "too much."
I've looked at third party alternatives, but none of them did much for me. What
I want is the middle ground: dots grouped by file. Thus, I give you Fivemat.
MiniTest, RSpec, and Cucumber are supported.


%package       -n gem-fivemat-doc
Version:       1.3.7
Release:       alt1
Summary:       Why settle for a test output format when you could have a test output fivemat? documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fivemat
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fivemat) = 1.3.7

%description   -n gem-fivemat-doc
Why settle for a test output format when you could have a test output fivemat?
documentation files.

MiniTest/RSpec/Cucumber formatter that gives each test file its own line of
dots. Why settle for a test output format when you can have a test output
fivemat?

I'm tired of the two de facto standards for test output:

* Bunch of dots - Wait till the end to see what failed, and guess the dot count
  to estimate progress.
* Extreme verbosity - See failures as they happen if you pay very, very close
  attention.

In other words, you can choose between "too little" or "too much."
I've looked at third party alternatives, but none of them did much for me. What
I want is the middle ground: dots grouped by file. Thus, I give you Fivemat.
MiniTest, RSpec, and Cucumber are supported.

%description   -n gem-fivemat-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fivemat.


%package       -n gem-fivemat-devel
Version:       1.3.7
Release:       alt1
Summary:       Why settle for a test output format when you could have a test output fivemat? development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fivemat
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fivemat) = 1.3.7
Requires:      gem(rake) >= 0 gem(rake) < 14

%description   -n gem-fivemat-devel
Why settle for a test output format when you could have a test output fivemat?
development package.

MiniTest/RSpec/Cucumber formatter that gives each test file its own line of
dots. Why settle for a test output format when you can have a test output
fivemat?

I'm tired of the two de facto standards for test output:

* Bunch of dots - Wait till the end to see what failed, and guess the dot count
  to estimate progress.
* Extreme verbosity - See failures as they happen if you pay very, very close
  attention.

In other words, you can choose between "too little" or "too much."
I've looked at third party alternatives, but none of them did much for me. What
I want is the middle ground: dots grouped by file. Thus, I give you Fivemat.
MiniTest, RSpec, and Cucumber are supported.

%description   -n gem-fivemat-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fivemat.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.markdown
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-fivemat-doc
%doc README.markdown
%ruby_gemdocdir

%files         -n gem-fivemat-devel
%doc README.markdown


%changelog
* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.7-alt1
- + packaged gem with Ruby Policy 2.0
