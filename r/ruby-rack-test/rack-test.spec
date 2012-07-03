# vim: set ft=spec: -*- rpm-spec -*-

%define plugname rack-test

Name: ruby-%plugname
Version: 0.5.3
Release: alt1

Summary: a small, simple testing API for Rack apps
License: MIT
Group: Development/Ruby
Url: http://gitrdoc.com/brynary/rack-test/tree/master

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
Source: %name-%version.tar

PreReq: ruby-railties >= 2.1.0-alt2

BuildRequires: ruby-test-unit ruby-tool-rdoc ruby-tool-setup rpm-build-ruby ruby-rack

%description
Rack::Test is a small, simple testing API for Rack apps. It can be used on its
own or as a reusable starting point for Web frameworks and testing libraries to
build on. Most of its initial functionality is an extraction of Merb 1.0's
request helpers feature.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -q
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
mkdir -p %buildroot%_datadir/rails/plugins/%plugname
%ruby_install
%rdoc lib/


%files
%doc README.rdoc History.txt
%ruby_sitelibdir/rack/*

%files doc
%ruby_ri_sitedir/Rack/Test

%changelog
* Thu Feb 18 2010 Timur Batyrshin <erthad@altlinux.org> 0.5.3-alt1
- Initial build for sisyphus


