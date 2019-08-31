%define        pkgname clamp

Name:          gem-%pkgname
Version:       1.3.0
Release:       alt1
Summary:       a Ruby command-line application framework 
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mdub/clamp
%vcs           https://github.com/mdub/clamp.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
"Clamp" is a minimal framework for command-line utilities.

It handles boring stuff like parsing the command-line, and generating help, so
you can get on with making your command actually do stuff.


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
* Thu Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
