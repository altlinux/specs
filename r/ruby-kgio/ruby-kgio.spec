%define pkgname kgio

Name:     ruby-%pkgname
Version:  2.11.2
Release:  alt3

Summary:  kinder, gentler I/O for Ruby
Group:    Development/Ruby
License:  LGPLv2
Url:      https://bogomips.org/kgio
# VCS:    https://bogomips.org/kgio.git

Source:  %pkgname-%version.tar
Source1: %pkgname-%version.gemspec

BuildRequires(pre): rpm-build-ruby

%description
kgio provides non-blocking I/O methods for Ruby without raising
exceptions on EAGAIN and EINPROGRESS. It is intended for use with the
Unicorn and Rainbows! Rack servers, but may be used by other
applications (that run on Unix-like platforms).

%package doc
Summary: Documentation files for %name
Group: Documentation
BuildArch: noarch

%description doc 
Documentation files for %name.

%prep
%setup -n %pkgname-%version
cp %SOURCE1 %pkgname-%version.gemspec
%update_setup_rb

%build 
%ruby_config
%ruby_build

%install
export VERSION=%version
%ruby_install
%rdoc lib/
mkdir -p %buildroot%rubygem_gemdir/%pkgname-%version/lib/ %buildroot%rubygem_extdir/%pkgname-%version/
find %buildroot%ruby_sitelibdir/ -type f -name "*.so" -exec mv {} %buildroot%rubygem_extdir/%pkgname-%version/ \;
touch %buildroot%rubygem_extdir/%pkgname-%version/gem.build_complete
mv %buildroot%ruby_sitelibdir/* %buildroot%rubygem_gemdir/%pkgname-%version/lib/
touch %buildroot.manifest

%check
%ruby_test

%files
%doc README TODO
%rubygem_gemdir/*
%rubygem_extdir/*
%rubygem_specdir/*

%files doc
%doc COPYING HACKING ISSUES
%ruby_ri_sitedir/

%changelog
* Wed Jan 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.11.2-alt3
- Place library into proper ruby gem folder.

* Thu Nov 15 2018 Pavel Skrylev <majioa@altlinux.org> 2.11.2-alt2
- Fix binding with compiled binary so-libs.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.2-alt1.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.2-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.2-alt1.1
- Rebuild with Ruby 2.5.0

* Wed Jan 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.2-alt1
- New version.

* Tue Dec 19 2017 Andrey Cherepanov <cas@altlinux.org> 2.11.1-alt1
- New version.

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 2.11.0-alt2.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.11.0-alt2.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 2.11.0-alt2
- Rebuild with new %%ruby_sitearchdir location

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 2.11.0-alt1
- new version 2.11.0

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 2.10.0-alt1
- new version 2.10.0

* Fri Nov 07 2014 Anton Gorlov <stalker@altlinux.ru> 2.9.2-alt1
- new version

* Wed Mar 19 2014 Led <led@altlinux.ru> 2.7.2-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Fri Dec 07 2012 Led <led@altlinux.ru> 2.7.2-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Tue Jan 10 2012 Anton Gorlov <stalker@altlinux.ru> 2.7.2-alt1
- new version

* Wed Aug 10 2011 Anton Gorlov <stalker@altlinux.ru> 2.6.0-alt1
- initial build for altlinux
