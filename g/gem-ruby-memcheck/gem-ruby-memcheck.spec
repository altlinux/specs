%define        _unpackaged_files_terminate_build 1
%define        gemname ruby_memcheck

Name:          gem-ruby-memcheck
Version:       2.2.1
Release:       alt1
Summary:       Use Valgrind memcheck without going crazy
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/peterzhu2118/ruby_memcheck
Vcs:           https://github.com/peterzhu2118/ruby_memcheck.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(minitest-parallel_fork) >= 1.2
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rake-compiler) >= 1.1
BuildRequires: gem(rspec-core) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-shopify) >= 2.3
BuildRequires: gem(nokogiri) >= 0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(minitest-parallel_fork) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-shopify) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_alias_names ruby_memcheck,ruby-memcheck
Requires:      gem(nokogiri) >= 0
Provides:      gem(ruby_memcheck) = 2.2.1

%ruby_bindir_to %ruby_bindir

%description
This gem provides a sane way to use Valgrind's memcheck on your native extension
gem.


%package       -n memcheck
Version:       2.2.1
Release:       alt1
Summary:       Use Valgrind memcheck without going crazy executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета ruby_memcheck
Group:         Other
BuildArch:     noarch

Requires:      gem(ruby_memcheck) = 2.2.1

%description   -n memcheck
Use Valgrind memcheck without going crazy executable(s).

This gem provides a sane way to use Valgrind's memcheck on your native extension
gem.

%description   -n memcheck -l ru_RU.UTF-8
Исполнямка для самоцвета ruby_memcheck.


%package       -n gem-ruby-memcheck-doc
Version:       2.2.1
Release:       alt1
Summary:       Use Valgrind memcheck without going crazy documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby_memcheck
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby_memcheck) = 2.2.1

%description   -n gem-ruby-memcheck-doc
Use Valgrind memcheck without going crazy documentation files.

This gem provides a sane way to use Valgrind's memcheck on your native extension
gem.

%description   -n gem-ruby-memcheck-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby_memcheck.


%package       -n gem-ruby-memcheck-devel
Version:       2.2.1
Release:       alt1
Summary:       Use Valgrind memcheck without going crazy development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby_memcheck
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby_memcheck) = 2.2.1
Requires:      gem(minitest) >= 5.0
Requires:      gem(minitest-parallel_fork) >= 1.2
Requires:      gem(rake) >= 13.0
Requires:      gem(rake-compiler) >= 1.1
Requires:      gem(rspec-core) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-shopify) >= 2.3
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-parallel_fork) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-shopify) >= 3

%description   -n gem-ruby-memcheck-devel
Use Valgrind memcheck without going crazy development package.

This gem provides a sane way to use Valgrind's memcheck on your native extension
gem.

%description   -n gem-ruby-memcheck-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby_memcheck.


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

%files         -n memcheck
%doc README.md
%ruby_bindir/ruby_memcheck

%files         -n gem-ruby-memcheck-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-ruby-memcheck-devel
%doc README.md


%changelog
* Fri Dec 01 2023 Pavel Skrylev <majioa@altlinux.org> 2.2.1-alt1
- ^ 1.0.2 -> 2.2.1

* Tue Jan 18 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1
- + packaged gem with Ruby Policy 2.0
