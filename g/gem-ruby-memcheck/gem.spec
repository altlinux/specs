%define        gemname ruby_memcheck

Name:          gem-ruby-memcheck
Version:       1.0.2
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
BuildRequires: gem(nokogiri) >= 0
BuildRequires: gem(minitest) >= 5.0 gem(minitest) < 6
BuildRequires: gem(minitest-parallel_fork) >= 1.2 gem(minitest-parallel_fork) < 2
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rake-compiler) >= 1.1 gem(rake-compiler) < 2
BuildRequires: gem(rspec-core) >= 0
BuildRequires: gem(rubocop) >= 1.15.0 gem(rubocop) < 2
BuildRequires: gem(rubocop-shopify) >= 2.3 gem(rubocop-shopify) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(nokogiri) >= 0
Provides:      gem(ruby_memcheck) = 1.0.2


%description
This gem provides a sane way to use Valgrind's memcheck on your native
extension gem.


%package       -n gem-ruby-memcheck-doc
Version:       1.0.2
Release:       alt1
Summary:       Use Valgrind memcheck without going crazy documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby_memcheck
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby_memcheck) = 1.0.2

%description   -n gem-ruby-memcheck-doc
Use Valgrind memcheck without going crazy documentation files.

This gem provides a sane way to use Valgrind's memcheck on your native
extension gem.

%description   -n gem-ruby-memcheck-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby_memcheck.


%package       -n gem-ruby-memcheck-devel
Version:       1.0.2
Release:       alt1
Summary:       Use Valgrind memcheck without going crazy development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby_memcheck
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby_memcheck) = 1.0.2
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6
Requires:      gem(minitest-parallel_fork) >= 1.2 gem(minitest-parallel_fork) < 2
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(rake-compiler) >= 1.1 gem(rake-compiler) < 2
Requires:      gem(rspec-core) >= 0
Requires:      gem(rubocop) >= 1.15.0 gem(rubocop) < 2
Requires:      gem(rubocop-shopify) >= 2.3 gem(rubocop-shopify) < 3

%description   -n gem-ruby-memcheck-devel
Use Valgrind memcheck without going crazy development package.

This gem provides a sane way to use Valgrind's memcheck on your native
extension gem.

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

%files         -n gem-ruby-memcheck-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-ruby-memcheck-devel
%doc README.md


%changelog
* Tue Jan 18 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1
- + packaged gem with Ruby Policy 2.0
