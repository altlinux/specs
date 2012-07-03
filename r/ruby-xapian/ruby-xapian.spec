%define oname xapian-bindings

Name: ruby-xapian
Version: 1.2.3
Release: alt1

Summary: Xapian search engine interface for Ruby
License: GPLv2
Group: Development/Ruby
Url: http://www.xapian.org/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source0: %oname-%version.tar.gz

# Automatically added by buildreq on Sun Mar 14 2010
BuildRequires: gcc-c++ libruby-devel libxapian-devel ruby

%description
Xapian is an Open Source Probabilistic Information Retrieval
framework. It offers a highly adaptable toolkit that allows
developers to easily add advanced indexing and search facilities
to applications. This package provides the files needed for
developing Python scripts which use Xapian.

%prep
%setup -n %oname-%version
# due to missing .la file
subst "s|--ltlibs|--libs|g" configure

%build
%configure --with-ruby
%make_build

%install
mkdir -p %buildroot%ruby_sitearchdir/
install -p -m644 ruby/.libs/_xapian.so %buildroot%ruby_sitearchdir/

mkdir -p %buildroot%ruby_sitelibdir/
install -p -m644 ruby/xapian.rb %buildroot%ruby_sitelibdir/

%files
%doc README
%ruby_sitearchdir/_xapian.so
%ruby_sitelibdir/xapian.rb

# TODO:
# - rework as full xapian-bindings package w/subpackages

%changelog
* Tue Oct 12 2010 Michael Shigorin <mike@altlinux.org> 1.2.3-alt1
- 1.2.3
- minor spec cleanup

* Sun Mar 14 2010 Igor Zubkov <icesik@altlinux.org> 1.0.18-alt1
- 1.0.17 -> 1.0.18

* Sun Jan 03 2010 Igor Zubkov <icesik@altlinux.org> 1.0.17-alt1
- build for Sisyphus

