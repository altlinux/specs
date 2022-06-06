%define        gemname ZenTest

Name:          gem-zentest
Version:       4.12.1
Release:       alt1
Summary:       ZenTest provides 4 different tools: zentest, unit_diff, autotest, and multiruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/zentest
Vcs:           https://github.com/seattlerb/zentest.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(hoe) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(ZenTest) = 4.12.1


%description
ZenTest provides 4 different tools: zentest, unit_diff, autotest, and
multiruby.

zentest scans your target and unit-test code and writes your missing code based
on simple naming rules, enabling XP at a much quicker pace. zentest only works
with Ruby and Minitest or Test::Unit. There is enough evidence to show that this
is still proving useful to users, so it stays.

unit_diff is a command-line filter to diff expected results from actual results
and allow you to quickly see exactly what is wrong. Do note that minitest 2.2+
provides an enhanced assert_equal obviating the need for unit_diff

autotest is a continous testing facility meant to be used during development. As
soon as you save a file, autotest will run the corresponding dependent
tests.

multiruby runs anything you want on multiple versions of ruby. Great for
compatibility checking! Use multiruby_setup to manage your installed
versions.

*NOTE:* The next major release of zentest will not include autotest (use
minitest-autotest instead) and multiruby will use rbenv / ruby-build for version
management.


%package       -n zentest
Version:       4.12.1
Release:       alt1
Summary:       ZenTest provides 4 different tools: zentest, unit_diff, autotest, and multiruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета ZenTest
Group:         Other
BuildArch:     noarch

Requires:      gem(ZenTest) = 4.12.1

%description   -n zentest
ZenTest provides 4 different tools: zentest, unit_diff, autotest, and multiruby
executable(s).

%description   -n zentest -l ru_RU.UTF-8
Исполнямка для самоцвета ZenTest.


%package       -n gem-zentest-doc
Version:       4.12.1
Release:       alt1
Summary:       ZenTest provides 4 different tools: zentest, unit_diff, autotest, and multiruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ZenTest
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ZenTest) = 4.12.1

%description   -n gem-zentest-doc
ZenTest provides 4 different tools: zentest, unit_diff, autotest, and multiruby
documentation files.

%description   -n gem-zentest-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ZenTest.


%package       -n gem-zentest-devel
Version:       4.12.1
Release:       alt1
Summary:       ZenTest provides 4 different tools: zentest, unit_diff, autotest, and multiruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ZenTest
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ZenTest) = 4.12.1
Requires:      gem(rdoc) >= 4.0
Requires:      gem(hoe) >= 0

%description   -n gem-zentest-devel
ZenTest provides 4 different tools: zentest, unit_diff, autotest, and multiruby
development package.

%description   -n gem-zentest-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ZenTest.


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

%files         -n zentest
%doc README.txt
%_bindir/multigem
%_bindir/multiruby
%_bindir/unit_diff
%_bindir/zentest

%files         -n gem-zentest-doc
%doc README.txt
%ruby_gemdocdir

%files         -n gem-zentest-devel
%doc README.txt


%changelog
* Sun May 08 2022 Pavel Skrylev <majioa@altlinux.org> 4.12.1-alt1
- + packaged gem with Ruby Policy 2.0
