%define        gemname minitest-pretty_diff

Name:          gem-minitest-pretty-diff
Version:       0.1.1
Release:       alt0.1
Summary:       Pretty-print hashes and arrays before diffing them in MiniTest
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/adammck/minitest-pretty_diff
Vcs:           https://github.com/adammck/minitest-pretty_diff.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_version minitest-pretty_diff:0.1.1
Provides:      gem(minitest-pretty_diff) = 0.1.1

%description
Monkey-patches MiniTest::Assertions#mu_pp to pretty-print hashes and arrays
before diffing them. This makes it much easier to spot the differences between
nested structures.


%package       -n gem-minitest-pretty-diff-doc
Version:       0.1.1
Release:       alt0.1
Summary:       Pretty-print hashes and arrays before diffing them in MiniTest documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-pretty_diff
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-pretty_diff) = 0.1.1

%description   -n gem-minitest-pretty-diff-doc
Pretty-print hashes and arrays before diffing them in MiniTest documentation
files.

Monkey-patches MiniTest::Assertions#mu_pp to pretty-print hashes and arrays
before diffing them. This makes it much easier to spot the differences between
nested structures.

%description   -n gem-minitest-pretty-diff-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-pretty_diff.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-minitest-pretty-diff-doc
%ruby_gemdocdir


%changelog
* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.1-alt0.1
- + packaged gem with Ruby Policy 2.0
