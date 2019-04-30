%define        pkgname  md2man

Name:          gem-%pkgname
Version:       5.1.2
Release:       alt1
Summary:       Converts markdown into UNIX manual pages
License:       ISC
Group:         Development/Ruby
Url:           https://sunaku.github.io/md2man/man
# VCS:         https://github.com/sunaku/md2man.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
md2man - markdown to manpage

md2man is a Ruby library and a set of command-line programs that convert
Markdown into UNIX manpages as well as HTML webpages using Redcarpet.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
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
%_bindir/%pkgname-*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Mon Apr 29 2019 Pavel Skrylev <majioa@altlinux.org> 5.1.2-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
