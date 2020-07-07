# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname aliyun-sdk

Name:          gem-%pkgname
Version:       0.7.2
Release:       alt1
Summary:       Aliyun OSS SDK for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://www.rubydoc.info/gems/aliyun-sdk/
Vcs:           https://github.com/aliyun/aliyun-oss-ruby-sdk.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
Alibaba Cloud OSS SDK for Ruby is a Ruby client program for convenient access
to Alibaba Cloud OSS (Object Storage Service) RESTful APIs. For more information
about OSS, visit the OSS official website.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       devel
Summary:       Development files for %gemname gem
Group:         Development/Ruby
BuildArch:     noarch

%description   devel
Development files for %gemname gem.

%description   devel -l ru_RU.UTF8
Файлы заголовков для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --ignore=rails

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         doc
%ruby_gemdocdir

%files         devel
%ruby_includedir/*


%changelog
* Mon Jun 15 2020 Pavel Skrylev <majioa@altlinux.org> 0.7.2-alt1
- + packaged gem with usage Ruby Policy 2.0
