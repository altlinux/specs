Name:    ruby-sassc
Version: 1.11.4
Release: alt1

Summary: Use libsass with Ruby!
License: MIT
Group:   Development/Ruby
Url:     https://github.com/sass/sassc-ruby

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
This gem combines the speed of libsass, the Sass C implementation, with
the ease of use of the original Ruby Sass library.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %name-%version
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
* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.11.4-alt1
- Initial build for Sisyphus
