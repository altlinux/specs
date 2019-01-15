%define  pkgname xmlrpc

Name:    ruby-%pkgname
Version: 0.3.0
Release: alt1

Summary: The Ruby standard library package 'xmlrpc'
License: BSD 2-clause Simplified License
Group:   Development/Ruby
Url:     https://github.com/ruby/xmlrpc
# VCS:   https://github.com/ruby/xmlrpc.git

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
XMLRPC is a lightweight protocol that enables remote procedure calls over HTTP.
It is defined at http://www.xmlrpc.com.

XMLRPC allows you to create simple distributed computing solutions that span
computer languages. Its distinctive feature is its simplicity compared to other
approaches like SOAP and CORBA.

The Ruby standard library package 'xmlrpc' enables you to create a server that
implements remote procedures and a client that calls them. Very little code is
required to achieve either of these.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%update_setup_rb
rm -f bin/{console,setup}

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
#%rake_test

%files
%doc *.md
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Jan 14 2019 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus, packaged as a gem
