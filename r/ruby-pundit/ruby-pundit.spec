%define  pkgname pundit

Name:    ruby-%pkgname
Version: 2.0.1
Release: alt1

Summary: Minimal authorization through OO design and pure Ruby classes
License: MIT
Group:   Development/Ruby
Url:     https://github.com/varvet/pundit

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
Pundit provides a set of helpers which guide you in leveraging regular Ruby
classes and object oriented design patterns to build a simple, robust and
scaleable authorization system.

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
* Sun Feb 03 2019 Mikhail Gordeev <obirvalger@altlinux.org> 2.0.1-alt1
- Initial build for Sisyphus
