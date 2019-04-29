%define        pkgname io-extra

Name:          ruby-%pkgname
Version:       1.3.0
Release:       alt1
Summary:       Adds IO.fdwalk, IO.closefrom and IO.directio
Group:         Development/Ruby
License:       Apache-2.0
Url:           https://github.com/djberg96/io-extra
# VCS:         https://github.com/djberg96/io-extra.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
the io-extra library provides a few extra IO methods that you may find
handy. They are IO.closefrom, IO.fdwalk, IO#directio and IO#directio.

Adds the IO.closefrom, IO.fdwalk, IO.pread, IO.pread_ptr, IO.pwrite, and
IO.writev singleton methods as well as the IO#directio, IO#directio? and
IO#ttyname instance methods (for those platforms that support them).


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-%pkgname-doc
Obsoletes:     ruby-%pkgname-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.


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

%changelog
* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- Move forward with sourcing from github
- Bump to 1.3.0
- Use Ruby Policy 2.0

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.7-alt1.6
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.7-alt1.5
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.7-alt1.4
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.7-alt1.3
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.7-alt1.2
- Rebuild with new %%ruby_sitearchdir location

* Mon Sep 26 2016 Andrey Cherepanov <cas@altlinux.org> 1.2.7-alt1.1
- Rebuild with Ruby 2.3.1

* Wed Nov 05 2014 Anton Gorlov <stalker@altlinux.ru> 1.2.7-alt1
- New version

* Wed Mar 19 2014 Led <led@altlinux.ru> 1.2.2-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Wed Dec 05 2012 Led <led@altlinux.ru> 1.2.2-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Thu Aug 11 2011 Anton Gorlov <stalker@altlinux.ru> 1.2.2-alt1
- initial build for ALTLinux
