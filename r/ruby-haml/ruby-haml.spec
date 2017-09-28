%define  pkgname haml

Name: 	 ruby-%pkgname
Version: 5.0.3
Release: alt1

Summary: HTML Abstraction Markup Language - A Markup Haiku
License: MIT
Group:   Development/Ruby
Url:     https://github.com/haml/haml

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

%filter_from_requires \!^ruby(haml/filters/textile)$!d;
%filter_from_requires \!^ruby(haml/filters/maruku)$!d;
%filter_from_requires /^ruby(action_view)$/d;

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
Haml is a templating engine for HTML. It's designed to make it both easier and
more pleasant to write HTML documents, by eliminating redundancy, reflecting
the underlying structure that the document represents, and providing an elegant
syntax that's both powerful and easy to understand.

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
%_bindir/%pkgname

%files doc
%ruby_ri_sitedir/*

%changelog
* Thu Sep 28 2017 Mikhail Gordeev <obirvalger@altlinux.org> 5.0.3-alt1
- Initial build for Sisyphus
