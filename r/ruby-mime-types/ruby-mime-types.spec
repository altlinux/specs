# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname mime-types

Name:    ruby-%pkgname
Version: 3.1
Release: alt1

Summary: Manages a MIME Content-Type database that will return the Content-Type for a given filename
Group:   Development/Ruby
License: Ruby/Perl/GPLv2+
Url:     https://github.com/mime-types/ruby-mime-types

BuildArch: noarch

Source0: %pkgname-%version.tar

BuildRequires: rpm-build-ruby ruby-tool-rdoc ruby-tool-setup

%description
MIME::Types for Ruby originally based on and synchronized with
MIME::Types for Perl by Mark Overmeer, copy right 2001 - 2009. As of
version 1.15, the data format for the MIME::Type list has changed and
the synchronization will no longer happen.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name.

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%check
%ruby_test_unit -Ilib:test tests

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%files
%doc *.rdoc
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Thu Mar 30 2017 Andrey Cherepanov <cas@altlinux.org> 3.1-alt1
- New version

* Mon Oct 19 2015 Andrey Cherepanov <cas@altlinux.org> 2.6.2-alt1
- New version
- Update homepage to https://github.com/mime-types/ruby-mime-types

* Fri Dec 07 2012 Led <led@altlinux.ru> 1.18-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Wed Apr 18 2012 Igor Zubkov <icesik@altlinux.org> 1.18-alt1
- 1.16 -> 1.18
- Fix repocop warning

* Sat Dec 12 2009 Igor Zubkov <icesik@altlinux.org> 1.16-alt1
- build for Sisyphus



