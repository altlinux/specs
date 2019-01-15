%define  pkgname power-assert

Name:    gem-%pkgname
Version: 1.1.3
Release: alt1

Summary: Power Assert for Ruby
License: BSD 2-clause Simplified License
Group:   Development/Ruby
Url:     https://github.com/k-tsj/power_assert
# VCS:   https://github.com/k-tsj/power_assert.git

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
rm -f bin/{console,setup}

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
#%ruby_test_unit -Ilib:test test

%files
%doc *.rdoc
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Jan 15 2019 Pavel Skrylev <majioa@altlinux.org> 1.1.3-alt1
- Initial build for Sisyphus, packaged as a gem
