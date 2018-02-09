Name: libxml-ruby
Version: 3.1.0
Release: alt1
Summary: Ruby language bindings for the GNOME Libxml2 XML toolkit
Group: Development/Ruby
License: MIT
URL: http://xml4r.github.io/%name/
Source: %name-%version.tar
#Patch: %name-%version-%release.patch

BuildPreReq: rpm-build-ruby
BuildRequires: libruby-devel libxml2-devel ruby-tool-setup zlib-devel

%description
The LibXML/Ruby project provides Ruby language bindings for the GNOME Libxml2 XML
toolkit.

%package doc
Summary: Documentation files for %name
Group: Development/Documentation
BuildArch: noarch

%description doc
Documentation files for %name.

%prep
%setup -q
#patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
rm -rf %buildroot%ruby_sitelibdir/libs
%rdoc ext/libxml/*.c lib/
ls -d %buildroot%ruby_ri_sitedir/* | grep -v '/LibXML$' | xargs rm -rf
install -d -m 0755 %buildroot%_docdir/%name-%version
gzip -9c HISTORY > %buildroot%_docdir/%name-%version/HISTORY.gz

%check
#ruby_test_unit -Ilib:ext/libxml:test test/test_suite.rb

%files
%ruby_sitearchdir/*
%ruby_sitelibdir/*

%files doc
%doc %_docdir/%name-%version
%doc %ruby_ri_sitedir/*

%changelog
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

