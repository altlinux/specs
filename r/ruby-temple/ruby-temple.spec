%define  pkgname temple

Name: 	 ruby-%pkgname
Version: 0.8.0
Release: alt1

Summary: Template compilation framework in Ruby
License: MIT
Group:   Development/Ruby
Url:     https://github.com/judofyr/temple

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
Temple is an abstraction and a framework for compiling templates to pure Ruby.
It's all about making it easier to experiment, implement and optimize template
languages. If you're interested in implementing your own template language, or
anything else related to the internals of a template engine: You've come to the
right place.

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

%files doc
%ruby_ri_sitedir/*

%changelog
* Thu Sep 28 2017 Mikhail Gordeev <obirvalger@altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus
