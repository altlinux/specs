%define        pkgname curses

Name: 	       ruby-%pkgname
Version:       1.2.7
Release:       alt1
Summary:       Ruby binding for curses, ncurses, and PDCurses
License:       MIT/Ruby
Group:         Development/Ruby
Url:           https://github.com/ruby/curses
# VCS:         https://github.com/ruby/curses.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: libncursesw-devel

%description
A Ruby binding for curses, ncurses, and PDCurses. curses is an extension
library for text UI applications.  Formerly part of the Ruby standard
library.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.


%package       -n gem-%pkgname-devel
Summary:       Development files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-devel
Development files for %gemname gem.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%files         -n gem-%pkgname-devel
%ruby_includedir/*

%changelog
* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.7-alt1
- Bump to 1.2.7
- Use Ruby Policy 2.0

* Tue Oct 16 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.5-alt1
- New version.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.4-alt1.3
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.4-alt1.2
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.4-alt1.1
- Rebuild with Ruby 2.4.2

* Wed Sep 13 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.4-alt1
- New version

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.3-alt1.1
- Rebuild with Ruby 2.4.1

* Mon Jul 03 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.3-alt1
- New version

* Sat Apr 22 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1
- New version

* Mon Mar 27 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1
- New version

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt2
- Rebuild with new %%ruby_sitearchdir location

* Wed Feb 22 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Sat Feb 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.3-alt1
- new version 1.1.3

* Tue Feb 07 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- new version 1.1.2

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- new version 1.1.1

* Fri Oct 21 2016 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt1
- Initial build in Sisyphus
