%define _unpackaged_files_terminate_build 1

Name:    gem-kramdown-parser-gfm
Version: 1.0.1
Release: alt1

Summary: This is a parser for kramdown that converts Markdown documents in the GFM dialect to HTML.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/kramdown/parser-gfm

Packager:  Dmitriy Voropaev <voropaevdmtr@altlinux.org>
BuildArch: noarch

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem-kramdown
BuildRequires: gem-rexml
%description
This is a parser for kramdown that converts Markdown documents
in the GFM dialect to HTML.

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

%check
%ruby_test_unit -Ilib:test test

%files
%doc *.md
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Mar 16 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 1.0.1-alt1
- initial build
