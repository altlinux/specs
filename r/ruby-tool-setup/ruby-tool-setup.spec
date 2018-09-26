%define pkgname setup

Name: ruby-tool-%pkgname
Version: 3.4.1
Release: alt13
Summary: Generic installer for ruby scripts and libraries
License: LGPLv2.1
Group: Development/Ruby
Url: http://i.loveruby.net/en/projects/setup/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Provides: ruby-%pkgname = %version-%release

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-module-etc ruby-module-fileutils ruby-module-stringio

Requires: git-core

Source: %pkgname-%version.tar
Patch: %name-%version-%release.patch

%description
setup.rb is a generic installer for ruby scripts and libraries.
You can use setup.rb to install your any ruby programs.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%patch -p1

%build
%ruby_config
%ruby_build
#for t in test/test_*.rb; do
#  %ruby_vendor "$t"
#done

%install
%__mkdir_p %buildroot%_datadir/ruby-%pkgname
%__install -p -m644 Template.README.* %buildroot%_datadir/ruby-%pkgname
%__install -p -m644 setup.rb %buildroot%_datadir/ruby-%pkgname

%files
%doc ChangeLog NEWS.* README.* TODO Usage_*.txt
%dir %_datadir/ruby-%pkgname
%_datadir/ruby-%pkgname/*

%files doc
%doc doc.* sample

%changelog
* Fri Sep 21 2018 Pavel Skrylev <majioa@altlinux.org> 3.4.1-alt13
- Add copying Gemfile w/o .gemspec to spec folder. Now name of the spec
  folder depends on the package name, not gem name,

* Tue Aug 07 2018 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt12
- Add missing gemspec call in Gemfile.

* Tue Jul 10 2018 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt11
- Install both gemspec and Gemfile in subdirectory of gem specifications.

* Thu Jul 05 2018 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt10
- Save pure gemspec file with name contains gem name and its version.

* Wed Jul 04 2018 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt9
- Init git repo for git ls-files and fix open gemspec.

* Thu Jun 28 2018 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt8
- Do not try to save gemspec with errors.

* Tue Jun 26 2018 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt7
- Install adapted *.gemspec if it exists.

* Mon Sep 12 2016 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt6
- Apply patches from Debian (also use RbConfig instead of Config)
- Provides ruby-setup

* Mon Jun 29 2009 Alexey I. Froloff <raorn@altlinux.org> 3.4.1-alt5
- Remove deps on test/unit module
- Fix ext installation

* Wed Aug 13 2008 Sir Raorn <raorn@altlinux.ru> 3.4.1-alt4
- Fixup config just after running metaconfigs

* Fri Jul 25 2008 Sir Raorn <raorn@altlinux.ru> 3.4.1-alt3
- Add "-rvendor-specific" when running ruby and is VENDOR_SPECIFIC

* Thu Apr 03 2008 Sir Raorn <raorn@altlinux.ru> 3.4.1-alt2
- Rebuilt with rpm-build-ruby

* Wed Dec 05 2007 Sir Raorn <raorn@altlinux.ru> 3.4.1-alt1
- Initial build for ALT Linux

