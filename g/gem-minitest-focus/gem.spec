%define        gemname minitest-focus

Name:          gem-minitest-focus
Version:       1.3.1
Release:       alt1
Summary:       Allows you to focus on a few tests with ease without having to use command-line arguments
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/minitest-focus
Vcs:           https://github.com/seattlerb/minitest-focus.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) >= 4 gem(minitest) < 6
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7
BuildRequires: gem(hoe) >= 3.22 gem(hoe) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Requires:      gem(minitest) >= 4 gem(minitest) < 6
Provides:      gem(minitest-focus) = 1.3.1


%description
Allows you to focus on a few tests with ease without having to use command-line
arguments. Good for tools like guard that don't have enough brains to understand
test output. Cf. ZenTest's autotest (an example of a test runner with strong
testing logic).

Inspired by https://github.com/seattlerb/minitest/issues/213


%package       -n gem-minitest-focus-doc
Version:       1.3.1
Release:       alt1
Summary:       Allows you to focus on a few tests with ease without having to use command-line arguments documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-focus
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-focus) = 1.3.1

%description   -n gem-minitest-focus-doc
Allows you to focus on a few tests with ease without having to use command-line
arguments documentation files.

Allows you to focus on a few tests with ease without having to use command-line
arguments. Good for tools like guard that don't have enough brains to understand
test output. Cf. ZenTest's autotest (an example of a test runner with strong
testing logic).

Inspired by https://github.com/seattlerb/minitest/issues/213

%description   -n gem-minitest-focus-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-focus.


%package       -n gem-minitest-focus-devel
Version:       1.3.1
Release:       alt1
Summary:       Allows you to focus on a few tests with ease without having to use command-line arguments development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-focus
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-focus) = 1.3.1
Requires:      gem(rdoc) >= 4.0 gem(rdoc) < 7
Requires:      gem(hoe) >= 3.22 gem(hoe) < 4

%description   -n gem-minitest-focus-devel
Allows you to focus on a few tests with ease without having to use command-line
arguments development package.

Allows you to focus on a few tests with ease without having to use command-line
arguments. Good for tools like guard that don't have enough brains to understand
test output. Cf. ZenTest's autotest (an example of a test runner with strong
testing logic).

Inspired by https://github.com/seattlerb/minitest/issues/213

%description   -n gem-minitest-focus-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-focus.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.txt
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-minitest-focus-doc
%doc README.txt
%ruby_gemdocdir

%files         -n gem-minitest-focus-devel
%doc README.txt


%changelog
* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.1-alt1
- + packaged gem with Ruby Policy 2.0
