%define  pkgname nio4r

Name:    ruby-%pkgname
Version: 2.3.1
Release: alt1

Summary: New I/O for Ruby: Cross-platform asynchronous I/O primitives for scalable network clients and servers
License: MIT
Group:   Development/Ruby
Url:     https://github.com/socketry/nio4r

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel

%filter_from_requires /^ruby(jruby)/d

%description
New I/O for Ruby (nio4r): cross-platform asynchronous I/O primitives for
scalable network clients and servers. Modeled after the Java NIO API,
but simplified for ease-of-use. nio4r provides an abstract,
cross-platform stateful I/O selector API for Ruby. I/O selectors are the
heart of "reactor"-based event loops, and monitor multiple I/O objects
for various types of readiness, e.g. ready for reading or writing.

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
* Fri Jun 15 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1
- Initial build for Sisyphus
