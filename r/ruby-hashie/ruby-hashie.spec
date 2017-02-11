
Name:    ruby-hashie
Version: 3.5.2
Release: alt1

Summary: Hashie is a simple collection of useful Hash extensions
Group:   Development/Ruby
License: MIT/Ruby
URL:     https://github.com/intridea/hashie

BuildArch: noarch

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-test-unit
BuildRequires: ruby-tool-setup

Source: %name-%version.tar

%description
Hashie is a growing collection of tools that extend Hashes and make them
more useful.

%package doc
Summary:   Documentation for %name
Group:     Development/Documentation
Requires:  %name = %version-%release
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -n %name-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%check
%ruby_test_unit -Ilib:test tests

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%files
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Sat Feb 11 2017 Andrey Cherepanov <cas@altlinux.org> 3.5.2-alt1
- new version 3.5.2

* Wed Feb 01 2017 Andrey Cherepanov <cas@altlinux.org> 3.5.1-alt1
- new version 3.5.1

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 3.4.6-alt1
- new version 3.4.6

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 3.4.4-alt1
- New version

* Wed Mar 05 2014 Andrey Cherepanov <cas@altlinux.org> 2.0.5-alt1
- Initial build for ALT Linux

