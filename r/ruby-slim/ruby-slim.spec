%define  pkgname slim

Name:    ruby-%pkgname
Version: 3.0.9
Release: alt1

Summary: Slim is a template language whose goal is to reduce the syntax to the essential parts without becoming cryptic.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/slim-template/slim

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
%doc *.md
%_bindir/slimrb
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Sun Feb 03 2019 Mikhail Gordeev <obirvalger@altlinux.org> 3.0.9-alt1
- Initial build for Sisyphus
