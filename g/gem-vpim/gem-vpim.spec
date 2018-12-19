%define  pkgname vpim

Name:    gem-%pkgname
Version: 13.11.11
Release: alt1

Summary: vPim provides calendaring, scheduling, and contact support for Ruby
License: GPL
Group:   Development/Ruby
Url:     https://github.com/aquasync/ruby-ole
# VCS:   https://github.com/aquasync/ruby-ole.git

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby

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
mkdir %{pkgname}_icalendar
cp gemspec.rb %{pkgname}_icalendar/
rm %{pkgname}_icalendar.gemspec
sed -e "/'ubygems/d" -e "/'pp/d" -e "s/FileList/Rake::FileList/" -i %{pkgname}.gemspec
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
#make test

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Dec 19 2018 Pavel Skrylev <majioa@altlinux.org> 13.11.11-alt1
- Initial build for Sisyphus bumped to 13.11.11.
