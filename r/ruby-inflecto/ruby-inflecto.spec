%define  pkgname inflecto

Name:    ruby-%pkgname
Version: 0.0.2
Release: alt2.gitb257665
Epoch:   1

Summary: Inflector for strings
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/mbj/inflecto

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
Inflector for strings.

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
rm -f Gemfile

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
* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.0.2-alt2.gitb257665
- Reset to last official version in gemspec.

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt1.gita39d9a5.2
- Rebuild for new Ruby autorequirements.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt1.gita39d9a5.1
- Rebuild with new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt1.gita39d9a5
- Initial build for Sisyphus.
