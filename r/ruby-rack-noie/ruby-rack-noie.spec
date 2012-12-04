# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname rack-noie

Name: ruby-%pkgname
Version: 0.1.0
Release: alt1.1

Summary: A Rack middleware to redirect (*cough* kick) IE6 users out of your website
Group: Development/Ruby
License: MIT/Ruby
Url: http://github.com/juliocesar/rack-noie

BuildArch: noarch

Source: ruby-%pkgname-%version.tar

# Automatically added by buildreq on Wed Mar 24 2010 (-bi)
BuildRequires: rpm-build-ruby ruby-test-unit ruby-tool-rdoc ruby-tool-setup ruby-rack-test

%description
rack-noie is the coolest rack middleware ever created. And it is so because it
does everyone a favor: it shows the way out of your website to poor souls out
there using Internet Explorer 6.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/


%check
%ruby_test_unit -Ilib:test -p '.*\_test\.rb' test

%files
%doc README.markdown
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/Rack/NoIE

%changelog
* Fri Dec 07 2012 Led <led@altlinux.ru> 0.1.0-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Wed Mar 24 2010 Timur Batyrshin <erthad@altlinux.org> 0.1.0-alt1
- Built for Sisyphus

