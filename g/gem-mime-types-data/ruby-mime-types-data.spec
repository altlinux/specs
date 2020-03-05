# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname mime-types-data

Name:          gem-%pkgname
Version:       3.2019.1009
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

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

%description
mime-types-data provides a registry for information about MIME media
type definitions. It can be used with the Ruby mime-types library or
other software to determine defined filename extensions for MIME types,
or to use filename extensions to look up the likely MIME type
definitions.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
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
