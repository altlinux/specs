%define  pkgname activemodel-serializers-xml

Name:    ruby-%pkgname
Version: 1.0.2
Release: alt1

Summary: This gem provides XML serialization for your Active Model objects and Active Record models
License: MIT
Group:   Development/Ruby
Url:     https://github.com/rails/activemodel-serializers-xml/

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
* Tue Oct 02 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus
