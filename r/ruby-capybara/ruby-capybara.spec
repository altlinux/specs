%define  pkgname capybara

Name:    ruby-%pkgname
Version: 3.12.0
Release: alt1

Summary: Acceptance test framework for web applications
License: MIT
Group:   Development/Ruby
Url:     https://github.com/teamcapybara/capybara

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
%summary

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
%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Dec 10 2018 Andrey Cherepanov <cas@altlinux.org> 3.12.0-alt1
- New version.

* Mon Oct 29 2018 Pavel Skrylev <majioa@altlinux.org> 3.10.0-alt1
- new version 3.10.0

* Thu Oct 04 2018 Andrey Cherepanov <cas@altlinux.org> 3.9.0-alt1
- New version.

* Thu Sep 27 2018 Andrey Cherepanov <cas@altlinux.org> 3.8.2-alt1
- New version.

* Tue Sep 25 2018 Andrey Cherepanov <cas@altlinux.org> 3.8.1-alt1
- New version.

* Fri Sep 21 2018 Andrey Cherepanov <cas@altlinux.org> 3.8.0-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.2-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt1
- Initial build for Sisyphus
