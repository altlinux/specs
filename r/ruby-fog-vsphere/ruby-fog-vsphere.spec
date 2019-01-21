%define     pkgname fog-vsphere

Name:       ruby-%pkgname
Version:    2.5.0
Release:    alt1

Summary:    Fog for vSphere
License:    MIT
Group:      Development/Ruby
Url:        https://github.com/fog/fog-vsphere
# VCS:      https://github.com/fog/fog-vsphere.git

Packager:   Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:  noarch

Source:     %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
The VMware vSphere provider allows you to use the abstractions of the Fog cloud
services library to communicate with vSphere.

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
* Mon Jan 21 2019 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt1
- Bump to 2.5.0.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus
