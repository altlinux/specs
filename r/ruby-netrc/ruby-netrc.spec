%define orig_name netrc

Summary: Library to read and write netrc files
Name: ruby-%orig_name
Version: 0.10.3
Release: alt1.1
Group: Development/Ruby
License: MIT
URL: https://github.com/geemus/netrc
Source0: %orig_name-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: ruby-tool-rdoc
BuildRequires: ruby-test-unit

%description
This library can read and update netrc files, preserving formatting including
comments and whitespace.


%package doc
Summary: Documentation for %name
Group: Documentation
Requires: %name = %version-%release
BuildArch: noarch

%description doc
Documentation for %name

%prep
%setup -n %orig_name-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

rm -f %buildroot%ruby_ri_sitedir/cache.ri
rm -f %buildroot%ruby_ri_sitedir/created.rid
rm -f %buildroot%_datadir/*.netrc

%check
chmod 600 data/newlineless.netrc
%ruby_test_unit -Ilib --ignore-name='test_encrypted_roundtrip' test

%files
%doc Readme.md changelog.txt
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%doc changelog.txt
%doc data
%doc test
%ruby_ri_sitedir/*

%changelog
* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.10.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Sun Sep 25 2016 Evgeny Sinelnikov <sin@altlinux.ru> 0.10.3-alt1
- Update to last release

* Sat Dec 08 2012 Evgeny Sinelnikov <sin@altlinux.ru> 0.7.7-alt1
- Initial build for Sisyphus

