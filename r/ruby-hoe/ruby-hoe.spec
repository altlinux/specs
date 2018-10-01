%define  pkgname hoe

Name:    ruby-%pkgname
Version: 3.17.1
Release: alt1

Summary: Hoe is a rake/rubygems helper for project Rakefiles
License: MIT
Group:   Development/Ruby
Url:     git://github.com/seattlerb/hoe

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby

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
rake debug_gem > %pkgname-%version.gemspec 

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib:test test

%files
%doc README*
%_bindir/sow
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Oct 01 2018 Andrey Cherepanov <cas@altlinux.org> 3.17.1-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.17.0-alt2.1
- Rebuild with new Ruby autorequirements.

* Thu Jul 05 2018 Andrey Cherepanov <cas@altlinux.org> 3.17.0-alt2
- Clarify ignored modules.
- Package as gem.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 3.17.0-alt1
- Initial build for Sisyphus
