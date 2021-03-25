%define _unpackaged_files_terminate_build 1

Name:    gem-em-websocket
Version: 0.5.2
Release: alt1

Summary: EventMachine based WebSocket server
License: MIT
Group:   Development/Ruby
Url:     https://github.com/igrigorik/em-websocket/

Packager:  Dmitriy Voropaev <voropaevdmtr@altlinux.org>
BuildArch: noarch

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
EventMachine based WebSocket server

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %name.

%prep
%setup -n %name-%version
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
* Tue Mar 21 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.5.2-alt1
- initial build
