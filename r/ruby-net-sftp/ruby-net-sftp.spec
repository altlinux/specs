%def_disable check
%define pkgname net-sftp

Name: ruby-%pkgname
Version: 2.1.2
Release: alt1

Summary: A pure Ruby implementation of the SFTP client protocol
Group: Development/Ruby
License: MIT
Url: https://github.com/net-ssh/net-sftp

BuildArch: noarch

Source0: %pkgname-%version.tar

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

%install
%ruby_install
%rdoc lib/

%check
%if_enabled check
%ruby_test_unit -Ilib:test test/test_all.rb
%endif

%files
%doc CHANGES.txt README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%dir %ruby_ri_sitedir/Net
%ruby_ri_sitedir/Net/SFTP

%changelog
* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt1
- New version.

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.3-alt2.2
- Rebuild with new Ruby autorequirements.

* Thu Dec 06 2012 Led <led@altlinux.ru> 2.0.3-alt2.1
- Rebuilt with ruby-1.9.3-alt1
- disabled check

* Sat Dec 12 2009 Alexey I. Froloff <raorn@altlinux.org> 2.0.3-alt2
- Fixed file conflict in doc subpackage with net-ssh and net-scp docs
- Enabled tests

* Sat Dec 05 2009 Igor Zubkov <icesik@altlinux.org> 2.0.3-alt1
- build for Sisyphus


