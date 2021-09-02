%define        gemname tins

Name:          gem-tins
Version:       1.29.0
Release:       alt1
Summary:       All the stuff that isn't good/big enough for a real library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/flori/tins
Vcs:           https://github.com/flori/tins.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(gem_hadar) >= 1.11.0 gem(gem_hadar) < 1.12
BuildRequires: gem(test-unit) >= 3.1 gem(test-unit) < 4
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(sync) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(sync) >= 0
Obsoletes:     ruby-tins < %EVR
Provides:      ruby-tins = %EVR
Provides:      gem(tins) = 1.29.0


%description
All the stuff that isn't good/big enough for a real library.


%package       -n gem-tins-doc
Version:       1.29.0
Release:       alt1
Summary:       All the stuff that isn't good/big enough for a real library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета tins
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(tins) = 1.29.0

%description   -n gem-tins-doc
All the stuff that isn't good/big enough for a real library documentation
files.

%description   -n gem-tins-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета tins.


%package       -n gem-tins-devel
Version:       1.29.0
Release:       alt1
Summary:       All the stuff that isn't good/big enough for a real library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета tins
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(tins) = 1.29.0
Requires:      gem(gem_hadar) >= 1.11.0 gem(gem_hadar) < 1.12
Requires:      gem(test-unit) >= 3.1 gem(test-unit) < 4
Requires:      gem(simplecov) >= 0

%description   -n gem-tins-devel
All the stuff that isn't good/big enough for a real library development
package.

%description   -n gem-tins-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета tins.


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

%files         -n gem-tins-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-tins-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.29.0-alt1
- ^ 1.20.2 -> 1.29.0

* Fri Mar 01 2019 Pavel Skrylev <majioa@altlinux.org> 1.20.2-alt1
- Bump to 1.20.2;
- Use Ruby Policy 2.0.

* Mon Oct 15 2018 Andrey Cherepanov <cas@altlinux.org> 1.17.0-alt1
- New version.

* Wed Sep 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.16.3-alt1
- Initial build for Sisyphus
