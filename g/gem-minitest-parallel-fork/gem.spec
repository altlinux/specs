%define        gemname minitest-parallel_fork

Name:          gem-minitest-parallel-fork
Version:       1.2.0
Release:       alt1
Summary:       Fork-based parallelization for minitest
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/jeremyevans/minitest-parallel_fork
Vcs:           https://github.com/jeremyevans/minitest-parallel_fork.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) >= 5.11.0 gem(minitest) < 6
BuildRequires: gem(minitest-global_expectations) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Provides:      gem(minitest-parallel_fork) = 1.2.0


%description
minitest-parallel_fork adds fork-based parallelization to Minitest. Each
test/spec suite is run in one of the forks, allowing this to work correctly when
using before_all/after_all/around_all hooks provided by minitest-hooks. Using
separate processes via fork can significantly improve spec performance when
using MRI, and can work in cases where Minitest's default thread-based
parallelism do not work, such as when specs modify the constant namespace.


%package       -n gem-minitest-parallel-fork-doc
Version:       1.2.0
Release:       alt1
Summary:       Fork-based parallelization for minitest documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-parallel_fork
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-parallel_fork) = 1.2.0

%description   -n gem-minitest-parallel-fork-doc
Fork-based parallelization for minitest documentation
files.

minitest-parallel_fork adds fork-based parallelization to Minitest. Each
test/spec suite is run in one of the forks, allowing this to work correctly when
using before_all/after_all/around_all hooks provided by minitest-hooks. Using
separate processes via fork can significantly improve spec performance when
using MRI, and can work in cases where Minitest's default thread-based
parallelism do not work, such as when specs modify the constant namespace.

%description   -n gem-minitest-parallel-fork-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-parallel_fork.


%package       -n gem-minitest-parallel-fork-devel
Version:       1.2.0
Release:       alt1
Summary:       Fork-based parallelization for minitest development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-parallel_fork
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-parallel_fork) = 1.2.0
Requires:      gem(minitest) >= 5.11.0 gem(minitest) < 6
Requires:      gem(minitest-global_expectations) >= 0

%description   -n gem-minitest-parallel-fork-devel
Fork-based parallelization for minitest development
package.

minitest-parallel_fork adds fork-based parallelization to Minitest. Each
test/spec suite is run in one of the forks, allowing this to work correctly when
using before_all/after_all/around_all hooks provided by minitest-hooks. Using
separate processes via fork can significantly improve spec performance when
using MRI, and can work in cases where Minitest's default thread-based
parallelism do not work, such as when specs modify the constant namespace.

%description   -n gem-minitest-parallel-fork-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-parallel_fork.


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

%files         -n gem-minitest-parallel-fork-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-minitest-parallel-fork-devel
%doc README.rdoc


%changelog
* Tue Jan 18 2022 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- + packaged gem with Ruby Policy 2.0
