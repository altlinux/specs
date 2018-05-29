%def_without tests

%define pkgname net-scp

Name: ruby-%pkgname
Version: 1.2.1
Release: alt1

Summary: A pure Ruby implementation of the SCP client protocol
Group: Development/Ruby
License: MIT
Url: http://rubyforge.org/projects/net-ssh/

BuildArch: noarch

Source0: %pkgname-%version.tar
Patch: net-scp-1.0.2-alt-tests.patch

BuildRequires: rpm-build-ruby ruby-mocha ruby-net-ssh ruby-tool-rdoc ruby-tool-setup
BuildRequires: ruby-test-unit
BuildRequires: ruby-mocha

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

%install
%ruby_install
%rdoc lib/

%check
%if_with tests
%ruby_test_unit -Ilib:test test/test_all.rb
%endif

%files
%doc README.rdoc
%ruby_sitelibdir/*

%files doc
%dir %ruby_ri_sitedir/Net
%ruby_ri_sitedir/Net/SCP

%changelog
* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1
- New version.
- Disable tests.

* Sat Dec 08 2012 Led <led@altlinux.ru> 1.0.2-alt2.1
- Rebuilt with ruby-1.9.3-alt1
- fixed BuildRequires

* Sat Dec 12 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.2-alt2
- Fixed file conflict in doc subpackage with net-ssh and net-sftp docs
- Enabled tests

* Sat Dec 05 2009 Igor Zubkov <icesik@altlinux.org> 1.0.2-alt1
- build for Sisyphus

