Name: ruby-mechanize
Version: 0.9.3
Release: alt1

Summary: WWW::Mechanize, a handy web browsing ruby object
License: GPLv2
Group: Development/Ruby
Url: http://rubyforge.org/projects/mechanize/

Source0: mechanize-%version.tgz

Packager: Igor Zubkov <icesik@altlinux.org>

BuildArch: noarch

# Automatically added by buildreq on Fri Dec 11 2009 (-bi)
BuildRequires: rpm-build-ruby ruby-tool-rdoc ruby-tool-setup

%description
The Mechanize library is used for automating interaction with websites.
Mechanize automatically stores and sends cookies, follows redirects,
can follow links, and submit forms.  Form fields can be populated and
submitted.  Mechanize also keeps track of the sites that you have visited as
a history.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name.

%prep
%setup -q -n mechanize-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%files
%doc CHANGELOG.rdoc EXAMPLES.rdoc FAQ.rdoc GUIDE.rdoc LICENSE.rdoc README.rdoc
%ruby_sitelibdir/*

%files doc
%doc examples
%ruby_ri_sitedir/Net
%ruby_ri_sitedir/WWW

%changelog
* Fri Dec 11 2009 Igor Zubkov <icesik@altlinux.org> 0.9.3-alt1
- build for Sisyphus

