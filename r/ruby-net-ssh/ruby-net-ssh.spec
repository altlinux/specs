# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname net-ssh

Name: ruby-%pkgname
Version: 2.0.15
Release: alt1

Summary: Pure-Ruby implementation of the SSH2 client protocol
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/net-ssh/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Thu Nov 19 2009 (-bi)
BuildRequires: rpm-build-ruby ruby-test-unit ruby-tool-rdoc ruby-tool-setup ruby-mocha

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
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build
%ruby_test_unit -Ilib:test test/test_all.rb

%install
%ruby_install
%rdoc lib/

%files
%doc README.rdoc THANKS.rdoc
%ruby_sitelibdir/*

%files doc
%dir %ruby_ri_sitedir/Net
%ruby_ri_sitedir/Net/SSH

%changelog
* Thu Nov 19 2009 Alexey I. Froloff <raorn@altlinux.org> 2.0.15-alt1
- [2.0.15]

* Fri Aug 07 2009 Konstantin Pavlov <thresh@altlinux.org> 2.0.11-alt1
- 2.0.11 release.

* Wed Nov 26 2008 Pavlov Konstantin <thresh@altlinux.ru> 2.0.4-alt1
- Initial build for ALT Linux.

