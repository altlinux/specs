%define  pkgname marcel

Name:    ruby-%pkgname
Version: 0.3.2
Release: alt1

Summary: Find the mime type of files, examining file, filename and declared type
License: MIT
Group:   Development/Ruby
Url:     https://github.com/basecamp/marcel

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
# For tests
#BuildRequires: ruby-rack-test
#BuildRequires: ruby-mimemagic

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
#%%ruby_test_unit -Ilib:test test/*.rb

%files
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt1
- Initial build for Sisyphus
