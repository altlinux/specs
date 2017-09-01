%define  pkgname parse-cron

Name: ruby-%pkgname
Version: 0.1.4
Release: alt1

Summary: Parse crontab syntax to determine scheduled run times
License: MIT
Group:   Development/Ruby
Url:     https://github.com/siebertm/parse-cron
BuildArch: noarch
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel

%description
Parse crontab syntax to determine scheduled run times.
The goal of this gem is to parse a crontab timing specification
and determine when the job should be run.
It is not a scheduler, it does not run the jobs.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup
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
* Fri Sep 01 2017 Alexey Shabalin <shaba@altlinux.ru> 0.1.4-alt1
- Initial build in Sisyphus

