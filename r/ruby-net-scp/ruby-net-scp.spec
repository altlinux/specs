# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname net-scp

Name: ruby-%pkgname
Version: 1.0.2
Release: alt2

Summary: A pure Ruby implementation of the SCP client protocol
Group: Development/Ruby
License: MIT
Url: http://rubyforge.org/projects/net-ssh/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source0: %pkgname-%version.tar.gz
Patch: net-scp-1.0.2-alt-tests.patch

# Automatically added by buildreq on Sat Dec 05 2009 (-bi)
BuildRequires: rpm-build-ruby ruby-mocha ruby-net-ssh ruby-tool-rdoc ruby-tool-setup

%description
Net::SCP is a pure-Ruby implementation of the SCP protocol. This operates over
SSH (and requires the Net::SSH library), and allows files and directory trees
to copied to and from a remote server.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%patch -p2
%update_setup_rb

%build
%ruby_config
%ruby_build
%ruby_test_unit -Ilib:test test/test_all.rb

%install
%ruby_install
%rdoc lib/

%files
%doc CHANGELOG.rdoc README.rdoc
%ruby_sitelibdir/*

%files doc
%dir %ruby_ri_sitedir/Net
%ruby_ri_sitedir/Net/SCP

%changelog
* Sat Dec 12 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.2-alt2
- Fixed file conflict in doc subpackage with net-ssh and net-sftp docs
- Enabled tests

* Sat Dec 05 2009 Igor Zubkov <icesik@altlinux.org> 1.0.2-alt1
- build for Sisyphus

