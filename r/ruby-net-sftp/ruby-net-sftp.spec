# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname net-sftp

Name: ruby-%pkgname
Version: 2.0.3
Release: alt2

Summary: A pure Ruby implementation of the SFTP client protocol
Group: Development/Ruby
License: MIT
Url: http://rubyforge.org/projects/net-ssh/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source0: %pkgname-%version.tar.gz

# Automatically added by buildreq on Sat Dec 05 2009 (-bi)
BuildRequires: rpm-build-ruby ruby-mocha ruby-net-ssh ruby-tool-rdoc ruby-tool-setup

%description
Net::SFTP is a pure-Ruby implementation of the SFTP protocol (specifically,
versions 1 through 6 of the SFTP protocol). Note that this is the "Secure File
Transfer Protocol", typically run over an SSH connection, and has nothing to
do with the FTP protocol.

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
%ruby_test_unit -Ilib:test test/test_all.rb

%install
%ruby_install
%rdoc lib/

%files
%doc CHANGELOG.rdoc README.rdoc
%ruby_sitelibdir/*

%files doc
%dir %ruby_ri_sitedir/Net
%ruby_ri_sitedir/Net/SFTP

%changelog
* Sat Dec 12 2009 Alexey I. Froloff <raorn@altlinux.org> 2.0.3-alt2
- Fixed file conflict in doc subpackage with net-ssh and net-scp docs
- Enabled tests

* Sat Dec 05 2009 Igor Zubkov <icesik@altlinux.org> 2.0.3-alt1
- build for Sisyphus


