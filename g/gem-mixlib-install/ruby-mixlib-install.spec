%define        gemname mixlib-install

Name:          gem-mixlib-install
Version:       3.12.11
Release:       alt1
Summary:       A library for interacting with Chef Software Inc's software distribution systems
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/mixlib-install
Vcs:           https://github.com/chef/mixlib-install.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(mixlib-shellout) >= 0
BuildRequires: gem(mixlib-versioning) >= 0
BuildRequires: gem(thor) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names acceptance
Requires:      gem(mixlib-shellout) >= 0
Requires:      gem(mixlib-versioning) >= 0
Requires:      gem(thor) >= 0
Obsoletes:     ruby-mixlib-install < %EVR
Provides:      ruby-mixlib-install = %EVR
Provides:      gem(mixlib-install) = 3.12.11


%description
A library for interacting with Chef Software Inc's software distribution
systems.


%package       -n mixlib-install
Version:       3.12.11
Release:       alt1
Summary:       A library for interacting with Chef Software Inc's software distribution systems executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета mixlib-install
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mixlib-install) = 3.12.11

%description   -n mixlib-install
A library for interacting with Chef Software Inc's software distribution systems
executable(s).

%description   -n mixlib-install -l ru_RU.UTF-8
Исполнямка для самоцвета mixlib-install.


%package       -n gem-mixlib-install-doc
Version:       3.12.11
Release:       alt1
Summary:       A library for interacting with Chef Software Inc's software distribution systems documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mixlib-install
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mixlib-install) = 3.12.11

%description   -n gem-mixlib-install-doc
A library for interacting with Chef Software Inc's software distribution systems
documentation files.

%description   -n gem-mixlib-install-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mixlib-install.


%package       -n gem-mixlib-install-devel
Version:       3.12.11
Release:       alt1
Summary:       A library for interacting with Chef Software Inc's software distribution systems development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mixlib-install
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mixlib-install) = 3.12.11

%description   -n gem-mixlib-install-devel
A library for interacting with Chef Software Inc's software distribution systems
development package.

%description   -n gem-mixlib-install-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mixlib-install.


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

%files         -n mixlib-install
%_bindir/mixlib-install

%files         -n gem-mixlib-install-doc
%ruby_gemdocdir

%files         -n gem-mixlib-install-devel


%changelog
* Wed Jun 30 2021 Pavel Skrylev <majioa@altlinux.org> 3.12.11-alt1
- ^ 3.11.20 -> 3.12.11

* Fri Jul 12 2019 Pavel Skrylev <majioa@altlinux.org> 3.11.20-alt1
- Fix spec
- Bump to 3.11.20

* Thu Apr 04 2019 Pavel Skrylev <majioa@altlinux.org> 3.11.11-alt1
- Bump to 3.11.11
- Use Ruby Policy 2.0

* Tue Nov 20 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.7-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.6-alt1
- New version.

* Sun Jul 08 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.1-alt1
- New version.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.0-alt1
- New version.
- Package as gem.

* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 3.10.0-alt1
- Initial build for Sisyphus
