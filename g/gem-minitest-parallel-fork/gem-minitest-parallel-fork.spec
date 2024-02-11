%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname minitest-parallel_fork

Name:          gem-minitest-parallel-fork
Version:       2.0.0
Release:       alt1
Summary:       Fork-based parallelization for minitest
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/jeremyevans/minitest-parallel_fork
Vcs:           https://github.com/jeremyevans/minitest-parallel_fork.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest) >= 5.15.0
BuildRequires: gem(minitest-hooks) >= 0
BuildRequires: gem(minitest-global_expectations) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names minitest-parallel_fork,minitest-parallel-fork
Requires:      gem(minitest) >= 5.15.0
Provides:      gem(minitest-parallel_fork) = 2.0.0


%description
minitest-parallel_fork adds fork-based parallelization to Minitest. Each
test/spec suite is run in one of the forks, allowing this to work correctly when
using before_all/after_all/around_all hooks provided by minitest-hooks. Using
separate processes via fork can significantly improve spec performance when
using MRI, and can work in cases where Minitest's default thread-based
parallelism do not work, such as when specs modify the constant namespace.


%if_enabled doc
%package       -n gem-minitest-parallel-fork-doc
Version:       2.0.0
Release:       alt1
Summary:       Fork-based parallelization for minitest documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-parallel_fork
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-parallel_fork) = 2.0.0

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
%endif


%if_enabled devel
%package       -n gem-minitest-parallel-fork-devel
Version:       2.0.0
Release:       alt1
Summary:       Fork-based parallelization for minitest development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-parallel_fork
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-parallel_fork) = 2.0.0
Requires:      gem(minitest-hooks) >= 0
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
%endif


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

%if_enabled doc
%files         -n gem-minitest-parallel-fork-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled devel
%files         -n gem-minitest-parallel-fork-devel
%doc README.rdoc
%endif

%changelog
* Fri Feb 09 2024 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- ^ 1.2.0 -> 2.0.0

* Tue Jan 18 2022 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- + packaged gem with Ruby Policy 2.0
