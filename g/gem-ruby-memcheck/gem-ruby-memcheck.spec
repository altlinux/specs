%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname ruby_memcheck

Name:          gem-ruby-memcheck
Version:       3.0.1
Release:       alt1
Summary:       Use Valgrind memcheck without going crazy
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/peterzhu2118/ruby_memcheck
Vcs:           https://github.com/peterzhu2118/ruby_memcheck.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(minitest-parallel_fork) >= 2.0
BuildRequires: gem(nokogiri) >= 0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rake-compiler) >= 1.1
BuildRequires: gem(rspec-core) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-shopify) >= 2.3
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(minitest-parallel_fork) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-shopify) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency minitest >= 6.0,minitest < 7
%ruby_alias_names ruby_memcheck,ruby-memcheck
Requires:      ruby >= 3.0.0
Requires:      gem(nokogiri) >= 0
Provides:      ruby_memcheck = %EVR
Provides:      gem(ruby_memcheck) = 3.0.1

%description
This gem provides a sane way to use Valgrind's memcheck on your native extension
gem.


%package       -n ruby-memcheck
Version:       3.0.1
Release:       alt1
Summary:       Use Valgrind memcheck without going crazy executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета ruby_memcheck
Group:         Other
BuildArch:     noarch

Requires:      gem(ruby_memcheck) = 3.0.1

%description   -n ruby-memcheck
Use Valgrind memcheck without going crazy executable(s).

This gem provides a sane way to use Valgrind's memcheck on your native extension
gem.

%description   -n ruby-memcheck -l ru_RU.UTF-8
Исполнямка для самоцвета ruby_memcheck.


%if_enabled    doc
%package       -n gem-ruby-memcheck-doc
Version:       3.0.1
Release:       alt1
Summary:       Use Valgrind memcheck without going crazy documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby_memcheck
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby_memcheck) = 3.0.1

%description   -n gem-ruby-memcheck-doc
Use Valgrind memcheck without going crazy documentation files.

This gem provides a sane way to use Valgrind's memcheck on your native extension
gem.

%description   -n gem-ruby-memcheck-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby_memcheck.
%endif


%if_enabled    devel
%package       -n gem-ruby-memcheck-devel
Version:       3.0.1
Release:       alt1
Summary:       Use Valgrind memcheck without going crazy development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby_memcheck
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby_memcheck) = 3.0.1
Requires:      gem(minitest) >= 5.0
Requires:      gem(minitest-parallel_fork) >= 2.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rake-compiler) >= 1.1
Requires:      gem(rspec-core) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-shopify) >= 2.3
Conflicts:     gem(minitest) >= 7
Conflicts:     gem(minitest-parallel_fork) >= 3
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
%doc LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n ruby-memcheck
%doc LICENSE.txt README.md
%_bindir/ruby_memcheck

%if_enabled    doc
%files         -n gem-ruby-memcheck-doc
%doc LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ruby-memcheck-devel
%doc LICENSE.txt README.md
%endif


%changelog
* Mon Aug 31 2026 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- ^ 3.0.0 -> 3.0.1

* Tue Jul 23 2024 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- ^ 2.2.1 -> 3.0.0

* Fri Dec 01 2023 Pavel Skrylev <majioa@altlinux.org> 2.2.1-alt1
- ^ 1.0.2 -> 2.2.1

* Tue Jan 18 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1
- + packaged gem with Ruby Policy 2.0
