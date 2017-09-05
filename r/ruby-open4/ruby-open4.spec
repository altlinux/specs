%define orig_name open4

Summary: Manage child processes and their IO handles easily
Name: ruby-%orig_name
Version: 1.3.3
Release: alt1.1
Group: Development/Ruby
License: BSD or Ruby
URL: http://github.com/ahoward/open4
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

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
%setup -n %name-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

rm -f %buildroot%ruby_ri_sitedir/cache.ri
rm -f %buildroot%ruby_ri_sitedir/created.rid

%check
#ruby_test_unit -Ilib -Itest/support test

%files
%doc LICENSE
%ruby_sitelibdir/*

%files doc
%doc samples
%doc test
%doc white_box
%ruby_ri_sitedir/*

%changelog
* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.3-alt1.1
- Rebuild with Ruby 2.4.1

* Sun Sep 25 2016 Evgeny Sinelnikov <sin@altlinux.ru> 1.3.3-alt1
- Update to latest release

* Sat Dec 08 2012 Evgeny Sinelnikov <sin@altlinux.ru> 1.3.0-alt1
- Initial build for Sisyphus

