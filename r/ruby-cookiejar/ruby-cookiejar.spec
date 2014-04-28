%define  pkgname cookiejar
 
Name: 	 ruby-%pkgname
Version: 0.3.2 
Release: alt1
 
Summary: The Ruby CookieJar is a library to help manage client-side cookies in pure Ruby
License: MIT/Ruby
Group:   Development/Ruby
Url:     http://github.com/dwaite/cookiejar
 
Packager: Andrey Cherepanov <cas@altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-test-unit ruby-tool-rdoc ruby-tool-setup
 
%description
The Ruby CookieJar is a library to help manage client-side cookies in
pure Ruby. It enables parsing and setting of cookie headers, alternating
between multiple 'jars' of cookies at one time (such as having a set of
cookies for each browser or thread), and supports persistence of the
cookies in a JSON string. Both Netscape/RFC 2109 cookies and RFC 2965
cookies are supported.

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
# For arch-specific files
#%%ruby_sitearchdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt1
- Initial build for ALT Linux
