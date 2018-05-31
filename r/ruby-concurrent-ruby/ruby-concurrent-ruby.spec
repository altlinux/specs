%define  pkgname concurrent-ruby

Name:    ruby-%pkgname
Version: 1.0.5
Release: alt1

Summary: Modern concurrency tools including agents, futures, promises, thread pools, supervisors, and more. Inspired by Erlang, Clojure, Scala, Go, Java, JavaScript, and classic concurrency patterns.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/ruby-concurrency/concurrent-ruby

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel

%filter_from_requires /^ruby(\(atomic\|concurrent_ruby_ext\|jruby\|win32ole\)/d

%description
%summary

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
* Fri Jun 01 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1
- Initial build for Sisyphus
