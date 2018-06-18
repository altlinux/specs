%def_disable check

%define pkgname net-ssh

Name: ruby-%pkgname
Version: 5.0.2
Release: alt1

Summary: Pure-Ruby implementation of the SSH2 client protocol
Group:   Development/Ruby
License: MIT/Ruby
Url:     https://github.com/net-ssh/net-ssh
BuildArch: noarch

Source: %pkgname-%version.tar

BuildRequires: rpm-build-ruby ruby-tool-setup ruby-mocha

%filter_from_requires /^ruby(dl/d

%description
Net::SSH is a pure-Ruby implementation of the SSH2 client protocol. It
allows you to write programs that invoke and interact with processes on
remote servers, via SSH2.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%check
%ruby_test_unit -Ilib:test test/test_all.rb

%files
%doc README.rdoc THANKS.txt
%ruby_sitelibdir/*

%files doc
%dir %ruby_ri_sitedir/Net
%ruby_ri_sitedir/Net/SSH

%changelog
* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.2-alt1
- New version.

* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.1-alt1
- New version.

* Mon Sep 11 2017 Andrey Cherepanov <cas@altlinux.org> 4.2.0-alt1
- New version

* Mon Sep 21 2015 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- New version

* Thu Dec 06 2012 Led <led@altlinux.ru> 2.0.15-alt1.1
- Rebuilt with ruby-1.9.3-alt1
- disabled check

* Thu Nov 19 2009 Alexey I. Froloff <raorn@altlinux.org> 2.0.15-alt1
- [2.0.15]

* Fri Aug 07 2009 Konstantin Pavlov <thresh@altlinux.org> 2.0.11-alt1
- 2.0.11 release.

* Wed Nov 26 2008 Pavlov Konstantin <thresh@altlinux.ru> 2.0.4-alt1
- Initial build for ALT Linux.

