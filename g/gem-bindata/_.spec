# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname bindata

Name:          gem-%pkgname
Version:       2.4.8
Release:       alt1
Summary:       BinData - Parsing Binary Data in Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/dmendel/bindata
Vcs:           https://github.com/dmendel/bindata.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
%summary.

BinData provides a declarative way to read and write structured binary data.

This means the programmer specifies what the format of the binary data is,
and BinData works out how to read and write data in this format. It is an
easier (and more readable) alternative to ruby's #pack and #unpack methods.

BinData makes it easy to create new data types. It supports all the common
primitive datatypes that are found in structured binary data formats. Support
for dependent and variable length fields is built in.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 2.4.8-alt1
- + packaged gem with usage Ruby Policy 2.0
