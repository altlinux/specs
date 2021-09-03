%define        gemname equatable

Name:          gem-equatable
Version:       0.7.0
Release:       alt1
Summary:       Allows ruby objects to implement equality comparison and inspection methods
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/piotrmurach/equatable
Vcs:           https://github.com/piotrmurach/equatable.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Provides:      gem(equatable) = 0.7.0


%description
By including this module, a class indicates that its instances have explicit
general contracts for hash, == and eql? methods. Specifically eql? contract
requires that it implements an equivalence relation. By default each instance of
the class is equal only to itself. This is a right behaviour when you have
distinct objects. However, it is the responsibility of any class to clearly
define their equality. Failure to do so may prevent instances to behave as
expected when for instance Array#uniq is invoked or when they are used as Hash
keys.


%package       -n gem-equatable-doc
Version:       0.7.0
Release:       alt1
Summary:       Allows ruby objects to implement equality comparison and inspection methods documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета equatable
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(equatable) = 0.7.0

%description   -n gem-equatable-doc
Allows ruby objects to implement equality comparison and inspection methods
documentation files.

By including this module, a class indicates that its instances have explicit
general contracts for hash, == and eql? methods. Specifically eql? contract
requires that it implements an equivalence relation. By default each instance of
the class is equal only to itself. This is a right behaviour when you have
distinct objects. However, it is the responsibility of any class to clearly
define their equality. Failure to do so may prevent instances to behave as
expected when for instance Array#uniq is invoked or when they are used as Hash
keys.

%description   -n gem-equatable-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета equatable.


%package       -n gem-equatable-devel
Version:       0.7.0
Release:       alt1
Summary:       Allows ruby objects to implement equality comparison and inspection methods development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета equatable
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(equatable) = 0.7.0
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4

%description   -n gem-equatable-devel
Allows ruby objects to implement equality comparison and inspection methods
development package.

By including this module, a class indicates that its instances have explicit
general contracts for hash, == and eql? methods. Specifically eql? contract
requires that it implements an equivalence relation. By default each instance of
the class is equal only to itself. This is a right behaviour when you have
distinct objects. However, it is the responsibility of any class to clearly
define their equality. Failure to do so may prevent instances to behave as
expected when for instance Array#uniq is invoked or when they are used as Hash
keys.

%description   -n gem-equatable-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета equatable.


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

%files         -n gem-equatable-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-equatable-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt1
- ^ 0.6.1 -> 0.7.0

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.1-alt1.1
- ! spec according to changelog rules

* Thu Aug 08 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.1-alt1
- + packaged gem with usage Ruby Policy 2.0
