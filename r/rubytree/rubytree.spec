%define pkgname rubytree

Name: %pkgname
Version: 1.0.0
Release: alt1

Summary: Simple implementation of the generic Tree data structure
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubytree.anupamsg.me/

BuildArch: noarch

Source: %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-gem(structured_warnings)

%description
Rubytree is a simple implementation of the generic Tree data structure.
This implementation is node-centric, where the individual nodes on the
tree are the primary objects and drive the structure.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%check
#%%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/Tree*

%changelog
* Tue Oct 02 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- New version.
- Disable tests.

* Tue Dec 04 2012 Led <led@altlinux.ru> 0.5.2-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Sat Nov 28 2009 Alexey I. Froloff <raorn@altlinux.org> 0.5.2-alt1
- Built for Sisyphus

