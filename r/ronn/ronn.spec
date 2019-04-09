%define	       pkgname ronn

Name:          %pkgname
Version:       0.7.3
Release:       alt2
Summary:       Ronn builds manuals from Markdown to roff format
License:       MIT
Group:         Development/Documentation
Url:           https://github.com/rtomayko/ronn/
# VCS:         https://github.com/rtomayko/ronn.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-hpricot
BuildRequires: rdiscount
BuildRequires: mustache

%description
Ronn builds manuals. It converts simple, human readable textfiles to
roff for terminal display, and also to HTML for the web. The source
format includes all of Markdown but has a more rigid structure and
syntax extensions for features commonly found in manpages (definition
lists, link notation, etc.). The ronn-format(7) manual page defines the
format in detail.


%package       -n gem-%pkgname
Summary:       Ruby library files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname
Documentation files for %gemname gem.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%doc README*
%_bindir/%name
%_mandir/*.1*
%_mandir/*.7*

%files         -n gem-%pkgname
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%changelog
* Tue Apr 09 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.3-alt1
- Initial build for Sisyphus
