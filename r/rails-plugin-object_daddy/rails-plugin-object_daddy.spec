# vim: set ft=spec: -*- rpm-spec -*-

%define plugname object_daddy

Name: rails-plugin-object_daddy
Version: 0.4.2
Release: alt2

Summary: Library designed to assist in automating testing of large collections of objects
License: MIT
Group: Development/Ruby
Url: http://github.com/flogic/object_daddy

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %plugname-%version.tar
Patch: %plugname-%version-%release.patch

PreReq: ruby-railties >= 2.1.0-alt2

# Automatically added by buildreq on Sun Oct 25 2009 (-bi)
BuildRequires: rpm-build-ruby ruby-tool-rdoc

%description
Object Daddy is a library (as well as a Ruby on Rails plugin) designed to
assist in automating testing of large collections of objects, especially webs
of ActiveRecord models. It is a descendent of the "Object Mother" pattern for
creating objects for testing, and is related to the concept of an "object
exemplar" or stereotype.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -q -n %plugname-%version
%patch -p1

%install
mkdir -p %buildroot%_datadir/rails/plugins/%plugname
cp -vpr init.rb lib/ %buildroot%_datadir/rails/plugins/%plugname/
%rdoc lib/

%files
%doc README.markdown
%_datadir/rails/plugins/%plugname

%files doc
%ruby_ri_sitedir/ObjectDaddy*

%changelog
* Sun Apr 25 2010 Alexey I. Froloff <raorn@altlinux.org> 0.4.2-alt2
- Allow creation of objects with generated attr_protected attributes

* Sun Oct 25 2009 Alexey I. Froloff <raorn@altlinux.org> 0.4.2-alt1
- Built for Sisyphus

