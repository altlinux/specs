%define  pkgname io-like

Name:    ruby-%pkgname
Version: 0.3.0
Release: alt1

Summary: A Ruby module which provides the interface of IO objects to classes providing a few simple methods.
License: GPL
Group:   Development/Ruby
Url:     https://github.com/javanthropus/io-like

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar
Source1: io-like-0.3.0.gemspec

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

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
cp %SOURCE1 io-like.gemspec
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
* Wed Sep 05 2018 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus bumped to 0.3.0.
