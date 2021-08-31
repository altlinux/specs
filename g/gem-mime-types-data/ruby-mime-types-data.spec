%define        gemname mime-types-data

Name:          gem-mime-types-data
Version:       3.2021.0704
Release:       alt1
Summary:       MIME Type registry data
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mime-types/mime-types-data
Vcs:           https://github.com/mime-types/mime-types-data.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(nokogiri) >= 1.6 gem(nokogiri) < 2
BuildRequires: gem(hoe-doofus) >= 1.0 gem(hoe-doofus) < 2
BuildRequires: gem(hoe-gemspec2) >= 1.1 gem(hoe-gemspec2) < 2
BuildRequires: gem(hoe-git) >= 1.6 gem(hoe-git) < 2
BuildRequires: gem(hoe-rubygems) >= 1.0 gem(hoe-rubygems) < 2
BuildRequires: gem(rake) >= 10.0 gem(rake) < 14
BuildRequires: gem(mime-types) >= 3.2.1 gem(mime-types) < 4
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7
BuildRequires: gem(hoe) >= 3.22 gem(hoe) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
Obsoletes:     ruby-mime-types-data < %EVR
Provides:      ruby-mime-types-data = %EVR
Provides:      gem(mime-types-data) = 3.2021.0704


%description
mime-types-data provides a registry for information about MIME media type
definitions. It can be used with the Ruby mime-types library or other software
to determine defined filename extensions for MIME types, or to use filename
extensions to look up the likely MIME type definitions.


%package       -n gem-mime-types-data-doc
Version:       3.2021.0704
Release:       alt1
Summary:       MIME Type registry data documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mime-types-data
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mime-types-data) = 3.2021.0704

%description   -n gem-mime-types-data-doc
MIME Type registry data documentation files.

mime-types-data provides a registry for information about MIME media type
definitions. It can be used with the Ruby mime-types library or other software
to determine defined filename extensions for MIME types, or to use filename
extensions to look up the likely MIME type definitions.

%description   -n gem-mime-types-data-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mime-types-data.


%package       -n gem-mime-types-data-devel
Version:       3.2021.0704
Release:       alt1
Summary:       MIME Type registry data development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mime-types-data
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mime-types-data) = 3.2021.0704
Requires:      gem(nokogiri) >= 1.6 gem(nokogiri) < 2
Requires:      gem(hoe-doofus) >= 1.0 gem(hoe-doofus) < 2
Requires:      gem(hoe-gemspec2) >= 1.1 gem(hoe-gemspec2) < 2
Requires:      gem(hoe-git) >= 1.6 gem(hoe-git) < 2
Requires:      gem(hoe-rubygems) >= 1.0 gem(hoe-rubygems) < 2
Requires:      gem(rake) >= 10.0 gem(rake) < 14
Requires:      gem(mime-types) >= 3.2.1 gem(mime-types) < 4
Requires:      gem(rdoc) >= 4.0 gem(rdoc) < 7
Requires:      gem(hoe) >= 3.22 gem(hoe) < 4

%description   -n gem-mime-types-data-devel
MIME Type registry data development package.

mime-types-data provides a registry for information about MIME media type
definitions. It can be used with the Ruby mime-types library or other software
to determine defined filename extensions for MIME types, or to use filename
extensions to look up the likely MIME type definitions.

%description   -n gem-mime-types-data-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mime-types-data.


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

%files         -n gem-mime-types-data-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-mime-types-data-devel
%doc README.md


%changelog
* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 3.2021.0704-alt1
- ^ 3.2019.1009 -> 3.2021.0704

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 3.2019.1009-alt1
- updated (^) 3.2019.0904 -> 3.2019.1009
- fixed (!) spec

* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 3.2019.0904-alt1
- updated (^) 3.2019.0331 -> 3.2019.0904
- fixed (!) spec

* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 3.2019.0331-alt1
- updated (^) 3.2018.0812 -> 3.2019.0331
- used (>) Ruby Policy 2.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.2018.0812-alt1
- New version.

* Wed Aug 22 2018 Andrey Cherepanov <cas@altlinux.org> 3.2016.0521-alt1.1
- Rebuild for new Ruby autorequirements.

* Fri Mar 31 2017 Andrey Cherepanov <cas@altlinux.org> 3.2016.0521-alt1
- Initial build in Sisyphus
