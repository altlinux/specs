%define plugname will_paginate

Name: rails-plugin-%plugname
Version: 2.3.11
Release: alt1
Summary: Most awesome pagination solution for Rails
License: MIT
Group: Development/Ruby
Url: http://rubyforge.org/projects/seattlerb/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %plugname-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

PreReq: ruby-railties >= 2.1.0-alt2

# Automatically added by buildreq on Sun Jul 13 2008 (-bi)
BuildRequires: rpm-build-ruby ruby-tool-rdoc ruby-tool-setup

%description
Pagination is just limiting the number of records displayed. Why
should you let it get in your way while developing, then? This
plugin makes magic happen. Did you ever want to be able to do
just this on a model:

  Post.paginate :page => 1, :order => 'created_at DESC'

... and then render the page links with a single view helper?
Well, now you can.

%package doc
Summary: Documentation files for %plugname rails plugin
Group: Documentation

%description doc
Documentation files for %plugname rails plugin.

%prep
%setup -q -n %plugname-%version
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
mkdir -p %buildroot%_datadir/rails/plugins/%plugname
%ruby_install
install -p -m644 init.rb %buildroot%_datadir/rails/plugins/%plugname/
%rdoc lib/

%files
%doc CHANGELOG.rdoc README.rdoc
%ruby_sitelibdir/*
%_datadir/rails/plugins/%plugname

%files doc
%ruby_ri_sitedir/WillPaginate*

%changelog
* Tue Jun 30 2009 Alexey I. Froloff <raorn@altlinux.org> 2.3.11-alt1
- [2.3.11]

* Tue Sep 09 2008 Sir Raorn <raorn@altlinux.ru> 2.3.3-alt1
- [2.3.3]

* Sun Jul 13 2008 Sir Raorn <raorn@altlinux.ru> 2.3.2-alt1
- Built for Sisyphus

