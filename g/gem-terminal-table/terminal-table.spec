%define _unpackaged_files_terminate_build 1

Name:    gem-terminal-table
Version: 3.0.0
Release: alt1

Summary: Simple, feature rich ascii table generation library
License: MIT
Group:   Development/Ruby
Url:     https://github.com/tj/terminal-table

Packager:  Dmitriy Voropaev <voropaevdmtr@altlinux.org>
BuildArch: noarch

Source:  %name-%version.tar
Patch: %name-%version-%release.patch
BuildRequires(pre): rpm-build-ruby

%description
Simple, feature rich ascii table generation library

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %name.

%prep
%setup -n %name-%version
%autopatch -p1
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
%doc *.md
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Mar 16 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 3.0.0-alt1
- initial build
