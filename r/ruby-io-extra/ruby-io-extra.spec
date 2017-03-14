%define pkgname io-extra

Name: ruby-%pkgname
Version: 1.2.7
Release: alt1.2

Summary: Adds IO.fdwalk, IO.closefrom and IO.directio
Group: Development/Ruby
License: Ruby
Url: http://rubyforge.org/projects/shards

Source: %pkgname-%version.tar

# Automatically added by buildreq on Thu Aug 11 2011
# optimized out: ruby ruby-stdlibs ruby-tool-rdoc
BuildRequires: libruby-devel ruby-test-unit ruby-tool-setup

%description
the io-extra library provides a few extra IO methods that you may find
handy. They are IO.closefrom, IO.fdwalk, IO#directio and IO#directio.

%package doc
Summary: Documentation files for %name
Group: Documentation
BuildArch: noarch

%description doc 
Documentation files for %name.

%prep
%setup -q -n  %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build


%install
%ruby_install
%rdoc ext/

%files
%doc README CHANGES
#ruby_sitelibdir/*
%ruby_sitearchdir/*

%files doc
%ruby_ri_sitedir/IO*

%changelog
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
