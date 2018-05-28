Name:    fog
Version: 2.0.0
Release: alt1

Summary: The Ruby cloud services library
License: MIT
Group:   Development/Ruby
Url:     https://github.com/fog/fog

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
fog is the Ruby cloud services library, top to bottom:

- Collections provide a simplified interface, making clouds easier to
  work with and switch between.
- Requests allow power users to get the most out of the features of each
  individual cloud.
- Mocks make testing and integrating a breeze.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup
rm -rf lib/fog/aws/service_mapper.rb lib/fog/ovirt*
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
%_bindir/%name
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed May 23 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus
