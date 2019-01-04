Name:    rake-compiler
Version: 1.0.7
Release: alt1

Summary: Provide a standard and simplified way to build and package Ruby C and Java extensions using Rake as glue.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/rake-compiler/rake-compiler

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
rake-compiler is first and foremost a productivity tool for Ruby
developers. Its goal is to make the busy developer's life easier by
simplifying the building and packaging of Ruby extensions by simplifying
code and reducing duplication.

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
%_bindir/%name
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Fri Jan 04 2019 Andrey Cherepanov <cas@altlinux.org> 1.0.7-alt1
- New version.

* Mon Dec 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.6-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1
- New version.

* Wed Jul 18 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt2
- Package as gem.

* Thu Jul 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1
- Initial build for Sisyphus
