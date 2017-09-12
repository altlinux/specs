%define orig_name httpclient

Summary: HTTP accessing library for Ruby
Name: ruby-%orig_name
Version: 2.8.2.4
Release: alt1.1
Group: Development/Ruby
License: GPLv2 or Ruby License
URL: https://github.com/nahi/httpclient
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildArch: noarch

BuildRequires: rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: ruby-tool-rdoc
BuildRequires: ruby-test-unit

%filter_from_requires /^ruby(httpclient\/jruby_ssl_socket)/d

%description
HTTP library gives something like the functionality of libwww-perl (LWP) in Ruby


%package doc
Summary: Documentation for %name
Group: Documentation
Requires: %name = %version-%release
BuildArch: noarch

%description doc
Documentation for %name

%prep
%setup -n %name-%version
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%check

%files
%doc README.md CHANGELOG.md
%_bindir/httpclient
%_bindir/jsonclient
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.8.2.4-alt1.1
- Rebuild with Ruby 2.4.1

* Sun Sep 25 2016 Evgeny Sinelnikov <sin@altlinux.ru> 2.8.2.4-alt1
- Update to latest release
 + Security CVE-2014-3566 critical to rhc:
   https://blog.openshift.com/poodle-ssl-vulnerability/

* Mon Aug 12 2013 Evgeny Sinelnikov <sin@altlinux.ru> 2.3.4.1-alt1
- Initial build for Sisyphus

