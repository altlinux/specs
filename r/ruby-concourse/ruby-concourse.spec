%define  pkgname concourse-gem

Name:    ruby-concourse
Version: 0.19.0
Release: alt1

Summary: Provide Rake tasks to ease management of Concourse pipelines. See https://concourse.ci/ to learn about Concourse.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/flavorjones/concourse-gem

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
%rubygem_specdir/*.gemspec

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt1
- New version.

* Thu Jul 05 2018 Andrey Cherepanov <cas@altlinux.org> 0.18.0-alt1
- Initial build for Sisyphus
