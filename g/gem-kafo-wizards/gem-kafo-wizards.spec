%define        pkgname kafo-wizards
%define        gemname kafo_wizards

Name:          gem-%pkgname
Version:       0.0.1
Release:       alt1
Summary:       This gem helps to create wizard like interfaces in terminal applications, has support for nesting and value validation
License:       GPLv3+
Group:         Development/Ruby
Url:           https://github.com/theforeman/kafo_wizards
%vcs           https://github.com/theforeman/kafo_wizards.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
With this gem it is possible to define form or wizard and display it to the user
using one of the defined backends. The form definition is independent on
the chosen backend so it can be changed freely. Currently only command line
(highline) backend is implemented, YAD or web based backend is planed.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Thu Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 0.0.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
