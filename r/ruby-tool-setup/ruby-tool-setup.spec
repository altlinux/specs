%define pkgname setup

Name: ruby-tool-%pkgname
Version: 3.4.1
Release: alt5
Summary: Generic installer for ruby scripts and libraries
License: LGPLv2.1
Group: Development/Ruby
Url: http://i.loveruby.net/en/projects/setup/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

BuildRequires(pre): rpm-build-ruby
# Automatically added by buildreq on Thu Apr 03 2008 (-bi)
BuildRequires: ruby-module-etc ruby-module-fileutils ruby-module-stringio

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

