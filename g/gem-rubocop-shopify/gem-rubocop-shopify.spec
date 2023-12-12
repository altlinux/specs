%define        _unpackaged_files_terminate_build 1
%define        gemname rubocop-shopify

Name:          gem-rubocop-shopify
Version:       2.14.0
Release:       alt1
Summary:       Shopify's style guide for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://shopify.github.io/ruby-style-guide/
Vcs:           https://github.com/shopify/ruby-style-guide/tree/v2.4.0.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(diffy) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(rubocop) >= 1.15.0
Conflicts:     gem(rubocop) >= 2
Provides:      gem(rubocop-shopify) = 2.14.0


%description
Gem containing the rubocop.yml config that corresponds to the implementation of
the Shopify's style guide for Ruby.


%package       -n gem-rubocop-shopify-devel
Version:       2.14.0
Release:       alt1
Summary:       Shopify's style guide for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-shopify
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-shopify) = 2.14.0
Requires:      gem(diffy) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(rake) >= 0

%description   -n gem-rubocop-shopify-devel
Shopify's style guide for Ruby development package.

Gem containing the rubocop.yml config that corresponds to the implementation of
the Shopify's style guide for Ruby.

%description   -n gem-rubocop-shopify-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-shopify.


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

%files         -n gem-rubocop-shopify-devel


%changelog
* Fri Dec 01 2023 Pavel Skrylev <majioa@altlinux.org> 2.14.0-alt1
- ^ 2.10.1 -> 2.14.0

* Wed Sep 21 2022 Pavel Skrylev <majioa@altlinux.org> 2.10.1-alt1
- ^ 2.4.0 -> 2.10.1

* Tue Jan 18 2022 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- + packaged gem with Ruby Policy 2.0
