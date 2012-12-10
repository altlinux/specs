# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname right_http_connection

Name: ruby-%pkgname
Version: 1.2.4
Release: alt2.1

Summary: Robust HTTP/S Ruby library
Group: Development/Ruby
License: MIT/Ruby
Url: http://github.com/rightscale/right_http_connection

BuildArch: noarch

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Mon Apr 26 2010 (-bi)
BuildRequires: rpm-build-ruby ruby-tool-rdoc ruby-tool-setup

%description
Rightscale::HttpConnection is a robust HTTP/S library.  It implements a
retry algorithm for low-level network errors.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%files
%doc README.txt History.txt
%ruby_sitelibdir/*

%files doc
%dir %ruby_ri_sitedir/Rightscale
%ruby_ri_sitedir/Rightscale/HttpConnection

%changelog
* Wed Dec 05 2012 Led <led@altlinux.ru> 1.2.4-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Thu Dec 09 2010 Alexey I. Froloff <raorn@altlinux.org> 1.2.4-alt2
- New git snapshot

* Mon Apr 26 2010 Alexey I. Froloff <raorn@altlinux.org> 1.2.4-alt1
- Built for Sisyphus

