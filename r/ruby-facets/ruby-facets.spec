%define  pkgname facets

Name:    ruby-%pkgname
Version: 3.1.0
Release: alt1

Summary: Ruby Facets
License: BSD 2 Clause
Group:   Development/Ruby
Url:     http://github.com/rubyworks/facets

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%filter_from_requires \,^ruby(facets/string/random_binary),d

%description
Ruby Facets is the premiere collection of general purpose method
extensions and standard additions for the Ruby programming language.

Facets houses the largest single collection of methods available for
extending the core capabilities of Ruby's built-in classes and modules.
This collection of extension methods are unique by virtue of their
atomicity. The methods are stored in individual files so that each can
be required independently. This gives developers the potential for much
finer control over which extra methods to bring into their code.

In addition Facets provides a collection of extensions to Ruby standard
library plus a small collection of add-on classes and modules. Together
these libraries constitute an reliable source of reusable components,
suitable to a wide variety of usecases.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
rm -f lib/core/facets/kernel/memo.rb
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
mkdir -p %buildroot%ruby_sitelibdir/facets
cp -a %buildroot%ruby_sitelibdir/{core,standard}/facets/* %buildroot%ruby_sitelibdir/facets
rm -rf %buildroot%ruby_sitelibdir/{core,standard}
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
* Mon May 28 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1
- Initial build for Sisyphus
