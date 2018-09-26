%define  pkgname roadie

Name:    ruby-%pkgname
Version: 3.4.0
Release: alt1

Summary: Making HTML emails comfortable for the Ruby rockstars
License: MIT
Group:   Development/Ruby
Url:     https://github.com/Mange/roadie

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
Roadie tries to make sending HTML emails a little less painful by inlining
stylesheets and rewriting relative URLs for you inside your emails.

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
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Sep 25 2018 Pavel Skrylev <majioa@altlinux.org> 3.4.0-alt1
- Initial gemified build for Sisyphus
