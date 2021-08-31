%define        gemname domain_name

Name:          gem-domain-name
Version:       0.5.20190701
Release:       alt1.1
Summary:       Domain Name manipulation library for Ruby
License:       BSD-2-Clause or BSD-3-Clause or MPL-2.0
Group:         Development/Ruby
Url:           https://github.com/knu/ruby-domain_name
Vcs:           https://github.com/knu/ruby-domain_name.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(unf) < 1.0.0 gem(unf) >= 0.0.5
BuildRequires: gem(test-unit) >= 2.5.5 gem(test-unit) < 4
BuildRequires: gem(bundler) >= 1.2.0
BuildRequires: gem(rake) >= 0.9.2.2
BuildRequires: gem(rdoc) >= 2.4.2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency test-unit >= 3.3.5,test-unit < 4
%ruby_alias_names domain_name,domain-name
Requires:      gem(unf) < 1.0.0 gem(unf) >= 0.0.5
Obsoletes:     ruby-domain_name < %EVR
Provides:      ruby-domain_name = %EVR
Provides:      gem(domain_name) = 0.5.20190701


%description
This is a Domain Name manipulation library for Ruby. It can also be used for
cookie domain validation based on the Public Suffix List.


%package       -n gem-domain-name-doc
Version:       0.5.20190701
Release:       alt1.1
Summary:       Domain Name manipulation library for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета domain_name
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(domain_name) = 0.5.20190701

%description   -n gem-domain-name-doc
Domain Name manipulation library for Ruby documentation files.

This is a Domain Name manipulation library for Ruby. It can also be used for
cookie domain validation based on the Public Suffix List.

%description   -n gem-domain-name-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета domain_name.


%package       -n gem-domain-name-devel
Version:       0.5.20190701
Release:       alt1.1
Summary:       Domain Name manipulation library for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета domain_name
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(domain_name) = 0.5.20190701
Requires:      gem(test-unit) >= 2.5.5 gem(test-unit) < 4
Requires:      gem(bundler) >= 1.2.0
Requires:      gem(rake) >= 0.9.2.2
Requires:      gem(rdoc) >= 2.4.2

%description   -n gem-domain-name-devel
Domain Name manipulation library for Ruby development package.

This is a Domain Name manipulation library for Ruby. It can also be used for
cookie domain validation based on the Public Suffix List.

%description   -n gem-domain-name-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета domain_name.


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

%files         -n gem-domain-name-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-domain-name-devel
%doc README.md


%changelog
* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.20190701-alt1.1
- ! spec

* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.20190701-alt1
- 0.5.20180417 -> 0.5.20190701
- update to Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.20180417-alt1.1
- Rebuild with new Ruby autorequirements.
- Package as gem.

* Thu Apr 19 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.20180417-alt1
- New version.

* Mon Sep 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.5.20170404-alt1
- Initial build for Sisyphus.
