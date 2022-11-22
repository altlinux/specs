%define        gemname tins

Name:          gem-tins
Version:       1.32.1
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
%if_with check
BuildRequires: gem(gem_hadar) >= 1.12.0 gem(gem_hadar) < 2
BuildRequires: gem(utils) >= 0
BuildRequires: gem(all_images) >= 0
BuildRequires: gem(debug) >= 0
BuildRequires: gem(term-ansicolor) >= 0
BuildRequires: gem(test-unit) >= 3.1 gem(test-unit) < 4
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(sync) >= 0
BuildRequires: gem(gem_hadar) >= 1.12.0 gem(gem_hadar) < 2
BuildRequires: gem(utils) >= 0
BuildRequires: gem(all_images) >= 0
BuildRequires: gem(debug) >= 0
BuildRequires: gem(term-ansicolor) >= 0
BuildRequires: gem(test-unit) >= 3.1 gem(test-unit) < 4
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(sync) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency gem_hadar >= 1.12.0,gem_hadar < 2
Requires:      gem(sync) >= 0
Obsoletes:     ruby-tins < %EVR
Provides:      ruby-tins = %EVR
Provides:      gem(tins) = 1.32.1


%description
All the stuff that isn't good/big enough for a real library.


%package       -n gem-tins-doc
Version:       1.32.1
Release:       alt1
Summary:       All the stuff that isn't good/big enough for a real library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета tins
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(tins) = 1.32.1

%description   -n gem-tins-doc
All the stuff that isn't good/big enough for a real library documentation files.

%description   -n gem-tins-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета tins.


%package       -n gem-tins-devel
Version:       1.32.1
Release:       alt1
Summary:       All the stuff that isn't good/big enough for a real library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета tins
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(tins) = 1.32.1
Requires:      gem(gem_hadar) >= 1.12.0 gem(gem_hadar) < 2
Requires:      gem(utils) >= 0
Requires:      gem(all_images) >= 0
Requires:      gem(debug) >= 0
Requires:      gem(term-ansicolor) >= 0
Requires:      gem(test-unit) >= 3.1 gem(test-unit) < 4
Requires:      gem(simplecov) >= 0

%description   -n gem-tins-devel
All the stuff that isn't good/big enough for a real library development package.

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
* Tue Nov 22 2022 Pavel Skrylev <majioa@altlinux.org> 1.32.1-alt1
- ^ 1.31.1 -> 1.32.1

* Wed Jul 06 2022 Pavel Skrylev <majioa@altlinux.org> 1.31.1-alt1
- ^ 1.29.0 -> 1.31.1

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.29.0-alt1
- ^ 1.20.2 -> 1.29.0

* Fri Mar 01 2019 Pavel Skrylev <majioa@altlinux.org> 1.20.2-alt1
- Bump to 1.20.2;
- Use Ruby Policy 2.0.

* Mon Oct 15 2018 Andrey Cherepanov <cas@altlinux.org> 1.17.0-alt1
- New version.

* Wed Sep 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.16.3-alt1
- Initial build for Sisyphus
