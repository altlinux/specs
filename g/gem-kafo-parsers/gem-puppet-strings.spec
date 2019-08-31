%define        pkgname kafo-parsers
%define        gemname kafo_parsers

Name:          gem-%pkgname
Version:       1.0.0
Release:       alt1
Summary:       This gem can parse values, validations, documentation, types, groups and conditions of parameters from your puppet modules
License:       GPLv3+
Group:         Development/Ruby
Url:           https://github.com/theforeman/kafo_parsers
%vcs           https://github.com/theforeman/kafo_parsers.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
This gem can parse values, validations, documentation, types, groups and
conditions of parameters from your puppet modules. Only thing you have to do is
provide a path to manifest file you want to be parsed.

The library is used in Kafo, which can be used to get an idea of what's possible
to build on top of this library.

Currently puppet classes and types (definitions) are supported.


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
* Thu Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
