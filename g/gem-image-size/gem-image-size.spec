%define        pkgname image-size

Name:          gem-%pkgname
Version:       2.0.0
Release:       alt1
Summary:       HTML entity encoding and decoding for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/toy/image_size
# VCS:         https://github.com/toy/image_size.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch
Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
HTMLEntities is a simple library to facilitate encoding and decoding of named
(&yacute; and so on) or numerical (&#123; or &#x12a;) entities in HTML and XHTML
documents.


%package       doc
Summary:       Documentation files for %pkgname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %{name}.

%description   doc -l ru_RU.UTF-8
Документация для %{name}.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%ruby_gemspecdir/*
%ruby_gemslibdir/*

%files         doc
%ruby_gemsdocdir/*

%changelog
* Sat Feb 23 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus, packaged as a gem according to Ruby Policy 2.0.
