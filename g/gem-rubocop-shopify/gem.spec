%define        gemname rubocop-shopify

Name:          gem-rubocop-shopify
Version:       2.4.0
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
BuildRequires: gem(rubocop) >= 1.15.0 gem(rubocop) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(rubocop) >= 1.15.0 gem(rubocop) < 2
Provides:      gem(rubocop-shopify) = 2.4.0

%ruby_on_build_rake_tasks generate

%description
Gem containing the rubocop.yml config that corresponds to the implementation of
the Shopify's style guide for Ruby.


%package       -n gem-rubocop-shopify-devel
Version:       2.4.0
Release:       alt1
Summary:       Shopify's style guide for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-shopify
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-shopify) = 2.4.0

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
* Tue Jan 18 2022 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- + packaged gem with Ruby Policy 2.0
