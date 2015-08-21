%define  pkgname syslog-logger
 
Name: 	 ruby-%pkgname
Version: 1.6.8 
Release: alt1
 
Summary: An improved Logger replacement that logs to syslog. It is almost drop-in with a few caveats
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/ngmoco/syslog_logger
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
Logger::Syslog is a Logger replacement that logs to syslog. It is almost
drop-in with a few caveats. You can add Logger::Syslog to your Rails
production environment to aggregate logs between multiple machines.

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
#ruby_test_unit -Ilib:test test
 
%files
%doc README*
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Wed Aug 19 2015 Andrey Cherepanov <cas@altlinux.org> 1.6.8-alt1
- Initial build for ALT Linux
- Disable tests
