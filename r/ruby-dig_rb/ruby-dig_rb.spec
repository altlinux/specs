%define  pkgname dig_rb

Name:    ruby-%pkgname
Version: 1.0.1
Release: alt1

Summary: Array/Hash/Struct#dig polyfill for ruby
License: MIT
Group:   Development/Ruby
Url:     https://github.com/jrochkind/dig_rb/

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

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Sat Sep 29 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus
