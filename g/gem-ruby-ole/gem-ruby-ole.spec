%define  pkgname ruby-ole

Name:    gem-%pkgname
Version: 1.2.12.1
Release: alt1

Summary: A library for easy read/write access to OLE compound documents for Ruby
License: MIT
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

%package -n oletool
Summary: Oletool is an executable to operate with OLE2 structured storage files from console.
Group: System/Base

BuildArch: noarch

Requires: ruby-gem(%pkgname) = %version

%description -n oletool
Oletool is an executable to operate with OLE2 structured storage files from
console.

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
rake test

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%files -n oletool
%_bindir/*

%changelog
* Wed Dec 19 2018 Pavel Skrylev <majioa@altlinux.org> 1.2.12.1-alt1
- Initial build for Sisyphus bumped to 1.2.12.1.
