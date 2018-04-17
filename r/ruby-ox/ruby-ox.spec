%define  pkgname ox

Name: 	 ruby-%pkgname
Version: 2.9.2
Release: alt1

Summary: Ruby Optimized XML Parser
License: MIT/Ruby
Group:   Development/Ruby
Url:     http://www.ohler.com/ox

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel

%description
A fast XML parser and object serializer that uses only standard C lib.
Optimized XML (Ox), as the name implies was written to provide speed
optimized XML handling. It was designed to be an alternative to Nokogiri
and other Ruby XML parsers for generic XML parsing and as an alternative
to Marshal for Object serialization.

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
* Tue Apr 17 2018 Andrey Cherepanov <cas@altlinux.org> 2.9.2-alt1
- New version.

* Sun Apr 15 2018 Andrey Cherepanov <cas@altlinux.org> 2.9.1-alt1
- New version.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.9.0-alt1.1
- Rebuild with Ruby 2.5.1

* Wed Mar 14 2018 Andrey Cherepanov <cas@altlinux.org> 2.9.0-alt1
- New version.

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.8.4-alt1.1
- Rebuild with Ruby 2.5.0

* Mon Mar 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.8.4-alt1
- New version.

* Thu Nov 02 2017 Andrey Cherepanov <cas@altlinux.org> 2.8.2-alt1
- New version

* Sat Oct 28 2017 Andrey Cherepanov <cas@altlinux.org> 2.8.1-alt1
- New version

* Sat Sep 23 2017 Andrey Cherepanov <cas@altlinux.org> 2.8.0-alt1
- New version

* Wed Sep 20 2017 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt1
- New version

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt1.1
- Rebuild with Ruby 2.4.1

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt1
- Initial build for ALT Linux
