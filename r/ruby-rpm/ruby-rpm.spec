# vim: set ft=spec: -*- rpm-spec -*-

Name: ruby-rpm
Version: 1.2.3
Release: alt9

Summary: Ruby/RPM is an interface to access RPM database for Ruby
Group: Development/Ruby
License: GPL
Url: http://rubyforge.org/projects/ruby-rpm/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

# Automatically added by buildreq on Mon Apr 14 2008 (-bi)
BuildRequires: librpm-devel libruby-devel ruby-test-unit ruby-tool-setup

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
Ruby/RPM is an interface to access RPM database for Ruby.

%prep
%setup
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build
%ruby_vendor tests/runner.rb

%install
%ruby_install

%files
%doc ChangeLog NEWS README
%ruby_sitearchdir/*
%ruby_sitelibdir/*

%changelog
* Fri Dec 02 2011 Dmitry V. Levin <ldv@altlinux.org> 1.2.3-alt9
- Dropped RPMTRANS_FLAG_DIRSTASH and RPMTRANS_FLAG_REPACKAGE to fix
  build with rpm >= 4.0.4-alt100.36.

* Wed Oct 13 2010 Alexey I. Froloff <raorn@altlinux.org> 1.2.3-alt8
- Fixed CHANGELOGTIME processing

* Tue Aug 31 2010 Alexey I. Froloff <raorn@altlinux.org> 1.2.3-alt7
- Dropped RPM::DBI_DEPENDS (rpm 4.0.4-alt98.39)

* Thu Oct 01 2009 Alexey Tourbin <at@altlinux.ru> 1.2.3-alt6
- Removed support for available packages.

* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.3-alt5.1
- Rebuilt with new librpmbuild.

* Sat Jun 27 2009 Alexey I. Froloff <raorn@altlinux.org> 1.2.3-alt5
- Rebuilt with Ruby 1.9

* Tue Mar 24 2009 Sir Raorn <raorn@altlinux.ru> 1.2.3-alt4
- Removed prehistoric multilib support (rpm >= 4.0.4-alt98.2)

* Mon Nov 17 2008 Sir Raorn <raorn@altlinux.ru> 1.2.3-alt3
- Added RPM::Package::each_from_file method for access to
  apt-rpm's pkglists

* Mon Apr 14 2008 Sir Raorn <raorn@altlinux.ru> 1.2.3-alt2
- Do not check for unneeded libdb

* Tue Feb 05 2008 Sir Raorn <raorn@altlinux.ru> 1.2.3-alt1
- Initial build

