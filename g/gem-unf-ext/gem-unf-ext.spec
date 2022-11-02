%define        gemname unf_ext

Name:          gem-unf-ext
Version:       0.0.8.2
Release:       alt1
Summary:       Unicode Normalization Form support library for CRuby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/knu/ruby-unf_ext
Vcs:           https://github.com/knu/ruby-unf_ext.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gcc-c++
%if_with check
BuildRequires: gem(rake) >= 0.9.2.2
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(rdoc) > 2.4.2
BuildRequires: gem(bundler) >= 1.2
BuildRequires: gem(rake-compiler) >= 1.1.1
BuildRequires: gem(rake-compiler-dock) >= 0.7
BuildRequires: gem(rake) >= 0.9.2.2
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(rdoc) > 2.4.2
BuildRequires: gem(bundler) >= 1.2
BuildRequires: gem(rake-compiler) >= 1.1.1
BuildRequires: gem(rake-compiler-dock) >= 0.7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake-compiler-dock >= 0.7,rake-compiler-dock < 1
%ruby_alias_names unf_ext,unf-ext
Obsoletes:     ruby-unf_ext < %EVR
Provides:      ruby-unf_ext = %EVR
Provides:      gem(unf_ext) = 0.0.8.2


%description
Unicode Normalization Form support library for CRuby.


%package       -n gem-unf-ext-doc
Version:       0.0.8.2
Release:       alt1
Summary:       Unicode Normalization Form support library for CRuby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета unf_ext
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(unf_ext) = 0.0.8.2
Obsoletes:     ruby-unf-ext-doc
Provides:      ruby-unf-ext-doc

%description   -n gem-unf-ext-doc
Unicode Normalization Form support library for CRuby documentation files.

%description   -n gem-unf-ext-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета unf_ext.


%package       -n gem-unf-ext-devel
Version:       0.0.8.2
Release:       alt1
Summary:       Unicode Normalization Form support library for CRuby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета unf_ext
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(unf_ext) = 0.0.8.2
Requires:      gem(rake) >= 0.9.2.2
Requires:      gem(test-unit) >= 0
Requires:      gem(rdoc) > 2.4.2
Requires:      gem(bundler) >= 1.2
Requires:      gem(rake-compiler) >= 1.1.1
Requires:      gem(rake-compiler-dock) >= 0.7

%description   -n gem-unf-ext-devel
Unicode Normalization Form support library for CRuby development package.

%description   -n gem-unf-ext-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета unf_ext.


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
%ruby_gemextdir

%files         -n gem-unf-ext-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-unf-ext-devel
%doc README.md


%changelog
* Thu Oct 27 2022 Pavel Skrylev <majioa@altlinux.org> 0.0.8.2-alt1
- ^ 0.0.8.1 -> 0.0.8.2

* Thu Mar 17 2022 Pavel Skrylev <majioa@altlinux.org> 0.0.8.1-alt1
- ^ 0.0.7.6 -> 0.0.8.1

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 0.0.7.6-alt1
- ^ 0.0.7.5 -> 0.0.7.6
- ! spec tags and syntax

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.0.7.5-alt2
- > Ruby Policy 2.0

* Wed Aug 22 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.7.5-alt1.3
- Rebuild for new Ruby autorequirements.
- Disable tests.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.7.5-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.7.5-alt1.1
- Rebuild with Ruby 2.5.0

* Tue Feb 06 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.7.5-alt1
- New version.

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 0.0.7.4-alt1.0.M80P.1
- Rebuild with Ruby 2.4.2

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.0.7.4-alt1.1
- Rebuild with Ruby 2.4.2

* Mon Sep 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.0.7.4-alt1
- Initial build for Sisyphus.
