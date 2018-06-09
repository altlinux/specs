%define  pkgname CFPropertyList

Name:    ruby-cfpropertylist
Version: 3.0.0
Release: alt2

Summary: Read, write and manipulate both binary and XML property lists as defined by apple
License: MIT
Group:   Development/Ruby
Url:     https://github.com/ckruse/CFPropertyList

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
# For tests
BuildRequires: ruby-nokogiri
BuildRequires: libxml-ruby

%description
CFPropertyList implementation class to read, manipulate and write both
XML and binary property list files (plist(5)) as defined by Apple. Have
a look at CFPropertyList::List for more documentation.

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
* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt2
- Rebuild with tests.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus
