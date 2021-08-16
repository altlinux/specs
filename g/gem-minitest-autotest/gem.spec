%define        gemname minitest-autotest

Name:          gem-minitest-autotest
Version:       1.1.1
Release:       alt1
Summary:       autotest is a continous testing facility meant to be used during development
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/minitest-autotest
Vcs:           https://github.com/seattlerb/minitest-autotest.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest-server) >= 1.0 gem(minitest-server) < 2
BuildRequires: gem(path_expander) >= 1.0 gem(path_expander) < 2
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7
BuildRequires: gem(hoe) >= 3.22 gem(hoe) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
Requires:      gem(minitest-server) >= 1.0 gem(minitest-server) < 2
Requires:      gem(path_expander) >= 1.0 gem(path_expander) < 2
Provides:      gem(minitest-autotest) = 1.1.1


%description
autotest is a continous testing facility meant to be used during development. As
soon as you save a file, autotest will run the corresponding dependent
tests.

minitest-autotest is the latest incarnation of the venerable and wise autotest.
This time, it talks to minitest via minitest-server. As a result, there is no
output parsing. There are no regexps to tweak. There's no cruft or overhead.


%package       -n autotest
Version:       1.1.1
Release:       alt1
Summary:       autotest is a continous testing facility meant to be used during development executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета minitest-autotest
Group:         Other
BuildArch:     noarch

Requires:      gem(minitest-autotest) = 1.1.1

%description   -n autotest
autotest is a continous testing facility meant to be used during development
executable(s).

autotest is a continous testing facility meant to be used during development. As
soon as you save a file, autotest will run the corresponding dependent
tests.

minitest-autotest is the latest incarnation of the venerable and wise autotest.
This time, it talks to minitest via minitest-server. As a result, there is no
output parsing. There are no regexps to tweak. There's no cruft or overhead.

%description   -n autotest -l ru_RU.UTF-8
Исполнямка для самоцвета minitest-autotest.


%package       -n gem-minitest-autotest-doc
Version:       1.1.1
Release:       alt1
Summary:       autotest is a continous testing facility meant to be used during development documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-autotest
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-autotest) = 1.1.1

%description   -n gem-minitest-autotest-doc
autotest is a continous testing facility meant to be used during development
documentation files.

autotest is a continous testing facility meant to be used during development. As
soon as you save a file, autotest will run the corresponding dependent
tests.

minitest-autotest is the latest incarnation of the venerable and wise autotest.
This time, it talks to minitest via minitest-server. As a result, there is no
output parsing. There are no regexps to tweak. There's no cruft or overhead.

%description   -n gem-minitest-autotest-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-autotest.


%package       -n gem-minitest-autotest-devel
Version:       1.1.1
Release:       alt1
Summary:       autotest is a continous testing facility meant to be used during development development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-autotest
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-autotest) = 1.1.1
Requires:      gem(rdoc) >= 4.0 gem(rdoc) < 7
Requires:      gem(hoe) >= 3.22 gem(hoe) < 4

%description   -n gem-minitest-autotest-devel
autotest is a continous testing facility meant to be used during development
development package.

autotest is a continous testing facility meant to be used during development. As
soon as you save a file, autotest will run the corresponding dependent
tests.

minitest-autotest is the latest incarnation of the venerable and wise autotest.
This time, it talks to minitest via minitest-server. As a result, there is no
output parsing. There are no regexps to tweak. There's no cruft or overhead.

%description   -n gem-minitest-autotest-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-autotest.


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

%files         -n autotest
%doc README.rdoc
%_bindir/autotest

%files         -n gem-minitest-autotest-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-minitest-autotest-devel
%doc README.rdoc


%changelog
* Thu Jul 15 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- + packaged gem with Ruby Policy 2.0
