%define        pkgname iconv

Name:          ruby-%pkgname
Version:       1.0.8
Release:       alt1
Summary:       iconv wrapper, used to be ext/iconv
License:       BSD 2-clause Simplified License/Ruby
Group:         Development/Ruby
URL:           https://github.com/nurse/iconv
# VCS:         https://github.com/ruby/iconv.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Iconv is a wrapper class for the UNIX 95 iconv() function family, which
translates string between various encoding systems.


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
* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.8-alt1
- Bump to 1.0.8
- Use Ruby Policy 2.0

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1.1
- Rebuild with Ruby 2.5.0

* Mon Dec 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1
- New version.

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt2.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt2.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt2
- Rebuild with new %%ruby_sitearchdir location

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1
- new version 1.0.4

* Fri Mar 21 2014 Led <led@altlinux.ru> 1.0-alt1
- initial build
