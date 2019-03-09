%define        pkgname libyajl2

Name:          gem-%pkgname
Version:       1.2.0
Release:       alt1
Summary:       gem to install the libyajl2 c-library for distributions which do not have it
Group:         Development/Ruby
License:       MIT/Ruby
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Url:           https://github.com/chef/libyajl2-gem
# VCS:         https://github.com/chef/libyajl2-gem.git
BuildArch:     noarch

Source:        %pkgname-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist *.sh

%description
%summary.

%package       doc
Summary:       Documentation files for %name
Group:         Documentation
BuildArch:     noarch

%description doc
Documentation files for %name.

%prep
%setup -n %pkgname-%version

%build
%gem_build

%install
%gem_install --mode=flex

%check
%gem_test

%files
%doc *.md
%ruby_gemlibdir/*
%ruby_gemspecdir/*

%files doc
%ruby_gemdocdir/*

%changelog
* Tue Feb 05 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- Initial build to ALT of 1.2.0 with usage of Ruby Policy 2.0.
