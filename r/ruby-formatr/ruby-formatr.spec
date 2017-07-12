%define  pkgname formatr

Name: 	 ruby-%pkgname
Version: 1.10.1
Release: alt1

Summary: Provides perl-like formats for ruby
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://rubygems.org/gems/formatr/versions/1.10.1

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
FormatR provides perl-like formats for ruby. These are used to create output
with a similar format but with changing values. It also supports the ability to
read in formatted text and extract values from the text.

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
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Jul 12 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.10.1-alt1
- Initial build for Sisyphus
