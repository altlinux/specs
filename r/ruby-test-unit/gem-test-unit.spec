%define  pkgname test-unit

Name:    ruby-%pkgname
Epoch:   1
Version: 3.2.9
Release: alt1

Summary: An xUnit family unit testing framework for Ruby.
License: GPLv2
Group:   Development/Ruby
Url:     http://test-unit.github.io/
# VCS:   https://github.com/test-unit/test-unit.git

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
#BuildRequires: gem(yard)

%description
An xUnit family unit testing framework for Ruby.

test-unit (Test::Unit) is unit testing framework for Ruby, based on xUnit
principles. These were originally designed by Kent Beck, creator of extreme
programming software development methodology, for Smalltalk's SUnit. It allows
writing tests, checking results and automated testing in Ruby.

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
#%rake_test

%files
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Jan 15 2019 Pavel Skrylev <majioa@altlinux.org> 1:3.2.9-alt1
- Bump to 3.2.9

* Sat Dec 29 2018 Pavel Skrylev <majioa@altlinux.org> 2.5.3-alt1
- Initial build for Sisyphus, packaged as a gem
