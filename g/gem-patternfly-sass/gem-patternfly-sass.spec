%define        pkgname patternfly-sass

Name:          gem-%pkgname
Version:       3.59.4
Release:       alt1
Summary:       Red Hat's Patternfly, converted to Sass and ready to drop into Rails
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://www.patternfly.org/
%vcs           https://github.com/patternfly/patternfly.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

#%gem_replace_version font-awesome-sass ~> 5.0
#%gem_replace_version sass ~> 3.4

%description
This reference implementation of PatternFly is based on Bootstrap v3. Think of
PatternFly as a "skinned" version of Bootstrap with additional components and
customizations. For information on how to quickly get started using PatternFly,
see the Quick Start Guide. Looking for RCUE (Red Hat Common User Experience)
information? See the RCUE Quick Start Guide.


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
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 3.59.4-alt1
- ^ v3.59.4
- ! spec

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 3.59.1-alt1
- + initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
