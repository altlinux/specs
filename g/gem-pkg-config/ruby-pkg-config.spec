%define        pkgname pkg-config

Name:          gem-%pkgname
Version:       1.4.1
Release:       alt1
Summary:       pkg-config implemented by pure Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby-gnome2/pkg-config
Vcs:           https://github.com/ruby-gnome2/pkg-config.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
pkg-config can be used in your extconf.rb to properly detect need libraries for
compiling Ruby native extensions


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
* Sat Jun 13 2020 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1
- ^ 1.3.7 -> 1.4.1

* Tue Mar 19 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.7-alt1
- ^ 1.3.3 -> 1.3.7

* Fri Feb 15 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.3-alt1
- > Ruby Policy 2.0
- ^ 1.3.1 -> 1.3.3

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Sat Apr 28 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- New version.

* Tue Apr 10 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1
- New version.

* Mon Jan 15 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.9-alt1
- New version.

* Thu Oct 19 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.8-alt1
- New version

* Wed Aug 16 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.7-alt1
- New version

* Mon Aug 14 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.6-alt1
- New version

* Mon Aug 07 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.4-alt1
- New version

* Tue May 30 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.3-alt1
- New version

* Mon May 29 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1
- New version

* Tue Apr 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- New version

* Fri Apr 21 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.9-alt1
- New version

* Thu Apr 20 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.8-alt1
- New version

* Mon Sep 26 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.7-alt1
- New version

* Tue Dec 04 2012 Led <led@altlinux.ru> 1.0.7-alt3.1
- Rebuilt with ruby-1.9.3-alt1

* Thu Nov 10 2011 Timur Aitov <timonbl4@altlinux.org> 1.0.7-alt3
- Repair build

* Fri Apr 29 2011 Timur Aitov <timonbl4@altlinux.org> 1.0.7-alt2
- Repair build

* Sun Jan 09 2011 Alexey I. Froloff <raorn@altlinux.org> 1.0.7-alt1
- Built for Sisyphus

