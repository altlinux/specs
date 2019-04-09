%define  pkgname configparser

Name:    ruby-%pkgname
Version: 0.1.7
Release: alt1

Summary: parses configuration files compatible with Python's ConfigParser
License: MIT
Group:   Development/Ruby
Url:     https://github.com/chrislee35/configparser

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

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%doc *.md
%ruby_gemspec
%ruby_gemlibdir

%files doc
%ruby_gemdocdir

%changelog
* Tue Apr 09 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.7-alt1
- Initial build for Sisyphus
