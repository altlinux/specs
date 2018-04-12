%define  pkgname mail
 
Name: 	 ruby-%pkgname
Version: 2.7.0
Release: alt1
 
Summary: A really Ruby Mail handler
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/mikel/mail
 
Packager: Andrey Cherepanov <cas@altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: ruby-mime-types
BuildRequires: ruby-treetop
 
%filter_from_requires /^ruby(\(ftools\|tlsmail\))/d

%description
Mail is an internet library for Ruby that is designed to handle emails
generation, parsing and sending in a simple, rubyesque manner.

%package doc
Summary: Documentation files for %name
Group: Documentation
 
BuildArch: noarch
 
%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%update_setup_rb
 
%build
%ruby_config
%ruby_build
 
%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}
 
%check
# Require network for tests
#ruby_test_unit -Ilib:test test
 
%files
%doc README*
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Wed Nov 01 2017 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt1
- New version

* Sat Jun 10 2017 Andrey Cherepanov <cas@altlinux.org> 2.6.6-alt1
- New version

* Thu Apr 27 2017 Andrey Cherepanov <cas@altlinux.org> 2.6.5-alt1
- New version

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 2.6.4-alt1
- New version
- Disable test because they require network connections

* Wed Apr 23 2014 Andrey Cherepanov <cas@altlinux.org> 2.5.4-alt1
- Initial build for ALT Linux
