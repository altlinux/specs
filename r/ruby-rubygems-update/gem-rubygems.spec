%define  pkgname rubygems-update

Name:    ruby-%pkgname
Version: 3.0.1
Release: alt1

Summary: Library packaging and distribution for Ruby.
License: MIT
Group:   Development/Ruby
Url:     https://rubygems.org/
# VCS:   https://github.com/rubygems/rubygems.git

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

Requires: /usr/bin/gem
BuildRequires(pre): rpm-build-ruby

%description
RubyGems is a package management framework for Ruby.

A package (also known as a library) contains a set of functionality that can be
invoked by a Ruby program, such as reading and parsing an XML file. We call
these packages "gems" and RubyGems is a tool to install, create, manage and
load these packages in your Ruby environment.

RubyGems is also a client for RubyGems.org, a public repository of Gems that
allows you to publish a Gem that can be shared and used by other developers.
See our guide on publishing a Gem at guides.rubygems.org

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
mkdir -p %buildroot%rubygem_gemdir/%pkgname-%version/lib/
mv %buildroot%ruby_sitelibdir/* %buildroot%rubygem_gemdir/%pkgname-%version/lib/
rm %buildroot%_bindir/gem

%check
%rake_test

%files
%doc *.md
%_bindir/*
%rubygem_gemdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Sat Dec 29 2018 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- Initial build for Sisyphus, packaged as a gem
