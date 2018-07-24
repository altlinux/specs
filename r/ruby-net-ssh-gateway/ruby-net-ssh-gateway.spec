%define pkgname net-ssh-gateway

Name: ruby-%pkgname
Version: 2.0.0
Release: alt1

Summary: A simple library to assist in establishing tunneled Net::SSH connections
Group: Development/Ruby
License: MIT
Url: https://github.com/net-ssh/net-ssh-gateway

BuildArch: noarch

Source0: %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
A simple library to assist in establishing tunneled Net::SSH connections.

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

%files
%doc CHANGES.txt README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/Net/SSH/Gateway

%changelog
* Wed Sep 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt2.3
- Rebuild with new Ruby autorequirements.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt2.2
- Rebuild with Ruby 2.4.1

* Wed Dec 05 2012 Led <led@altlinux.ru> 1.0.1-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Fri Dec 11 2009 Igor Zubkov <icesik@altlinux.org> 1.0.1-alt2
- fix License

* Sat Dec 05 2009 Igor Zubkov <icesik@altlinux.org> 1.0.1-alt1
- build for Sisyphus

