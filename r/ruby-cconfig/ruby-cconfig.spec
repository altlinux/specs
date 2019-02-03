%define  pkgname cconfig

Name:    ruby-%pkgname
Version: 1.2.1
Release: alt1

Summary: Container-aware configuration management gem
License: LGPL-3.0
Group:   Development/Ruby
Url:     https://github.com/mssola/cconfig

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby

%description

CConfig (Container Config) is a container-aware configuration management gem.
This is useful for applications that want to keep a reference configuration and
add modifications to it in two different ways:
- An alternative configuration file that lists all the modifications.
- A list of environment variables that follow a given naming policy.

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
%doc *.md
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Sun Feb 03 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus
