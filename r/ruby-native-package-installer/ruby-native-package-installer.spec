%define     pkgname native-package-installer

Name:       ruby-%pkgname
Version:    1.0.6
Release:    alt2

Summary:    It helps to install native packages on "gem install"
License:    LGPLv3+
Group:      Development/Ruby
Url:        https://github.com/ruby-gnome2/native-package-installer
# VCS:      https://github.com/ruby-gnome2/native-package-installer.git
Packager:   Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:  noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
Users need to install native packages to install an extension library
that depends on native packages. It bores users because users need to
install native packages and an extension library separately.
native-package-installer helps to install native packages on "gem install".
Users can install both native packages and an extension library by one action,
"gem install".

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
mkdir -p %buildroot%rubygem_gemdir/%pkgname-%version/lib/
mv %buildroot%ruby_sitelibdir/* %buildroot%rubygem_gemdir/%pkgname-%version/lib/

%check
%ruby_test

%files
%doc README*
%rubygem_gemdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Sun Jan 20 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.6-alt2
- Place library files into gem folder.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.6-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Sat Mar 31 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.6-alt1
- Initial build for Sisyphus
