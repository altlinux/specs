%define  pkgname cleanroom
 
Name: 	 ruby-%pkgname
Version: 1.0.0 
Release: alt1
 
Summary: (More) safely evaluate Ruby DSLs with cleanroom
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/sethvargo/cleanroom
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
Ruby is an excellent programming language for creating and managing
custom DSLs, but how can you securely evaluate a DSL while explicitly
controlling the methods exposed to the user? Our good friends
instance_eval and instance_exec are great, but they expose all methods -
public, protected, and private - to the user. Even worse, they expose
the ability to accidentally or intentionally alter the behavior of the
system! The cleanroom pattern is a safer, more convenient, Ruby-like
approach for limiting the information exposed by a DSL while giving
users the ability to write awesome code!

The cleanroom pattern is a unique way for more safely evaluating Ruby
DSLs without adding additional overhead.

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
%ruby_test_unit -Ilib:test test
 
%files
%doc README*
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Thu May 21 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial build for ALT Linux
