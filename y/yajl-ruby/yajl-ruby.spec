%define pkgname yajl-ruby

Name:          %pkgname
Version:       1.4.1
Release:       alt2
Summary:       YAJL C Bindings for Ruby
Group:         Development/Ruby
License:       MIT/Ruby
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Url:           https://github.com/brianmario/yajl-ruby
# VCS:         https://github.com/brianmario/yajl-ruby.git
Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec)
BuildRequires: gem(rake-compiler)

%description
This package is a C binding to the excellent YAJL JSON parsing and
generation library.


%package       devel
Summary:       Development files for %name
Group:         Development/Documentation
BuildArch:     noarch

%description   devel
Development files for %name.


%package       doc
Summary:       Documentation files for %name
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %name.


%prep
%setup

%build
%gem_build --use=yajl-ruby --join=lib:bin

%install
%gem_install -m lust

%check
%gem_test

%files
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         devel
%ruby_includedir/*

%files         doc
%ruby_gemdocdir

%changelog
* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt2
- Use setup gem's dependency detection

* Tue Feb 05 2019 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1
- Bump to 1.4.1;
- Use Ruby Policy 2.0.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Sat Apr 28 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- New version.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1.1
- Rebuild with Ruby 2.5.0

* Tue Nov 07 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- New version

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1
- New version

* Mon Sep 12 2016 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt2
- Rebuild with Ruby 2.3.1

* Thu Oct 01 2015 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1
- New version

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.7.5-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Tue Dec 04 2012 Led <led@altlinux.ru> 0.7.5-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Sun Apr 11 2010 Alexey I. Froloff <raorn@altlinux.org> 0.7.5-alt1
- Built for Sisyphus
