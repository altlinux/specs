%define        pkgname ast

Name:          gem-%pkgname
Version:       2.4.0
Release:       alt1
Summary:       A library for working with Abstract Syntax Trees
License:       MIT
Group:         Development/Ruby
Url:           https://whitequark.github.io/ast/
# VCS:         https://github.com/whitequark/ast.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch
Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler)

%description
AST is a small library for working with immutable abstract syntax trees.


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
* Thu Feb 28 2019 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
