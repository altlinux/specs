%define  pkgname dalli

%filter_from_requires /^ruby(inline)/d
%filter_from_requires /^ruby(action_dispatch\/middleware\/session\/abstract_store)/d

Name: ruby-%pkgname
Version: 2.7.6
Release: alt1

Summary: High performance memcached client for Ruby
License: MIT
Group:   Development/Ruby
Url:     https://github.com/petergoldstein/dalli
BuildArch: noarch
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel
BuildRequires: memcached

%description
High performance memcached client for Ruby.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup
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

%files doc
%ruby_ri_sitedir/*

%changelog
* Thu Aug 31 2017 Alexey Shabalin <shaba@altlinux.ru> 2.7.6-alt1
- Initial build in Sisyphus

