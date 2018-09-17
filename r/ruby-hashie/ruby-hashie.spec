
Name:    ruby-hashie
Version: 3.6.0
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
Patch:  alt-fix-gemfile.patch

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
%patch -p1
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
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.5.7-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Dec 20 2017 Andrey Cherepanov <cas@altlinux.org> 3.5.7-alt1
- New version.

* Wed Jul 12 2017 Andrey Cherepanov <cas@altlinux.org> 3.5.6-alt1
- New version

* Tue Feb 28 2017 Andrey Cherepanov <cas@altlinux.org> 3.5.5-alt1
- New version

* Thu Feb 23 2017 Andrey Cherepanov <cas@altlinux.org> 3.5.4-alt1
- new version 3.5.4

* Mon Feb 13 2017 Andrey Cherepanov <cas@altlinux.org> 3.5.3-alt1
- new version 3.5.3

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

