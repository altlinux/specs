%define        pkgname redcarpet

Name:          ruby-%pkgname
Version:       3.4.0
Release:       alt2
Summary:       The safe Markdown parser, reloaded
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/vmg/redcarpet
# VCS:         https://github.com/vmg/redcarpet.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Redcarpet is a Ruby library for Markdown processing that smells like
butterflies and popcorn.


%package       -n %pkgname
Summary:       %summary
Group:         Development/Documentation
BuildArch:     noarch

%description   -n %pkgname
%summary.

Executables files for %gemname gem.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-%pkgname-doc
Obsoletes:     ruby-%pkgname-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.


%package       -n gem-%pkgname-devel
Summary:       Development files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-devel
Development files for %gemname gem.


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
%ruby_gemextdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%files         -n gem-%pkgname-devel
%ruby_includedir/*

%files         -n %pkgname
%_bindir/*


%changelog
* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 3.4.0-alt2
- Use Ruby Policy 2.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- New version.

* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.3-alt1
- Initial build for Sisyphus
