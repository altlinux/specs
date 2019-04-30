%define        pkgname  binman

Name:          gem-%pkgname
Version:       5.1.0
Release:       alt1
Summary:       Creates manual pages from header comments
License:       ISC
Group:         Development/Ruby
Url:           http://sunaku.github.io/binman/man/
# VCS:         https://github.com/sunaku/binman.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
binman generates manual pages from header comments in your scripts so that you
can keep your documentation and implementation together, in the same file, for
easy maintenance. But keeping them apart, in separate files, is supported too.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


%package       -n %pkgname
Summary:       Executables for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n %pkgname
Executables for %gemname gem.


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
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         -n %pkgname
%_bindir/%{pkgname}*

%changelog
* Mon Apr 29 2019 Pavel Skrylev <majioa@altlinux.org> 5.1.0-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
