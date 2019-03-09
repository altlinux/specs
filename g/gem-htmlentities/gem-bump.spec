%define        pkgname htmlentities

Name:          gem-%pkgname
Version:       4.3.3
Release:       alt1
Summary:       HTML entity encoding and decoding for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/threedaymonk/htmlentities
# VCS:         https://github.com/threedaymonk/htmlentities.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch
Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
HTMLEntities is a simple library to facilitate encoding and decoding of named
(&yacute; and so on) or numerical (&#123; or &#x12a;) entities in HTML and XHTML
documents.


%package       doc
Summary:       Documentation files for %name
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
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Sat Feb 23 2019 Pavel Skrylev <majioa@altlinux.org> 4.3.3-alt1
- Initial build for Sisyphus, packaged as a gem according to Ruby Policy 2.0.
