
Name:    ruby-addressable
Version: 2.5.0
Release: alt1

Summary: Addressable is a replacement for the URI implementation that is part of Ruby's standard library
Group:   Development/Ruby
License: MIT/Ruby
URL:     http://addressable.rubyforge.org/

BuildArch: noarch

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-test-unit
BuildRequires: ruby-tool-setup

Source: %name-%version.tar

%description
Addressable is a replacement for the URI implementation that is part of
Ruby's standard library. It more closely conforms to RFC 3986, RFC 3987,
and RFC 6570 (level 4), providing support for IRIs and URI templates.

%package doc
Summary:   Documentation for %name
Group:     Development/Documentation
Requires:  %name = %version-%release
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -n %name-%version
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
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1
- new version 2.5.0

* Sun Jun 05 2016 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt1
- new version 2.4.0

* Wed Mar 05 2014 Andrey Cherepanov <cas@altlinux.org> 2.3.5-alt1
- Initial build for ALT Linux

