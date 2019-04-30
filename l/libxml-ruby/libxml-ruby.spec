%define        pkgname libxml-ruby
%define        gemname libxml-ruby

Name:          %pkgname
Version:       3.1.0
Release:       alt2
Summary:       Ruby language bindings for the GNOME Libxml2 XML toolkit
Group:         Development/Ruby
License:       MIT
URL:           http://xml4r.github.io/%name/
# VCS:         https://github.com/xml4r/libxml-ruby.git
Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: libxml2-devel
BuildRequires: zlib-devel

%description
The LibXML/Ruby project provides Ruby language bindings for the GNOME Libxml2
XML toolkit.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch
Obsoletes:     %pkgname-doc
Provides:      %pkgname-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.


%package       -n gem-%pkgname-devel
Summary:       Development files for %gemname gem
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-%pkgname-devel
Development files for %gemname gem.


%prep
%setup

%build
%gem_build --join=lib:bin

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
* Wed Apr 10 2019 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt2
- Use Ruby Policy 2.0

* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1.1
- Rebuild with Ruby 2.5.0

* Fri Feb 09 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1
- New version.

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- New version

* Tue Sep 13 2016 Andrey Cherepanov <cas@altlinux.org> 2.9.0-alt1
- New version
- Disable tests

* Wed Mar 19 2014 Led <led@altlinux.ru> 2.6.0-alt3
- Rebuilt with ruby-2.0.0-alt1

* Sat Mar 15 2014 Led <led@altlinux.ru> 2.6.0-alt2
- upstream fixes

* Fri Apr 12 2013 Led <led@altlinux.ru> 2.6.0-alt1
- 2.6.0
- cleaned up %%description
- updated URL
- fixed Group for %%name-doc subpackage

* Fri Dec 07 2012 Led <led@altlinux.ru> 1.1.3-alt2
- Rebuilt with ruby-1.9.3-alt1
- fixed build with ruby 1.9
- updated BuildRequires
- disabled check

* Fri May 08 2009 Alexey I. Froloff <raorn@altlinux.org> 1.1.3-alt1
- [1.1.3]

* Sat Nov 01 2008 Sir Raorn <raorn@altlinux.ru> 0.8.3-alt1
- [0.8.3]

* Fri Feb 02 2007 Sir Raorn <raorn@altlinux.ru> 0.3.8.4-alt1
- Built for Sisyphus

