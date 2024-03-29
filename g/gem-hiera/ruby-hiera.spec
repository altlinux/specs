%define        gemname hiera

Name:          gem-hiera
Version:       3.9.0
Release:       alt1
Summary:       A simple pluggable Hierarchical Database
License:       Apache-2.0
Group:         Development/Ruby
Url:           http://projects.puppetlabs.com/projects/hiera/
Vcs:           https://github.com/puppetlabs/hiera.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR
Provides:      gem(hiera) = 3.9.0


%description
A simple pluggable Hierarchical Database.


%package       -n hiera
Version:       3.9.0
Release:       alt1
Summary:       A simple pluggable Hierarchical Database executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета hiera
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hiera) = 3.9.0

%description   -n hiera
A simple pluggable Hierarchical Database executable(s).

%description   -n hiera -l ru_RU.UTF-8
Исполнямка для самоцвета hiera.


%package       -n gem-hiera-doc
Version:       3.9.0
Release:       alt1
Summary:       A simple pluggable Hierarchical Database documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hiera
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hiera) = 3.9.0

%description   -n gem-hiera-doc
A simple pluggable Hierarchical Database documentation files.

%description   -n gem-hiera-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hiera.


%package       -n gem-hiera-devel
Version:       3.9.0
Release:       alt1
Summary:       A simple pluggable Hierarchical Database development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hiera
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hiera) = 3.9.0

%description   -n gem-hiera-devel
A simple pluggable Hierarchical Database development package.

%description   -n gem-hiera-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hiera.


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

%files         -n hiera
%_bindir/hiera

%files         -n gem-hiera-doc
%ruby_gemdocdir

%files         -n gem-hiera-devel


%changelog
* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 3.9.0-alt1
- ^ 3.6.0 -> 3.9.0

* Tue Sep 15 2020 Pavel Skrylev <majioa@altlinux.org> 3.6.0-alt1
- ^ 3.6.0pre -> 3.6.0
- ! spec tags

* Fri Jul 12 2019 Pavel Skrylev <majioa@altlinux.org> 3.6.0-alt0.1
- ^ 3.5.0 -> 3.6.0 pre
- ! spec

* Fri Feb 22 2019 Pavel Skrylev <majioa@altlinux.org> 3.5.0-alt1
- Bump to 3.5.0;
- Use Ruby Policy 2.0.

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 3.4.5-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.4.4-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.4.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Sat Apr 14 2018 Andrey Cherepanov <cas@altlinux.org> 3.4.3-alt1
- New version.

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 3.4.2-alt1
- New version

* Wed Sep 13 2017 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt1
- New version

* Sat Sep 09 2017 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1.1
- Rebuild with Ruby 2.4.1

* Sat Jul 01 2017 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- New version

* Tue Jun 13 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.2-alt1
- New version

* Mon Mar 13 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.1-alt1
- New version

* Wed Mar 01 2017 Andrey Cherepanov <cas@altlinux.org> 3.3.0-alt1
- New version
- Remove autoreq on win32/dir

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.2-alt1
- new version 3.2.2

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 3.2.0-alt1
- New version

* Wed Apr 23 2014 Andrey Cherepanov <cas@altlinux.org> 1.3.2-alt1
- Initial build for ALT Linux
