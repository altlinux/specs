%define        gemname mixlib-archive

Name:          gem-mixlib-archive
Version:       1.1.7
Release:       alt1
Summary:       A very simple gem to create and extract archives
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/mixlib-archive
Vcs:           https://github.com/chef/mixlib-archive.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(mixlib-log) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(mixlib-log) >= 0
Obsoletes:     ruby-mixlib-archive < %EVR
Provides:      ruby-mixlib-archive = %EVR
Provides:      gem(mixlib-archive) = 1.1.7


%description
A simple interface to various archive formats.


%package       -n gem-mixlib-archive-doc
Version:       1.1.7
Release:       alt1
Summary:       A very simple gem to create and extract archives documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mixlib-archive
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mixlib-archive) = 1.1.7

%description   -n gem-mixlib-archive-doc
A very simple gem to create and extract archives documentation files.

A simple interface to various archive formats.

%description   -n gem-mixlib-archive-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mixlib-archive.


%package       -n gem-mixlib-archive-devel
Version:       1.1.7
Release:       alt1
Summary:       A very simple gem to create and extract archives development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mixlib-archive
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mixlib-archive) = 1.1.7

%description   -n gem-mixlib-archive-devel
A very simple gem to create and extract archives development package.

A simple interface to various archive formats.

%description   -n gem-mixlib-archive-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mixlib-archive.


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

%files         -n gem-mixlib-archive-doc
%ruby_gemdocdir

%files         -n gem-mixlib-archive-devel


%changelog
* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.7-alt1
- ^ 0.4.18 -> 1.1.7

* Tue Oct 16 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.18-alt1
- New version.

* Mon Oct 15 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.17-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.16-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.9-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 22 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.9-alt1
- New version.

* Thu Jun 21 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.8-alt1
- New version.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.7-alt1
- Initial build for Sisyphus
