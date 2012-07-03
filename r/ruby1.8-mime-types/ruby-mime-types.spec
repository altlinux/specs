# vim: set ft=spec: -*- rpm-spec -*-

%define ruby_major 1.8
%define pkgname mime-types

Name: ruby%ruby_major-%pkgname
Version: 1.18
Release: alt1

Summary: Manages a MIME Content-Type database that will return the Content-Type for a given filename
Group: Development/Ruby
License: Ruby/GPLv2+
Url: http://rubyforge.org/projects/mime-types/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source0: %pkgname-%version.tar
Patch0: %pkgname-%version-%release.patch

# Automatically added by buildreq on Sat Dec 12 2009 (-bi)
BuildRequires: rpm-build-ruby ruby%ruby_major-tool-rdoc ruby%ruby_major-tool-setup

%description
MIME::Types for Ruby originally based on and synchronized with MIME::Types for
Perl by Mark Overmeer, copy right 2001 - 2009. As of version 1.15, the data
format for the MIME::Type list has changed and the synchronization will no
longer happen.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name.

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%files
%doc *.txt
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/MIME

%changelog
* Sat Apr 14 2012 Evgeny Sinelnikov <sin@altlinux.ru> 1.18-alt1
- Initial ruby-1.8 version build for Sisyphus

* Sat Dec 12 2009 Igor Zubkov <icesik@altlinux.org> 1.16-alt1
- build for Sisyphus



