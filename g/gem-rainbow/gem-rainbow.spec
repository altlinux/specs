%define        pkgname rainbow

Name:          gem-%pkgname
Version:       3.0.0
Release:       alt1
Summary:       Colorize printed text on ANSI terminals
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sickill/rainbow
# VCS:         https://github.com/sickill/rainbow.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler)

%description
Rainbow is a ruby gem for colorizing printed text on ANSI terminals.

It provides a string presenter object, which adds several methods to your
strings for wrapping them in ANSI escape codes. These codes when printed in a
terminal change text attributes like text color, background color, intensity
etc.


%package       doc
Summary:       Documentation files for %name
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %{name}.


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
* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
