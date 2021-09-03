%define        gemname liquid

Name:          gem-liquid
Version:       5.0.1
Release:       alt1
Summary:       Liquid markup language
License:       MIT
Group:         Development/Ruby
Url:           https://shopify.github.io/liquid/
Vcs:           https://github.com/shopify/liquid.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(minitest) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(liquid) = 5.0.1


%description
Liquid is a template engine which was written with very specific
requirements:

* It has to have beautiful and simple markup. Template engines which don't
produce good looking markup are no fun to use.
* It needs to be non evaling and secure. Liquid templates are made so that users
can edit them. You don't want to run code on your server which your users
wrote.
* It has to be stateless. Compile and render steps have to be separate so that
the expensive parsing and compiling can be done once and later on you can just
render it passing in a hash with local variables and objects.


%package       -n gem-liquid-doc
Version:       5.0.1
Release:       alt1
Summary:       Liquid markup language documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета liquid
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(liquid) = 5.0.1

%description   -n gem-liquid-doc
Liquid markup language documentation files.

Liquid is a template engine which was written with very specific
requirements:

* It has to have beautiful and simple markup. Template engines which don't
produce good looking markup are no fun to use.
* It needs to be non evaling and secure. Liquid templates are made so that users
can edit them. You don't want to run code on your server which your users
wrote.
* It has to be stateless. Compile and render steps have to be separate so that
the expensive parsing and compiling can be done once and later on you can just
render it passing in a hash with local variables and objects.

%description   -n gem-liquid-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета liquid.


%package       -n gem-liquid-devel
Version:       5.0.1
Release:       alt1
Summary:       Liquid markup language development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета liquid
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(liquid) = 5.0.1
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(minitest) >= 0

%description   -n gem-liquid-devel
Liquid markup language development package.

Liquid is a template engine which was written with very specific
requirements:

* It has to have beautiful and simple markup. Template engines which don't
produce good looking markup are no fun to use.
* It needs to be non evaling and secure. Liquid templates are made so that users
can edit them. You don't want to run code on your server which your users
wrote.
* It has to be stateless. Compile and render steps have to be separate so that
the expensive parsing and compiling can be done once and later on you can just
render it passing in a hash with local variables and objects.

%description   -n gem-liquid-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета liquid.


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

%files         -n gem-liquid-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-liquid-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 5.0.1-alt1
- ^ 4.0.3 -> 5.0.1

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 4.0.3-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
