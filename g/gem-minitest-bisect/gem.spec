%define        gemname minitest-bisect

Name:          gem-minitest-bisect
Version:       1.5.1
Release:       alt1
Summary:       Hunting down random test failures can be very very difficult, sometimes impossible, but minitest-bisect makes it easy
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/minitest-bisect
Vcs:           https://github.com/seattlerb/minitest-bisect.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest-server) >= 1.0 gem(minitest-server) < 2
BuildRequires: gem(path_expander) >= 1.1 gem(path_expander) < 2
BuildRequires: gem(rake) > 0 gem(rake) < 14
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7
BuildRequires: gem(hoe) >= 3.22 gem(hoe) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
Requires:      gem(minitest-server) >= 1.0 gem(minitest-server) < 2
Requires:      gem(path_expander) >= 1.1 gem(path_expander) < 2
Provides:      gem(minitest-bisect) = 1.5.1


%description
Hunting down random test failures can be very very difficult, sometimes
impossible, but minitest-bisect makes it easy.

minitest-bisect helps you isolate and debug random test failures.

If your tests only fail randomly, you can reproduce the error consistently by
using `--seed <num>`, but what then? How do you figure out which combination of
tests out of hundreds are responsible for the failure? You know which test is
failing, but what others are causing it to fail or were helping it succeed in a
different order? That's what minitest-bisect does best.


%package       -n minitest-bisect
Version:       1.5.1
Release:       alt1
Summary:       Hunting down random test failures can be very very difficult, sometimes impossible, but minitest-bisect makes it easy executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета minitest-bisect
Group:         Other
BuildArch:     noarch

Requires:      gem(minitest-bisect) = 1.5.1

%description   -n minitest-bisect
Hunting down random test failures can be very very difficult, sometimes
impossible, but minitest-bisect makes it easy executable(s).

Hunting down random test failures can be very very difficult, sometimes
impossible, but minitest-bisect makes it easy.

minitest-bisect helps you isolate and debug random test failures.

If your tests only fail randomly, you can reproduce the error consistently by
using `--seed <num>`, but what then? How do you figure out which combination of
tests out of hundreds are responsible for the failure? You know which test is
failing, but what others are causing it to fail or were helping it succeed in a
different order? That's what minitest-bisect does best.

%description   -n minitest-bisect -l ru_RU.UTF-8
Исполнямка для самоцвета minitest-bisect.


%package       -n gem-minitest-bisect-doc
Version:       1.5.1
Release:       alt1
Summary:       Hunting down random test failures can be very very difficult, sometimes impossible, but minitest-bisect makes it easy documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-bisect
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-bisect) = 1.5.1

%description   -n gem-minitest-bisect-doc
Hunting down random test failures can be very very difficult, sometimes
impossible, but minitest-bisect makes it easy documentation files.

Hunting down random test failures can be very very difficult, sometimes
impossible, but minitest-bisect makes it easy.

minitest-bisect helps you isolate and debug random test failures.

If your tests only fail randomly, you can reproduce the error consistently by
using `--seed <num>`, but what then? How do you figure out which combination of
tests out of hundreds are responsible for the failure? You know which test is
failing, but what others are causing it to fail or were helping it succeed in a
different order? That's what minitest-bisect does best.

%description   -n gem-minitest-bisect-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-bisect.


%package       -n gem-minitest-bisect-devel
Version:       1.5.1
Release:       alt1
Summary:       Hunting down random test failures can be very very difficult, sometimes impossible, but minitest-bisect makes it easy development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-bisect
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-bisect) = 1.5.1
Requires:      gem(rake) > 0 gem(rake) < 14
Requires:      gem(rdoc) >= 4.0 gem(rdoc) < 7
Requires:      gem(hoe) >= 3.22 gem(hoe) < 4

%description   -n gem-minitest-bisect-devel
Hunting down random test failures can be very very difficult, sometimes
impossible, but minitest-bisect makes it easy development package.

Hunting down random test failures can be very very difficult, sometimes
impossible, but minitest-bisect makes it easy.

minitest-bisect helps you isolate and debug random test failures.

If your tests only fail randomly, you can reproduce the error consistently by
using `--seed <num>`, but what then? How do you figure out which combination of
tests out of hundreds are responsible for the failure? You know which test is
failing, but what others are causing it to fail or were helping it succeed in a
different order? That's what minitest-bisect does best.

%description   -n gem-minitest-bisect-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-bisect.


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

%files         -n minitest-bisect
%doc README.rdoc
%_bindir/minitest_bisect

%files         -n gem-minitest-bisect-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-minitest-bisect-devel
%doc README.rdoc


%changelog
* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 1.5.1-alt1
- + packaged gem with Ruby Policy 2.0
