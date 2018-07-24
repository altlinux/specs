%define  pkgname listen

Name:    ruby-%pkgname
Version: 3.1.5
Release: alt2.git587f4a7

Summary: The Listen gem listens to file modifications and notifies you about the changes.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/guard/listen

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
sed -i '/rb-fsevent/d' %pkgname.gemspec
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
%_bindir/%pkgname
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Jul 16 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.5-alt2.git587f4a7
- Upgrade to git 587f4a7.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.5-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.5-alt1
- Initial build for Sisyphus
