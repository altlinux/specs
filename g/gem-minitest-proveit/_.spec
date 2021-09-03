%define        gemname minitest-proveit

Name:          gem-minitest-proveit
Version:       1.0.0
Release:       alt1.1
Summary:       minitest-proveit forces all tests to prove success
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/minitest-proveit
Vcs:           https://github.com/seattlerb/minitest-proveit.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) >= 5 gem(minitest) < 7
BuildRequires: gem(hoe) >= 3.15 gem(hoe) < 4
BuildRequires: gem(rdoc) >= 4 gem(rdoc) < 7

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.0,rdoc < 7
Provides:      gem(minitest-proveit) = 1.0.0

%description
Originally written by github user bradleyjames, minitest-proveit forces all
tests to prove success (via at least one assertion) rather than rely on the
absence of failure.


%package       -n gem-minitest-proveit-doc
Version:       1.0.0
Release:       alt1.1
Summary:       minitest-proveit forces all tests to prove success documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-proveit
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-proveit) = 1.0.0

%description   -n gem-minitest-proveit-doc
minitest-proveit forces all tests to prove success documentation
files.

Originally written by github user bradleyjames, minitest-proveit forces all
tests to prove success (via at least one assertion) rather than rely on the
absence of failure.

%description   -n gem-minitest-proveit-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-proveit.


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

%files         -n gem-minitest-proveit-doc
%ruby_gemdocdir


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1.1
- ! spec

* Tue Oct 22 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
