%define bname iconv
Name: ruby-%bname
Version: 1.0.4
Release: alt2
Summary: Ruby iconv module
License: Ruby
Group:   Development/Ruby
URL:     https://github.com/nurse/iconv
Source:  %name-%version.tar
Conflicts: rubu-stdlibs <= 1.9.3
Requires: ruby-stdlibs

BuildPreReq: rpm-build-ruby ruby-tool-setup
BuildRequires: ruby libruby-devel ruby-tool-rdoc

%description
This package contains deprecated Ruby iconv module.

%prep
%setup -q
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%files
%ruby_sitelibdir/*
%ruby_sitearchdir/*
%ruby_ri_sitedir/*

%changelog
* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt2
- Rebuild with new %%ruby_sitearchdir location

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1
- new version 1.0.4

* Fri Mar 21 2014 Led <led@altlinux.ru> 1.0-alt1
- initial build
